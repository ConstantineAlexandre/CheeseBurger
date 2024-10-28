#!/usr/bin/env python3
import sys
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

def capture_screenshot(url, output_path):
    # Set options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")  # Screenshot size

    # Initialize driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open URL and wait a moment for the page to load
        driver.get(url)
        time.sleep(2)  # Wait for the page to fully load

        # Screenshot and save
        driver.save_screenshot(output_path)

    except Exception as e:
        print(Fore.RED + f"Error taking screenshot for {Fore.GREEN}{url}{Fore.RED}: {e}")
    finally:
        driver.quit()

def is_subdomain_active(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code in [200]  # Check for status code 200,301,404
    except requests.RequestException:
        return False

def process_subdomains(file_path, screenshot_folder, protocol, juicy_files):
    if not os.path.exists(file_path):
        print(Fore.RED + f"File {file_path} not found.")
        return

    # Ensure the screenshot folder exists
    os.makedirs(screenshot_folder, exist_ok=True)

    with open(file_path, 'r') as file:
        subdomains = file.read().splitlines()

    total_subdomains = len(subdomains)

    # Display initial message
    print(Fore.YELLOW + "Processing Enumeration 🍸...")

    try:
        for index, subdomain in enumerate(subdomains):
            # Validate and format subdomain to ensure it has the correct protocol
            if not subdomain.startswith("http://") and not subdomain.startswith("https://"):
                url = f"{protocol}://{subdomain}"
            else:
                url = subdomain  # Use the full URL as is if protocol is already included

            # Check if the subdomain is active
            if is_subdomain_active(url):
                # Screenshot the main page
                output_path = os.path.join(screenshot_folder, f"{subdomain.replace('://', '_').replace('/', '_')}.png")
                capture_screenshot(url, output_path)

                # Enumerate and screenshot juicy files
                for juicy_file in juicy_files:
                    juicy_url = f"{url}/{juicy_file}"
                    juicy_output_path = os.path.join(screenshot_folder, f"{subdomain.replace('://', '_').replace('/', '_')}_{juicy_file}.png")
                    capture_screenshot(juicy_url, juicy_output_path)

            else:
                print(Fore.YELLOW + f"Subdomain {Fore.GREEN}{url}{Fore.YELLOW} is not active or cannot be accessed.")

            # Update loading bar
            progress = index + 1
            percent = (progress / total_subdomains) * 100
            
            # Create loading bar
            bar_length = 50  # Length of loading bar
            filled_length = int(bar_length * progress // total_subdomains)
            bar = Fore.GREEN + '█' * filled_length + '-' * (bar_length - filled_length)  # Bar colored green
            
            # Display loading bar
            print(f'\r|{bar}| {percent:.2f}% Complete ', end='')

        print()  # Move to a new line after loading is complete
        print(Fore.GREEN + "Process complete!")  # Completion message

    except KeyboardInterrupt:
        print(Fore.RED + "\nProcess interrupted by user.")  # Message if interrupted
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")


# Main program
if __name__ == "__main__":
    # Initialize variables to store arguments
    subdomain_file = None
    screenshot_folder = None
    protocol = None
    juicy_files = []

    # Check if any arguments are given
    if len(sys.argv) < 2:
        print(Fore.RED + "[No parameters given.]")
        print(Fore.WHITE + "Usage: CheeseBurger.py --subdomain=[file_subdomains_location.txt] --screenshot=[folder_screenshots_location] --protocol=[http/https] --juicy=[file1,file2,...]")
        sys.exit(1)

    # Parse arguments from command line
    for arg in sys.argv[1:]:
        if arg.startswith("--subdomain="):
            subdomain_file = arg.split("=")[1]
        elif arg.startswith("--screenshot="):
            screenshot_folder = arg.split("=")[1]
        elif arg.startswith("--protocol="):
            protocol = arg.split("=")[1]
        elif arg.startswith("--juicy="):
            juicy_files = arg.split("=")[1].split(",")

    # Input validation
    if not subdomain_file or not screenshot_folder or not protocol:
        print(Fore.RED + "Usage: python take.py --subdomain=<file_subdomains.txt> --screenshot=<folder_screenshots> --protocol=<http/https> --juicy=<file1,file2,...>")
    elif not subdomain_file:
        print(Fore.RED + "Parameter --subdomain cannot be empty.")
    elif not screenshot_folder:
        print(Fore.RED + "Parameter --screenshot cannot be empty.")
    elif protocol not in ["http", "https"]:
        print(Fore.RED + "Protocol must be 'http' or 'https'.")
    else:
        process_subdomains(subdomain_file, screenshot_folder, protocol, juicy_files)