import requests
import time
import random
from datetime import datetime, timedelta
import os
import textwrap

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Mobula API key (replace with your actual key)
API_KEY = "your_api_key"

# Tracking today's results and a weekly contract storage
today_results = {'eth': 0, 'polygon': 0}
last_reset = datetime.utcnow().date()
weekly_contracts = []

# Function to get new contracts from the Mobula API
def get_new_contracts(blockchain):
    url = f"https://api.mobula.io/api/1/market/query/token?sortBy=listed_at&sortOrder=desc&blockchain={blockchain}"
    headers = {'Authorization': f'Bearer {API_KEY}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except requests.HTTPError:
        return []
    except requests.RequestException:
        return []

# Function to save contract info to files in a specific format
def save_contracts_to_file(filename, contract_info_list, blockchain_name):
    timestamp = datetime.utcnow().strftime("%Y.%m.%d %H:%M UTC")
    header = f"=================================================================================================\n"
    header += f"TIME: {timestamp} | {blockchain_name} New Contracts\n"
    header += f"=================================================================================================\n"
    
    with open(filename, "a") as f:
        f.write(header)
        for contract_info in contract_info_list:
            blockchain = contract_info['blockchain']
            name = contract_info['name']
            address = contract_info['address']
            f.write(f"{blockchain:<10} | {name:<30} | {address:<42}\n")

# Function to update the contract list (remove contracts older than 48 hours)
def update_recent_contracts():
    current_time = datetime.utcnow()
    global weekly_contracts
    weekly_contracts = [contract for contract in weekly_contracts if current_time - contract['found_at'] < timedelta(hours=48)]

# Function to display contracts found in the last 48 hours
def display_recent_contracts():
    print(f"{WHITE}" + "="*99)
    print(f"{'CONTRACTS FOUND IN THE LAST 48 HOURS:':^99}")
    print("="*99)
    for contract in weekly_contracts:
        print(f"{contract['blockchain']:<10} | {contract['name']:<30} | {contract['address']:<42}")
    print("="*99 + f"{RESET}")

# Function to reset daily counts if a new UTC day starts
def reset_today_results():
    global last_reset, today_results
    current_date = datetime.utcnow().date()
    if current_date != last_reset:
        today_results = {'eth': 0, 'polygon': 0}
        last_reset = current_date

# Function to display a fixed header at the top
def display_fixed_header(current_time, total_eth, total_polygon):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{YELLOW}" + "="*99)
    print("LET'S GO HUNTERS ! ! ! STAY SHARP, STAY FAST ! ! ! JUST CREATED CONTRACTS ! ! !")
    print("="*99)
    warning_text = (
        "WARNING: Many newly listed tokens may be scams, spam, or contain malicious code. "
        "Always do your own research before investing (DYOR). "
        "This scanner is for informational and educational purposes only. "
        "The author assumes no responsibility for financial loss, damage, or misuse. "
        "NEVER share your API key – it is your personal access key!"
    )
    wrapped_warning = "\n".join(textwrap.wrap(warning_text, width=99))
    print(f"{YELLOW}{wrapped_warning}{RESET}")
    print(f"{YELLOW}" + "="*99)
    print(f"DATE: {current_time} | UTC TIME: {datetime.utcnow().strftime('%H:%M')} | Total found: EtherScan: {total_eth} | PolygonScan: {total_polygon}")
    print("="*99)

# Function to display contracts in limited batches (18 at a time)
def display_contracts_with_limit(contract_list):
    for i in range(0, len(contract_list), 18):
        display_fixed_header(datetime.utcnow().strftime("%Y.%m.%d"), len(contract_list), len(contract_list))
        for contract in contract_list[i:i+18]:
            display_contract(contract)
            time.sleep(1)  # Delay between contract displays set to 1 second

# Function to display a single contract's information
def display_contract(contract_info):
    name = contract_info['name'].encode('ascii', 'ignore').decode('ascii')
    name = name[:30]
    address = contract_info['address']
    blockchain = contract_info['blockchain']
    
    print(f"{WHITE}{blockchain:<10} | {name:<30} | {address:<42}{RESET}")

# Main function to search for new contracts
def search_new_contracts():
    while True:
        reset_today_results()
        current_time = datetime.utcnow().strftime("%Y.%m.%d")

        eth_contracts = get_new_contracts("Ethereum")
        polygon_contracts = get_new_contracts("Polygon")

        total_eth = len(eth_contracts)
        total_polygon = len(polygon_contracts)

        today_results['eth'] += total_eth
        today_results['polygon'] += total_polygon

        eth_contract_list = []
        for contract in eth_contracts:
            contract_info = {
                'name': contract.get('name', 'Unknown Token'),
                'address': contract.get('address', 'Unknown Address'),
                'blockchain': 'Ethereum',
                'found_at': datetime.utcnow()
            }
            eth_contract_list.append(contract_info)
            weekly_contracts.append(contract_info)

        save_contracts_to_file("eth_new_contracts.txt", eth_contract_list, "Ethereum")

        polygon_contract_list = []
        for contract in polygon_contracts:
            contract_info = {
                'name': contract.get('name', 'Unknown Token'),
                'address': contract.get('address', 'Unknown Address'),
                'blockchain': 'Polygon',
                'found_at': datetime.utcnow()
            }
            polygon_contract_list.append(contract_info)
            weekly_contracts.append(contract_info)

        save_contracts_to_file("pol_new_contracts.txt", polygon_contract_list, "Polygon")

        update_recent_contracts()
        display_contracts_with_limit(eth_contract_list + polygon_contract_list)

        time.sleep(random.uniform(0.5, 3))

# Start the contract search
search_new_contracts()
