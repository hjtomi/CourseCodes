import pandas as pd
import matplotlib.pyplot as plt
from DataScience.my_data_science import blank_lines
import matplotlib.dates as mdates


def all_print():
    print(df_tesla)
    blank_lines()
    print(df_unemployment)
    blank_lines()
    print(df_btc_search)
    blank_lines()
    print(df_btc_monthly)


df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
df_btc_price.dropna(inplace=True)

df_tesla['MONTH'] = pd.to_datetime(df_tesla['MONTH'])
df_btc_search['MONTH'] = pd.to_datetime(df_btc_search['MONTH'])
df_btc_price['DATE'] = pd.to_datetime(df_btc_price['DATE'])
df_unemployment['MONTH'] = pd.to_datetime(df_unemployment['MONTH'])

df_btc_monthly = df_btc_price.resample('M', on='DATE').mean()

years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

# TESLA
# plt.figure(figsize=(14, 8), dpi=120)
# plt.xticks(fontsize=14, rotation=45)
# plt.title('TESLA WEB SEARCH VS PRICE')
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_xlim([0, 600])
# ax2.set_xlim([df_tesla['MONTH'].min(), df_tesla['MONTH'].max()])
#
# ax1.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], color='blue', linewidth=3)
# ax2.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color='red', linewidth=3)
#
# ax1.set_ylabel('TSLA STOCK PRICE', color='blue', fontsize=14)
# ax2.set_ylabel('SEARCH TREND', color='red', fontsize=14)
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# plt.show()

# BITCOIN

# print(df_btc_monthly)
# blank_lines()
# print(df_btc_search)
#
# plt.figure(figsize=(14, 8), dpi=120)
# plt.xticks(fontsize=14, rotation=45)
# plt.title('Bitcoin News Search vs Resampled Price')
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_ylim([0, 16000])
# ax2.set_xlim([df_btc_search['MONTH'].min(), df_btc_search['MONTH'].max()])
#
# ax1.plot(df_btc_search['MONTH'], df_btc_monthly['CLOSE'], color='blue', linewidth=3, linestyle='--')
# ax2.plot(df_btc_search['MONTH'], df_btc_search['BTC_NEWS_SEARCH'], color='red', linewidth=3, marker='o')
#
# ax1.set_ylabel('BTC PRICE', color='blue', fontsize=14)
# ax2.set_ylabel('SEARCH TREND', color='red', fontsize=14)
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# plt.show()

# UNEMPLOYMENT BENEFITS

# - 2019
# print(df_unemployment)
#
# roll_df = df_unemployment[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()
#
# plt.figure(figsize=(14, 8), dpi=120)
# plt.xticks(fontsize=14, rotation=45)
# plt.grid(color='grey', linestyle='--')
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate')
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_ylim([3, 11])
# ax2.set_xlim([df_unemployment['MONTH'].min(), df_unemployment['MONTH'].max()])
#
# ax1.plot(df_unemployment['MONTH'], roll_df['UNRATE'], color='blue', linewidth=3, linestyle='--')
# ax2.plot(df_unemployment['MONTH'], roll_df['UE_BENEFITS_WEB_SEARCH'], color='red', linewidth=3, marker='o')
#
# ax1.set_ylabel('FRED U/E Rate', color='blue', fontsize=14)
# ax2.set_ylabel('WEB SEARCH', color='red', fontsize=14)
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
#
# plt.show()

# - 2020

df_unemployment_2020 = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
df_unemployment_2020['MONTH'] = pd.to_datetime(df_unemployment_2020['MONTH'])

plt.figure(figsize=(14, 8), dpi=120)
plt.xticks(fontsize=14, rotation=45)
plt.grid(color='grey', linestyle='--')
plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate')

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylim([3, 15])
ax2.set_xlim([df_unemployment_2020['MONTH'].min(), df_unemployment_2020['MONTH'].max()])

ax1.plot(df_unemployment_2020['MONTH'], df_unemployment_2020['UNRATE'], color='blue', linewidth=3, linestyle='--')
ax2.plot(df_unemployment_2020['MONTH'], df_unemployment_2020['UE_BENEFITS_WEB_SEARCH'], color='red', linewidth=3, marker='o')

ax1.set_ylabel('FRED U/E Rate', color='blue', fontsize=14)
ax2.set_ylabel('WEB SEARCH', color='red', fontsize=14)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)


plt.show()
