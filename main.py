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
browser=webdriver.Chrome(options=option)
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
    print('fist success')
else:
    print('Fail,Something wrongs')

#进入到设备列表页
device=browser.find_element_by_class_name("button-container").click()
strs = browser.current_url
if strs=="http://dkcphweb15/Xpress/28.X.Development/MDCT/select-devices":
    print('second success')
else:
    print('Fail,Something wrongs')

#选择设备添加到右侧中
browser.find_element_by_xpath("//label[contains(text(),'Jabra SPEAK 510')]") .click()
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

#获取设置表格的行数
set_table=browser.find_element_by_class_name('settings-table')
td_content=set_table.find_elements_by_tag_name('tr')
set_content=browser.find_element_by_class_name("setting-name")
table_tr_number=len(td_content)
print('Setting table has '+str(table_tr_number)+' rows:')
#输入选择项
fw_selected=Select(fw_select).first_selected_option
print(fw_selected.text)
print('finish')
# #进入softphone配置页
# browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# #进入到下载页
# browser.find_element_by_xpath("//input[@value='NEXT >']").click()
# #勾选同意协议
# browser.find_element_by_id('eulaOk').click()
# #点击下载
# browser.find_element_by_id('download64bit').click()