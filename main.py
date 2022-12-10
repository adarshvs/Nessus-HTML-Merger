import os
from bs4 import BeautifulSoup

# Define the paths to the two input files
input_file1 = 'nessus1.html'
input_file2 = 'nessus2.html'

# Define the path to the output file
output_file = 'nessus_merged.html'

# Read the HTML content from the first input file
with open(input_file1, 'r') as f:
  html1 = f.read()

# Read the HTML content from the second input file
with open(input_file2, 'r') as f:
  html2 = f.read()

# Parse the HTML content from the first input file
soup1 = BeautifulSoup(html1, 'html.parser')

# Parse the HTML content from the second input file
soup2 = BeautifulSoup(html2, 'html.parser')

# Find the table elements in the HTML content
tables1 = soup1.find_all('table')
tables2 = soup2.find_all('table')

# Merge the table elements from the two input files
tables = tables1 + tables2

# Create a new BeautifulSoup object to hold the merged HTML content
soup = BeautifulSoup('', 'html.parser')

# Add the merged table elements to the BeautifulSoup object
for table in tables:
  soup.append(table)

# Write the merged HTML content to the output file
with open(output_file, 'w') as f:
  f.write(str(soup))
