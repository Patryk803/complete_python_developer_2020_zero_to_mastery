import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string= 'Patryk@gmail.com'

a = pattern.search(string)
print(a)

#Email validator 
#Go to https://emailregex.com/


