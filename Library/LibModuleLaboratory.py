import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
AppName = AC.appName
##########################
def collectLabSample(HospitalNo, testname):
      global barcodeno
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)
      if AppName == "SNCH":
         danpheEMR.find_element_by_xpath("//a[contains(text(),' Sample Collection ')]").click()
         danpheEMR.find_element_by_id("quickFilterInput").click()
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(5)
         danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         danpheEMR.find_element_by_css_selector(".btn").click()
         time.sleep(9)
         barcodeno = danpheEMR.find_element_by_css_selector("tbody:nth-child(2) td:nth-child(3)").text
         print(barcodeno)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Close')]").click()
def addLabResult():
      print("Starting>Adding Lab Report")
      if AppName == "SNCH":
         danpheEMR.find_element_by_link_text("Laboratory").click()
         time.sleep(1)
         danpheEMR.find_element_by_link_text("Add Results").click()
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(barcodeno)
         time.sleep(2)
         time.sleep(2)
         danpheEMR.find_element_by_link_text("Add Result").click()
         time.sleep(7)
         # ---------------this is hardcoded for TFT test-----------
         danpheEMR.find_element_by_id("inputbox000").send_keys("2.23")
         danpheEMR.find_element_by_id("inputbox001").send_keys("15.0")
         danpheEMR.find_element_by_id("inputbox002").send_keys("4.05")
         time.sleep(7)
         danpheEMR.find_element_by_xpath("//div[3]/button").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Proceed')]").click()  # proced for abnormal result
         time.sleep(3)
         danpheEMR.find_element_by_css_selector(".c-btn > .fa").click()
         danpheEMR.find_element_by_id("btnUpdateSignatories").click()
         time.sleep(2)
def verifyLabReport(HospitalNo):
      danpheEMR.find_element_by_link_text("PendingReports").click()
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(2)
      danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Verify ')]").click()
def printLabReport(HospitalNo, t3, t4, tsh):
      danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)
      danpheEMR.find_element_by_link_text("Final Reports").click()
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(7)
      #isprinted = danpheEMR.find_element_by_css_selector("span > b").text
      #print(isprinted)
      #assert isprinted == "NO"
      #danpheEMR.find_element_by_link_text("View Details").click()
      danpheEMR.find_element_by_xpath("//a[contains(text(),'View Details')]").click()
      time.sleep(2)
      assert t3 == danpheEMR.find_element_by_xpath("//td[2]/span").text
      print(t3)
      sysT4 = danpheEMR.find_element_by_xpath("//tr[3]/td[2]/span").text
      print("SysT4:", sysT4)
      print("T4:", t4)
      assert t4 == danpheEMR.find_element_by_xpath("//tr[3]/td[2]/span").text
      print(t4)
      assert tsh == danpheEMR.find_element_by_xpath("//tr[4]/td[2]/span").text
      print(tsh)
def checkLabDuplicateRequisition(HospitalNo, ItemName):
      print("Start>>checkLabDuplicateRequisition")
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)
      if AppName == "SNCH":
         danpheEMR.find_element_by_xpath("//a[contains(text(),' Sample Collection ')]").click()
         danpheEMR.find_element_by_id("quickFilterInput").click()
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(5)
         x = danpheEMR.find_element_by_xpath("//span[contains(text(),'No Rows To Show')]",).text
         print("x", x)
         assert x == "No Rows To Show"
      print("End>>checkLabDuplicateRequisition")
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()
def __str__():
      return

