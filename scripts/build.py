#!/usr/bin/env python
import shutil

shutil.copy("main.css", "../_cards/main.css")


header = """
<html>
<head>
  <link rel="stylesheet" href="main.css">
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
  <div class="uid">
    {}
  </div>
  <img src="./img/{}.jpeg" />
  <div class="word">
    {}
  </div>
</div>
"""

cards = ''
for line in Lines:
    count += 1
    uid = line.strip().split()[0]
    word = line.strip().split()[1]
    cards = cards + temp.format(uid, uid, word)
  

content = header + cards + footer

# writing to file
file1 = open('../_cards/index.html', 'w')
file1.write(content)
file1.close()