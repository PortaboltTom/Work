# energy_profile.py
import numpy as np

def generate_daily_profile(company_profile, interval_seconds=3600):
    """
    Generate a daily energy consumption profile for a company.
    Each hour is divided into intervals of seconds (default is 1 hour = 3600 seconds).
    """
    if interval_seconds <= 0:
        raise ValueError("interval_seconds must be greater than 0")

    hours_in_day = 24
    intervals_per_hour = 3600 // interval_seconds
    total_intervals = hours_in_day * intervals_per_hour
    profile = np.zeros(total_intervals)

    for i in range(total_intervals):
        hour = i // intervals_per_hour  # Get the current hour
        if company_profile['working_hours'][0] <= hour < company_profile['working_hours'][1]:
            # During working hours, use peak energy with mechanical work spikes every 5 seconds
            if (i % (5 * intervals_per_hour // 3600)) == 0:
                # Simulate power peak every 5 seconds
                profile[i] = company_profile['peak_kw'] * np.random.uniform(1.1, 1.5)  # Simulate peak with fluctuation
            else:
                profile[i] = company_profile['peak_kw'] * np.random.uniform(0.9, 1.1)  # Natural fluctuations during peak hours
        else:
            # Outside working hours, use baseload energy with some fluctuations
            profile[i] = company_profile['baseload_kw'] * np.random.uniform(0.9, 1.1)  # Natural fluctuations in baseload

    return profile


def resample_to_hourly(profile, interval_seconds=3600):
    """
    Resample the profile from intervals to hourly data by taking the average of intervals.
    """
    intervals_per_hour = 3600 // interval_seconds
    hours_in_day = len(profile) // intervals_per_hour
    hourly_profile = np.zeros(hours_in_day)

    for hour in range(hours_in_day):
        start = hour * intervals_per_hour
        end = start + intervals_per_hour
        hourly_profile[hour] = np.mean(profile[start:end])  # Take average over the hour

    return hourly_profile
