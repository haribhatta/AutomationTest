from selenium import webdriver
import time
import random
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

AppName = GSV.appName
HospitalNo = None
# Module:Appointment --------------------
def addBirthCertificate(danpheEMR, HospitalNo):
   print(">>START: addBirthCertificate")
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
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
      danpheEMR.find_element_by_id("babyWt").send_keys(3)
      birthType = Select(danpheEMR.find_element_by_id("ddlBirthType"))
      birthType.select_by_visible_text("Spontaneous Vaginal Delivery")
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//button[contains(text(),'Add Certificate')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
   print("<<END: addBirthCertificate")
def addMRwithDischargeTypeDeath(danpheEMR):
   print(">>START: addMRwithDischargeTypeDeath")
   ######## add MR with discharge Type = Death goes here
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element_by_link_text("MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element_by_link_text("MR Inpatient List").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(2112109496)
      danpheEMR.find_element_by_xpath("//button[contains(text(),'Load Patients')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Add MR')]").click()
      danpheEMR.find_element(By.CSS_SELECTOR, ".cstm-field-sel").click()
      dropdown = danpheEMR.find_element(By.XPATH, "//select[@class='cstm-field-sel ng-pristine ng-valid ng-touched']")
      dropdown.find_element(By.XPATH, "//option[. = 'Death']").click() ##
      danpheEMR.find_element(By.CSS_SELECTOR, ".row:nth-child(4) .cstm-field-sel").click()
      dropdown = danpheEMR.find_element(By.CSS_SELECTOR, ".row:nth-child(4) .cstm-field-sel")
      time.sleep(4)
      dropdown.find_element(By.XPATH, "//option[. = 'Post Operative Death']").click() ##
      danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-7 > .ng-untouched").click()
      dropdown = danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-7 > .ng-untouched")
      dropdown.find_element(By.XPATH, "//option[. = '<48']").click() ##
      danpheEMR.find_element(By.ID, "icd10code").send_keys("A00 | Cholera")
      #danpheEMR.find_element(By.ID, "certNum").click()
      danpheEMR.find_element(By.ID, "Submit").click()
      danpheEMR.find_element(By.CSS_SELECTOR, ".all-buttons > .green").click()
      time.sleep(3)

   print(">>End: addMRwithDischargeTypeDeath")
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

