import yaml
import json

with open('skaters.yaml', 'r') as file:
    yaml_skater_data = yaml.safe_load(file)

# Embed the full data as JSON string for JavaScript
data_json = json.dumps(yaml_skater_data['skaters'])

html_content = f"""
<!DOCTYPE html>
<html>
<head>
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
    <div class="container">
        <button onclick="showAllScoresGivenCategory(category='Senior Men')">Senior Men</button>
        <button onclick="showAllScoresGivenCategory(category='Senior Women')">Senior Women</button>
        <button onclick="showAllScoresGivenCategory(category='Senior Pairs')">Senior Pairs</button>
        <button onclick="showAllScoresGivenCategory(category='Senior Ice Dance')">Senior Ice Dance</button>
    </div>
    <div class="container">
        <button onclick="showAllScores()">Show All Scores</button>
        <button onclick="showUniqueHighest()">Show Unique Highest Score</button>
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
        const skaters = {data_json};

        function renderTable(data) {{
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = '';
            data.forEach((skater, index) => {{
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

        function showAllScoresGivenCategory(category) {{
            // Filter by category
            const filtered = skaters.filter(skater => skater.category === category);

            const sorted = [...filtered].sort((a, b) => parseFloat(b.points) - parseFloat(a.points));
            renderTable(sorted);
        }}

        function showAllScores() {{
            const sorted = [...skaters].sort((a, b) => parseFloat(b.points) - parseFloat(a.points));
            renderTable(sorted);
        }}

        function showUniqueHighest() {{
            const uniqueMap = new Map();
            skaters.forEach(s => {{
                if (!uniqueMap.has(s.name) || parseFloat(s.points) > parseFloat(uniqueMap.get(s.name).points)) {{
                    uniqueMap.set(s.name, s);
                }}
            }});
            const uniqueArray = Array.from(uniqueMap.values());
            uniqueArray.sort((a, b) => parseFloat(b.points) - parseFloat(a.points));
            renderTable(uniqueArray);
        }}

        // Initial render with all scores
        showAllScores();
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)