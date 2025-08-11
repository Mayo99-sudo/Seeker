import requests

def triangulate_ip(ip_address):
    """Fetch geolocation data for an IP address using ipinfo.io"""
    token = '2e5a607f3e9d46what'  # Your actual token
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"IP Address: {data.get('ip')}")
        print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
        print(f"Coordinates: {data.get('loc')}")
        print(f"ISP: {data.get('org')}")
    else:
        print("Failed to retrieve IP data.")

def triangulate_phone(phone_number):
    """Fetch location data for a phone number using numverify.com"""
    access_key = 'YOUR_NUMVERIFY_KEY'  # Replace with your actual key
    url = f"http://apilayer.net/api/validate?access_key={access_key}&number={phone_number}&country_code=&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Phone Number: {data.get('international_format')}")
        print(f"Country: {data.get('country_name')}")
        print(f"Location: {data.get('location')}")
        print(f"Carrier: {data.get('carrier')}")
        print(f"Line Type: {data.get('line_type')}")
    else:
        print("Failed to retrieve phone data.")

# Example usage
choice = input("Triangulate (1) IP or (2) Phone Number? Enter 1 or 2: ")
if choice == '1':
    ip = input("Enter IP address: ")
    triangulate_ip(ip)
elif choice == '2':
    number = input("Enter phone number (with country code): ")
    triangulate_phone(number)
else:
    print("Invalid choice.")
