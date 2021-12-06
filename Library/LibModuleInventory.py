import time
import Library.ApplicationConfiguration as AC
import random
from selenium.webdriver.common.keys import Keys

danpheEMR = AC.danpheEMR
AppName = AC.appName

# Module:Inventory---------------------------------------------------------
def createInventoryGoodReceipt(qty, item, rate):
      print(">>START: createGoodReceipt")
      global BillNo
      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("Procurement").click()
         time.sleep(5)
         danpheEMR.find_element_by_link_text("Goods Arrival Notification").click()
         time.sleep(5)
         danpheEMR.find_element_by_xpath("//a[contains(.,' Create Goods Receipt')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").click()
         time.sleep(2)
         danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .form-control").send_keys(Keys.RETURN)
         BillNo = random.randint(100, 99999)
         print("Bill No", BillNo)
         danpheEMR.find_element_by_xpath("//input[@formcontrolname='BillNo']").send_keys(BillNo) # LPH-934, LPH_V1.9.3
         danpheEMR.find_element_by_id("itemName0").send_keys(item)
         danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
         danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
         time.sleep(2)
         danpheEMR.find_element_by_id("rateip0").clear()
         danpheEMR.find_element_by_id("rateip0").send_keys(rate)
         danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//button[contains(text(),'Back to Goods Receipt List')]").click()
      print("<<END: createGoodReceipt")
def editInventoryGoodsReceipt():
      print(">>START: edit GoodReceipt")
      time.sleep(2)
      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("Procurement").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("Goods Arrival Notification").click()
         time.sleep(3)
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(BillNo)
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//button[contains(text(),' Edit Receipt ')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_id("qtyip0").clear() #Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
         danpheEMR.find_element_by_id("qtyip0").send_keys(2)
         danpheEMR.find_element_by_id("SaveGoodsReceiptbtn").click()
def InventoryConsumption(item, qty, store):
      time.sleep(5)
      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("SubStore").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//i[contains(text(),'Billing Store')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("Consumption").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("New Consumption").click()
         time.sleep(2)
         danpheEMR.find_element_by_id("itemName0").clear()
         danpheEMR.find_element_by_id("itemName0").send_keys(item)
         danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
         danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").clear()
         danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").send_keys(qty)
         danpheEMR.find_element_by_css_selector(".btn-success").click()
         time.sleep(2)
def createInventoryDirectDispatch(itemname, qty, store):
       print(">>START: directDispatch")
       if AppName == 'SNCH':
          time.sleep(3)
          danpheEMR.find_element_by_link_text("Inventory").click()
          time.sleep(9)
          danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
          time.sleep(3)
          danpheEMR.find_element_by_link_text("Internal").click()
          time.sleep(5)
          danpheEMR.find_element_by_xpath("//button[contains(.,'Direct Dispatch  ')]").click()
          time.sleep(2)
          danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(store)
          danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(Keys.TAB)
          time.sleep(3)
          danpheEMR.find_element_by_id("itemName0").send_keys(itemname)
          time.sleep(3)
          danpheEMR.find_element_by_id("itemName0").send_keys(Keys.ENTER)
          time.sleep(3)
          danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
          time.sleep(5)
          #danpheEMR.find_element_by_id("qtyip0").send_keys(Keys.ENTER)
          danpheEMR.find_element_by_id("remarks").send_keys("Direct dispatch test")
          time.sleep(1)
          danpheEMR.find_element_by_xpath("//input[@value='Direct Dispatch']").click()
          time.sleep(8)
          RequsitionNo = danpheEMR.find_element_by_xpath("//div[contains(text(),'Requisition No:')]/child::b").text
          return RequsitionNo
       print("<<END: directDispatch")
def verifyInventoryDirectDispatch(RequisitionNo, ItemName, qty, StoreName):
    print(">>Start: verifyInventoryDirectDispatch")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        #time.sleep(9)
        #danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//label[2]/span").click()
        time.sleep(3)
        ReqNo = danpheEMR.find_element_by_xpath("(//div[@col-id='RequisitionNo'])[2]").text
        time.sleep(2)
        assert ReqNo == RequisitionNo
    print("<<End: verifyInventoryDirectDispatch")
def dispatchRequisition(ssReqNo, GeneralInventory, itemname, qty):
    print(">>START: DispatchRequisition")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        #danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Requisition").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(ssReqNo)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//a[contains(text(),'Dispatch Requisition')]").click() # This step can get failed if "AllowSubstoreDispatchWithoutVerification" = false.
        time.sleep(2)
        danpheEMR.find_element_by_id("remarks").send_keys("dispatching req")
        danpheEMR.find_element_by_id("DispatchBtn").click()
        time.sleep(9)
        danpheEMR.find_element_by_xpath("//button[contains(text(),'Back to Requisition List')]").click()
    print("<<END: dispatchRequisition")
