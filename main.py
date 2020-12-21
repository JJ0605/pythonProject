from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from tkinter import simpledialog
from time import sleep
from tkinter import *
import os

#赋予按钮功能
def submit():
    printdevice()
    closewindow()
def printdevice():
    print(u.get())
def closewindow():
    root.destroy()
def mkdir(path):
    folder=os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print('Create Success')
    else:
        print("--- Device Folder is exist ----")


#定义输入设备的窗口
root=Tk()
root.title('GET DEVICE NAME')
frame=Frame(root)
frame.pack(padx=8,pady=8,ipadx=4) #设置边距
label=Label(frame,text="Device Name:")
label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

#定义窗口内容
u=StringVar()
deviceget=Entry(frame,textvariable=u)
deviceget.grid(row=0,column=1,sticky='ew',columnspan=2)
button = Button(frame, text="OK",command=submit,default='active')
button.grid(row=2,column=1)

#居中显示窗口和窗口大小
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.geometry('380x80')
root.mainloop()

#创建一个设备的文件夹
file="C:\\download\\"+u.get()
#实例化浏览器

#配置下载的选择项
options=webdriver.ChromeOptions()
prefs = {"download.default_directory": "C:\\download\\"+u.get(),"download.prompt_for_download": False}
options.add_experimental_option('prefs',prefs)
# 不显示浏览器
# option=Options()
# option.add_argument('--headless')
# browser=webdriver.Chrome(chrome_options=option)

#显示浏览器
browser=webdriver.Chrome(chrome_options=options)

#导入网址
browser.get("http://dkcphweb15/Xpress/28.X.Development/MDCT/thin-client")
#sleep(3)
#定位元素
# name=browser.find_element_by_link_text('NEXT >').click()
#获取页面网址判断是否成功
strs = browser.current_url
if strs=="http://dkcphweb15/Xpress/28.X.Development/MDCT/thin-client":
    print('Into thin-clinet success')
else:
    print('Fail,Something wrongs')

#进入到设备列表页
#deviceName=simpledialog.askstring('Input device name','',initialvalue='')
device=browser.find_element_by_class_name("button-container").click()
strs = browser.current_url
if strs=="http://dkcphweb15/Xpress/28.X.Development/MDCT/select-devices":
    print('Enter select-devices page success')
else:
    print('Fail,Something wrongs')

#选择设备添加到右侧中
browser.find_element_by_xpath("//label[contains(text(),'"+u.get()+"')]") .click()
browser.find_element_by_id('btnAdd').click()

#进入到设置项页
browser.find_element_by_xpath("//input[@value='NEXT >']").click()

#判断
strs = browser.current_url
if strs=="http://dkcphweb15/Xpress/28.X.Development/MDCT/configuration":
    print('Third success')
else:
    print('Fail,Something wrongs')

#选择版本

fw_select = browser.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
fw_verision=Select(fw_select).options
print("-----------------------------------------------------")
print("Verision list:")
for i in fw_verision:
    print(i.text)
print("-----------------------------------------------------")
Select(fw_select).select_by_index("1")


def isElementExist(element):
    flag = True
    try:
        browser.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag

def isInputExist(element):
    try:
        browser.find_element_by_css_selector(element)
        return True
    except:
        return False


#获取设置表格的行数
set_table=browser.find_element_by_class_name('settings-table')
td_content=set_table.find_elements_by_tag_name('tr')
set_content=browser.find_element_by_class_name("setting-name")
table_tr_number=len(td_content)
print('Setting table has '+str(table_tr_number)+' rows:')

# 遍历所有的设置项并进行选择
# 特殊情况：关联项和非选择框（输入框）处理
i=0
while i<table_tr_number:
    flag=isElementExist("select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings["+str(i)+"].SelectedValue']")
    if flag:
        setting = browser.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']")
        if Select(setting):
            Select(setting).select_by_index("1")
            i = i + 1
            continue
    elif isInputExist("input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings["+str(i)+"].SelectedValue']"):
        browser.find_element_by_css_selector("input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']").send_keys('2020')
        i = i + 1
        continue
    else:
        i=i+1
        continue
#输入选择项
fw_selected=Select(fw_select).first_selected_option
print(fw_selected.text)
print('Configure finish')
# #进入softphone配置页
browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# #进入到下载页
# browser.find_element_by_xpath("//input[@value='NEXT >']").click()

#进入到summary页面
browser.find_element_by_xpath("//input[@value='NEXT >']").click()
#下载Summary
browser.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
# 重命名summary文件
sleep(5)
summary=file+'\\summary.html'
renamesummary=file+'\\6551.html'
try:
    os.rename(summary,renamesummary)
    print(u.get()+'6551 summary download successful')
    summary = file+'\\JabraXpressFiles.zip'
    renamesummary = file+'\\6551.zip'
except Exception as e:
    print(e)
#返回到下载页
browser.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
#勾选同意协议
browser.find_element_by_id('eulaOk').click()
#输入网址：
browser.find_element_by_css_selector("input[name='localServerUrl']").send_keys('http://my.gn.com/')
# #点击下载
browser.find_element_by_id('downloadZip').click()
sleep(80)
try:
    os.rename(summary,renamesummary)
    print(u.get()+'6551 download successful')
except Exception as e:
    sleep(40)
    os.rename(summary,renamesummary)
    print('rename success')
