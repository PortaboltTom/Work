import pandas as pd
import matplotlib.pyplot as plt

# Bestandspad naar de CSV met totale vermogen per minuut
file_path = r'C:\GIT\Work\MIT_AIP\src\sandbox\energy_profile\data\totaal_vermogen_per_minuut_rounded.csv'

# Lees de CSV in een DataFrame
data = pd.read_csv(file_path)

# Zorg ervoor dat de timestamp kolom wordt geïnterpreteerd als datetime
data['timestamp_rounded'] = pd.to_datetime(data['timestamp_rounded'])

# Maak de grafiek
plt.figure(figsize=(10, 6))
plt.plot(data['timestamp_rounded'], data['totaal_vermogen'], label='Totaal vermogen (kW)', color='b')

# Opmaak van de plot
plt.title('Totaal vermogen per minuut Centaurusweg')
plt.xlabel('Tijd')
plt.ylabel('Totaal vermogen (kW)')
plt.xticks(rotation=45)  # Zorg voor goed leesbare tijdstempels
plt.grid(True)
plt.legend()

# Pad waar de grafiek wordt opgeslagen
output_figure_path = r'C:\GIT\Work\MIT_AIP\src\sandbox\energy_profile\figures\totaal_vermogen_per_minuut.png'

# Grafiek opslaan
plt.tight_layout()
plt.savefig(output_figure_path)

# Toon de plot als je dat wilt (optioneel)
# plt.show()

print(f"Grafiek opgeslagen op: {output_figure_path}")
