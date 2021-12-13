import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.LibModuleAppointment as LA
import random
########
danpheEMR = AC.danpheEMR
AppName = AC.appName
########
#Module:Incentive ******************

def ExistingPatientNewVisit():
    global NSHI
    print("Start >> Existing Patient Registration")
    danpheEMR.find_element_by_link_text("GovInsurance").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("allPatWithOutIns").click()
    danpheEMR.find_element_by_id("allPatWithOutIns").send_keys(HospitalNo)
    danpheEMR.find_element_by_id("allPatWithOutIns").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element_by_id("allPatWithOutIns").send_keys(Keys.TAB)
    NSHI = str(random.randint(11111, 99999))
    danpheEMR.find_element_by_id("Ins_NshiNumber").send_keys(NSHI)
    danpheEMR.find_element_by_id("Ins_InsuranceBalance").send_keys(50000)
    dropdown = danpheEMR.find_element_by_id("firstServicePoint")
    dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
    danpheEMR.find_element_by_id("firstServicePoint").click()
    time.sleep(3)
    dropdown = danpheEMR.find_element_by_id("IsFamilyHead")
    dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
    danpheEMR.find_element_by_id("IsFamilyHead").click()
    danpheEMR.find_element_by_id("register").click()
def insurancePatientRegistration():
      global NSHI
      print("Start >> Insurance Patient Registration")
      danpheEMR.find_element_by_link_text("GovInsurance").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Patient List").click()
      danpheEMR.find_element_by_id("btnNewInsurancePat").click()
      fname = str(random.randint(1111, 9999))
      danpheEMR.find_element_by_id("aptPatFirstName").send_keys("insu", fname)
      #danpheEMR.find_element_by_id("middleName").send_keys("Patient")
      danpheEMR.find_element_by_id("lastName").send_keys("registration")
      dropdown = danpheEMR.find_element_by_id("selGender")
      dropdown.find_element_by_xpath("//option[. = 'Male']").click()
      danpheEMR.find_element_by_id("selGender").click()
      danpheEMR.find_element_by_id("age").send_keys(5)
      NSHI = str(random.randint(11111, 99999))
      danpheEMR.find_element_by_id("Ins_NshiNumber").send_keys(NSHI)
      danpheEMR.find_element_by_id("Ins_InsuranceBalance").send_keys(50000)
      dropdown = danpheEMR.find_element_by_id("firstServicePoint")
      dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
      danpheEMR.find_element_by_id("firstServicePoint").click()
      time.sleep(3)
      dropdown = danpheEMR.find_element_by_id("IsFamilyHead")
      dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
      danpheEMR.find_element_by_id("IsFamilyHead").click()
      danpheEMR.find_element_by_id("register").click()
def insuranceNewVisit():
      global NSHI
      print(">> Start: Create insurance patient new visit")
      danpheEMR.find_element_by_link_text("GovInsurance").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Patient List").click()
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(NSHI)
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'New Visit')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("txtDepartment").send_keys("GYNAE & OBS")
      time.sleep(3)
      danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.RETURN)
      time.sleep(2)
      danpheEMR.find_element_by_id("btnPrintInvoice").click()
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

