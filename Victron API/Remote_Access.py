import requests

# Step 1: Login to get the bearer token
def login(username, password, sms_token=None):
    login_url = "https://vrmapi.victronenergy.com/v2/auth/login"
    login_payload = {
        "username": "tombergisch@gmail.com",  # Replace with your email
        "password": "*4z_gERn67nciHmK",  # Replace with your password
        "sms_token": "123456",  # Optional: Replace with your 2FA code if needed
        "remember_me": True  # Optional: Set to True if you want a long-lived token
    }
    login_headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(login_url, json=login_payload, headers=login_headers)

    if response.status_code == 200:
        data = response.json()
        return data.get("token"), data.get("idUser")
    else:
        raise Exception(f"Login failed! Status code: {response.status_code}, Response: {response.text}")

# Step 2: Retrieve the list of installations
def get_installations(bearer_token, idUser):
    installations_url = f"https://vrmapi.victronenergy.com/v2/users/{idUser}/installations"
    installations_headers = {
        "x-authorization": f"Bearer {bearer_token}"
    }
    installations_params = {
        "extended": 1
    }

    response = requests.get(installations_url, headers=installations_headers, params=installations_params)

    if response.status_code == 200:
        return response.json().get('records', [])
    else:
        raise Exception(f"Failed to retrieve installations! Status code: {response.status_code}, Response: {response.text}")

# Step 3: Set max kW output for a specified installation
def set_max_kw_output(bearer_token, idSite, max_kw_output):
    config_url = f"https://vrmapi.victronenergy.com/v2/installations/{idSite}/dynamic-ess-settings"
    config_payload = {
        "batteryCapacity": 10,  # Example value, adjust as needed
        "batteryCosts": 0.02,  # Example value, adjust as needed
        "batteryFlowRestriction": "unrestricted",  # Example value, adjust as needed
        "batteryPrice": 250,  # Example value, adjust as needed
        "buyEnergyProviderId": 1,  # Example value, adjust as needed
        "buyPriceFormula": "1.21*p+0.04",  # Example value, adjust as needed
        "buyPriceSchedule": [],  # Example value, adjust as needed
        "buyPriceType": 1,  # Example value, adjust as needed
        "chargePower": max_kw_output,
        "dischargePower": max_kw_output,
        "gridSell": 1,  # Example value, adjust as needed
        "idBiddingZone": 1,  # Example value, adjust as needed
        "isDessSocDifferent": False,  # Example value, adjust as needed
        "isGreenModeOn": False,  # Example value, adjust as needed
        "isOn": True,  # Example value, adjust as needed
        "maxPowerFromGrid": max_kw_output,
        "maxPowerToGrid": max_kw_output,
        "sellEnergyProviderId": 1,  # Example value, adjust as needed
        "sellPriceSchedule": [],  # Example value, adjust as needed
        "sellPriceFormula": "1.21*p+0.04",  # Example value, adjust as needed
        "sellPriceType": 1  # Example value, adjust as needed
    }
    config_headers = {
        "x-authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(config_url, json=config_payload, headers=config_headers)

    if response.status_code == 200:
        print("Max kW output successfully set!")
    else:
        raise Exception(f"Failed to set max kW output! Status code: {response.status_code}, Response: {response.text}")

# Step 4: Verify max kW output for a specified installation
def verify_max_kw_output(bearer_token, idSite):
    config_url = f"https://vrmapi.victronenergy.com/v2/installations/{idSite}/dynamic-ess-settings"
    config_headers = {
        "x-authorization": f"Bearer {bearer_token}"
    }

    response = requests.get(config_url, headers=config_headers)

    if response.status_code == 200:
        data = response.json()
        print("Current ESS Settings:")
        print(f"Charge Power: {data.get('chargePower')}")
        print(f"Discharge Power: {data.get('dischargePower')}")
        print(f"Max Power From Grid: {data.get('maxPowerFromGrid')}")
        print(f"Max Power To Grid: {data.get('maxPowerToGrid')}")
    else:
        raise Exception(f"Failed to retrieve ESS settings! Status code: {response.status_code}, Response: {response.text}")

# Step 5: Disable Dynamic ESS for a specified installation
def disable_dynamic_ess(bearer_token, idSite):
    config_url = f"https://vrmapi.victronenergy.com/v2/installations/{idSite}/dynamic-ess-settings"
    config_payload = {
        "isOn": True  # Set to False to disable Dynamic ESS
    }
    config_headers = {
        "x-authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(config_url, json=config_payload, headers=config_headers)

    if response.status_code == 200:
        print("Dynamic ESS successfully disabled!")
    else:
        raise Exception(f"Failed to disable Dynamic ESS! Status code: {response.status_code}, Response: {response.text}")


# Example usage
username = "tombergisch@gmail.com"
password = "*4z_gERn67nciHmK"
sms_token = "your_2fa_code"  # Optional
idSite = "168714"  # Replace with your site ID
max_kw_output = 1000  # Set the desired max kW output

try:
    token, user_id = login(username, password, sms_token)
    installations = get_installations(token, user_id)
    for installation in installations:
        print(f"Installation Name: {installation['name']}, ID: {installation['idSite']}")
    
    # Set max kW output for the specified installation
    set_max_kw_output(token, idSite, max_kw_output)
    verify_max_kw_output(token, idSite)
    # Disable Dynamic ESS for the specified installation
    disable_dynamic_ess(token, idSite)
except Exception as e:
    print(e)
    
    
