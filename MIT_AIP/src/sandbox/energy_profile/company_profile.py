# company_profile.py
def define_company_profile():
    """
    Define an average company energy profile.
    This can later be extended with different types of companies.
    """
    profile = {
        'company_type': 'office',  # e.g., office, industrial, retail
        'working_hours': (8, 18),  # 8 AM to 6 PM
        'baseload_kw': 20,         # Constant energy use outside working hours
        'peak_kw': 100,            # Peak energy usage during working hours
        'weekend_factor': 0.5,     # Reduced usage on weekends
        'seasonal_variation': 0.1  # 10% variation depending on the season
    }
    return profile
