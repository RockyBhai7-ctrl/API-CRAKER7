import requests
import time
import os

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m")
    print("="*60)
    print("       𝐀𝐏𝐈 𝐂𝐇𝐄𝐂𝐊𝐄𝐑 𝐓𝐎𝐎𝐋")
    print("        DARK X CYBER")
    print("="*60)
    print("\033[91m        DEVELOPER: DARK HACKER \033[0m")
    print("="*60)
    print("\033[0m")

def check_api_status(url):
    print(f"\n\033[94m[~] CHECKING YOUR API WAIT ⏳\033[0m {url}")

    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)

        print("\033[92m\n[✓] API IS LIVE\033[0m")
        print(f"\033[96m[+] STATUS Code:\033[0m {response.status_code}")
        print(f"\033[96m[+] RESPONSE Time:\033[0m {response_time} ms")

    except requests.exceptions.RequestException as e:
        print("\033[91m\n[X] API IS DOWN OR UNREACHABLE.\033[0m")
        print(f"\033[91m[!] Error:\033[0m {str(e)}")

while True:
    banner()
    user_input = input("\033[93mENTER YOUR API URL (with https://): \033[0m").strip()

    if not user_input:
        user_input = "https://jsonplaceholder.typicode.com/posts"

    check_api_status(user_input)

    print("\n\033[93m" + "="*60)
    print("PRESS Y TO ANOTHER API")
    print("PRESS E TO EXIT TOOL")
    print("="*60 + "\033[0m")
    
    choice = input("\033[93mYOUR CHOICE: \033[0m").strip().lower()
    if choice != 'y':
        print("\033[91m\n[!] EXITING TOOL GOOD-BYE BRO!\033[0m\n")
        break