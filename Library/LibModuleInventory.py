import time
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

AppName = GSV.appName

# Module:Inventory---------------------------------------------------------
def createInventoryGoodReceipt(danpheEMR, qty, item, rate):
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
        danpheEMR.find_element_by_xpath("//input[@formcontrolname='BillNo']").send_keys(BillNo)  # LPH-934, LPH_V1.9.3
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

def editInventoryGoodsReceipt(danpheEMR):
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
        danpheEMR.find_element_by_id("qtyip0").clear()  # Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
        danpheEMR.find_element_by_id("qtyip0").send_keys(2)
        danpheEMR.find_element_by_id("SaveGoodsReceiptbtn").click()

def consumptionStore(danpheEMR, itemName, qty, store):
    time.sleep(5)
    if AppName == 'SNCH' or AppName == 'LPH':
        danpheEMR.find_element_by_link_text("SubStore").click()
        time.sleep(9)
        try:
            danpheEMR.find_element_by_xpath("//i[contains(text(),'ADMINISTRATION')]").click()
            #danpheEMR.find_element_by_xpath("//i[contains(text(),'Billing Store')]").click()
        except:
            pass
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Consumption").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("New Consumption").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("itemName0").clear()
        danpheEMR.find_element_by_id("itemName0").send_keys(itemName)
        danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
        danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").clear()
        danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").send_keys(qty)
        danpheEMR.find_element_by_css_selector(".btn-success").click()
        time.sleep(2)

def activateInventory(danpheEMR, inventory='General Inventory' or 'Medical Inventory'):
    print("Inventory Selection Start")
    danpheEMR.find_element_by_link_text("Inventory").click()
    time.sleep(2)
    if inventory == 'General Inventory':
        danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
    else:
        danpheEMR.find_element_by_xpath("//i[contains(text(),'Medical Inventory')]").click()
    print("Inventory Selection End")

def createInventoryDirectDispatch(danpheEMR, itemname, qty, store):
    print(">>START: directDispatch")
    global RequsitionNo
    if AppName == 'SNCH' or AppName== 'LPH' or AppName == 'MPH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        try:
            danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        except:
            pass
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//button[contains(.,'Direct Dispatch  ')]").click()
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(store)
        danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(Keys.ENTER)
        time.sleep(3)
        danpheEMR.find_element_by_id("itemName0").send_keys(itemname)
        time.sleep(2)
        danpheEMR.find_element_by_id("itemName0").send_keys(Keys.ENTER)
        time.sleep(3)
        danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
        danpheEMR.find_element_by_id("qtyip0").send_keys(Keys.ENTER)
        time.sleep(5)
        Quantity = danpheEMR.find_element_by_xpath("//input[@name='availableQuantity']").get_attribute("value")
        print("Available Quantity :", Quantity)
        Quantity = int(Quantity)
        print("Available Quantity :", Quantity)
        # danpheEMR.find_element_by_id("qtyip0").send_keys(Keys.ENTER)
        danpheEMR.find_element_by_id("remarks").send_keys("Direct dispatch test")
        time.sleep(5)
        danpheEMR.find_element_by_id("directDispatchButton").click()
        time.sleep(5)
        if AppName == 'LPH':
            RequsitionNo = danpheEMR.find_element_by_xpath("//div[contains(text(),'निकासा नं:')]").text
        else:
            RequsitionNo = danpheEMR.find_element_by_xpath("//div[contains(text(),'Requisition No:')]/child::b").text
        print("Requisition Number is :", RequsitionNo)
        danpheEMR.find_element_by_xpath("//button[contains(.,'Back to Requisition List')]").click()
    print("<<END: directDispatch")
    return RequsitionNo

