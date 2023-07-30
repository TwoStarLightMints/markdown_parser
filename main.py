SPECIAL_CHARACTERS = [
    "#"
]

with open("markdown_doc.md", "r") as m:
    content = m.readlines()

parsed = list()

for line in content:
    if line.startswith("#"):
        final = line.rfind("#")        

        parsed.append(f"<h{final+1}>{line[final+2:]}</h{final+1}>")

print(parsed)