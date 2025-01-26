Vehicle Data Scraper

This repository contains a Python script designed to scrape vehicle listings from a specific website. The script collects data such as the title, location, price, mileage (KM), and date of the vehicle listings. Duplicate entries are filtered to ensure unique records, which are stored in a file named with the current date.
Features

    Efficient Data Extraction: Scrapes key details from vehicle listings, including title, location, price, KM, and date.
    Duplicate Filtering: Ensures no duplicate entries are saved in the output file.
    Output to File: Saves results in a file dynamically named with the current date.
    Parallel Bash Integration: Utilizes bash scripts for fetching web pages in parallel for faster execution.

Requirements
System

    Operating System: This script is designed to run on Linux-based systems.

Python Packages

The script requires the following Python packages:

    beautifulsoup4
    requests

You can install these dependencies with:

pip install beautifulsoup4 requests

Usage

    #Clone the repository:
    git clone https://github.com/KavishkaC/vehical-data-fetcher.git
    cd vehical-data-scraper

Make sure your system meets the requirements mentioned above.

Run the Python script:

    python3 riyasewana.py

  The output will be saved in a file named vehicle-data-YYYY-MM-DD.txt in the same directory.

Created By

Kavishka Wijerathna
GitHub: https://github.com/KavishkaC/
Acknowledgments

Hail Open Source! 🌟
