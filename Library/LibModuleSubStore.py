import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

AppName = GSV.appName
#Module: SubStore Test Actions
def selectSubStore(danpheEMR, substore='Administration' or 'Emergency Store'):
      print("Start>> selectSubStore")
      danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      if substore == "Administration":
            danpheEMR.find_element_by_xpath("//i[contains(text(),'ADMINISTRATION')]").click()
      elif substore == 'Emergency Store':
            danpheEMR.find_element_by_xpath("//i[contains(text(),'Emergency Store')]").click()
      else:
            danpheEMR.find_element_by_xpath("//i[contains(text(),'Emergency Store')]").click()
      print("End<<selectSubStore")

def createSubStoreRequisition(danpheEMR, InventoryName, ItemName, Qty):
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

def verifySubStoreRequisition(danpheEMR, ssReqNo, InventoryName, ItemName, Qty):
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

def receiveInventoryDispatch(danpheEMR, substore, ssReqNo):
      print("Start>> createSubStoreRequisition")
      time.sleep(6)
      danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(5)
      danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory')]").click()
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

def verifyReceivedInventoryDispatch(danpheEMR, ssReqNo):
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

def countStockSub(danpheEMR, itemname):
      print(">>START: Counting Sub-store's Stock of :", itemname)
      time.sleep(5)
      danpheEMR.find_element_by_link_text("SubStore").click()
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Inventory')]").click()
      # danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(itemname)
      time.sleep(2)
      stock = danpheEMR.find_element_by_css_selector("span > div").text
      print("Stock of item is :", stock)
      print(">>END: End of Sub-store stock count")
      return stock

def prestockcountSub(stock):
      preStock = int(stock)
      print("previous Stock of Item is :", preStock)
      return preStock

def verifyStockSub(qty, preStock, stock):
     time.sleep(2)
     print("Start to Verify Stock")
     print("Prestock of substore's item  is :", int(preStock))
     print("Substore's Item Stock is :", int(stock))
     assert int(qty) == int(stock) - int(preStock)
     print("End of Verifying Stock")

def createNewConsumption(danpheEMR, substore, itemName):
      print(">>Start : Consumption of item by Staff")
      danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
      time.sleep(2)
      # since store is choosen no need to choose this
      # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
      time.sleep(1)
      # danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
      danpheEMR.find_element(By.XPATH, "//div[2]/ul/li[2]/a").click()
      danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/WardSupply/Inventory/Consumption')]").click()
      danpheEMR.find_element(By.XPATH, " //a[contains(text(),'New Consumption')]").click()
      time.sleep(2)
      danpheEMR.find_element(By.ID, "itemName0").click()
      danpheEMR.find_element(By.ID, "itemName0").send_keys(itemName)
      time.sleep(2)
      danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.ENTER)
      danpheEMR.find_element(By.ID, "remark").send_keys("Consumption by  user name Sabitri")
      danpheEMR.find_element(By.ID, "save").click()







def wait_for_window(danpheEMR, timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

