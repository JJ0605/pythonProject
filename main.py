from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from time import sleep


#自动下载，无需点击
auotDownload=webdriver.ChromeOptions()
#prefs={'profile.default_content_settings.popups':0,'download.default_directory':'c:\\'}
prefs = {"download.default_directory": "c:\download","download.prompt_for_download": False,}
auotDownload.add_experimental_option('prefs',prefs)


#实例化浏览器

#不显示窗口
option=Options()
option.add_argument('--headless')
# option.add_argument("--user-data-dir="+r"C:/Users/extalin/AppData/Local/Google/Chrome/User Data/")
browser=webdriver.Chrome()
# browser=webdriver.Chrome(chrome_options=option)
# browser.command_executor._commands["send_command"]=("POST", '/session/$sessionId/chromium/send_command')
# params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': "c:\download"}}
# command_result=browser.execute("send_command",params)

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
device=browser.find_element_by_class_name("button-container").click()
strs = browser.current_url
if strs=="http://dkcphweb15/Xpress/28.X.Development/MDCT/select-devices":
    print('Enter select-devices page success')
else:
    print('Fail,Something wrongs')

#选择设备添加到右侧中
browser.find_element_by_xpath("//label[contains(text(),'Jabra BIZ 2400 II Duo')]") .click()
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
#TODO 统计该设备所有设置项的个数

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
        print("似乎设置失败了")
        i=i+1
        continue



#判断元素是否存在的方法;

#输入选择项
fw_selected=Select(fw_select).first_selected_option
print(fw_selected.text)
print('Configure finish')
# #进入softphone配置页
browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# #进入到下载页
# browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# #勾选同意协议
# browser.find_element_by_id('eulaOk').click()
# #点击下载
# browser.find_element_by_id('download64bit').click()