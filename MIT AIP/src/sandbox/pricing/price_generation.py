import random
import datetime

def generate_next_day_prices(base_price=50, volatility=5):
    """
    Generates prices for the next day with specific patterns: 
    - Morning peak, 
    - Trough around noon, 
    - Evening peak around 7 PM, 
    - Gradual decline at night.
    :param base_price: The average price of electricity.
    :param volatility: The range by which prices can fluctuate.
    :return: A dictionary with the date and corresponding 24 prices.
    """
    next_day = datetime.date.today() + datetime.timedelta(days=1)
    
    # Define the price pattern throughout the day
    price_pattern = []
    for hour in range(24):
        if 6 <= hour <= 9:  # Morning peak (6 AM - 9 AM)
            price = base_price + 10
        elif 12 <= hour <= 14:  # Trough around noon (12 PM - 2 PM)
            price = base_price - 10
        elif 17 <= hour <= 20:  # Evening peak (5 PM - 8 PM)
            price = base_price + 15
        else:  # Night and other times (gradual decline)
            price = base_price
        
        # Add some random volatility
        fluctuation = random.uniform(-volatility, volatility)
        price += fluctuation
        price_pattern.append(round(price, 2))
    
    return {"date": next_day, "prices": price_pattern}

# Example usage:
if __name__ == "__main__":
    next_day_prices = generate_next_day_prices(base_price=10, volatility=5)
    print(f"Prices for {next_day_prices['date']}: {next_day_prices['prices']}")
