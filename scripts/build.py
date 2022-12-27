#!/usr/bin/env python

L = """
hello
peter
<div>
</div>
"""

# writing to file
file1 = open('index.html', 'w')
file1.write(L)
file1.close()
