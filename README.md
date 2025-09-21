# Bank-Deposit-Distribution-Analysis-Quarterly-Trends-by-Account-Type-
📊 Analyses Performed

Data Cleaning & Transformation

Removed metadata rows

Converted dataset into tidy (long) format

Standardized column names

Descriptive Statistics

Mean, median, and standard deviation per account type

Ranking by total deposits

Aggregations

Totals by quarter and year

Percentage contribution of account types

Visualizations

📉 Line Chart: top 5 account types across quarters

📊 Stacked Bar Chart: deposit mix by period

🥧 Pie Chart: distribution in the latest period

🔥 Heatmap: deposit intensities (quarter × account type)

Advanced Analyses

Correlation matrix between account types

KMeans clustering of account types

Exponential Smoothing forecasting (ETS)

📁 Output Files

tidy_deposits_long_v2.csv → Cleaned dataset in long format

desc_by_account_v2.csv → Descriptive statistics per account type

totals_by_period_v2.csv → Aggregated deposits by quarter/year

forecast_v2.csv → Forecasted values for next periods

clusters_v2.csv → Cluster membership for each account type

corr_v2.csv → Correlation matrix of account types

stacked_deposits_v2.png → Stacked bar chart of deposits

line_top5_v2.png → Line plot of top 5 account types

pie_latest_v2.png → Pie chart for the latest quarter

heatmap_v2.png → Heatmap of deposits over time

🚀 How to Run

Clone this repo or copy the files.

Place the dataset in the data/ folder.

Run the analysis pipeline:

python main.py


Outputs will be saved in the analysis_outputs/ folder.

📌 Notes

Current column names like col_4, col_11, etc., are placeholders. You should map them to real deposit types for clarity.

Forecasting is based on limited quarterly data — results should be interpreted cautiously.

More advanced methods (ARIMA, Prophet) can be added if needed.
