import requests
import os
import time

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
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] != 'success':
            print("    [!] Error retrieving data. IP may be invalid or API limit reached.")
            time.sleep(2)
            return

        clear_screen()
        print_banner()
        print(f"\n    [ ~ ] IP: {data.get('query', 'N/A')}")
        print(f"    [ ~ ] City: {data.get('city', 'N/A')}")
        print(f"    [ ~ ] Region: {data.get('regionName', 'N/A')}")
        print(f"    [ ~ ] Country: {data.get('country', 'N/A')}")
        print(f"    [ ~ ] Latitude: {data.get('lat', 'N/A')}")
        print(f"    [ ~ ] Longitude: {data.get('lon', 'N/A')}")
        print(f"    [ ~ ] ZIP Code: {data.get('zip', 'N/A')}")
        print(f"    [ ~ ] Timezone: {data.get('timezone', 'N/A')}")
        print(f"    [ ~ ] ISP: {data.get('isp', 'N/A')}")
        print(f"    [ ~ ] ASN: {data.get('as', 'N/A')}")
        print(f"    [ ~ ] VPN/Proxy: {'Yes' if data.get('proxy', False) else 'No'}")
        print(f"    [ ~ ] Mobile: {'Yes' if data.get('mobile', False) else 'No'}")
        input("\nPress Enter to return to the menu...")
    except Exception as e:
        print(f"    [!] Error retrieving IP data: {e}")
        time.sleep(2)

def about():
    clear_screen()
    print_banner()
    print("\n    Track IPLocation v1 - By Malphas")
    print("    A real-time IP tracking tool for Linux terminal.")
    print("    Uses IP-API for accurate geolocation data.")
    print("    Developed with Python and optimized for performance.\n")
    input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main_menu()
