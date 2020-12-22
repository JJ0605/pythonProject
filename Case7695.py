# Case 7695
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import os
from main import getDeviceName
from main import isElementExist
from main import deviceFolder
from main import isInputExist


##实例化浏览器并显示
print("7695 is begin")

options = webdriver.ChromeOptions()
prefs = {"download.default_directory": "C:\\download\\" + getDeviceName(), "download.prompt_for_download": False}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)
# 导入网址
browser.get("http://dkcphweb15/Xpress/28.X.Development/MDCT/thin-client")
# sleep(3)
# 定位元素
# name=browser.find_element_by_link_text('NEXT >').click()
# 获取页面网址判断是否成功
strs = browser.current_url
if strs == "http://dkcphweb15/Xpress/28.X.Development/MDCT/thin-client":
    print('Into thin-clinet success')
else:
    print('Fail,Something wrongs')

# 进入到设备列表页
# deviceName=simpledialog.askstring('Input device name','',initialvalue='')
device = browser.find_element_by_class_name("button-container").click()
strs = browser.current_url
if strs == "http://dkcphweb15/Xpress/28.X.Development/MDCT/select-devices":
    print('Enter select-devices page success')
else:
    print('Enter select-devices page fail')

# 选择设备添加到右侧中
browser.find_element_by_xpath("//label[contains(text(),'" + getDeviceName()+ "')]").click()
browser.find_element_by_id('btnAdd').click()

# 进入到设置项页
browser.find_element_by_xpath("//input[@value='NEXT >']").click()

# 判断
strs = browser.current_url
if strs == "http://dkcphweb15/Xpress/28.X.Development/MDCT/configuration":
    print('Enter cofiguretion')
else:
    print('Enter cofiguretion fail')

# 选择版本
fw_select = browser.find_element_by_css_selector("select[name='configurationViewModel.Devices[0].SelectedFirmware.Id']")
fw_verision = Select(fw_select).options
print("-----------------------------------------------------")
print("Verision list:")
for i in fw_verision:
    print(i.text)
print("-----------------------------------------------------")
Select(fw_select).select_by_index("1")

# 获取设置表格的行数
set_table = browser.find_element_by_class_name('settings-table')
td_content = set_table.find_elements_by_tag_name('tr')
set_content = browser.find_element_by_class_name("setting-name")
table_tr_number = len(td_content)
# print('Setting table has '+str(table_tr_number)+' rows:')

# 遍历所有的设置项并进行选择
# 特殊情况：关联项和非选择框（输入框）处理
i = 0
while i < table_tr_number:
    flag = isElementExist(
        "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']")
    if flag:
        setting = browser.find_element_by_css_selector(
            "select[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']")
        if Select(setting):
            Select(setting).select_by_index("1")
            i = i + 1
            continue
    elif isInputExist(
            "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(i) + "].SelectedValue']"):
        browser.find_element_by_css_selector(
            "input[name='configurationViewModel.Devices[0].SelectedFirmware.Settings[" + str(
                i) + "].SelectedValue']").send_keys('2020')
        i = i + 1
        continue
    else:
        i = i + 1
        continue

# TODO 对于有些输入框是在关联项之前，因此会出现在遍历到该输入框时无法输入，而后当勾选了关联项之后又需要输入的现象
# TODO 目前想到的解决思路是，当“NEXT”按钮是灰色的时候，进行设置项表格中输入框的重新遍历

# 输入选择项
fw_selected = Select(fw_select).first_selected_option
print(fw_selected.text)
print('Configure finish')
# #进入softphone配置页
browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# #进入到下载页
# browser.find_element_by_xpath("//input[@value='NEXT >']").click()

# 进入到summary页面
browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# 下载Summary
browser.find_element_by_xpath("//input[@value='DOWNLOAD SUMMARY']").click()
# 重命名summary文件
sleep(5)
summary = deviceFolder() + '\\summary.html'
renamesummary = deviceFolder() + '\\7695.html'
try:
    os.rename(summary, renamesummary)
    print(getDeviceName() + '7695 summary download successful')
    summary = deviceFolder() + '\\JabraXpressFiles.zip'
    renamesummary = deviceFolder() + '\\7695.zip'
except Exception as e:
    print(e)
# 返回到下载页
browser.find_element_by_xpath("//input[@value='< PREVIOUS']").click()
# 勾选同意协议
browser.find_element_by_id('eulaOk').click()
# 输入网址：
browser.find_element_by_css_selector("input[name='localServerUrl']").send_keys('http://my.gn.com/')
# #点击下载
browser.find_element_by_id('downloadZip').click()
sleep(80)
try:
    os.rename(summary, renamesummary)
    print(getDeviceName() + '7695 download successful')
    browser.close()
except Exception as e:
    sleep(40)
    os.rename(summary, renamesummary)
    print('rename success')
    browser.close()
