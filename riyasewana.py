from bs4 import BeautifulSoup
import subprocess
import threading
import itertools
import sys
import time

def show_loading():
    """Display a loading spinner in the terminal."""
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    while not stop_loading_event.is_set():
        sys.stdout.write(f"\rFetching all vehicle data from the internet... {next(spinner)}")
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write("\rDone!          \n")  # Clear spinner after completion

# Define the path to the bash script
bash_script_path = "./riyasewana.sh"

# Create an event to signal when to stop the spinner
stop_loading_event = threading.Event()

# Start the spinner in a separate thread
loading_thread = threading.Thread(target=show_loading)
loading_thread.start()

# Run the bash script
try:
    result = subprocess.run(
        ["bash", bash_script_path],  # Command to execute the script
        check=True,                 # Raise an error if the command fails
        text=True,                  # Capture the output as a string
        capture_output=True         # Capture stdout and stderr
    )
    # Stop the spinner
    stop_loading_event.set()
    loading_thread.join()

    # Print the script's output
    print("\nBash Script Output:")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    # Stop the spinner
    stop_loading_event.set()
    loading_thread.join()

    print("An error occurred while running the bash script.")
    print(f"Error Code: {e.returncode}")
    print(f"Error Output: {e.stderr}")



# Read the HTML content from output.txt
with open("output.txt", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all the 'li' elements with class 'item round'
items = soup.find_all('li', class_='item round')

# Set to store unique combinations of title, location, price, and km
unique_entries = set()

for item in items:
    # Extract the title
    title = item.find('h2', class_='more').find('a').get('title')
    URL = item.find('h2', class_='more').find('a').get('href')
    # Extract values inside div with class 'boxintxt'
    boxintxt_values = item.find_all('div', class_='boxintxt')
    
    # Handle missing data
    location = boxintxt_values[0].text.strip() if len(boxintxt_values) > 0 else "N/A"
    price = boxintxt_values[1].text.strip() if len(boxintxt_values) > 1 else "N/A"
    km = boxintxt_values[2].text.strip() if len(boxintxt_values) > 2 else "N/A"
    date = boxintxt_values[3].text.strip() if len(boxintxt_values) > 3 else "N/A"
    
    # Create a tuple of the unique attributes
    entry = (title, URL, location, price, km)
    
    # Check if this entry is already processed
    if entry in unique_entries:
        continue  # Skip this entry if it's a duplicate
    
    # Add the entry to the set of unique entries
    unique_entries.add(entry)
    
    # Print the extracted values
    print(f"URL: {URL}")
    print(f"Title: {title}")
    print(f"Location: {location}")
    print(f"Price: {price}")
    print(f"KM: {km}")
    print(f"Date: {date}")
    print("-" * 40)