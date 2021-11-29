from selenium import webdriver
import time
import random
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
AppName = AC.appName
HospitalNo = None
# Module:Appointment --------------------
def addBirthCertificate(HospitalNo):
   print(">>START: addBirthCertificate")
   if  AppName == "SNCH" or AppName == "MPH":
      time.sleep(2)
      danpheEMR.find_element_by_link_text("MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element_by_link_text("Birth List").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Add New Birth Certificate')]").click()
      time.sleep(4)
      danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
      time.sleep(3)
      number = str(random.randint(1, 9999))
      danpheEMR.find_element_by_id("certNum").send_keys(number)
      time.sleep(3)
      birthCondition = Select(danpheEMR.find_element_by_id("ddlBirthCondition"))
      birthCondition.select_by_visible_text("Live Birth")
      gender = Select(danpheEMR.find_element_by_id("sex"))
      gender.select_by_visible_text("Male")
      time.sleep(3)
      danpheEMR.find_element_by_id("babyWt").send_keys(2.2)
      birthType = Select(danpheEMR.find_element_by_id("ddlBirthType"))
      birthType.select_by_visible_text(" Spontaneous Vaginal Delivery")
      time.sleep(3)
   print("<<END: addBirthCertificate")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

