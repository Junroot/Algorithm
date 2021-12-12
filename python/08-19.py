import re
p = re.compile(r"^(.+\s\d+[-]\d+[-])\d+", re.MULTILINE)

phone_numbers = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

print(p.sub(r"\g<1>####", phone_numbers))
