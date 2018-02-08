import re
p = re.compile('ab*')
#p = re.compile('ab*', re.IGNORECASE)

#raw string so that backslashes don't need to be escaped  
p = re.compile(r'ab*')

p.findall("string")

p.match("string") # match returns None if not found
# or
re.match("string")
