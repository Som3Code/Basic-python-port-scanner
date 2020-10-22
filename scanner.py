import socket
from IPy import IP

echo "# Basic-python-port-scanner" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Som3Code/Basic-python-port-scanner.git
git push -u origin main

print("")

while True:
    def scan(target):
        converted_ip = check_ip(target)
        print('\n' + '[Scanning.....] ' + str(target))
        print("")
        for port in range(0,100):
            scan_port(converted_ip, port)

    def check_ip(ip):
        try:
            IP(ip)
            return(ip)
        except ValueError:
            return socket.gethostbyname(ip)

    def scan_port(ipaddress, port):

        try:
            sock = socket.socket()

            sock.settimeout(0.100)

            sock.connect((ipaddress, port))
    
            print("[+] Port " + str(port) + " is open")
        except:
            
            pass
    print("")
    targets = input("[X] Enter Ip/website[ , to split scan]: ")
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)


    print("")
  


        