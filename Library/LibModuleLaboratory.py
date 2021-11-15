from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)

#Module:Laboratory****************************
   def collectLabSample(self, testname):
      global barcodeno
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)

      # if appPort == "81":
      #    self.danpheEMR.find_element_by_link_text("Lab Requisition").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      #    time.sleep(5)
      #    self.danpheEMR.find_element_by_link_text("View Details").click()
      #    time.sleep(9)
      #    sampleno = self.danpheEMR.find_element_by_name("Sample number").get_attribute("value")
      #    print(sampleno)
      #    samplecode = self.danpheEMR.find_element_by_name("Sample Code").get_attribute("value")
      #    print(samplecode)
      #    time.sleep(9)
      #    self.danpheEMR.find_element_by_css_selector(".btn").click()
      #    time.sleep(9)
      #    barcodeno = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(2) td:nth-child(3)").text
      #    print(barcodeno)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Close')]").click()
      if appPort == "82":
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sample Collection ')]").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(5)
         self.danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         #sampleno = self.danpheEMR.find_element_by_name("Sample number").get_attribute("value") #removed on new changes
         #print(sampleno)
         #samplecode = self.danpheEMR.find_element_by_name("Sample Code").get_attribute("value")
         #print(samplecode)
         time.sleep(9)
         self.danpheEMR.find_element_by_css_selector(".btn").click()
         time.sleep(9)
         barcodeno = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(2) td:nth-child(3)").text
         print(barcodeno)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Close')]").click()
   def addLabResult(self):
      print("Starting>Adding Lab Report")

      # if appPort == "81":
      #    self.danpheEMR.find_element_by_link_text("Laboratory").click()
      #    time.sleep(1)
      #    self.danpheEMR.find_element_by_link_text("Add Results").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(barcodeno)
      #    time.sleep(2)
      #    # self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("Add Result").click()
      #    time.sleep(7)
      #    # ---------------this is hardcoded for TFT test-----------
      #    self.danpheEMR.find_element_by_id("inputbox000").send_keys("2.23")
      #    self.danpheEMR.find_element_by_id("inputbox001").send_keys("15.0")
      #    self.danpheEMR.find_element_by_id("inputbox002").send_keys("4.05")
      #    time.sleep(7)
      #    self.danpheEMR.find_element_by_xpath("//div[3]/button").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Proceed')]").click()  # proceed for abnormal result
      #
      #    time.sleep(7)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Update Signatories and Print ')]").click()
      #    self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Back To Grid ')]").click()

      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Laboratory").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_link_text("Add Results").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(barcodeno)
         time.sleep(2)
         # self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Add Result").click()
         time.sleep(7)
         # ---------------this is hardcoded for TFT test-----------
         self.danpheEMR.find_element_by_id("inputbox000").send_keys("2.23")
         self.danpheEMR.find_element_by_id("inputbox001").send_keys("15.0")
         self.danpheEMR.find_element_by_id("inputbox002").send_keys("4.05")
         time.sleep(7)
         self.danpheEMR.find_element_by_xpath("//div[3]/button").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Proceed')]").click()  # proced for abnormal result

         time.sleep(3)
         self.danpheEMR.find_element_by_css_selector(".c-btn > .fa").click()
         #self.danpheEMR.find_element_by_css_selector(".pure-checkbox:nth-child(2) > label").click()
         #self.danpheEMR.find_element_by_css_selector(".ng-untouched .row:nth-child(1)").click()
         #self.danpheEMR.find_element_by_css_selector(".margin-7-hr").click()
         self.danpheEMR.find_element_by_id("btnUpdateSignatories").click()

         time.sleep(2)
         #self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Edit Signatories')]/preceding-sibling::button").click()
         #self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Back To Grid ')]").click()
         # self.danpheEMR.find_element_by_id("close print window").click()   # failed with bug ID:
         # self.danpheEMR.find_element_by_xpath("//div[3]/div/div/button").click()
         # self.danpheEMR.close()
         # self.danpheEMR.find_element_by_xpath("//button[contains(.,' Back To Grid')]").click()
   def verifyLabReport(self):
      self.danpheEMR.find_element_by_link_text("PendingReports").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Verify ')]").click()
   def printLabReport(self, t3, t4, tsh):
      self.danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Final Reports").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(7)
      #isprinted = self.danpheEMR.find_element_by_css_selector("span > b").text
      #print(isprinted)
      #assert isprinted == "NO"
      #self.danpheEMR.find_element_by_link_text("View Details").click()
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'View Details')]").click()
      time.sleep(2)
      assert t3 == self.danpheEMR.find_element_by_xpath("//td[2]/span").text
      print(t3)
      assert t4 == self.danpheEMR.find_element_by_xpath("//tr[3]/td[2]/span").text
      print(t4)
      assert tsh == self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]/span").text
      print(tsh)
   def checkLabDuplicateRequisition(self, ItemName):
      print("Start>>checkLabDuplicateRequisition")
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)
      # if appPort == "81":
      #    self.danpheEMR.find_element_by_link_text("Lab Requisition").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      #    time.sleep(5)
      #    self.danpheEMR.find_element_by_link_text("View Details").click()
      #    time.sleep(9)
      #    sampleno = self.danpheEMR.find_element_by_name("Sample number").get_attribute("value")
      #    print(sampleno)
      #    samplecode = self.danpheEMR.find_element_by_name("Sample Code").get_attribute("value")
      #    print(samplecode)
      #    time.sleep(9)
      #    self.danpheEMR.find_element_by_css_selector(".btn").click()
      #    time.sleep(9)
      #    barcodeno = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(2) td:nth-child(3)").text
      #    print(barcodeno)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Close')]").click()
      if appPort == "82":
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sample Collection ')]").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(5)
         x = self.danpheEMR.find_element_by_xpath("//span[contains(text(),'No Rows To Show')]",).text
         print("x", x)
         assert x == "No Rows To Show"
      print("End>>checkLabDuplicateRequisition")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

