import os
os.chdir('C:\GIT\Rentalfleet\Project')
from Single_item_class import *
# Create some items
IV_45_001 = InverterRack(name ='IV_45_001', build_date="2022-01-01",  power = 45)
IV_45_002 = InverterRack(name ='IV_45_002', build_date="2022-01-01",  power = 45)

BAT001 = BatteryRack(name='BAT001', build_date = datetime(22,2,3))
BAT002 = BatteryRack(name='BAT002', build_date = datetime(22,4,3))

PB01 = Trailer(name='PB01', build_date = datetime(23,3,2), leeg_gewicht=650, assen=2, laadgewicht=2000)
PB02 = Trailer(name='PB02', build_date = datetime(23,3,2), leeg_gewicht=450, assen=1, laadgewicht=1350)

K32A_5M_001 = Cable(name = 'K32A_5M_001', build_date = datetime.now())

# Create a contract
contract_1 = Contract("Contract 1")

# Add some items to the contract
start_date = datetime(2022, 1, 1)
items_to_add = [IV_45_001, BAT001, BAT002, PB01]
added_items = contract_1.add_items(items_to_add, start_date)
contract_1.items
contract_1.remove_item(IV_45_001)
contract_1.remove_multiple_items(added_items)
#tot hier werkt het nu 

'''
items_in_contract = contract_1.get_items()
items_name = [item.name for item in items_in_contract]
contract_1.remove_items(contract_1.items)
items_in_contract = contract_1.get_items()
contract_1.remove_items(PB01)
contract_1.items

#Note to self, ik krijg mijn lijst niet aan de praat waarin ik items tegelijk van het contract verwijder
#omdat ze niet dezelfde class zijn, chatai werkt niet dus morgen weer een dag. 


###Create artificial real contract###
#create contract
Nomi = Contract(name = 'Nomi')
#add items
start_date = datetime(2022, 12, 1)
items_to_add = [inverter_rack_1, battery_rack_1, trailer_1, Kabel_32A_5M_001]
added_items = Nomi.add_items(items_to_add, start_date )
#week later, add more items
#2 weeks later remove 2 items

'''

'''
# Print the items in the contract
#contract_1.print_items()
# Output: Inverter Rack 1, Battery Rack 1, Trailer 1

# Generate an invoice for the contract
period = 4
contract_1.generate_invoice(period)
# Output: Invoice total: 350.00

# Remove some items from the contract
items_to_remove = [inverter_rack_1, trailer_1]
end_dates = [datetime(2022, 1, 15), datetime(2022, 2, 1)]
removed_items = contract_1.remove_items(items_to_remove, end_dates)

# Print the items in the contract
#contract_1.print_items()
# Output: Battery Rack 1

# Generate an invoice for the contract
period = 4
contract_1.generate_invoice(period)
# Output: Invoice total: 225.00
'''

