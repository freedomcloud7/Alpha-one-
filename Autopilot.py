import os

# ENTER YOUR ID HERE
TRACKING_ID = "yourid-20" 

# Content Library
data = [
    {"p": "Logitech MX Master 3 Reset", "l": "https://www.amazon.com/s?k=Logitech+MX+Master+3"},
    {"p": "Canon EOS R5 Manual", "l": "https://www.amazon.com/s?k=Canon+EOS+R5+Guide"},
    {"p": "Sony WH-1000XM4 Battery Fix", "l": "https://www.amazon.com/s?k=XM4+Replacement+Battery"}
]

with open("index.html", "r") as f:
    html = f.read()

# Generate new links with your ID
new_entries = ""
for item in data:
    link = f"{item['l']}&tag={TRACKING_ID}"
    new_entries += f"<li><a href='{link}'>{item['p']} Solutions</a></li>"

updated_html = html.replace("", 
                            f"<ul>{new_entries}</ul>")

with open("index.html", "w") as f:
    f.write(updated_html)
