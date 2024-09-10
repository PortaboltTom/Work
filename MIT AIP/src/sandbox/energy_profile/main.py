# main.py
import matplotlib.pyplot as plt
from company_profile import define_company_profile
from energy_profile import generate_daily_profile

def simulate_energy_profile():
    # Step 1: Define the company profile
    company = define_company_profile()

    # Step 2: Generate the energy profile for one day
    daily_profile = generate_daily_profile(company)

    # Step 3: Plot the results
    plt.plot(daily_profile)
    plt.title("Daily Energy Consumption Profile")
    plt.xlabel("Hour of the Day")
    plt.ylabel("Energy Consumption (kW)")
    plt.show()

if __name__ == "__main__":
    simulate_energy_profile()
