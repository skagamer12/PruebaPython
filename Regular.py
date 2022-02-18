import math
import re

print("Regular expresions :3")
print("**********************\n")

pattern = r"spam"

# if re.match(pattern, "spamspamspam"):
#     print("Match")
# else:
#     print("No manches como esto bva a hacer match")

# if re.search(pattern,"spalspolspanspa2m"):
#     print("Cheee vos lo encontraste")
# else:
#     print("Sos re maleta weon")

match = re.search(pattern,"eggspamsausage")
if math:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


str = ("Che boludo sho soy el Duyinooo. Alo pelotudo")
partner = r"o"

newstr = re.sub(partner, "º", str)
print(newstr)
"""
# Metacharacters

patern = r"^gr.y$"

if re.match(patern, "grey"):
    print("Match 1")
if re.match(patern, "gray"):
    print("Match 2")
if re.match(patern, "stingray"):
    print("Match 3")
"""
# patern = r"[^0-9]"

# if re.search(patern, "123"):
#     print("Match 1")
# if re.search(patern, "qwert2yuiop"):
#     print("Match 2")
# if re.search(patern, "rhythma myths"):
#     print("Match 3")

# partner = r"a(bc)(de)(f(g)h)i"
# match = re.match(partner,"abcdefghijklmnop")
# if match:
#     print(match.group())
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group())
# number = r"9{1,3}$"

# if re.match(number, "9"):
#     print("Match 1")

# if re.match(number, "999"):
#     print("Match 2")

# if re.match(number, "99999"):
#     print("Match 3")

# partner = r"gr(a|e)y"

# match = re.match(partner, "grey")

# if match:
#     print("match1")

# match = re.match(partner, "gray")

# if match:
#     print("match2")

# match = re.match(partner, "groy")

# if match:
#     print("match3")



partner = r"([01])+0$ \1"

match = re.match(partner, "011101")

if match:
    print("match1")

match = re.match(partner, "0101")

if match:
    print("match2")

match = re.match(partner, "10101111001010")

if match:
    print("match3")


print("*******************")

partner = r"(\D+\d)"

match = re.match(partner, "hI 666")

if match:
    print("match1")

match = re.match(partner, "1, 23, 456!")

if match:
    print("match2")

match = re.match(partner, "! 2$?")

if match:
    print("match3")

print("*******************")

partner = r"\b(cat)\b"

match = re.match(partner, "THE >CAT< SAT!")

if match:
    print("match1")

match = re.match(partner, "We s>cat<tared?")

if match:
    print("match2")

match = re.match(partner, "We s>cat< scattered.")

if match:
    print("match3")

print("*******************")

partner = r"(189)"

match = re.match(partner, "hI 666")

if match:
    print("match1")

match = re.match(partner, "1, 23, 456!")

if match:
    print("match2")

match = re.match(partner, "! 2$?")

if match:
    print("match3")