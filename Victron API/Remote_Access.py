import requests

# Define the login endpoint and credentials
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

# Make the POST request to login
login_response = requests.post(login_url, json=login_payload, headers=login_headers)

# Check if the login was successful
if login_response.status_code == 200:
    login_data = login_response.json()
    bearer_token = login_data.get("token")
    idUser = login_data.get("idUser")

    print("Login successful!")
    print("Bearer Token:", bearer_token)
    print("User ID:", idUser)

    # Define the installations endpoint
    installations_url = f"https://vrmapi.victronenergy.com/v2/users/{idUser}/installations"
    installations_params = {
        "extended": 1  # Set to 1 if you want to include all optional response values
    }
    installations_headers = {
        "x-authorization": f"Bearer {bearer_token}"
    }

    # Make the GET request to retrieve installations
    installations_response = requests.get(installations_url, headers=installations_headers, params=installations_params)

    # Check if the request was successful
    if installations_response.status_code == 200:
        installations_data = installations_response.json()
        print("Request successful!")
        for installation in installations_data['records']:
            print(f"Installation Name: {installation['name']}")
            print(f"Installation ID: {installation['idSite']}")
            print(f"Access Level: {installation['accessLevel']}")
            print(f"Owner: {installation['owner']}")
            print(f"Is Admin: {installation['is_admin']}")
            print(f"Identifier: {installation['identifier']}")
            # Add more fields as needed
    else:
        print("Failed to retrieve installations! Status code:", installations_response.status_code)
        print("Response:", installations_response.text)
else:
    print("Login failed! Status code:", login_response.status_code)
    print("Response:", login_response.text)
