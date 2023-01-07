import os
os.chdir('C:\\GIT\\Rentalfleet\\Project')

from contract_classes import *

#create 3 instances of inverterrack
IV45_001 = InverterRack(build_date='2022-01-01', rental_price=100.0, power = 45)
IV45_002 = InverterRack(build_date='2022-01-01', rental_price=100.0, power = 45)
IV45_003 = InverterRack(build_date='2022-01-01', rental_price=100.0, power = 45)
IV45_001,IV45_002, IV45_003 

#Create 3 instances of batteryrack 
BAT001= BatteryRack(build_date='2022-01-02', rental_price=200.0)
BAT002= BatteryRack(build_date='2022-01-02', rental_price=200.0)
BAT003= BatteryRack(build_date='2022-01-02', rental_price=200.0)
BAT001, BAT002, BAT003

#Create 3 instances of Trailer
PB01 = Trailer(build_date='2022-01-03', rental_price=300.0)
PB02 = Trailer(build_date='2022-01-03', rental_price=300.0)
PB03 = Trailer(build_date='2022-01-03', rental_price=300.0)

HanenBerg = Contract(name = 'Hanenberg')
HanenBerg.add_items([BAT001, IV45_001, PB01],'12')
HanenBerg.items

contract.add_item([inverter_rack, battery_rack, trailer, trailer])
contract.remove_item(trailer)
contract.print_items()


# Add items to the contract with a start date and no end date
start_date = datetime(2022, 1, 1)
#contract.add_items([inverter_rack, battery_rack, trailer], start_date=start_date)

# Print the items in the contract
contract.print_items()  # Output: InverterRack, BatteryRack, Trailer

# Remove an item from the contract
#contract.remove_item(inverter_rack)

# Generate an invoice for a 4 week period
contract.generate_invoice(4)  # Output: Invoice total: 500.00

# Add an item to the contract with a start date and end date
start_date = datetime(2022, 1, 15)
end_date = datetime(2022, 2, 5)
#contract.add_items([inverter_rack], start_date=start_date, end_date=end_date)

# Generate an invoice for a 4 week period
contract.generate_invoice(4)  # Output: Invoice total: 700.00