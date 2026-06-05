python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Abu_Dhabi_Public_Transport_Usage_2026.csv"
transport_data = pd.read_csv(file_path)

# Example analysis: Peak and Off-Peak Passenger Volume
# Group data by time of travel
peak_hours = ["07:00", "08:00", "09:00", "17:00", "18:00"]
transport_data['is_peak'] = transport_data['time_of_travel'].isin(peak_hours)
peak_data = transport_data[transport_data['is_peak'] == True]
off_peak_data = transport_data[transport_data['is_peak'] == False]

# Calculate total passengers during peak and off-peak hours
total_peak_passengers = peak_data['passenger_count'].sum()
total_off_peak_passengers = off_peak_data['passenger_count'].sum()

# Plot the data
plt.bar(['Peak Hours', 'Off-Peak Hours'], [total_peak_passengers, total_off_peak_passengers], color=['blue', 'green'])
plt.title('Passenger Volume During Peak and Off-Peak Hours')
plt.ylabel('Number of Passengers')
plt.show()

# Example output of punctuality analysis
average_punctuality = transport_data['on_time_performance'].mean()
print(f"Average Punctuality: {average_punctuality:.2f}%")
