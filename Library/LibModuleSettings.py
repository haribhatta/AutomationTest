import time
from selenium.webdriver.common.by import By
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
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


def addLongSignatureOfEmployee(danpheEMR, doctor, doctor2):
    print("Start : Adding long Signature of Employee")
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Employee')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Add Employee')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(doctor)
    time.sleep(3)
    element = danpheEMR.find_element(By.XPATH, "//div[@col-id=0]/a")
    time.sleep(1)
    danpheEMR.execute_script("arguments[0].click();", element)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//textarea[@formcontrolname = 'LongSignature']").clear()
    danpheEMR.find_element(By.XPATH, "//textarea[@formcontrolname = 'LongSignature']").send_keys(doctor)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "Add").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").clear()
    time.sleep(1)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(doctor2)
    time.sleep(3)
    element2 = danpheEMR.find_element(By.XPATH, "//div[@col-id=0]/a")
    time.sleep(1)
    danpheEMR.execute_script("arguments[0].click();", element2)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//textarea[@formcontrolname = 'LongSignature']").clear()
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//textarea[@formcontrolname = 'LongSignature']").send_keys(doctor2)
    danpheEMR.find_element(By.ID, "Add").click()
    print("END: Employee long signature added")


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
    print(password)
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


# Check Core CFG Parameter Value


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


# Dispensary


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


# Laboratory
def ChangePaymentLabelSettingstoMaternityPayment(danpheEMR):
    print("START: changing UserCollectionPaymentLabelSetting to  Maternity Payment (Net)")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("UserCollectionOtherPaymentsLabelSettings")
    danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[7]/a").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//input[@class = 'form-control ng-untouched ng-pristine ng-valid']").clear()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@class = 'form-control ng-pristine ng-valid ng-touched']").click()
    danpheEMR.find_element(By.XPATH, "//input[@class = 'form-control ng-pristine ng-valid ng-touched']").send_keys("Maternity Payment (Net)")
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Update')]").click()


# Inventory


def EnableReceivedItemInSubstore(danpheEMR):
    print("START:EnableReceivedItemInSubstore")
    global EnableReceiveItemsInDispensary
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("EnableReceivedItemInSubstore")
    EnableReceivedItemInSubstore = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ParameterValue'])[2]").text
    print("EnableReceivedItemInSubstore:", EnableReceivedItemInSubstore)
    print("END:EnableReceivedItemInSubstore")
    return EnableReceiveItemsInDispensary


def CheckNepaliReceiptValue(danpheEMR):
    print("START:Checking that Nepali Receipt is Enable or Not")
    global NepaliReceipt
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("NepaliReceipt")
    NepaliReceipt = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[3]").text
    print("Nepali Receipt is Enable :", NepaliReceipt)
    return NepaliReceipt


# def CheckCreditOrganizationMandatory(danpheEMR):  This Features is being Changing so this script is onHold
#     print("START: Checking credit Organization Mandatory")
#     global CreditOrganizationMandatory
#     danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
#     time.sleep(5)
#     danpheEMR.find_element(By.LINK_TEXT, "Core CFG Parameters").click()
#     time.sleep(5)
#     danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("CreditOrganizationMandatory")
#     time.sleep(5)
#     CreditOrganizationMandatory = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[3]").text
#     time.sleep(2)
#     print("Parameter Value for Credit Organization is :", CreditOrganizationMandatory)
#     assert CreditOrganizationMandatory == "true"
#     print("END: Credit Organization Non Mandatory")


def paymentModeOpBillingDisplaySequence(danpheEMR):
    print("START: PaymentMode Sequence in Op Billing")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'More...')]").click()
    danpheEMR.find_element(By.LINK_TEXT, "Payment Mode Settings").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("OPBilling")
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Edit')]").click()
    time.sleep(1)
    # Discount
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[12]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[12]").send_keys(1)
    # Cash
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[1]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[1]").send_keys(2)
    # Credit
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[2]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[2]").send_keys(3)
    # e-sewa
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[4]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[4]").send_keys(3)
    # FonePay
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[5]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[5]").send_keys(4)
    # Khalthi
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[6]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[6]").send_keys(5)
    # IPS Connect
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[7]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[7]").send_keys(6)
    # POS-1
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[8]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[8]").send_keys(7)
    # Cheque
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[3]").clear()
    danpheEMR.find_element(By.XPATH, "(//input[@type='number'])[9]").send_keys(8)
    # update
    danpheEMR.find_element(By.ID, "update").click()

# Check and make Billing Membership Referral Active


def makeReferalMembershipActive(danpheEMR):
    print("Checking the Referal Membership Active")
    danpheEMR.find_element(By.LINK_TEXT, "Settings").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Billing')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[normalize-space()='Memberships']").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("Referal")
    try:
        status = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[5]").text
        print("current status of Referral is :", status)
        status = str(status)
        print(status)
        if status == "true":
            print("Membership Referal is Active")
        else:
            danpheEMR.find_element(By.XPATH, "(//a[normalize-space()='Edit'])[1]").click()
            time.sleep(2)
            isActive = danpheEMR.find_element(By.XPATH, "//label[@class='mt-checkbox mt-checkbox-outline']//span")
            isActive.is_selected()
            isActive.click()
            time.sleep(2)
            afterSelect = danpheEMR.find_element(By.XPATH, "//label[@class='mt-checkbox mt-checkbox-outline']//span")
            afterSelect.is_selected()
            danpheEMR.find_element(By.ID, "savebtn").click()
    except NoSuchElementException:
        try:
            danpheEMR.find_element(By.XPATH, "//a[normalize-space()='Add Membership']").click()
            danpheEMR.find_element(By.XPATH, "//input[@id='CommunityName']").send_keys("Hospital")
            danpheEMR.find_element(By.XPATH, "//input[@id='CommunityName']").send_keys(Keys.ENTER)
            danpheEMR.find_element(By.XPATH, "//input[@id='MembershipTypeName']").send_keys("Referal")
            danpheEMR.find_element(By.XPATH, "//input[@id='MembershipTypeName']").send_keys(Keys.ENTER)
            danpheEMR.find_element(By.XPATH, "//input[@id='Discount']").send_keys(10)
            danpheEMR.find_element(By.XPATH, "//input[@id='savebtn']").click()
        except:
            print("Please Add a Referal membership")
    print("Added Membership Referal Active")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
