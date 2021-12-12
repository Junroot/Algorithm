import re

p = re.compile(".*[@].*[.](?=com$|net$)", re.MULTILINE)

print(p.match("pahkey@gmail.com"))
print(p.match("kim@daum.net"))
print(p.match("lee@myhome.co.kr"))
