import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())