def countStock(danpheEMR, itemname):
    danpheEMR.find_element_by_link_text("Inventory").click()
    time.sleep(2)
    # danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Stock").click()
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(itemname)
    time.sleep(2)
    itemstock = danpheEMR.find_element_by_css_selector("span > div").text
    time.sleep(5)
    print(itemstock)
    time.sleep(5)
    danpheEMR.find_element_by_css_selector(".fa-sign-out")
    danpheEMR.find_element_by_css_selector(".fa-sign-out").click()
    return itemstock

def preCountStock(itemstock):
    time.sleep(2)
    preitemstock = int(itemstock)
    print(preitemstock)
    return preitemstock

def verifyStock(qty, preitemstock, itemstock):
    time.sleep(2)
    print("Start to Verify Stock")
    print("Preitem stock is :", int(preitemstock))
    print("Item Stock is :", int(itemstock))
    assert int(qty) == int(preitemstock) - int(itemstock)
    print("End of Verifying Stock")

def verifyInventoryDirectDispatch(danpheEMR, RequisitionNo, itemname, qty, store):
    print(">>Start: verifyInventoryDirectDispatch")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(2)
        # danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//label[2]/span").click()
        time.sleep(3)
        ReqNo = danpheEMR.find_element_by_xpath("(//div[@col-id='RequisitionNo'])[2]").text
        time.sleep(2)
        assert ReqNo == RequisitionNo
    print("<<End: verifyInventoryDirectDispatch")

def dispatchRequisition(danpheEMR, ssReqNo, GeneralInventory, itemname, qty):
    print(">>START: DispatchRequisition")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        # danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Requisition").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(ssReqNo)
        time.sleep(3)
        danpheEMR.find_element_by_xpath(
            "//a[contains(text(),'Dispatch Requisition')]").click()  # This step can get failed if "AllowSubstoreDispatchWithoutVerification" = false.
        time.sleep(2)
        danpheEMR.find_element_by_id("remarks").send_keys("dispatching req")
        danpheEMR.find_element_by_id("DispatchBtn").click()
        time.sleep(9)
        danpheEMR.find_element_by_xpath("//button[contains(text(),'Back to Requisition List')]").click()
    print("<<END: dispatchRequisition")

def verifyDispatchRequisition(danpheEMR, ssReqNo):
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

def createPurchaseRequest(danpheEMR, ItemName, qty):
    print(">>START: createPurchaseRequest")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        # danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
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

def verifyPurchaseRequest(danpheEMR, PRNo, ItemName, qty):
    print(">>START: verifyPurchaseRequest")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(9)
        # danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Internal").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Purchase Request").click()
        time.sleep(3)
        PRNo1 = int(danpheEMR.find_element_by_xpath("(//div[@col-id='PRNumber'])[2]").text)
        assert PRNo1 == PRNo
    print(">>END: veriifyPurchaseRequest")

def InventoryStockManage(danpheEMR, managetype):
    print(">>START: InventoryStockManage")
    global actualAvailableQty
    global grNo
    global UnitPrice
    danpheEMR.find_element_by_link_text("Inventory").click()
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(2)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys("PLANE SCISSOR 6")
    time.sleep(2)
    actualAvailableQty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
    actualAvailableQty = int(actualAvailableQty)
    print("actualAvailableQty", actualAvailableQty)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
    time.sleep(6)
    grNo = danpheEMR.find_element_by_xpath("(//div[@col-id='GoodsReceiptNo'])[2]").text
    print("Goods Receipt No", grNo)
    UnitPrice = danpheEMR.find_element_by_xpath("(//div[@col-id='ItemRate'])[2]").text
    print("Unit Price", UnitPrice)
    danpheEMR.find_element_by_xpath("//i[@class='fa fa-backward']").click()
    time.sleep(2)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys("PLANE SCISSOR 6")
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Manage Stock')]").click()
    time.sleep(3)
    grNoTemp = danpheEMR.find_element_by_xpath(
        "//td[contains(text(),'GR No.')]/parent::tr/parent::thead/following-sibling::tbody/child::tr/child::td").text
    assert grNo == grNoTemp
    currentQty = danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").get_attribute("value")
    print("currentQty", currentQty)
    currentQty = int(currentQty)
    assert currentQty == actualAvailableQty
    modifyin = currentQty + 1
    modifyOut = currentQty - 1
    print("modifyin", modifyin)
    print("modifyOut", modifyOut)
    danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").clear()
    time.sleep(3)
    if managetype == "in":
        danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").send_keys(modifyin)
        time.sleep(3)
        print("Manage In done")
    if managetype == "out":
        danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").send_keys(modifyOut)
        time.sleep(3)
        print("Manage Out done")
        time.sleep(3)
    danpheEMR.find_element_by_xpath("//input[@value='Update Stock']").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys("PLANE SCISSOR 6")
    time.sleep(2)
    newavailableQty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
    newavailableQty = int(newavailableQty)
    print("newavailableQty", newavailableQty)  #
    if managetype == "in":
        expectedAvailableQty = actualAvailableQty + 1
        print("expectedAvailableQty", expectedAvailableQty)
        assert newavailableQty == expectedAvailableQty
    if managetype == "out":
        expectedAvailableQty = actualAvailableQty - 1
        print("expectedAvailableQty:", expectedAvailableQty)
        assert newavailableQty == expectedAvailableQty

