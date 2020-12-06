import sys
import json
import requests
import csv
import socket
import ast
from tkinter import *


def trigger_api(ip):
  querystring = {"ip": ip}
  url = "https://geo.ipify.org/api/v1?apiKey=at_LHZrfcs9aoOIVLAmHfZdyGOj9hzKW&ipAddress="+ip

  response =  requests.request('GET', 'http://ip-api.com/json/'+ip)

  if(200 == response.status_code):
    return json.loads(response.text)
  else:
    return None


root = Tk()
root.title('Geolocation Tracker')
root.geometry("800x500")

def connectip():
  s = socket.socket()
  port=12347
  s.connect(('127.0.0.1', port))
  api_response=s.recv(1024).decode()
  s.close()
  return api_response

def convert(api_response):
    temp=api_response.split(",")
    temp=[x.strip("'") for x in temp]
    temp=[x.strip("{") for x in temp]
    temp=[x.split(":") for x in temp]

    temp[len(temp)-1][1]=temp[len(temp)-1][1].split(".")    
    temp[len(temp)-1][1]=[x.strip("\"} ") for x in temp[len(temp)-1][1]]
    temp[len(temp)-1][1]=[temp[len(temp)-1][1][0],temp[len(temp)-1][1][1],temp[len(temp)-1][1][2],temp[len(temp)-1][1][3]]
    temprem=temp[len(temp)-1][1][3]
    temprem=temp[len(temp)-1][1][3].split("\"")
    temp[len(temp)-1][1][3]=temprem[0]
    
    iptemp="."
    iptemp=iptemp.join(temp[len(temp)-1][1])
    data={
      'status':temp[0][1][2:],
      'country':temp[1][1][2:],
      'countryCode':temp[2][1][2:],
      'region':temp[3][1][2:],
      'regionName':temp[4][1][2:],
      'city':temp[5][1][2:],
      'zip':temp[6][1][2:],
      'lat':temp[7][1].lstrip("'"),
      'lon':temp[8][1].lstrip("'"),
      'timezone':temp[9][1][2:],
      'isp':temp[10][1][2:],
      'as':temp[12][1][2:],
      'ip':iptemp[1:],
    }
    return data
    


def location():
  print("GUI REQUESTED NEW DATA.....")
  api_response=connectip()
  api_response=convert(api_response)
  # print("Getting details for IP: " + ip+".....")
  l1.config(text="Getting details for IP: " +api_response['ip']+".....")
  # print("Details:")
  l2.config(text="--DETAILS--")

  l3.config(text='Status : ' + api_response['status'])
  l4.config(text='Country : ' + api_response['country'])
  l5.config(text='CountryCode : ' + api_response['countryCode'])
  l6.config(text='Region : ' + api_response['region'])
  l7.config(text='RegionName : ' + api_response['regionName'])
  l8.config(text='City : ' + api_response['city'])
  l9.config(text='Zip : ' + api_response['zip'])
  l10.config(text='LAT : ' + str(api_response['lat']))
  l11.config(text='LON : ' + str(api_response['lon']))
  l12.config(text='Timezone : ' + api_response['timezone'])
  l13.config(text='ISP : ' + api_response['isp'])
  l15.config(text='AS : ' + api_response['as'])



bg = PhotoImage(file="bg.png")

label=Label(root,image=bg)
label.place(x=0,y=0,relwidth=1,relheight=1)

button = Button(root, text="Click me to get your location!", padx=20, pady=10, command=location, bg='white')
# button.config(font=("Robotto", 10))
button.pack(pady=10)

l1 = Label(root,text="IP?",fg="white",bg="black",padx='3')
l1.pack(pady=3)
l1.config(font=("Robotto", 12))
l2 = Label(root,text="Details?",fg="white",bg="black",padx='3')
l2.pack(pady=3)
l2.config(font=("Robotto", 12))
l3 = Label(root,text="Status?",fg="white",bg="black",padx='3')
l3.pack(pady=3)
l3.config(font=("Robotto", 12))
l4 = Label(root,text="Country?",fg="white",bg="black",padx='3')
l4.pack(pady=3)
l4.config(font=("Robotto", 12))
l5 = Label(root,text="CountryCode?",fg="white",bg="black",padx='3')
l5.pack(pady=3)
l5.config(font=("Robotto", 12))
l6 = Label(root,text="Region?",fg="white",bg="black",padx='3')
l6.pack(pady=3)
l6.config(font=("Robotto", 12))
l7 = Label(root,text="RegionName?",fg="white",bg="black",padx='3')
l7.pack(pady=3)
l7.config(font=("Robotto", 12))
l8 = Label(root,text="City?",fg="white",bg="black",padx='3')
l8.pack(pady=3)
l8.config(font=("Robotto", 12))
l9 = Label(root,text="ZIP?",fg="white",bg="black",padx='3')
l9.pack(pady=3)
l9.config(font=("Robotto", 12))
l10 = Label(root,text="LAT?",fg="white",bg="black",padx='3')
l10.pack(pady=3)
l10.config(font=("Robotto", 12))
l11 = Label(root,text="LON?",fg="white",bg="black",padx='3')
l11.pack(pady=3)
l11.config(font=("Robotto", 12))
l12 = Label(root,text="Timezone?",fg="white",bg="black",padx='3')
l12.pack(pady=3)
l12.config(font=("Robotto", 12))
l13 = Label(root,text="ISP?",fg="white",bg="black",padx='3')
l13.pack(pady=3)
l13.config(font=("Robotto", 12))
l15 = Label(root,text="AS?",fg="white",bg="black",padx='3')
l15.pack(pady=3)
l15.config(font=("Robotto", 12))


root.mainloop()


if __name__ == "__main__":
  # location()
  print("GUI CLOSED")
