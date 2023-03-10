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

#Create new contract with current date
HanenBerg = Contract(name = 'Hanenberg')
HanenBerg.add_items([BAT001, IV45_001, PB01],'8-1-2023')
HanenBerg

#add duplicate items to test that instance has correct current_contract attritbute
BAT001
HanenBerg.add_items([BAT001], '8-1-2022')

#remove item to check updates attribute of current_contract
HanenBerg.remove_item(BAT001)
BAT001

#check if contract still keeps track of removed items
HanenBerg.removed_items

#remove rest so i can make a new test with the same items
HanenBerg.remove_items([PB01])




#create artifical contract
ERA = Contract(name = 'ERA')
ERA.add_items([PB01, BAT001, BAT002, IV45_001], start_date= '1-9-2022')

#check if items have current_contract property
PB01.current_contract
BAT001.current_contract
BAT002.current_contract
IV45_001.current_contract

'''
#check contract 
HanenBerg.remove_item()
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
'''