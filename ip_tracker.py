import requests
import os
import time
import pycountry
from datetime import datetime

API_KEY = "00132319ef996e"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
  _____ _____        _                  _             
 \_   _|  __ \      | |                | |            
   | | | |__) |_____| |_ _ __ __ _  ___| | _____ _ __ 
   | | |  ___/______| __| '__/ _` |/ __| |/ / _ \ '__|
  _| |_| |          | |_| | | (_| | (__|   <  __/ |   
  \___/|_|           \__|_|  \__,_|\___|_|\_\___|_|   
                                                      
      }----------------------------------------{
   }-------------- Track IPLocation --------------{
      }----------------------------------------{
                   v0.1 - By Malphas
"""
    print(banner)

def get_region_code(country_code, region_name):
    try:
        subdivisions = pycountry.subdivisions.get(country_code=country_code)
        for sub in subdivisions:
            if sub.name.lower() == region_name.lower():
                return sub.code.split('-')[-1] 
    except:
        return "N/A"
    return "N/A"

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print("\n   [ 1 ] Track IP Address.")
        print("   [ 2 ] About us.")
        print("   [ x ] Exit")
        choice = input("\n   > ")

        if choice == '1':
            track_ip()
        elif choice == '2':
            about()
        elif choice.lower() == 'x':
            exit()
        else:
            print("\n   [!] Invalid option. Try again!")
            time.sleep(1)

def track_ip():
    clear_screen()
    print_banner()
    ip = input("\n    [ ~ ] Enter the IP: ")
    if not ip.strip():
        print("    [!] IP cannot be empty!")
        time.sleep(1)
        return

    print(f"\n    [ ~ ] Looking up data for: {ip}")
    time.sleep(2)
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers)

        if response.status_code != 200:
            print("    [!] Error retrieving data. Check API key or IP address.")
            time.sleep(2)
            return
        data = response.json()
        country_code = data.get("country", "N/A")

        country_name = pycountry.countries.get(alpha_2=country_code)
        country_name = country_name.name if country_name else "Unknown Country"

        region_name = data.get("region", "N/A")
        region_code = get_region_code(country_code, region_name)

        location = data.get("loc", "N/A").split(",")

        timezone = data.get("timezone", "N/A")
        current_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S') if timezone != "N/A" else "N/A"

        asn_number = data.get("asn", {}).get("asn")
        if not asn_number:
            asn_number = data.get("org", "N/A").split(" ")[0] if "AS" in data.get("org", "N/A") else "N/A"

        clear_screen()
        print_banner()
        print(f"\n    [ ~ ] IP: {data.get('ip', 'N/A')}")
        print(f"    [ ~ ] Country: {country_name}")  
        print(f"    [ ~ ] Country Code: {country_code}")  
        print(f"    [ ~ ] Region: {region_name}")
        print(f"    [ ~ ] Region Code: {region_code}")  
        print(f"    [ ~ ] City: {data.get('city', 'N/A')}")
        print(f"    [ ~ ] ZIP Code: {data.get('postal', 'N/A')}") 
        print(f"    [ ~ ] Location: {location[0] + ', ' + location[1] if len(location) > 1 else 'N/A'}")
        print(f"    [ ~ ] Data & Time: {current_time}")
        print(f"    [ ~ ] ISP: {data.get('org', 'N/A')}")
        print(f"    [ ~ ] Organization: {data.get('org', 'N/A')}")
        print(f"    [ ~ ] Timezone: {timezone}")
        print(f"    [ ~ ] ASN: {asn_number}")  
        print(f"    [ ~ ] VPN/Proxy: {bool(data.get('privacy', {}).get('vpn', False))}")
        print(f"    [ ~ ] Mobile: {bool(data.get('carrier'))}")
        input("\nPress Enter to return to the menu...")
    except Exception as e:
        print(f"    [!] Error retrieving IP data: {e}")
        time.sleep(2)

def about():
    clear_screen()
    print_banner()
    print("\n    Track IPLocation v7 - By Malphas")
    print("    A real-time IP tracking tool for Linux terminal.")
    print("    Uses IPinfo.io for accurate geolocation data.")
    print("    Now includes full country names, region codes, and ASN numbers correctly.")
    print("    Developed with Python and optimized for performance.\n")
    input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main_menu()
