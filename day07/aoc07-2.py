import re

f = open('07_input.txt', 'r')
ips = f.read().split('\n')
f.close()

def supports_ssl(ip):
    babs = []
    for bracketed in re.finditer(r'\[[\w]*(\w)\w\1[\w]*\]', ip):
        s = bracketed.group(0)[1:-1]
        for i in xrange(2, len(s)):
            candidate = s[i-2:i+1]
            if candidate[0] == candidate[2] and candidate[0] != candidate[1]:
                babs.append(candidate)

    abas = []
    non_bracketed = [re.sub(r'\w*\]', '', s) for s in ip.split('[')]
    for s in non_bracketed:
        for i in xrange(2, len(s)):
            candidate = s[i-2:i+1]
            if candidate[0] == candidate[2] and candidate[0] != candidate[1]:
                abas.append(candidate)
    
    for aba in abas:
        for bab in babs:
            if aba[0] == bab[1] and aba[1] == bab[0]:
                return True

    return False

count = 0
for ip in ips:
    if supports_ssl(ip):
        count += 1
print count
