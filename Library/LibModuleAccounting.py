import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.LibModuleAppointment as LA
########
danpheEMR = AC.danpheEMR
AppName = AC.appName
########
#Module:Incentive ******************
def verifyAcMasterMapping():
      print(" ##Start of ACC_MST_Hospital table mapping with AccPrimaryHospitalShortName core cfg parameter value ##")
def createManualVoucher():
      danpheEMR.find_element_by_link_text("Accounting").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Transaction").click()
      danpheEMR.find_element_by_link_text("Voucher Entry").click()
      dropdown = danpheEMR.find_element_by_id("voucher")
      dropdown.find_element_by_xpath("//option[. = 'Purchase Voucher']").click()
      assert danpheEMR.switch_to.alert.text == "Are you sure you want to change the Voucher Type?"
      danpheEMR.switch_to.alert.accept()
      danpheEMR.find_element_by_css_selector(".fa-question").click()
      assert danpheEMR.switch_to.alert.text == "Do you want to create new Ledger?"
      danpheEMR.switch_to.alert.accept()
      time.sleep(4)
      danpheEMR.find_element_by_id("primarygroup").click()
      time.sleep(3)
      dropdown = danpheEMR.find_element_by_id("primarygroup")
      time.sleep(3)
      dropdown.find_element_by_xpath("//option[. = 'Assets']").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("primarygroup").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("primarygroup").click()
      danpheEMR.find_element_by_css_selector(".div-relative .ng-untouched").click()
      danpheEMR.find_element_by_css_selector(".col-md-8 > .danphe-auto-complete-wrapper > .ng-untouched").click()
      danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .ng-dirty").send_keys("Test Dr. 1")
      danpheEMR.find_element_by_css_selector(".btn-primary").click()
      danpheEMR.find_element_by_id("Amount_1").send_keys(100)
      time.sleep(2)
      danpheEMR.find_element_by_css_selector(".fa-plus").click()
      danpheEMR.find_element_by_id("DrCr_2").click()
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

