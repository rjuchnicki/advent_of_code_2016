import re

f = open('07_input.txt', 'r')
ips = f.read().split('\n')
f.close()

def is_valid(ip):
    # Return false if any characters between square brackets form an ABBA. 
    for bracketed in re.finditer(r'\[[\w]*(\w)(\w)\2\1[\w]*\]', ip):
        abbas = re.findall(r'(\w)(\w)\2\1', bracketed.group(0))
        for abba in abbas:
            if abba[0] != abba[1]:
                return False

    # Any remaining ABBA's should be outside brackets. Return true if there are
    # any.
    for abba in re.findall(r'(\w)(\w)\2\1', ip):
        if abba[0] != abba[1]:
            return True

count = 0
for ip in ips:
    if is_valid(ip):
        count += 1
print count
