import requests
from bs4 import BeautifulSoup
import yaml

# URL of the page
url_list_men = ['https://www.isuresults.com/results/season2526/gpjpn2025/CAT001RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT001RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT001RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT001RS.htm',
           'https://ijs.usfigureskating.org/leaderboard/results/2025/36369/CAT001RS.htm']

url_list_women = ['https://www.isuresults.com/results/season2526/gpjpn2025/CAT002RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT002RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT002RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT002RS.htm',
           'https://ijs.usfigureskating.org/leaderboard/results/2025/36369/CAT002RS.htm']

url_list_pairs = ['https://www.isuresults.com/results/season2526/gpjpn2025/CAT003RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT003RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT003RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT003RS.htm']

url_list_icedance = ['https://www.isuresults.com/results/season2526/gpjpn2025/CAT004RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT004RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT004RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT004RS.htm']

competition_ID_men = ['NHK25', 'SCI25', 'CoC25', 'GPFra25', 'CranberryCup'] 
competition_ID_women = ['NHK25', 'SCI25', 'CoC25', 'GPFra25', 'CranberryCup'] 
competition_ID_pairs = ['NHK25', 'SCI25', 'CoC25', 'GPFra25'] 
competition_ID_icedance = ['NHK25', 'SCI25', 'CoC25', 'GPFra25'] 

url_list_combined = [url_list_men, url_list_women, url_list_pairs, url_list_icedance]
competition_ID_list_combined = [competition_ID_men, competition_ID_women, competition_ID_pairs, competition_ID_icedance]
category_IDs = ['SeniorMen', 'SeniorWomen', 'SeniorPairs', 'SeniorIceDance']


for i in range(len(category_IDs)):
    url_list = url_list_combined[i]
    competition_ID = competition_ID_list_combined[i]
    category = category_IDs[i]

    skater_data = []

    for url, comp_id in zip(url_list, competition_ID):
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Check that request was successful

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

                print(points)

                skater_data.append({
                    "name": name,
                    "country": country_code,
                    "points": points,
                    "compID": comp_id,
                    "category": category
                })
                
    with open(f"skaters_{category}.yaml", "w") as f:
        yaml.dump({"skaters": skater_data}, f)
