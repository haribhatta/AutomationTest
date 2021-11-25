# Objective: Verify Post to Accounting.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
from selenium.webdriver.support.select import Select
import time

AC.applicationSelection()
AC.openBrowser()

danpheEMR = AC.danpheEMR
AppName = AC.appName

# admin user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
AC.login(foUserId, foUserPwd)
danpheEMR.find_element_by_link_text("Accounting").click()
time.sleep(5)
danpheEMR.find_element_by_link_text("Post to Accounting").click()
time.sleep(5)
Module = Select(danpheEMR.find_element_by_id("sectionid"))
time.sleep(5)
Module.select_by_visible_text("Billing")
time.sleep(3)
Voucher = Select(danpheEMR.find_element_by_id("voucherhead"))
time.sleep(3)
Voucher.select_by_visible_text("test")
time.sleep(3)
danpheEMR.find_element_by_xpath("//button[@title='Load records of selected date']").click()
time.sleep(3)
danpheEMR.find_element_by_xpath("//button[@title='save selected to accounting'][1]").click()


