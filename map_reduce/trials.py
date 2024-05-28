import re

with open("./Assets/sample_mr.csv","r") as f:
    lines = f.readlines()
    found = re.search('^[0-9]',lines[5])
    print(found)