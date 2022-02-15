import time
from selenium.webdriver.common.by import By
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
import random

########
danpheEMR = AC.danpheEMR
AppName = AC.appName


########
def Setting_add_employee():
    global randomnum
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Employee')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Add Employee')]").click()
    time.sleep(5)
    randomnum = str(random.randint(1111, 9999))
    danpheEMR.find_element(By.ID, "FirstName").send_keys("DR. Ankit", randomnum)
    danpheEMR.find_element(By.ID, "LastName").send_keys("lastname")
    dropdown = danpheEMR.find_element(By.ID, "Gender")
    dropdown.send_keys("M")
    danpheEMR.find_element(By.ID, "EmployeeDepartment").send_keys("admin")
    # danpheEMR.find_element(By.ID, "isApptApplicable").click()
    danpheEMR.find_element(By.ID, "Add").click()


def Setting_Adding_User():
    global randomnum
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Security')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Add User')]").click()
    time.sleep(5)
    Select_emp = danpheEMR.find_element(By.ID, "EmployeeId")
    Select_emp.send_keys(Keys.TAB)
    user_name = danpheEMR.find_element(By.ID, "UserName")
    user_name.send_keys("Ankit", randomnum)
    Email = danpheEMR.find_element(By.ID, "EmailId")
    Email.send_keys("ankit", randomnum, "@gmail.com")
    password = danpheEMR.find_element(By.ID, "Password").send_keys("pass123")
    danpheEMR.find_element(By.ID, "Addbtn").click()


def checkAutoAddItems():
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),' ADT ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Manage Auto Add Billing Items").click()
    time.sleep(2)
    # danpheEMR.find_element(By.XPATH, "//h4[text()='Auto Add Bill Item: ']").click()
    autoaddbillitemvalue = danpheEMR.find_element(By.XPATH, "//b[contains(.,'  False')]").text
    autoaddBeditemvalue = danpheEMR.find_element(By.XPATH, "//b[contains(.,'  True')]").text
    print("autoaddbillitemvalue", autoaddbillitemvalue)
    print("autoaddBeditemvalue", autoaddBeditemvalue)


def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
