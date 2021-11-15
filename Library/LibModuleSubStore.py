from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)

#Module: SubStore Test Actions
   def selectSubStore(self, substore):
      print("Start>> selectSubStore")
      self.danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//i[contains(text(),'ADMINISTRATION')]").click()
      print("End<<selectSubStore")
   def createSubStoreRequisition(self, InventoryName, ItemName, Qty):
      print("Start>> createSubStoreRequisition")
      self.danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory Requisition')]").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//input[@class='btn btn-primary']").click()


      print("End<<createSubStoreRequisition")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

