f = open('07_input.txt', 'r')
input = f.read()
f.close()

ips = input.split('\n')

count = 0
for ip in ips:
	
