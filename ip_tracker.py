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
\033[1m  _____ _____        _                  _             
 \_   _|  __ \      | |                | |            
   | | | |__) |_____| |_ _ __ __ _  ___| | _____ _ __ 
   | | |  ___/______| __| '__/ _` |/ __| |/ / _ \ '__|
  _| |_| |          | |_| | | (_| | (__|   <  __/ |   
  \___/|_|           \__|_|  \__,_|\___|_|\_\___|_|   
                                                      
      }----------------------------------------{
   }-------------- Track IPLocation --------------{
      }----------------------------------------{
                   v0.1 - By Malphas
\033[0m"""
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
        print("\n   \033[1m[ 1 ] Track IP Address.\033[0m")
        print("\033[1m   [ 2 ] About us.\033[0m")
        print("\033[1m   [ x ] Exit\033[0m")
        choice = input("\n   \033[1m> \033[0m")

        if choice == '1':
            track_ip()
        elif choice == '2':
            about()
        elif choice.lower() == 'x':
            exit()
        else:
            print("\n   \033[1m[!] Invalid option. Try again!\033[0m")
            time.sleep(1)

def track_ip():
    clear_screen()
    print_banner()
    ip = input("\n    \033[1m[ ~ ] Enter the IP: \033[0m")
    if not ip.strip():
        print("\033[1m    [!] IP cannot be empty!\033[0m")
        time.sleep(1)
        return

    print(f"\n    \033[1m[ ~ ] Looking up data for: {ip}\033[0m")
    time.sleep(2)
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.get(f"https://ipinfo.io/{ip}/json", headers=headers)

        if response.status_code != 200:
            print("\033[1m    [!] Error retrieving data. Check API key or IP address.\033[0m")
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
        print(f"\n    \033[1m[ ~ ] IP: {data.get('ip', 'N/A')}\033[0m")
        print(f"\033[1m    [ ~ ] Country: {country_name}\033[0m")  
        print(f"\033[1m    [ ~ ] Country Code: {country_code}\033[0m")  
        print(f"\033[1m    [ ~ ] Region: {region_name}\033[0m")
        print(f"\033[1m    [ ~ ] Region Code: {region_code}\033[0m")  
        print(f"\033[1m    [ ~ ] City: {data.get('city', 'N/A')}\033[0m")
        print(f"\033[1m    [ ~ ] ZIP Code: {data.get('postal', 'N/A')}\033[0m") 
        print(f"\033[1m    [ ~ ] Location: {location[0] + ', ' + location[1] if len(location) > 1 else 'N/A'}\033[0m")
        print(f"\033[1m    [ ~ ] Data & Time: {current_time}\033[0m")
        print(f"\033[1m    [ ~ ] ISP: {data.get('org', 'N/A')}\033[0m")
        print(f"\033[1m    [ ~ ] Organization: {data.get('org', 'N/A')}\033[0m")
        print(f"\033[1m    [ ~ ] Timezone: {timezone}\033[0m")
        print(f"\033[1m    [ ~ ] ASN: {asn_number}\033[0m")  
        print(f"\033[1m    [ ~ ] VPN/Proxy: {bool(data.get('privacy', {}).get('vpn', False))}\033[0m")
        print(f"\033[1m    [ ~ ] Mobile: {bool(data.get('carrier'))}\033[0m")
        input("\n\033[1mPress Enter to return to the menu...\033[0m")
    except Exception as e:
        print(f"\033[1m    [!] Error retrieving IP data: {e}\033[0m")
        time.sleep(2)

def about():
    clear_screen()
    print_banner()
    print("\n    \033[1mTrack IPLocation v1 - By Malphas\033[0m")
    print("\033[1m    A real-time IP tracking tool for Linux terminal.\033[0m")
    print("\033[1m    Uses IPinfo.io for accurate geolocation data.\033[0m")
    print("\033[1m    Now includes full country names, region codes, and ASN numbers correctly.\033[0m")
    print("\033[1m    Developed with Python and optimized for performance.\033[0m\n")
    input("\033[1mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main_menu()
