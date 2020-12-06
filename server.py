# import socket programming library 
import socket 

# import thread module 
from _thread import *
import threading 
import sys
import json
import requests
import csv
import socket
from signal import signal, SIGINT
from sys import exit

ip=requests.get('https://api.ipify.org').text #public ip
iptable=[]

print_lock = threading.Lock() 

def handler(signal_received,frame):
    data = {}
    f = open('sample.json',)
    d = json.load(f)
    f.close()
    d['count']=d['count']+1
    # temp = "IP-Login-"+str(d['count'])
    num = d['count']
    temp = 'IP-Login-' + str(num)
    d[temp]=[]
    print("\nCurent IPTABLE before Terminating the Program:")
    ind=1
    print("Index\t\t\t","IPs")
    print("----------------------------------------------------------------------------")
    if not iptable:
        print("IPTABLE IS EMPTY!!!")
    else:
        for x in iptable:
            d[temp].append({
                'Index':ind,
                'IP No.':x
                })
            print(str(ind),"\t\t\t",x)
            ind+=1
    with open('sample.json', 'w') as outfile:
        json.dump(d, outfile)
    sys.exit()


def trigger_api(ip):
  querystring = {"ip": ip}
  url = "https://geo.ipify.org/api/v1?apiKey=at_LHZrfcs9aoOIVLAmHfZdyGOj9hzKW&ipAddress="+ip

  response =  requests.request('GET', 'http://ip-api.com/json/'+ip)

  if(200 == response.status_code):
    return json.loads(response.text)
  else:
    return None

def main(ip):
          
    print("Getting details for IP: " + ip+".....")
    print("Details Sent!!!")
    api_response = trigger_api(ip)
    return api_response

def splitip():
    global ip
    ip1=ip.split(".")
    temp=int(ip1[3])+1
    if(temp>255):
        temp-=254
    ip1[3]=str(temp)
    ip="."
    ip=ip.join(ip1)


# thread function 
def threaded(c,addr):
    flag=0
    global ip,iptable
    for i in range(len(iptable)):
        if(iptable[i][0][1]==addr[1] and iptable[i][0][0]==addr[0]):
            flag=1
            ip=iptable[i][1][0]
            break
    if(flag==0): iptable.append([addr,(ip,addr[1])])
    print_lock.release()
    info=main(ip)
    c.send(str(info).encode())
    c.close()
    splitip()



    

def Main(): 
	host = "" 

	# reverse a port on your computer 
	# in our case it is 12345 but it 
	# can be anything 
	port = 12347
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 

	# put the socket into listening mode 
	s.listen(5) 
	print("socket is listening") 

	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		c, addr = s.accept() 

		# lock acquired by client 
		print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,addr)) 
	s.close() 


if __name__ == '__main__':
    signal(SIGINT,handler)
    Main()
