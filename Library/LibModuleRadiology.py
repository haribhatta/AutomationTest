from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
#Module:Radiology ***************************
   def doRadioScan(self):
      # if appPort == '81':
      #    time.sleep(5)
      #    self.danpheEMR.find_element_by_link_text("Radiology").click()
      #    self.danpheEMR.find_element_by_link_text("List Requests").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_link_text("Scan Done").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Done')]").click()
      if appPort == '82':
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Radiology").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_link_text("List Requests").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Scan Done").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Done')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Add Report')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//input[@value='Submit & Print']").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.ESCAPE)
   def getTotalItemsBill(self):
      print(">>START: getTotalItemsBill")
      global sysreturnQty
      global sysreturnSubtotal
      global sysreturnQtyDiscount
      global sysreturnTotalamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Total Items Bill')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysreturnQty = self.danpheEMR.find_element_by_xpath('//tr[4]/td[2]').text
      print(sysreturnQty)
      sysreturnSubtotal = self.danpheEMR.find_element_by_xpath('//tr[4]/td[3]').text
      print(sysreturnSubtotal)
      #sysreturnQtyDiscount = self.danpheEMR.find_element_by_xpath('//tr[4]/td[4]').text
      #print(sysreturnQtyDiscount)
      #sysreturnTotalamount = self.danpheEMR.find_element_by_xpath('//tr[4]/td[5]').text
      #print(sysreturnTotalamount)
      print("<<END: getTotalItemsBill")
   def preSystemTotalItemsBill(self):
      print(">>START: preSystemTotalItemsBill")
      global presysreturnQty
      global presysreturnSubtotal
      global presysreturnQtyDiscount
      global presysreturnTotalamount
      presysreturnQty = int(sysreturnQty)
      print(presysreturnQty)
      presysreturnSubtotal = int(sysreturnSubtotal)
      print(presysreturnSubtotal)
      presysreturnQtyDiscount = int(sysreturnQtyDiscount)
      print(presysreturnQtyDiscount)
      presysreturnTotalamount = int(sysreturnTotalamount)
      print(presysreturnTotalamount)
      print("<<END: preSystemTotalItemsBill")
   def verifyTotalItemsBill(self, returnamt, discountamt):
      print(">>START: verifyTotalItemsBill")
      if returnamt > 0:
         assert int(sysreturnQty) == (presysreturnQty + 1)
         assert int(sysreturnSubtotal) == (presysreturnSubtotal + returnamt)
         assert  int(sysreturnQtyDiscount) == (presysreturnQtyDiscount + discountamt)
         assert  int(sysreturnTotalamount) == (presysreturnTotalamount + returnamt)
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

