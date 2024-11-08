import os
import time
import requests
import sys
import webbrowser
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def print_banner():
    banner = """
                     :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~    hydarip tracker v1
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
    """
    print(banner)
def get_ip_details(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        if 'error' in data:
            print("Error fetching details for the IP address.")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
def show_ip_details(ip_data):
    if ip_data:
        print("\nIP Address Details:")
        print(f"IP Address: {ip_data.get('ip', 'N/A')}")
        print(f"Hostname: {ip_data.get('hostname', 'N/A')}")
        print(f"City: {ip_data.get('city', 'N/A')}")
        print(f"Region: {ip_data.get('region', 'N/A')}")
        print(f"Country: {ip_data.get('country', 'N/A')}")
        print(f"Location: {ip_data.get('loc', 'N/A')}")
        loc = ip_data.get('loc', '').split(',')
        if len(loc) == 2:
            lat, lon = loc
            google_maps_url = f"https://www.google.com/maps?q={lat},{lon}"
            print(f"View Location on Google Maps: {google_maps_url}")
        else:
            print("Location coordinates are unavailable.")
    else:
        print("No data available to display.")
def main():
    clear_screen()  
    print_banner()  
    ip_address = input("\nEnter an IP address to get details: ")
    ip_data = get_ip_details(ip_address)
    show_ip_details(ip_data)
    open_map = input("\nDo you want to open the location on Google Maps? (yes/no): ").strip().lower()
    if open_map == "yes" and ip_data:
        loc = ip_data.get('loc', '').split(',')
        if len(loc) == 2:
            lat, lon = loc
            google_maps_url = f"https://www.google.com/maps?q={lat},{lon}"
            webbrowser.open(google_maps_url)
        else:
            print("Unable to open Google Maps, location coordinates are unavailable.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