def verifyDispatchRequisition(ssReqNo):
    print(">>START: verifyDispatchRequisition")
    if AppName == 'SNCH':
        danpheEMR.find_element_by_xpath("//label[2]/span").click()
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(ssReqNo)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
        time.sleep(4)
        ssReqNo1 = danpheEMR.find_element_by_xpath("//div[contains(text(),'Requisition No:')]/child::b").text
        print("ssReqNo1:", ssReqNo1)
        print("ssReqNo:", ssReqNo)
        assert ssReqNo1 == ssReqNo
    print("<<END: verifyDispatchRequisition")
def createPurchaseRequest(ItemName, qty):
    print(">>START: createPurchaseRequest")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        #danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Purchase Request").click()
        time.sleep(2)
        PRNo = int(danpheEMR.find_element_by_xpath("(//div[@col-id='PRNumber'])[2]").text)
        print("PRNo:", PRNo)
        danpheEMR.find_element_by_xpath("//button[contains(.,'Create Purchase Request')]").click()
        time.sleep(4)
        danpheEMR.find_element_by_id("itemName0").send_keys(ItemName)
        time.sleep(2)
        danpheEMR.find_element_by_id("qty0").send_keys(qty)
        danpheEMR.find_element_by_id("RequestPORequisition").click()
        PRNo = PRNo + 1
        return PRNo
    print("<<END: createPurchaseRequest")
def verifyPurchaseRequest(PRNo, ItemName, qty):
    print(">>START: verifyPurchaseRequest")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        #danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Purchase Request").click()
        time.sleep(3)
        PRNo1 = int(danpheEMR.find_element_by_xpath("(//div[@col-id='PRNumber'])[2]").text)
        assert PRNo1 == PRNo
    print(">>END: veriifyPurchaseRequest")
def InventoryStockManage(managetype):
      print(">>START: InventoryStockManage")
      danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys("PHOTOCOPY PAPER (CUTTING)")
      time.sleep(2)
      availableQty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
      availableQty = int(availableQty)
      print("case1", availableQty)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
      grNo = danpheEMR.find_element_by_xpath("(//div[@col-id='GoodsReceiptNo'])[2]").text
      print("Goods Receipt No", grNo)
      global UnitPrice
      UnitPrice = danpheEMR.find_element_by_xpath("(//div[@col-id='ItemRate'])[2]").text
      print("Unit Price", UnitPrice)
      danpheEMR.find_element_by_xpath("//i[@class='fa fa-backward']").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys("PHOTOCOPY PAPER (CUTTING)")
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Manage Stock')]").click()
      time.sleep(3)
      grNoTemp = danpheEMR.find_element_by_xpath("//td[contains(text(),'GR No.')]/parent::tr/parent::thead/following-sibling::tbody/child::tr/child::td").text
      assert grNo == grNoTemp
      currentQty = danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").get_attribute("value")
      print("currentQty", currentQty)
      currentQty = float(currentQty)
      modifyin = int(currentQty + 1)
      modifyOut = int(currentQty - 1)
      print("modifyOut", modifyOut)
      print("modifyin", modifyin)
      danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").clear()
      if managetype == "in":
         danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").send_keys(modifyin)
         print("Manage In done")
      if managetype == "out":
         danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").send_keys(modifyOut)
         print("Manage Out done")
         time.sleep(3)
      danpheEMR.find_element_by_xpath("//input[@value='Update Stock']").click()
      danpheEMR.find_element_by_id("quickFilterInput").send_keys("PHOTOCOPY PAPER (CUTTING)")
      time.sleep(2)
      newavailableQty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
      print("newavailableQty", newavailableQty)         #
      print("availableQty", availableQty)               #
      if managetype == "in":
         assert int(newavailableQty) == int(availableQty + 1)
      if managetype == "out":
         assert int(newavailableQty) == availableQty - 1
def verifyInventoryDailyItemDispatchReport(itemname, qty):
       danpheEMR.find_element_by_link_text("Inventory").click()
       time.sleep(3)
       danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
       time.sleep(2)
       danpheEMR.find_element_by_xpath("//i[contains(.,'Daily Item Dispatch')]").click()
       time.sleep(2)
       danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
       time.sleep(2)
       danpheEMR.find_element_by_id("quickFilterInput").send_keys("nursing store")
       time.sleep(2)
       danpheEMR.find_element_by_xpath("//span[contains(.,'Requisition ID')]").click()
       time.sleep(3)
       danpheEMR.find_element_by_xpath("//span[contains(.,'Requisition ID')]").click()
       time.sleep(2)
       element1 = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
       assert element1 == itemname
       element2 = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
       print(element2)
       print(qty)
       assert element2 == str(qty)
