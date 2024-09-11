# main.py
import matplotlib.pyplot as plt
from company_profile import define_company_profile
from energy_profile import generate_daily_profile, resample_to_hourly

def simulate_energy_profile():
    # Step 1: Define the company profile
    company = define_company_profile()

    # Step 2: Generate the energy profile for one day with 5-second intervals
    daily_profile = generate_daily_profile(company, interval_seconds=5)

    # Step 3: Resample the profile to hourly data for plotting
    hourly_profile = resample_to_hourly(daily_profile, interval_seconds=5)

    # Step 4: Plot the results
    plt.plot(hourly_profile)
    plt.title("Hourly Energy Consumption Profile with Mechanical Power Peaks")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Energy Consumption (kW)")
    plt.show()

if __name__ == "__main__":
    simulate_energy_profile()
