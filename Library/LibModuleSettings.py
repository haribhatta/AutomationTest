import time
from selenium.webdriver.common.by import By
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
import random
########
AppName = GSV.appName
########
def Setting_add_employee(danpheEMR):
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

def Setting_Adding_User(danpheEMR):
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

def checkAutoAddItems(danpheEMR):
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

######## Check Core CFG Parameter Value
def checkCoreCFGadmitDocMandatory(danpheEMR):
    print("START>>checkCoreCFGadmitDocMandatory")
    global admittingDoctorMandatory
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("AdtNewAdmissionDisplaySettings")
    admittingDoctorMandatory = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ParameterValue'])[2]").text
    print("admittingDoctorMandatory:", admittingDoctorMandatory)
    admittingDoctorMandatory = admittingDoctorMandatory.partition(",")[0]
    admittingDoctorMandatory = admittingDoctorMandatory.partition(":")[2]
    print("checkCoreCFGadmitDocMandatory:", admittingDoctorMandatory)
    return admittingDoctorMandatory

def checkCoreLabReportVerify(danpheEMR):
    print("START>>checkCoreLabReportVerify")
    global labReportVerify
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("LabReportVerificationNeededB4Print")
    labReportVerify = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ParameterValue'])[2]").text
    print("labReportVerify:", labReportVerify)
    labReportVerify = labReportVerify.partition(",")[0]
    print("labReportVerify:", labReportVerify)
    labReportVerify = labReportVerify.partition(":")[2]
    print("labReportVerify:", labReportVerify)
    print("END>>checkCoreLabReportVerify")
    return labReportVerify

def checkCoreCFGdiscountMembership(danpheEMR):
    print("START>>checkCoreCFGdiscountMembership")
    global admittingDoctorMandatory
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("MembershipTypeDiscount")
    membershipTypeDiscountValue = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ParameterValue'])[2]").text
    print("membershipTypeDiscountValue:", membershipTypeDiscountValue)
    danpheEMR.find_element(By.ID, "quickFilterInput").clear()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("MembershipSchemeSettings")
    membershipSchemeSettingsValue = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ParameterValue'])[2]").text
    print("membershipSchemeSettingsValue:", membershipSchemeSettingsValue)
    print("END>>checkCoreCFGdiscountMembership")
    return membershipTypeDiscountValue, membershipSchemeSettingsValue

def EnableReceiveItemsInDispensary(danpheEMR):
    print("START:EnableReceiveItemsInDispensary")
    global EnableReceiveItemsInDispensary
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("EnableReceiveItemsInDispensary")
    EnableReceiveItemsInDispensary = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ParameterValue'])[2]").text
    print("EnableReceiveItemsInDispensary:", EnableReceiveItemsInDispensary)
    print("END:EnableReceiveItemsInDispensary")
    return EnableReceiveItemsInDispensary

def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()

def __str__():
    return