def getInventoryCurrentStockLevelReport(store):
      global TotalStockQuantity
      global TotalStockValue
      danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Current Stock Level')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_css_selector(".fa-remove").click()
      danpheEMR.find_element_by_xpath("//span[contains(.,'---Select Item---')]").click()
      danpheEMR.find_element_by_xpath("//input[@type='text']").send_keys(store)
      if store == "Main Store":
         danpheEMR.find_element_by_xpath("//label[contains(.,'Main Store')]").click()
      if store == "OT Store":
         danpheEMR.find_element_by_xpath("//label[contains(.,'OT Store')]").click()
      danpheEMR.find_element_by_xpath("//button[contains(.,' Load')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("(//a[contains(text(),'View')])[1]").click()
      time.sleep(3)
      sysStoreName = danpheEMR.find_element_by_xpath(
         "(//th[contains(text(),' Store Name ')]/parent::tr/following-sibling::tr/child::td)[1]").text
      print("sysStoreName", sysStoreName)
      assert store == sysStoreName
      danpheEMR.find_element_by_xpath("//a[@title='Cancel']").click()
      time.sleep(7)
      TotalStockQuantity = danpheEMR.find_element_by_xpath(
         "//b[contains(text(),' Total Stock Quantity ')]/parent::span/parent::td/following-sibling::td[1]").text
      print("TotalStockQuantity-:", TotalStockQuantity)
      TotalStockValue = danpheEMR.find_element_by_xpath(
         "//b[contains(text(),' Total Stock Value ')]/parent::span/parent::td/following-sibling::td[1]").text
      TotalStockValue = TotalStockValue.replace(',', '')
      print("TotalStockValue:", TotalStockValue)
def preInventoryCurrentStockLevelReport():
      global preTotalStockQuantity
      global preTotalStockValue
      preTotalStockQuantity = float(TotalStockQuantity)
      preTotalStockValue = float(TotalStockValue)
def verifyInventoryCurrentStockLevelReport(type, qty, unitprice):
      global calcTotalStockQuantity
      global calcTotalStockValue
      print("preTotalStockQuantity", preTotalStockQuantity)
      print("TotalStockQuantity", TotalStockQuantity)
      print("qty", qty)
      calcQtyValue = float(qty * unitprice)
      if type == "out":
         calcTotalStockQuantity = format(preTotalStockQuantity - qty)
         calcTotalStockValue = float(preTotalStockValue - calcQtyValue)
      if type == "in":
         calcTotalStockQuantity = float(preTotalStockQuantity + qty)
         calcTotalStockValue = float(preTotalStockValue + calcQtyValue)
      print("calcTotalStockQuantity", calcTotalStockQuantity)
      calcTotalStockQuantityf = calcTotalStockQuantity.partition(".")[0]
      TotalStockQuantityf = TotalStockQuantity.partition(".")[0]
      print("calcTotalStockQuantityf", calcTotalStockQuantityf)
      print("TotalStockQuantityf", TotalStockQuantityf)
      assert TotalStockQuantityf == calcTotalStockQuantityf
      print("calcQtyValue", calcQtyValue)
      print("calcTotalStockValue", calcTotalStockValue)
      print("TotalStockValue", TotalStockValue)
      calcTotalStockValue = float(calcTotalStockValue)
      TotalStockValuec = float(TotalStockValue)
      assert round(float(TotalStockValuec)) == round(float(calcTotalStockValue))
def selectInventory(inventory):
      time.sleep(5)
      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("Inventory").click()
         time.sleep(5)
         danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
         time.sleep(3)
def selectDispensary(dispensary):
      time.sleep(5)

      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("Dispensary").click()
         time.sleep(5)
         danpheEMR.find_element_by_xpath("//i[contains(text(),'MainDispensary')]").click()
         time.sleep(3)
def getInventorySummaryReport():
      global OpeningValue
      global OpeningQty
      global PurchaseValue
      global PurchaseQty
      global StockManageInValue
      global StockManageInQty
      global StockManageOutValue
      global StockManageOutQty
      global ConsumptionValue
      global ConsumptionQty
      global ClosingValue
      global ClosingQty
      time.sleep(3)
      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("Inventory").click()
         time.sleep(5)
         danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//i[contains(.,'Inventory Summary')]").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//button[contains(.,' Load')]").click()
         time.sleep(7)
         OpeningValue = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),' Opening Value ')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         OpeningValue = float(OpeningValue.replace(',', ''))
         print("OpeningValue", OpeningValue)
         OpeningQty = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Opening Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("OpeningQty", OpeningQty)
         PurchaseValue = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),' Purchase Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         PurchaseValue = float(PurchaseValue.replace(',', ''))
         print("PurchaseValue", PurchaseValue)
         PurchaseQty = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Purchase Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("PurchaseQty", PurchaseQty)
         StockManageInValue = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage In-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         StockManageInValue = float(StockManageInValue.replace(',', ''))
         print("StockManageInValue", StockManageInValue)
         StockManageInQty = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage In-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("StockManageInQty", StockManageInQty)
         StockManageOutValue = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage OUT-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         StockManageOutValue = float(StockManageOutValue.replace(',', ''))
         print("StockManageOutValue", StockManageOutValue)
         StockManageOutQty = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage OUT-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("StockManageOutQty", StockManageOutQty)
         ConsumptionValue = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Consumption Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         ConsumptionValue = float(ConsumptionValue.replace(',', ''))
         print("ConsumptionValue", ConsumptionValue)
         ConsumptionQty = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Consumption Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("ConsumptionQty", ConsumptionQty)
         ClosingValue = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Closing Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         ClosingValue = float(ClosingValue.replace(',', ''))
         print("ClosingValue", ClosingValue)
         ClosingQty = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Closing Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("ClosingQty", ClosingQty)
