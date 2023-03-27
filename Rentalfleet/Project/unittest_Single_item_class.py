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

