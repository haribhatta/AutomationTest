import time
import random
import Library.ApplicationConfiguration as AC
from selenium.webdriver.support.select import Select

danpheEMR = AC.danpheEMR
AppName = AC.appName

#Module:Patient_Registration -----------------
def patientRegistration():
      global contactno
      global HospitalNo
      global FullName
      time.sleep(5)
      danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(5)
      danpheEMR.find_element_by_link_text("Register Patient").click()
      time.sleep(2)
      age = random.randint(1, 99)
      danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(age)
      contactno = random.randint(9811111111, 9899999999)
      danpheEMR.find_element_by_xpath("//input[@type='tel']").send_keys(contactno)
      print(contactno)
      if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
         danpheEMR.find_element_by_link_text("Register Patient").click()
         danpheEMR.find_element_by_id("regPatFirstName").send_keys("auto")
         sname = str(random.randint(1111, 9999))
         danpheEMR.find_element_by_xpath("(//input[@value=''])[3]").send_keys("preg", sname)
         gender = Select(danpheEMR.find_element_by_xpath("//select[@formcontrolname='Gender']"))
         gender.select_by_visible_text("Female")
      time.sleep(5)
      danpheEMR.find_element_by_id("regPatientSubmitBtn").click()
      time.sleep(7)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(contactno)
      time.sleep(5)
      assert str(contactno) == danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                                    "/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      global HospitalNo
      HospitalNo = danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                        "/div/div/div/div[3]/div[2]/div/div/div/div").text
      print(HospitalNo)


def patientRegistrationMultipleClick():
    global contactno
    global HospitalNo
    global FullName
    time.sleep(5)
    danpheEMR.find_element_by_link_text("Patient").click()
    time.sleep(5)
    danpheEMR.find_element_by_link_text("Register Patient").click()
    time.sleep(5)
    age = random.randint(1, 99)
    danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(age)
    contactno = random.randint(9811111111, 9899999999)
    danpheEMR.find_element_by_xpath("//input[@type='tel']").send_keys(contactno)
    print(contactno)
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element_by_link_text("Register Patient").click()
        danpheEMR.find_element_by_id("regPatFirstName").send_keys("auto")
        sname = str(random.randint(1111, 9999))
        danpheEMR.find_element_by_xpath("(//input[@value=''])[3]").send_keys("preg", sname)
        gender = Select(danpheEMR.find_element_by_xpath("//select[@formcontrolname='Gender']"))
        gender.select_by_visible_text("Female")
    danpheEMR.find_element_by_xpath("//input[@value='Register Patient']").click()
    danpheEMR.find_element_by_xpath("//input[@value='Register Patient']").click()
    print("Contact No", contactno)
    return contactno
def verifyMultipleRegistration(ContactNo):
    print(">>START: verifyMultipleRegistration")
    danpheEMR.find_element_by_link_text("Patient").click()
    time.sleep(5)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(ContactNo)
    time.sleep(5)
    searchResult = danpheEMR.find_element_by_xpath("//div[@class='page-items']").text
    print("searchResult:", searchResult)
    searchResult = searchResult.partition("Showing ")[2]
    print("searchResult:", searchResult)
    searchResult = searchResult.partition(" /")[0]
    print("searchResult:", searchResult)
    assert searchResult == "1"
    print("<<END: verifyMultipleRegistration")
def getRandomPatient():
      danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(5)
      global HospitalNo
      HospitalNo = danpheEMR.find_element_by_xpath("(//div[@col-id='PatientCode'])[2]").text


def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

