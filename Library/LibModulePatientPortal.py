import time
from selenium.webdriver.common.by import By
import random
import Library.GlobalShareVariables as GSV
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

AppName = GSV.appName


# Module:Patient_Registration -----------------
def patientRegistration(danpheEMR):
    global contactno
    global HospitalNo
    global FullName
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Patient").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Register Patient").click()
    time.sleep(2)
    age = random.randint(1, 99)
    danpheEMR.find_element(By.XPATH, "//input[@type='number']").send_keys(age)
    contactno = random.randint(9811111111, 9899999999)
    danpheEMR.find_element(By.XPATH, "//input[@type='tel']").send_keys(contactno)
    print(contactno)
    danpheEMR.find_element(By.ID, "regPatFirstName").send_keys("auto")
    sname = str(random.randint(1111, 9999))
    danpheEMR.find_element(By.XPATH, "(//input[@value=''])[3]").send_keys("preg", sname)
    gender = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname='Gender']"))
    gender.select_by_visible_text("Female")
    danpheEMR.find_element(By.ID, "txtPanNumber").send_keys(Keys.ENTER)
    time.sleep(5)
    danpheEMR.find_element(By.ID, "regPatientSubmitBtn").click()
    time.sleep(7)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(contactno)
    time.sleep(5)
    assert str(contactno) == danpheEMR.find_element(By.XPATH, "//ag-grid-angular[@id='myGrid']"
                                                              "/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    global HospitalNo
    HospitalNo = danpheEMR.find_element(By.XPATH, "//ag-grid-angular[@id='myGrid']"
                                                  "/div/div/div/div[3]/div[2]/div/div/div/div").text
    print("HospitalNo:", HospitalNo)
    return HospitalNo


def patientRegistrationMultipleClick(danpheEMR):
    global contactno
    global HospitalNo
    global FullName
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Patient").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Register Patient").click()
    time.sleep(5)
    age = random.randint(1, 99)
    danpheEMR.find_element(By.XPATH, "//input[@type='number']").send_keys(age)
    contactno = random.randint(9811111111, 9899999999)
    danpheEMR.find_element(By.XPATH, "//input[@type='tel']").send_keys(contactno)
    print(contactno)
    danpheEMR.find_element(By.LINK_TEXT, "Register Patient").click()
    danpheEMR.find_element(By.ID, "regPatFirstName").send_keys("auto")
    sname = str(random.randint(1111, 9999))
    danpheEMR.find_element(By.XPATH, "(//input[@value=''])[3]").send_keys("preg", sname)
    gender = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname='Gender']"))
    gender.select_by_visible_text("Female")
    danpheEMR.find_element(By.XPATH, "//input[@value='Register Patient']").click()
    danpheEMR.find_element(By.XPATH, "//input[@value='Register Patient']").click()
    print("Contact No", contactno)
    return contactno


def verifyMultipleRegistration(danpheEMR, ContactNo):
    print(">>START: verifyMultipleRegistration")
    danpheEMR.find_element(By.LINK_TEXT, "Patient").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ContactNo)
    time.sleep(5)
    searchResult = danpheEMR.find_element(By.XPATH, "//div[@class='page-items']").text
    print("searchResult:", searchResult)
    searchResult = searchResult.partition("Showing ")[2]
    print("searchResult:", searchResult)
    searchResult = searchResult.partition(" /")[0]
    print("searchResult:", searchResult)
    assert searchResult == "1"
    print("<<END: verifyMultipleRegistration")


def getRandomPatient(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Patient").click()
    time.sleep(5)
    global HospitalNo
    HospitalNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='PatientCode'])[2]").text
    print("HospitalNo:", HospitalNo)
    return HospitalNo


def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
