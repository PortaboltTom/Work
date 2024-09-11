import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Voeg het volledige pad van de sandbox en al zijn submappen toe aan sys.path
sandbox_path = r'C:\GIT\Work\MIT_AIP\src\sandbox'

# Loop door alle submappen van de sandbox en voeg ze toe aan sys.path
for root, dirs, files in os.walk(sandbox_path):
    if root not in sys.path:
        sys.path.append(root)

# Importeer vervolgens je modules
from energy_profile import generate_daily_profile
from company_profile import define_company_profile
from pricing.price_generation import generate_next_day_prices

def optimize_trading(energy_profile, price_data, battery_capacity_kwh=100, max_charge_rate=10, max_discharge_rate=10):
    """
    Optimaliseer het energieverbruik door elektriciteit te kopen wanneer de prijs laag is en te verkopen wanneer de prijs hoog is.
    
    Parameters:
        energy_profile: DataFrame met energieverbruik (kW) per minuut.
        price_data: DataFrame met energieprijzen (per kWh) per minuut.
        battery_capacity_kwh: Capaciteit van de batterij in kWh.
        max_charge_rate: Maximale oplaadsnelheid van de batterij (kW).
        max_discharge_rate: Maximale ontlaadsnelheid van de batterij (kW).
    
    Returns:
        DataFrame met de optimalisatiebeslissingen (koop/verkopen/opslag).
    """
    # Zorg ervoor dat beide DataFrames dezelfde tijdstempels hebben
    energy_profile = energy_profile.set_index('timestamp')
    price_data = price_data.set_index('timestamp')

    # Controleer of de tijdstempels overeenkomen
    if not energy_profile.index.equals(price_data.index):
        raise ValueError("Tijdstempels van het energieprofiel en de prijsdata komen niet overeen.")

    # Initieer variabelen
    battery_storage = 0  # Start met lege batterij
    battery_history = []  # Geschiedenis van batterijopslag
    actions = []  # Beslissingen voor kopen/verkopen

    # Doorloop elk tijdstip en neem beslissingen
    for i in range(len(energy_profile)):
        current_demand = energy_profile['totaal_vermogen'].iloc[i]
        current_price = price_data['prijs'].iloc[i]

        if current_price < price_data['prijs'].mean():
            # Laad de batterij wanneer de prijs laag is (koop energie)
            charge_amount = min(max_charge_rate, battery_capacity_kwh - battery_storage)  # Laad niet meer dan de batterij aankan
            battery_storage += charge_amount
            actions.append(f"Koop {charge_amount:.2f} kW")
        elif current_price > price_data['prijs'].mean() and battery_storage > 0:
            # Ontlaad de batterij wanneer de prijs hoog is (verkoop energie)
            discharge_amount = min(max_discharge_rate, battery_storage)  # Ontlaad niet meer dan er in de batterij zit
            battery_storage -= discharge_amount
            actions.append(f"Verkoop {discharge_amount:.2f} kW")
        else:
            # Doe niets
            actions.append("Geen actie")

        # Bewaar de batterijstatus
        battery_history.append(battery_storage)

    # Maak een DataFrame met de beslissingen en batterijopslag
    result = pd.DataFrame({
        'timestamp': energy_profile.index,
        'totaal_vermogen': energy_profile['totaal_vermogen'],
        'prijs': price_data['prijs'],
        'actie': actions,
        'batterijopslag': battery_history
    })

    return result

# 1. Simuleer het energieprofiel
company_profile = define_company_profile()
timestamps = pd.date_range(start="2024-09-10", periods=1440, freq='T')  # 1440 minuten = 1 dag
daily_energy_profile = generate_daily_profile(company_profile)

# Maak een DataFrame van het gesimuleerde energieprofiel
energy_profile_df = pd.DataFrame({
    'timestamp': timestamps,
    'totaal_vermogen': daily_energy_profile
})

# 2. Simuleer de prijsdata
price_data_df = pd.DataFrame({
    'timestamp': timestamps,
    'prijs': generate_price_data(hours=24)  # Simuleer prijzen voor 24 uur
})

# 3. Voer de optimalisatie uit
optimized_result = optimize_trading(energy_profile_df, price_data_df)

# 4. Toon de resultaten
print(optimized_result.head())

# 5. Sla de resultaten op in een CSV-bestand
output_csv_path = r'C:\GIT\Work\MIT_AIP\src\sandbox\energy_profile\data\optimized_trading_results.csv'
optimized_result.to_csv(output_csv_path, index=False)
print(f"Optimalisatiebeslissingen opgeslagen in: {output_csv_path}")