def preInventorySummaryReport():
      global preOpeningValue
      global preOpeningQty
      global prePurchaseValue
      global prePurchaseQty
      global preStockManageInValue
      global preStockManageInQty
      global preStockManageOutValue
      global preStockManageOutQty
      global preConsumptionValue
      global preConsumptionQty
      global preClosingValue
      global preClosingQty
      preOpeningValue = OpeningValue
      preOpeningQty = OpeningQty
      prePurchaseValue = PurchaseValue
      prePurchaseQty = PurchaseQty
      preStockManageInValue = StockManageInValue
      preStockManageInQty = StockManageInQty
      preStockManageOutValue = StockManageOutValue
      preStockManageOutQty = StockManageOutQty
      preConsumptionValue = ConsumptionValue
      preConsumptionQty = ConsumptionQty
      preClosingValue = ClosingValue
      preClosingQty = ClosingQty
def verifyInventorySummaryReport(purchaseqty, purchaseamount, consumeqty, consumeamount, manageinqty, manageinamount, manageoutqty, manageoutamount):
      print("preOpeningValue", preOpeningValue)
      print("OpeningValue", OpeningValue)
      time.sleep(3)
      assert OpeningValue == preOpeningValue
      assert OpeningQty == preOpeningQty
      x = PurchaseValue
      print("x", x)
      y = prePurchaseValue + purchaseamount
      print("y", y)
      assert x == y
      assert int(PurchaseQty) == int(prePurchaseQty) + purchaseqty
      calcNewStockManageInValue = preStockManageInValue + manageinamount   #
      print("calcNewStockManageInValue", calcNewStockManageInValue)        #
      print("StockManageInValue", StockManageInValue)
      print("preStockManageInValue", preStockManageInValue)
      print("manageinamount", manageinamount)
      assert StockManageInValue == preStockManageInValue + manageinamount #script failing with bug: EMR-2832
      assert int(StockManageInQty) == int(preStockManageInQty) + manageinqty
      assert StockManageOutValue == preStockManageOutValue + manageoutamount
      assert int(StockManageOutQty) == int(preStockManageOutQty) + manageoutqty
      print("ConsumptionValue", ConsumptionValue)
      print("preConsumptionValue", preConsumptionValue)
      print("consumeamount", consumeamount)
      tempSum = float(preConsumptionValue) + float(consumeamount)
      print("TempSum", tempSum)
      assert int(ConsumptionValue) == int(tempSum)
      assert int(ConsumptionQty) == int(preConsumptionQty) + consumeqty
      print("ClosingValue", ClosingValue)
      print("preClosingValue", preClosingValue)
      print("purchaseamount", purchaseamount)
      print("consumeamount", consumeamount)
      print("manageinamount", manageinamount)
      tempclosing = float(preClosingValue) + float(purchaseamount) + float(manageinamount) - float(consumeamount) - float(manageoutamount)
      print("tempclosing", tempclosing)
      assert float(ClosingValue) == tempclosing
      print("ClosingQty", ClosingQty)
      print("preClosingQty", preClosingQty)
      print("purchaseqty", purchaseqty)
      print("consumeqty", consumeqty)
      print("manageinqty", manageinqty)
      tempclosingqty = float(preClosingQty) + purchaseqty +manageinqty - consumeqty -manageoutqty
      print("tempclosingqty", tempclosingqty)
      print("ClosingQty", ClosingQty)
      assert float(ClosingQty) == float(tempclosingqty)
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

