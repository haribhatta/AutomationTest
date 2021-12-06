from selenium import webdriver
import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys

danpheEMR = AC.danpheEMR
AppName = AC.appName

#Module: SubStore Test Actions
def selectSubStore(substore):
      print("Start>> selectSubStore")
      danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'ADMINISTRATION')]").click()
      print("End<<selectSubStore")
def createSubStoreRequisition(InventoryName, ItemName, Qty):
      print("Start>> createSubStoreRequisition")
      time.sleep(6)
      danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'Administration Store')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory Requisition')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//input[@class='btn btn-primary']").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("activeInventory").send_keys(InventoryName)
      time.sleep(3)
      danpheEMR.find_element_by_id("activeInventory").send_keys(Keys.TAB)
      time.sleep(3)
      danpheEMR.find_element_by_id("itemName0").send_keys(ItemName)
      danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
      danpheEMR.find_element_by_id("qtyip0").send_keys(Qty)
      time.sleep(3)
      danpheEMR.find_element_by_id("save_requisition").click()
      time.sleep(5)
      ssReqNo = danpheEMR.find_element_by_xpath("//p[contains(text(),'Requisition No:')]/child::b").text
      print("Sub Store Requisition No", ssReqNo)
      danpheEMR.find_element_by_id("backToList").click()
      print("End<<createSubStoreRequisition")
      return ssReqNo
def verifySubStoreRequisition(ssReqNo, InventoryName, ItemName, Qty):
      print("Start>> verifySubStoreRequisition")
      #time.sleep(6)
      #danpheEMR.find_element_by_link_text("SubStore").click()
      #time.sleep(5)
      #danpheEMR.find_element_by_xpath("//i[contains(text(),'Administration Store')]").click()
      #time.sleep(5)
      #danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory Requisition')]").click()
      time.sleep(5)
      ReqNo = danpheEMR.find_element_by_xpath("(//div[@col-id='RequisitionNo'])[2]").text
      assert ReqNo == ssReqNo
      #danpheEMR.find_element_by_xpath("//label[2]/span").click()
      #time.sleep(3)
      #ssReqNo1 =
      print("<<END: verifySubStoreRequisition")
def receiveInventoryDispatch(ssReqNo):
      print("Start>> createSubStoreRequisition")
      time.sleep(6)
      danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      #danpheEMR.find_element_by_xpath("//i[contains(text(),'Administration Store')]").click()
      #time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory Requisition')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(ssReqNo)
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Receive Items')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("ReceiveButton").click()
      time.sleep(5)
      #danpheEMR.find_element_by_id("backToList").click()
      danpheEMR.find_element_by_xpath("(//button[@class='btn btn-primary btn-sm'])[1]").click()
def verifyReceivedInventoryDispatch(ssReqNo):
      print(">>START: verifyReceivedInventoryDispatch")
      time.sleep(6)
      danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      #danpheEMR.find_element_by_xpath("//i[contains(text(),'Administration Store')]").click()
      #time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory Requisition')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//label[2]/span").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(ssReqNo)
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
      time.sleep(3)
      ssReqNo1= danpheEMR.find_element_by_xpath("//p[contains(text(),'Requisition No:')]/child::b").text
      assert ssReqNo1 == ssReqNo
      danpheEMR.find_element_by_id("backToList").click()
      print("<<END: verifyReceivedInventoryDispatch")
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