def verifyInventoryDailyItemDispatchReport(danpheEMR, itemname, qty):
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

def getInventoryStoreCurrentStockLevelReport(danpheEMR, inventory, store):
    global actualTotalStockQuantityInventory
    global actualTotalStockValueInventory
    global actualTotalStockQuantityStore
    global actualTotalStockValueStore
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Inventory").click()
    time.sleep(3)
    try:
        danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
    except:
        pass
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//i[contains(.,'Current Stock Level')]").click()
    time.sleep(2)
    ### for main inventory stock
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-remove").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".c-btn > .fa").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(2)").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(2)").send_keys("general inventory")
    danpheEMR.find_element(By.CSS_SELECTOR, "span > .pure-checkbox > label").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".btn > .fa").click()
    time.sleep(5)
    actualTotalStockQuantityInventory = danpheEMR.find_element_by_xpath(
        "//b[contains(text(),' Total Stock Quantity ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockQuantityInventory = float(actualTotalStockQuantityInventory)
    print("actualTotalStockQuantityInventory-:", actualTotalStockQuantityInventory)
    actualTotalStockValueInventory = danpheEMR.find_element_by_xpath(
        "//b[contains(text(),' Total Stock Value ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockValueInventory = actualTotalStockValueInventory.replace(',', '')
    actualTotalStockValueInventory = float(actualTotalStockValueInventory)
    print("actualTotalStockValueInventory:", actualTotalStockValueInventory)
    ### for sub store stock
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-remove").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".c-btn > .fa").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".pure-checkbox:nth-child(30) > label").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//span[contains(text(),'Load')]").click()
    #danpheEMR.driver.find_element(By.CSS_SELECTOR, ".btn > .fa").click()
    #danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(30)").click()
    #danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(30)").send_keys("ADMINISTRATION")
    #danpheEMR.find_element(By.CSS_SELECTOR, "span > .pure-checkbox > label").click()
    #danpheEMR.find_element(By.CSS_SELECTOR, ".btn > .fa").click()
    time.sleep(5)
    actualTotalStockQuantityStore = danpheEMR.find_element_by_xpath(
        "//b[contains(text(),' Total Stock Quantity ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockQuantityStore = float(actualTotalStockQuantityStore)
    print("actualTotalStockQuantityStore-:", actualTotalStockQuantityStore)
    actualTotalStockValueStore = danpheEMR.find_element_by_xpath(
        "//b[contains(text(),' Total Stock Value ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockValueStore = actualTotalStockValueStore.replace(',', '')
    actualTotalStockValueStore = float(actualTotalStockValueStore)
    print("actualTotalStockValueStore:", actualTotalStockValueStore)

def preInventoryStoreCurrentStockLevelReport():
    global preTotalStockQuantityInventory
    global preTotalStockValueInventory
    global preTotalStockQuantityStore
    global preTotalStockValueStore
    ### for main inventory stock
    preTotalStockQuantityInventory = actualTotalStockQuantityInventory
    preTotalStockValueInventory = actualTotalStockValueInventory
    ### for sub store stock
    preTotalStockQuantityStore = actualTotalStockQuantityStore
    preTotalStockValueStore = actualTotalStockValueStore
def verifyInventoryStoreCurrentStockLevelReport(type, qty, unitprice):
    global expectedTotalStockQuantityInventory
    global expectedTotalStockValueInventory
    global expectedTotalStockQuantityStore
    global expectedTotalStockValueStore
    ### for Main Inventory stock verification
    if type == 'DirectDispatch':
        ### for Main Inventory stock verification
        expectedTotalStockQuantityInventory = preTotalStockQuantityInventory - qty
        print("expectedTotalStockQuantityInventory:", expectedTotalStockQuantityInventory)
        assert actualTotalStockQuantityInventory == expectedTotalStockQuantityInventory
        expectedTotalStockValueInventory = preTotalStockValueInventory - qty*unitprice
        print("expectedTotalStockValueInventory:", expectedTotalStockValueInventory)
        assert actualTotalStockValueInventory == expectedTotalStockValueInventory
        ### for sub Store Stock verification
        expectedTotalStockQuantityStore = preTotalStockQuantityStore + qty
        print("expectedTotalStockQuantityStore:", expectedTotalStockQuantityStore)
        assert actualTotalStockQuantityStore == expectedTotalStockQuantityStore
        expectedTotalStockValueStore = preTotalStockValueStore + qty * unitprice
        print("expectedTotalStockValueStore:", expectedTotalStockValueStore)
        assert actualTotalStockValueStore == expectedTotalStockValueStore
    elif type == 'SubStoreConsumption':
        ### for sub Store Stock verification
        expectedTotalStockQuantityStore = preTotalStockQuantityStore - qty
        print("expectedTotalStockQuantityStore:", expectedTotalStockQuantityStore)
        assert actualTotalStockQuantityStore == expectedTotalStockQuantityStore
        expectedTotalStockValueStore = preTotalStockValueStore - qty*unitprice
        print("expectedTotalStockValueStore:", expectedTotalStockValueStore)
        assert actualTotalStockValueStore == expectedTotalStockValueStore
def selectInventory(danpheEMR, inventory):
    time.sleep(5)
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Inventory").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)

def selectDispensary(danpheEMR, dispensary):
    time.sleep(5)
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Dispensary").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//i[contains(text(),'MainDispensary')]").click()
        time.sleep(3)

def getInventorySummaryReport(danpheEMR):
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

def verifyInventorySummaryReport(purchaseqty, purchaseamount, consumeqty, consumeamount, manageinqty, manageinamount,
                                 manageoutqty, manageoutamount):
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
    calcNewStockManageInValue = preStockManageInValue + manageinamount  #
    print("calcNewStockManageInValue", calcNewStockManageInValue)  #
    print("StockManageInValue", StockManageInValue)
    print("preStockManageInValue", preStockManageInValue)
    print("manageinamount", manageinamount)
    assert StockManageInValue == preStockManageInValue + manageinamount  # script failing with bug: EMR-2832
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
    tempclosing = float(preClosingValue) + float(purchaseamount) + float(manageinamount) - float(consumeamount) - float(
        manageoutamount)
    print("tempclosing", tempclosing)
    assert float(ClosingValue) == tempclosing
    print("ClosingQty", ClosingQty)
    print("preClosingQty", preClosingQty)
    print("purchaseqty", purchaseqty)
    print("consumeqty", consumeqty)
    print("manageinqty", manageinqty)
    tempclosingqty = float(preClosingQty) + purchaseqty + manageinqty - consumeqty - manageoutqty
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
