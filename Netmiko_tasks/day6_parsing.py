import os
script_directiry = os.path.dirname(os.path.abspath(__file__))
key_word = "hostname"
filename = os.path.join(script_directiry, "backup-router-2025-12-19.txt")

print(f"serching key word {key_word} in: {filename}....")
found_keyword = False

with open(filename, 'r') as file:
    for line in file:
        if key_word in line and "location" not in line:
            words = line.split()
            actual_name = words[1]
            print (f"found it : {actual_name}")
            found_keyword = True
if not found_keyword:
    print (f"Cant find key word - {key_word} in {filename}")