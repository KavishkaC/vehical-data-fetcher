#!/bin/bash

# Define variables
BASE_URL="https://riyasewana.com/search/price-1000000-30000000?page="
OUTPUT_FILE="output.txt"
MAX_PAGE=1000  # Replace with the actual maximum number of pages if known

# Function to fetch a single page
fetch_page() {
    PAGE_NUMBER=$1
    echo "Fetching page number: $PAGE_NUMBER"  # Echo the page number
    curl -s "${BASE_URL}${PAGE_NUMBER}"
}

export -f fetch_page
export BASE_URL

# Use parallel to fetch pages concurrently and print page numbers
seq 1 "$MAX_PAGE" | parallel -j 10 fetch_page > "$OUTPUT_FILE"

echo "Data fetched and written to $OUTPUT_FILE"
