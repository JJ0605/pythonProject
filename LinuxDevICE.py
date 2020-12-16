from selenium import webdriver
from time import sleep

deviceList=webdriver.Chrome()
deviceList.get("http://dkcphweb15/Xpress/28.X.Development/MDCT/thin-client")
device=deviceList.find_element_by_class_name("button-container").click()
names=deviceList.find_elements_by_xpath('//*[@id="availableDevices"]')

file = open('linux.txt', 'w', encoding='utf-8')

lists=[]

for i in names:
    device=i.text
    lists.append(device)
    print(device,i.get_attribute("href"))
    file.write(device)


print(len(lists[0].split('\n')))