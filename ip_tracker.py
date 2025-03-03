import requests
import os
import time


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
                   v0.2 - By Malphas
"""
    print(banner)

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
        location = data.get("loc", "N/A").split(",")

        clear_screen()
        print_banner()
        print(f"\n    [ ~ ] IP: {data.get('ip', 'N/A')}")
        print(f"    [ ~ ] City: {data.get('city', 'N/A')}")
        print(f"    [ ~ ] Region: {data.get('region', 'N/A')}")
        print(f"    [ ~ ] Country: {data.get('country', 'N/A')}")
        print(f"    [ ~ ] ZIP Code: {data.get('postal', 'N/A')}") 
        print(f"    [ ~ ] Latitude: {location[0] if len(location) > 1 else 'N/A'}")
        print(f"    [ ~ ] Longitude: {location[1] if len(location) > 1 else 'N/A'}")
        print(f"    [ ~ ] Timezone: {data.get('timezone', 'N/A')}")
        print(f"    [ ~ ] ISP: {data.get('org', 'N/A')}")
        print(f"    [ ~ ] ASN: {data.get('asn', {}).get('asn', 'N/A')}")
        print(f"    [ ~ ] VPN/Proxy: {'Yes' if 'VPN' in data.get('privacy', {}).get('vpn', '') else 'No'}")
        print(f"    [ ~ ] Mobile: {'Yes' if data.get('carrier') else 'No'}")
        input("\nPress Enter to return to the menu...")
    except Exception as e:
        print(f"    [!] Error retrieving IP data: {e}")
        time.sleep(2)

def about():
    clear_screen()
    print_banner()
    print("\n    Track IPLocation v2 - By Malphas")
    print("    A real-time IP tracking tool for Linux terminal.")
    print("    Uses IPinfo.io for accurate geolocation data.")
    print("    Developed with Python and optimized for performance.\n")
    input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main_menu()
