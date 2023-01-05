from datetime import datetime
from flask import Flask, render_template, request

# Import the classes from the contract_classes module
from contract_classes import InverterRack, BatteryRack, Trailer, Contract
import os

os.chdir('C:\\GIT\\Rentalfleet\\Project')

app = Flask(__name__)

# Create a global contract object
contract = Contract()
contracts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contract', methods=['POST'])
def add_contract():
    # Create a new contract object
    new_contract = Contract()
    
    # Add the contract to the global list of contracts
    contracts.append(new_contract)
    
    return 'Contract added'

@app.route('/add_item', methods=['POST'])
def add_item():
    # Get the item type from the form
    item_type = request.form['item_type']
    
    # Create an instance of the appropriate item class
    if item_type == 'InverterRack':
        item = InverterRack(build_date='2022-01-01', rental_price=100.0)
    elif item_type == 'BatteryRack':
        item = BatteryRack(build_date='2022-01-01', rental_price=200.0)
    elif item_type == 'Trailer':
        item = Trailer(build_date='2022-01-01', rental_price=300.0)
    else:
        return 'Invalid item type'
    
    # Add the item to the contract
    contract.add_items([item])
    
    return 'Item added to contract'

@app.route('/view_contracts')
def view_contracts():
    # Create a list of the names of the items in each contract
    contract_items = []
    for contract in contracts:
        items = []
        for item in contract.items:
            items.append(item.__class__.__name__)
        contract_items.append(items)
    
    # Render the view_contracts.html template and pass the list of contracts and their items
    return render_template('view_contracts.html', contracts=contracts, contract_items=contract_items)

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(e)
    finally:
        print('Server shutting down')