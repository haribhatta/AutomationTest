from selenium import webdriver
import time
import random
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

AppName = GSV.appName
HospitalNo = None
# Module:Appointment --------------------
def getHospitalServiceSummaryReport(danpheEMR):
   print(">>START: getHospitalServiceSummaryReport")
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element_by_link_text("MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),' Reports ')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'Hospital Service Summary Report')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//button[contains(text(),' Show Report ')]").click()
      time.sleep(4)
   print("<<END: getHospitalServiceSummaryReport")
def storeHospitalServiceSummaryReport(danpheEMR):
   print("Start >> assignHospitalServiceSummaryReport")
   ######## Code goes here
   print("End >> assignHospitalServiceSummaryReport")
def verifyHospitalServiceSummaryReport(danpheEMR):
   print("Start >> verifyHospitalServiceSummaryReport")
   ######## Code goes here
   print("End >> verifyHospitalServiceSummaryReport")

def getInpatientMorbidityReport(danpheEMR):
   print(">>START: getInpatientMorbidityReport")
   if  AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
      time.sleep(2)
      danpheEMR.find_element_by_link_text("MedicalRecords").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),' Reports ')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'Inpatient Morbidity Report')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//button[contains(text(),' Show Report ')]").click()
      time.sleep(4)
   print("<<END: getInpatientMorbidityReport")
def storeInpatientMorbidityReport(danpheEMR):
   print("Start >> assignInpatientMorbidityReport")
   ######## Code goes here
   print("End >> assignInpatientMorbidityReport")
def verifyInpatientMorbidityReport(danpheEMR):
   print("Start >> verifyInpatientMorbidityReport")
   ######## Code goes here
   print("End >> verifyInpatientMorbidityReport")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

