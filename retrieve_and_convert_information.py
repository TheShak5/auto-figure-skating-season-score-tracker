import requests
from bs4 import BeautifulSoup
import yaml

# URL of the page
url_list_men = ['https://results.skateaustria.at/competition/saison2526/040/CAT001RS.htm',
            'https://www.isuresults.com/results/season2526/gpjpn2025/CAT001RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT001RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT001RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT001RS.htm',
           'https://ijs.usfigureskating.org/leaderboard/results/2025/36369/CAT001RS.htm',
           'https://www.jsfresults.com/InterNational/2025-2026/csjpn2025/CAT001RS.htm',
           'https://www.fisg.it/upload/result/6845/online/CAT001RS.htm',
           'https://www.kraso.sk/wp-content/uploads/sutaze/2025_2026/MON25/CAT001RS.htm',
           'http://www.deu-event.de/results/Nebelhorn_2025/CSGER2025/CAT001RS.htm',
           'https://turnir.rline.kz/2025/cskaz2025/CAT001RS.htm',
           'https://results.vistream.com.pl/FS/2526/CSGEO2025/CAT001RS.htm',
           'https://results.isu.org/results/season2526/qogfsk2025/CAT001RS.htm']

url_list_women = ['https://results.skateaustria.at/competition/saison2526/040/CAT002RS.htm',
            'https://www.isuresults.com/results/season2526/gpjpn2025/CAT002RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT002RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT002RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT002RS.htm',
           'https://ijs.usfigureskating.org/leaderboard/results/2025/36369/CAT002RS.htm',
           'https://www.jsfresults.com/InterNational/2025-2026/csjpn2025/CAT002RS.htm',
           'https://www.fisg.it/upload/result/6845/online/CAT002RS.htm',
           'https://www.kraso.sk/wp-content/uploads/sutaze/2025_2026/MON25/CAT002RS.htm',
           'http://www.deu-event.de/results/Nebelhorn_2025/CSGER2025/CAT002RS.htm',
           'https://turnir.rline.kz/2025/cskaz2025/CAT002RS.htm',
           'https://results.vistream.com.pl/FS/2526/CSGEO2025/CAT002RS.htm',
           'https://results.isu.org/results/season2526/qogfsk2025/CAT002RS.htm']

url_list_pairs = ['https://results.skateaustria.at/competition/saison2526/040/CAT003RS.htm',
            'https://www.isuresults.com/results/season2526/gpjpn2025/CAT003RS.htm',
            'https://www.isuresults.com/results/season2526/gpcan2025/CAT003RS.htm',
            'https://www.isuresults.com/results/season2526/gpchn2025/CAT003RS.htm',
            'https://results.isu.org/results/season2526/gpfra2025/CAT003RS.htm',
            'https://ijs.usfigureskating.org/leaderboard/results/2025/36395/CAT001RS.htm',
            'https://www.jsfresults.com/InterNational/2025-2026/csjpn2025/CAT003RS.htm',
            'https://www.fisg.it/upload/result/6845/online/CAT003RS.htm',
            'http://www.deu-event.de/results/Nebelhorn_2025/CSGER2025/CAT003RS.htm',
            'https://results.vistream.com.pl/FS/2526/CSGEO2025/CAT003RS.htm',
            'https://results.isu.org/results/season2526/qogfsk2025/CAT003RS.htm']

url_list_icedance = ['https://results.skateaustria.at/competition/saison2526/040/CAT004RS.htm',
                    'https://www.isuresults.com/results/season2526/gpjpn2025/CAT004RS.htm',
                    'https://www.isuresults.com/results/season2526/gpcan2025/CAT004RS.htm',
                    'https://www.isuresults.com/results/season2526/gpchn2025/CAT004RS.htm',
                    'https://results.isu.org/results/season2526/gpfra2025/CAT004RS.htm',
                    'https://www.jsfresults.com/InterNational/2025-2026/csjpn2025/CAT004RS.htm',
                    'https://www.fisg.it/upload/result/6845/online/CAT004RS.htm',
                    'https://www.kraso.sk/wp-content/uploads/sutaze/2025_2026/MON25/CAT003RS.htm',
                    'http://www.deu-event.de/results/Nebelhorn_2025/CSGER2025/CAT004RS.htm',
                    'https://turnir.rline.kz/2025/cskaz2025/CAT003RS.htm',
                    'https://results.vistream.com.pl/FS/2526/CSGEO2025/CAT004RS.htm',
                    'https://results.isu.org/results/season2526/qogfsk2025/CAT004RS.htm']

competition_ID_men = ['Graz Ice Challenge', 'GP Japan', 'GP Canada', 'GP China', 'GP France', 'CranberryCup', 'Kinoshita Group Cup 2025', 'Lombardia Trophy 2025', 'Nepela Memorial 2025', 'Nebelhorn Trophy 2025', 'Denis Ten Memorial 2025', 'Trialeti Trophy 2025', 'Olympic Qualifier'] 
competition_ID_women = ['Graz Ice Challenge', 'GP Japan', 'GP Canada', 'GP China', 'GP France', 'CranberryCup', 'Kinoshita Group Cup 2025', 'Lombardia Trophy 2025', 'Nepela Memorial 2025', 'Nebelhorn Trophy 2025', 'Denis Ten Memorial 2025', 'Trialeti Trophy 2025', 'Olympic Qualifier'] 
competition_ID_pairs = ['Graz Ice Challenge', 'GP Japan', 'GP Canada', 'GP China', 'GP France', 'John Nicks Pairs Challenge Inter. 2025', 'Kinoshita Group Cup 2025', 'Lombardia Trophy 2025', 'Nebelhorn Trophy 2025', 'Trialeti Trophy 2025', 'Olympic Qualifier'] 
competition_ID_icedance = ['Graz Ice Challenge', 'GP Japan', 'GP Canada', 'GP China', 'GP France', 'Kinoshita Group Cup 2025', 'Lombardia Trophy 2025', 'Nepela Memorial 2025', 'Nebelhorn Trophy 2025', 'Denis Ten Memorial 2025', 'Trialeti Trophy 2025', 'Olympic Qualifier'] 

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
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check that request was successful
        except:
            print('Unable to access website for ', comp_id)
            print('Skipping!')
            continue

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
                    "compID": comp_id,
                    "category": category
                })
                
    with open(f"skaters_{category}.yaml", "w") as f:
        yaml.dump({"skaters": skater_data}, f)
