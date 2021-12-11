import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.LibModuleAppointment as LA
import Library.GlobalShareVariables as GSV
########
#danpheEMR = AC.danpheEMR
AppName = GSV.appName
########
#Module:Radiology ***************************
def doRadioScan(danpheEMR, HospitalNo):
   print(">>START: doRadioScan")
   if AppName == 'SNCH':
         time.sleep(3)
         danpheEMR.find_element_by_link_text("Radiology").click()
         time.sleep(5)
         danpheEMR.find_element_by_link_text("List Requests").click()
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(3)
         danpheEMR.find_element_by_link_text("Scan Done").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Done')]").click()
         time.sleep(3)
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//a[contains(text(),'Add Report')]").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//input[@value='Submit & Print']").click()
         time.sleep(5)
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.ESCAPE)
   print("<<END: doRadioScan")
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

