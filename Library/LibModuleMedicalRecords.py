import random
from selenium.common.exceptions import NoSuchElementException
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

AppName = GSV.appName
HospitalNo = None
# Module:Appointment --------------------
def addBirthCertificate(danpheEMR, HospitalNo):
   print(">>START: addBirthCertificate")
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element(By.LINK_TEXT, "Birth List").click()
      time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Add New Birth Certificate')]").click()
      time.sleep(4)
      danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
      time.sleep(3)
      number = str(random.randint(1, 9999))
      danpheEMR.find_element(By.ID, "certNum").send_keys(number)
      print(number)
      time.sleep(3)
      birthCondition = Select(danpheEMR.find_element(By.ID, "ddlBirthCondition"))
      birthCondition.select_by_visible_text("Live Birth")
      gender = Select(danpheEMR.find_element(By.ID, "sex"))
      gender.select_by_visible_text("Male")
      time.sleep(3)
      danpheEMR.find_element(By.ID, "babyWt").send_keys(2)
      time.sleep(5)
      # birthType = Select(danpheEMR.find_element(By.ID, "ddlBirthType")).click()
      # birthType.select_by_visible_text(" Spontaneous Vaginal Delivery")
      # time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Add Certificate')]").click()
      time.sleep(5)
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Submit')]").click()
      # return number for the verifying the certificate number
      return number
   print("<<END: addBirthCertificate")

def verifyaddbirthCertificate(danpheEMR , certNo):
   print("Verifying Certificate Start")
   danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
   time.sleep(5)
   danpheEMR.find_element(By.LINK_TEXT, "Birth List").click()
   time.sleep(3)
   danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(certNo)
   time.sleep(2)
   try:
      danpheEMR.find_element(By.XPATH,  "(//a[contains(text(),'Certificate')])[2]").click()
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Cancel')]").click()
      print("End of Verifying Certificate")

   except NoSuchElementException:
       print("Not verified")
       raise NoSuchElementException("FileNotFoundError")


def addMRwithDischargeTypeDeath(danpheEMR, HospitalNo):
   print(">>START: addMRwithDischargeTypeDeath")
   ######## add MR with discharge Type = Death goes here
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element(By.LINK_TEXT, "MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element(By.LINK_TEXT, "MR Inpatient List").click()
      time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Load Patients')]").click()
      danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Add MR')]").click()
      time.sleep(3)
      dischargeType = Select(danpheEMR.find_element(By.XPATH, "//select"))
      dischargeType.select_by_visible_text("Death")
      time.sleep(3)
      dischargeCondition = Select(danpheEMR.find_element(By.CSS_SELECTOR, ".row:nth-child(4) .cstm-field-sel"))
      dischargeCondition.select_by_visible_text('Post Operative Death')
      time.sleep(3)
      deathPeriod = Select(danpheEMR.find_element(By.CSS_SELECTOR, ".row:nth-child(5) .cstm-field-sel"))
      time.sleep(1)
      deathPeriod.select_by_visible_text("<48")
      danpheEMR.find_element(By.ID, "icd10code").send_keys("A00 | Cholera")
      number = str(random.randint(1, 9999))
      danpheEMR.find_element(By.ID, "certNum").send_keys(number)
      print(number)
      danpheEMR.find_element(By.ID, "Submit").click()
      # danpheEMR.find_element(By.ID, "certNum").send_keys()
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

