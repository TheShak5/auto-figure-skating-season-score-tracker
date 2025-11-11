import yaml
import json

with open('skaters_SeniorMen.yaml', 'r') as file:
    yaml_skater_data_men = yaml.safe_load(file)
with open('skaters_SeniorWomen.yaml', 'r') as file:
    yaml_skater_data_women = yaml.safe_load(file)
with open('skaters_SeniorPairs.yaml', 'r') as file:
    yaml_skater_data_pairs = yaml.safe_load(file)
with open('skaters_SeniorIceDance.yaml', 'r') as file:
    yaml_skater_data_icedance = yaml.safe_load(file)
    
# Embed the full data as JSON string for JavaScript
data_json_men = json.dumps(yaml_skater_data_men['skaters'])
data_json_women = json.dumps(yaml_skater_data_women['skaters'])
data_json_pairs = json.dumps(yaml_skater_data_pairs['skaters'])
data_json_icedance = json.dumps(yaml_skater_data_icedance['skaters'])

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="style.css" />
    <title>Skaters Points Table</title>
    <style>
        table {{ border-collapse: collapse; width: 80%; margin: auto; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: center; }}
        th {{ background-color: #f2f2f2; }}
        caption {{ font-size: 1.5em; margin: 10px; }}
        button {{ margin: 10px; padding: 10px 15px; }}
        .container {{ text-align: center; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <script src="cascade.js"></script>
    <div class="container">
        <button onclick="setCategory('SeniorMen')">Senior Men</button>
        <button onclick="setCategory('SeniorWomen')">Senior Women</button>
        <button onclick="setCategory('SeniorPairs')">Senior Pairs</button>
        <button onclick="setCategory('SeniorIceDance')">Senior Ice Dance</button>
    </div>
    <div class="container">
        <button onclick="setMode('all')">Show All Scores</button>
        <button onclick="setMode('unique')">Show Unique Highest Score</button>
    </div>
    <table>
        <caption>Skaters Scores and Rankings</caption>
        <thead>
            <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Country</th>
                <th>Points</th>
                <th>Competition</th>
            </tr>
        </thead>
        <tbody id="tableBody"></tbody>
    </table>

    <script>
        let skaters = {data_json_men};
        let selectedCategory = 'SeniorMen'; // store currently selected category
        let selectedMode = 'all'; // 'all' or 'unique'

        function setCategory(category){{
            selectedCategory = category;

            if(category=='SeniorMen'){{
                skaters = {data_json_men};
            }}

            if(category=='SeniorWomen'){{
                skaters = {data_json_women};
            }}

            if(category=='SeniorPairs'){{
                skaters = {data_json_pairs};
            }}

            if(category=='SeniorIceDance'){{
                skaters = {data_json_icedance};
            }}

            updateTable();
        }}

        function setMode(mode){{
            selectedMode = mode;
            updateTable();
        }}

        function getFilteredSkaters(){{
            if (selectedCategory){{
            return skaters.filter(s => s.category === selectedCategory);
            }}
            return skaters;
        }}
        
        function renderTable(data) {{
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = '';
            data.forEach((skater, index) => {{
                // Determine the row class for top 3 ranks
                let rowClass = '';
                if (index === 0){{
                    rowClass = 'gold-row';
                }} else if (index === 1) {{
                    rowClass = 'silver-row';
                }} else if (index === 2) {{
                    rowClass = 'bronze-row';
                }}
                const row = `<tr>
                    <td>${{index + 1}}</td>
                    <td>${{skater.name}}</td>
                    <td>${{skater.country}}</td>
                    <td>${{skater.points}}</td>
                    <td>${{skater.compID}}</td>
                </tr>`;
                tbody.insertAdjacentHTML('beforeend', row);
            }});
        }}

        # function updateTable(){{
        #     let filtered = getFilteredSkaters();
        #     let dataToShow = [];

        #     if (selectedMode === 'unique'){{
        #     const uniqueMap = new Map();
        #     filtered.forEach(s =>{{
        #         if (!uniqueMap.has(s.name) || parseFloat(s.points) > parseFloat(uniqueMap.get(s.name).points)){{
        #         uniqueMap.set(s.name, s);
        #         }}
        #     }});
        #     dataToShow = Array.from(uniqueMap.values());
        #     }} else {{
        #         dataToShow = [...filtered];
        #     }}

        #     dataToShow.sort((a, b) => parseFloat(b.points) - parseFloat(a.points));
        #     renderTable(dataToShow);
        # }}

        function updateTable(){{
            let filtered = getFilteredSkaters();
            let dataToShow = [];

            if (selectedMode === 'unique'){{
                const uniqueMap = new Map();
                filtered.forEach(s =>{{
                    if (!uniqueMap.has(s.name) || parseFloat(s.points) > parseFloat(uniqueMap.get(s.name).points)){{
                        uniqueMap.set(s.name, s);
                    }}
                }});
                dataToShow = Array.from(uniqueMap.values());
            }} else {{
                dataToShow = [...filtered];
            }}

            // Sort descending by points
            dataToShow.sort((a, b) => parseFloat(b.points) - parseFloat(a.points));

            // Add rank to each item starting from 1
            dataToShow.forEach((item, index) => {{
                item.rank = index + 1;
            }});

            // Now modify your renderTable to use this rank for row coloring
            renderTable(dataToShow);
        }}

        // Initial render
        updateTable();
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)