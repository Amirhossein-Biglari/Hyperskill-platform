# Import libraries and set the device
import torch
import numpy as np
import pandas as pd
from sklearn.preprocessing import MaxAbsScaler
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
from finrl.meta.preprocessor.preprocessors import GroupByScaler
from finrl.meta.env_portfolio_optimization.env_portfolio_optimization import PortfolioOptimizationEnv
from finrl.agents.portfolio_optimization.models import DRLAgent
from finrl.agents.portfolio_optimization.architectures import EIIE
import optuna

# Set device to GPU if available, otherwise use CPU
device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

# Define a custom list of stocks for portfolio analysis
CUSTOM_STOCK_LIST = ["AAPL", "MSFT", "GOOGL", "AMZN"]

# Download historical stock data for the defined stocks from Yahoo Finance
START_DATE = '2020-01-01'  # Start date for portfolio data
END_DATE = '2022-12-31'    # End date for portfolio data
portfolio_raw_df = YahooDownloader(
    start_date=START_DATE,
    end_date=END_DATE,
    ticker_list=CUSTOM_STOCK_LIST
).fetch_data()

# Apply normalization to the data using GroupByScaler based on ticker (tic) column
scaler = GroupByScaler(by='tic', scaler=MaxAbsScaler)
portfolio_norm_df = scaler.fit_transform(portfolio_raw_df)

# Extract only the date, ticker, and essential price columns
df_portfolio = portfolio_norm_df[["date", "tic", "close", "high", "low"]]

# Define date ranges for splitting data into training and testing sets
START_DATE_TRAIN = '2020-01-01'  # Start date for training data
END_DATE_TRAIN = '2021-12-31'    # End date for training data
START_DATE_TEST = '2022-01-01'   # Start date for testing data
END_DATE_TEST = '2022-12-31'     # End date for testing data

# Filter portfolio data to create training and testing datasets
df_portfolio_train = df_portfolio[(df_portfolio["date"] >= START_DATE_TRAIN) & (df_portfolio["date"] < END_DATE_TRAIN)]
df_portfolio_test = df_portfolio[(df_portfolio["date"] >= START_DATE_TEST) & (df_portfolio["date"] < END_DATE_TEST)]

# Print the shape (number of rows and columns) of the training and testing datasets
TRAIN_DF_SHAPE = df_portfolio_train.shape
TEST_DF_SHAPE = df_portfolio_test.shape
print("Train df shape: ", TRAIN_DF_SHAPE)
print("Test df shape: ", TEST_DF_SHAPE)
