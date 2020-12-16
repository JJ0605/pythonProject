from selenium import webdriver
import time
deviceList=webdriver.Chrome()
deviceList.get("http://dkcphweb15/Xpress/28.X.Development/MDCT/select-devices")

names=deviceList.find_elements_by_xpath('//*[@id="availableDevices"]')

file = open('windowsdevice.txt', 'w', encoding='utf-8')

lists=[]

for i in names:
    device=i.text
    lists.append(device)
    print(device,i.get_attribute("href"))
    file.write(device)


print(len(lists[0].split('\n')))