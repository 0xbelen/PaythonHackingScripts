import nmap

scanner = namp.PortScanner()
target =input(f"Enter the target IP address: ")
scanner.scan(target, '1-1000','-sV')  # Scan ports from 1 to  1000 with -sV option which shows version of services running on those ports

print("the host name is:" +  scanner[target].hostname())
print ("the host status is :" + scanner[target].state())

keys = scanner[target]['tcp'].keys()
for i in keys:
    print("-------------------------")
    print('the port :' + str(i) + ":")
    res = scanner[target]['tcp'][i]
    for re in res:
        print(re + ":" + res[re])

#print(keys)

