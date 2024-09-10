# energy_profile.py
import numpy as np

def generate_daily_profile(company_profile):
    """
    Generate a daily energy consumption profile for a company.
    """
    hours_in_day = 24
    profile = np.zeros(hours_in_day)

    for hour in range(hours_in_day):
        if company_profile['working_hours'][0] <= hour < company_profile['working_hours'][1]:
            # During working hours, use peak energy
            profile[hour] = company_profile['peak_kw']
        else:
            # Outside working hours, use baseload energy
            profile[hour] = company_profile['baseload_kw']

    return profile
