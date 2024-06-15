import requests
from config import LOGIN_URL, INSTALLATIONS_URL, DATA_DOWNLOAD_URL

def login(username, password, sms_token=None):
    login_payload = {
        "username": username,
        "password": password,
        "sms_token": sms_token,
        "remember_me": True
    }
    response = requests.post(LOGIN_URL, json=login_payload)

    if response.status_code == 200:
        data = response.json()
        return data.get("token"), data.get("idUser")
    else:
        raise Exception(f"Login failed! Status code: {response.status_code}, Response: {response.text}")

def get_installations(token, user_id):
    installations_url = INSTALLATIONS_URL.format(user_id=user_id)
    headers = {"x-authorization": f"Bearer {token}"}
    response = requests.get(installations_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['records']
    else:
        raise Exception(f"Failed to retrieve installations! Status code: {response.status_code}, Response: {response.text}")

def get_data_download(token, id_site, start=None, end=None):
    download_url = DATA_DOWNLOAD_URL.format(id_site=id_site)
    headers = {"x-authorization": f"Bearer {token}"}
    params = {"start": int(start.timestamp()), "end": int(end.timestamp())} if start and end else {}
    response = requests.get(download_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.content.decode('utf-8')
    else:
        raise Exception(f"Failed to retrieve data! Status code: {response.status_code}, Response: {response.text}")
