#!/usr/bin/python3
import re
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(re.findall(r'object-oriented programming', str)[0])
