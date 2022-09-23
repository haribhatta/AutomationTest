import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleBillingReports as LBR
import Library.LibModuleSettings as LS
from selenium.webdriver.common.by import By
import math

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
userName = GSV.foUserName
#
opdRate = GSV.opdRate
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(GSV.adminUserID, GSV.adminUserPwD)
#LB.counteractivation(EMR)
time.sleep(2)

# 1. User Collection Report
print("Start getting Payment Wise Report")
EMR.find_element(By.LINK_TEXT, "Reports").click()
time.sleep(3)
EMR.find_element(By.LINK_TEXT, "Billing Reports").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//i[contains(text(),'User Collection')]").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
time.sleep(4)
netCashCollection1 = EMR.find_element(By.XPATH, "//td[contains(text(),' Total Collection ')]/following-sibling::td").text
netCashCollection1 = netCashCollection1.replace(',', '')
print("netCashCollection1:", netCashCollection1)
netSales1 = EMR.find_element(By.XPATH, "//td[contains(text(),'Net Sales')]/following-sibling::td").text
netSales1 = netSales1.replace(',', '')
print("netSales1:", netSales1)

# 2. Total Items Bill Report
print("Start getting Payment Wise Report")
EMR.find_element(By.LINK_TEXT, "Reports").click()
time.sleep(3)
EMR.find_element(By.LINK_TEXT, "Billing Reports").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//i[contains(text(),'Total Items Bill')]").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
time.sleep(4)
netSales2 = EMR.find_element(By.XPATH, "//td[contains(text(),'Net Sales')]/following-sibling::td").text
netSales2 = netSales2.replace(',', '')
print("netSales2:", netSales2)

#####Assertion: Start#####
assert netSales1 == netSales2
#####Assertion: End#####

# 3. Income Segregation Report
print("Start getting Payment Wise Report")
EMR.find_element(By.LINK_TEXT, "Reports").click()
time.sleep(3)
EMR.find_element(By.LINK_TEXT, "Billing Reports").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//i[contains(text(),'Income Segregation')]").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
time.sleep(4)
netSales3 = EMR.find_element(By.XPATH, "//td[contains(text(),'Net Sales')]/following-sibling::td").text
netSales3 = netSales3.replace(',', '')
print("netSales3:", netSales3)

#####Assertion: Start#####
assert netSales1 == netSales3
#####Assertion: End#####

# # 4. Department Summary Report
# print("Start getting Payment Wise Report")
# EMR.find_element(By.LINK_TEXT, "Reports").click()
# time.sleep(3)
# EMR.find_element(By.LINK_TEXT, "Billing Reports").click()
# time.sleep(3)
# EMR.find_element(By.XPATH, "//i[contains(text(),'Department Summary')]").click()
# time.sleep(3)
# EMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
# time.sleep(4)
# netCashCollection4 = EMR.find_element(By.XPATH, "//td[contains(text(),'Net Cash Collection (K+L-M-N+O-P)')]/following-sibling::td").text
# netCashCollection4 = netCashCollection4.replace(',', '')
# print("netCashCollection4:", netCashCollection4)
# netSales4 = EMR.find_element(By.XPATH, "//td[contains(text(),'Net Sales')]/following-sibling::td").text
# netSales4 = netSales4.replace(',', '')
# print("netSales4:", netSales4)
#
# #####Assertion: Start#####
# assert netSales1 == netSales4
# assert netCashCollection1 == netCashCollection4
# #####Assertion: End#####

# 5. User Wise Cash Collection Report
print("Start getting Payment Wise Report")
EMR.find_element(By.LINK_TEXT, "Reports").click()
time.sleep(3)
EMR.find_element(By.LINK_TEXT, "Billing Reports").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//i[contains(text(),'User Wise Cash Collection')]").click()
time.sleep(3)
EMR.find_element(By.XPATH, "//button[@class='btn blue']").click()
time.sleep(4)
netCashCollection5 = EMR.find_element(By.XPATH, "//td[contains(text(),'Net Cash Collection')]/following-sibling::td").text
netCashCollection5 = netCashCollection5.replace(',', '')
print("netCashCollection5:", netCashCollection5)

#####Assertion: Start#####
netCashCollection1 = float(netCashCollection1)
netCashCollection1 = math.trunc(netCashCollection1)
print("after truncate:", netCashCollection1)
assert int(netCashCollection1) == int(netCashCollection5)
#####Assertion: End#####

AC.logout()
AC.closeBrowser()
