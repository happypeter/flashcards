#!/usr/bin/env python
import os
import shutil

if os.path.exists('../_cards'):
  shutil.rmtree('../_cards')

os.system("mv ~/Desktop/*.jpeg ../img/")

os.mkdir('../_cards')
os.symlink("../scripts/main.css", "../_cards/main.css")
os.symlink("../img/", "../_cards/img")


header = """
<html>
<head>
  <link rel="stylesheet" href="./main.css">
</head>
<body>
"""

footer = """
</body>
</html>
"""

file2 = open('../words.md', 'r')

Lines = file2.readlines()
  
count = 0

temp = """
<div class="card">
  <img src="./img/{}.jpeg" />
  <h2 class="word">
    {}
  </h2>
</div>
"""

cards = ''
for line in Lines:
    count += 1
    uid = line.strip().split()[0]
    word = line.strip()
    cards = cards + temp.format(uid, word)

content = header + cards + footer

# writing to file
file1 = open('../_cards/index.html', 'w')
file1.write(content)
file1.close()
