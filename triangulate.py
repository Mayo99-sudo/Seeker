import requests
import os
import re
import logging

logging.basicConfig(level=logging.INFO)

def is_valid_ip(ip):
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return re.match(pattern, ip) is not None

def triangulate_ip(ip_address):
    """
    Fetch geolocation data for an IP address using ipinfo.io.
    Returns dict with data or error.
    """
    if not is_valid_ip(ip_address):
        return {"error": "Invalid IP address format."}

    token = os.getenv('IPINFO_TOKEN')
    if not token:
        return {"error": "IPINFO_TOKEN environment variable not set."}
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "IP": data.get('ip'),
            "Location": f"{data.get('city')}, {data.get('region')}, {data.get('country')}",
            "Coordinates": data.get('loc'),
            "ISP": data.get('org')
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": f"Request failed: {e}"}

def is_valid_phone(phone):
    pattern = r"^\+?\d{7,15}$"
    return re.match(pattern, phone) is not None

def triangulate_phone(phone_number):
    """
    Fetch location data for a phone number using numverify.com.
    Returns dict with data or error.
    """
    if not is_valid_phone(phone_number):
        return {"error": "Invalid phone number format."}

    access_key = "34eecb403a239db4a1ef3aba35d5e782"  # Your actual key
    url = f"http://apilayer.net/api/validate?access_key={access_key}&number={phone_number}&country_code=&format=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "Phone Number": data.get('international_format'),
            "Country": data.get('country_name'),
            "Location": data.get('location'),
            "Carrier": data.get('carrier'),
            "Line Type": data.get('line_type')
        }
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return {"error": f"Request failed: {e}"}

def main():
    choice = input("Triangulate (1) IP or (2) Phone Number? Enter 1 or 2: ")
    if choice == '1':
        ip = input("Enter IP address: ")
        result = triangulate_ip(ip)
        print(result)
    elif choice == '2':
        number = input("Enter phone number (with country code): ")
        result = triangulate_phone(number)
        print(result)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
