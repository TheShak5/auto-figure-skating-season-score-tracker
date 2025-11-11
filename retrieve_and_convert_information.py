import requests
from bs4 import BeautifulSoup
import yaml

# URL of the page
url = 'https://www.isuresults.com/results/season2526/gpcan2025/CAT001RS.htm'

# Fetch the page content
response = requests.get(url)
response.raise_for_status()  # Check that request was successful

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Inspecting the structure of the attached page,
# skater names appear to be in table rows <tr> within <td> tags in a results table.
# Usually, the second or third column contains the name

# Find the results table (usually the first or only table on that page)
table = soup.find('table')

# Extract the skater names
skater_names = []
for row in table.find_all('tr')[1:]:  # skip the header row
    cols = row.find_all('td')
    if len(cols) > 2:
        name = cols[2].get_text(strip=True)
        skater_names.append(name)

# If desired, write to a YAML file
data = {'skaters': skater_names}
# with open('skater_names.yaml', 'w') as f:
#     yaml.dump(data, f)

print(f"Extracted {len(skater_names)} skater names:")
for name in skater_names:
    print(name)
