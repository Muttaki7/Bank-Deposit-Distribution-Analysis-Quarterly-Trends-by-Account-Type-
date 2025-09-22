import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
file_path = r"C:\Users\Muttaki\Desktop\analysis gov\undo\data-resource_2024_06_25_Table-21 Advances Classified by Major Economic Purposes.csv"
df = pd.read_csv(file_path, skiprows=2)
df.rename(columns={
    "Table-21: Advances Classified by Major Economic Purposes": "Quarter",
    "Unnamed: 1": "Agriculture, Fishing and Forestry",
    "Unnamed: 2": "Industry",
    "Unnamed: 3": "Construction",
    "Unnamed: 4": "Transport",
    "Unnamed: 5": "Trade & Commerce",
    "Unnamed: 6": "Other Institutional Loan",
    "Unnamed: 7": "Consumer Finance",
    "Unnamed: 8": "Miscellaneous",
    "Unnamed: 9": "Total"
}, inplace=True)
df = df[df["Quarter"].str.contains(r"\d{4}, Q-\d", na=False)]
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df["Year"] = df["Quarter"].str.extract(r"(\d{4})").astype(int)
df["Quarter_No"] = df["Quarter"].str.extract(r"Q-(\d)").astype(int)
plt.figure(figsize=(12, 6))
for col in df.columns[1:9]:  # sectors only
    plt.plot(df["Quarter"], df[col], marker="o", label=col)
plt.xticks(rotation=45)
plt.title("Quarterly Advances by Sector")
plt.ylabel("Advances (Crore Tk)")
plt.legend()
plt.tight_layout()
plt.show()
sector_cols = df.columns[1:9]
df_share = df.copy()
for col in sector_cols:
    df_share[col] = df[col] / df["Total"] * 100
df_share.set_index("Quarter", inplace=True)
df_share[sector_cols].plot.area(figsize=(12,6), colormap="tab20")
plt.title("Sector Contribution to Total Advances (%)")
plt.ylabel("Share (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
yearly = df.groupby("Year")[sector_cols.tolist() + ["Total"]].sum()
yearly.plot(kind="bar", stacked=True, figsize=(12,6), colormap="tab20")
plt.title("Yearly Advances by Sector")
plt.ylabel("Advances (Crore Tk)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
df_growth = df.copy()
for col in sector_cols:
    df_growth[col + " Growth %"] = df[col].pct_change() * 100

print("\n--- Growth Rates (Quarterly %) ---")
print(df_growth[[ "Quarter"] + [c for c in df_growth.columns if "Growth" in c]].head(10))
plt.figure(figsize=(10,6))
sns.heatmap(df[sector_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation of Advances Between Sectors")
plt.show()
volatility = df[sector_cols].std().sort_values(ascending=False)
print("\n--- Sector Volatility (Std Dev) ---")
print(volatility)
sector_cols = df.columns[1:9]

plt.figure(figsize=(12, 6))
sns.boxplot(x="Quarter_No", y="Industry", data=df)
plt.title("Seasonality in Industry Advances (by Quarter)")
plt.xlabel("Quarter")
plt.ylabel("Advances (Crore Tk)")
plt.show()

# Compare seasonality across all sectors
seasonality = df.groupby("Quarter_No")[sector_cols].mean()
seasonality.plot(kind="bar", figsize=(12,6))
plt.title("Average Advances by Quarter (Seasonality)")
plt.ylabel("Avg Advances (Crore Tk)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
plt.figure(figsize=(12, 6))
for col in sector_cols:
    plt.plot(df["Quarter"], df[col], marker="o", label=col)

plt.xticks(rotation=45)
plt.title("Quarterly Advances by Sector")
plt.ylabel("Advances (Crore Tk)")
plt.legend()
plt.tight_layout()
plt.show()
df_area = df.set_index("Quarter")
df_area[sector_cols].plot.area(figsize=(12,6), colormap="tab20")
plt.title("Sector Contribution to Total Advances")
plt.ylabel("Advances (Crore Tk)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(10,6))
sns.heatmap(df[sector_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Sectors")
plt.show()

# -----------------------------
# 6. Forecasting (Optional)
# -----------------------------
# Example: Forecast for 'Industry'
df_forecast = df.set_index(pd.PeriodIndex(df["Year"].astype(str) + "Q" + df["Quarter_No"].astype(str), freq="Q"))

y = df_forecast["Industry"]

# Holt-Winters Exponential Smoothing
# new recommended way
model = ExponentialSmoothing(
    data,
    seasonal='add',
    seasonal_periods=4,   # 4 for quarterly data
    initialization_method="estimated"
)

fit_model = model.fit(optimized=True)
forecast = fit_model.forecast(4)  # forecast next 4 quarters
print(forecast)
 # Forecast next 8 quarters (2 years)

plt.figure(figsize=(12,6))
plt.plot(y.index.to_timestamp(), y, label="Historical")
plt.plot(forecast.index.to_timestamp(), forecast, label="Forecast", linestyle="--")
plt.title("Forecast of Industry Advances (Holt-Winters)")
plt.ylabel("Advances (Crore Tk)")
plt.legend()
plt.show()