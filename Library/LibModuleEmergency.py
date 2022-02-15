from selenium import webdriver
import time
import random
import GlobalShareVariables
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
AppName = AC.appName
HospitalNo = None
########
def EmergencyRegistration():
   danpheEMR.find_element_by_link_text("Emergency").click()
   time.sleep(3)
   danpheEMR.find_element_by_xpath("//a[contains(text(),'New patient')]").click()
   time.sleep(3)
   danpheEMR.find_element_by_xpath("//a[contains(text(),'New Registration ')]").click()
   time.sleep(5)
   # danpheEMR.find_element_by_id("erPatFirstName").send_keys("ram")
   danpheEMR.find_element_by_xpath("//span[contains(text(),'Add Unknown ER-Patient')]").click()
   time.sleep(2)
   danpheEMR.find_element_by_id("erPatGender").send_keys("M")
   danpheEMR.find_element_by_xpath("//button[@id='register']").click()

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

