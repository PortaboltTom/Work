from Single_item_class import *
# Create some items
inverter_rack_1 = RentalItem("Inverter Rack 1", ItemType.INVERTER_RACK, 100.0)
battery_rack_1 = RentalItem("Battery Rack 1", ItemType.BATTERY_RACK, 75.0)
trailer_1 = RentalItem("Trailer 1", ItemType.TRAILER, 50.0)

# Create a contract
contract_1 = Contract("Contract 1")

# Add some items to the contract
start_date = datetime(2022, 1, 1)
items_to_add = [inverter_rack_1, battery_rack_1, trailer_1]
added_items = contract_1.add_items(items_to_add, start_date)

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


