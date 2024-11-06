import pandas as pd
import matplotlib.pyplot as plt

# Load the scraped data from the CSV file
weather_df = pd.read_csv('mars_weather.csv')

# Rename the column 'terrestrial_date' to 'Terrestrial Date'
weather_df.rename(columns={'terrestrial_date': 'Terrestrial Date'}, inplace=True)

# Convert 'Terrestrial Date' to datetime
weather_df['Terrestrial Date'] = pd.to_datetime(weather_df['Terrestrial Date'])

# How many months exist on Mars?
mars_months = weather_df['month'].nunique()
print(f"Number of months on Mars: {mars_months}")

# How many Martian days worth of data exist in the scraped dataset?
martian_days = weather_df['sol'].nunique()
print(f"Number of Martian days in the dataset: {martian_days}")

# Coldest and warmest months on Mars
average_min_temp = weather_df.groupby('month')['min_temp'].mean()
coldest_month = average_min_temp.idxmin()
warmest_month = average_min_temp.idxmax()
print(f"Coldest month on Mars: Month {coldest_month}")
print(f"Warmest month on Mars: Month {warmest_month}")

# Define month names
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Plot the average minimum daily temperature for all months
plt.figure(figsize=(10, 5))
bars = plt.bar(average_min_temp.index, average_min_temp, tick_label=month_names)
plt.xlabel('Month')
plt.ylabel('Average Minimum Temperature (C)')
plt.title('Average Minimum Daily Temperature by Month on Mars')

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')  # ha: horizontal alignment, va: vertical alignment

plt.show()

# Months with the lowest and highest atmospheric pressure on Mars
average_pressure = weather_df.groupby('month')['pressure'].mean()
lowest_pressure_month = average_pressure.idxmin()
highest_pressure_month = average_pressure.idxmax()
print(f"Month with the lowest atmospheric pressure: Month {lowest_pressure_month}")
print(f"Month with the highest atmospheric pressure: Month {highest_pressure_month}")

# Plot the average daily atmospheric pressure for all months
plt.figure(figsize=(10, 5))
bars = plt.bar(average_pressure.index, average_pressure, tick_label=month_names)
plt.xlabel('Month')
plt.ylabel('Average Atmospheric Pressure')
plt.title('Average Daily Atmospheric Pressure by Month on Mars')

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')  # ha: horizontal alignment, va: vertical alignment

plt.show()

# About how many terrestrial days exist in a Martian year?
weather_df.set_index('Terrestrial Date', inplace=True)
min_temp_plot = weather_df['min_temp'].plot()
min_temp_plot.set_ylabel('Minimum Temperature (C)')
plt.title('Minimum Daily Temperature over Time on Mars')
plt.show()
