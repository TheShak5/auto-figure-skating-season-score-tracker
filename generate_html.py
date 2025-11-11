import yaml

# Parse YAML
# data = yaml.safe_load(yaml_data)
with open('skaters_men.yaml', 'r') as file:
    yaml_skater_data = yaml.safe_load(file)


# Sort skaters by points (convert points string to float for sorting)
sorted_skaters = sorted(yaml_skater_data['skaters'], key=lambda x: float(x['points']), reverse=True)

# Generate HTML table
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Skaters Points Table</title>
    <style>
        table { border-collapse: collapse; width: 80%; margin: auto; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: center; }
        th { background-color: #f2f2f2; }
        caption { font-size: 1.5em; margin: 10px; }
    </style>
</head>
<body>
    <a href="test.html" class="linkstyle">test</a>
    <table>
        <caption>Skaters Ranked by Points (Highest to Lowest)</caption>
        <thead>
            <tr>
                <th>Rank</th>
                <th>Name</th>
                <th>Country</th>
                <th>Points</th>
                <th>Competition ID</th>
            </tr>
        </thead>
        <tbody>
"""

# Add table rows
for rank, skater in enumerate(sorted_skaters, start=1):
    html_content += f"""
            <tr>
                <td>{rank}</td>
                <td>{skater['name']}</td>
                <td>{skater['country']}</td>
                <td>{skater['points']}</td>
                <td>{skater['compID']}</td>
            </tr>
    """

# Closing tags
html_content += """
        </tbody>
    </table>
</body>
</html>
"""

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)