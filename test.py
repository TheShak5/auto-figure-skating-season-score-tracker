import requests
from bs4 import BeautifulSoup
import yaml

url_men_test = 'https://results.isu.org/results/season2526/ec2026/CAT001RS.htm'
competition_ID_men = 'Europeans 2026'
category_ID = 'SeniorMen'

skater_data = []
 
# Fetch the page content
try:
    response = requests.get(url_men_test)
    response.raise_for_status()  # Check that request was successful
except:
    print('Unable to access website for ', competition_ID_men)
    print('Skipping!')
    exit()

# print(comp_id)

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Inspecting the structure of the attached page,
# skater names appear to be in table rows <tr> within <td> tags in a results table.
# Usually, the second or third column contains the name

main_table = soup.find("table")
rows = main_table.find_all("tr")[1:]  # skip header row

for row in rows:
    tds = row.find_all("td", recursive=False)

    if len(tds) >= 4:

        if tds[1].get_text(strip=True) == 'Final Not Reached':
            break

        # Extract skater name
        name_tag = tds[1].find("a")
        name = name_tag.get_text(strip=True) if name_tag else None
        # print(name)

        # Extract country code from nested table in third <td>
        country_td = tds[2]
        nested_table = country_td.find("table")
        country_code = None
        if nested_table:
            nested_tr = nested_table.find("tr")
            country_code = nested_tr.get_text(strip=True)
            # print(country_code)

        # Extract points (fourth <td>)
        if (tds[0].get_text(strip=True) == 'WD'): # dealing with any withdraws from competition
            continue

        points = tds[3].get_text(strip=True)

        # print(points)

        skater_data.append({
            "name": name,
            "country": country_code,
            "points": points,
            "compID": competition_ID_men,
            "category": category_ID
        })