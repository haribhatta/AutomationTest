import time
import Library.GlobalShareVariables as GSV
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

AppName = GSV.appName


# Module:Inventory---------------------------------------------------------
def createInventoryGoodReceipt(danpheEMR, qty, item, rate, paymentMode):
    print(">>START: createGoodReceipt")
    global BillNo
    #if AppName == 'SNCH':
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,  "//a[contains(.,' Create Goods Receipt')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//input[@onclick='this.select();']").click()
    time.sleep(2)
    danpheEMR.find_element(By.CSS_SELECTOR,   ".danphe-auto-complete-wrapper > .form-control").send_keys(Keys.RETURN)
    BillNo = random.randint(100, 99999)
    print("Bill No", BillNo)
    danpheEMR.find_element(By.XPATH,  "//input[@formcontrolname='BillNo']").send_keys(BillNo)  # LPH-934, LPH_V1.9.3
    time.sleep(5)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(item)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "qtyip0").send_keys(qty)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "rateip0").clear()
    danpheEMR.find_element(By.ID, "rateip0").send_keys(rate)
    if paymentMode == 'Cash':
        payMode = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname='PaymentMode']"))
        payMode.select_by_visible_text("Cash")
    danpheEMR.find_element(By.XPATH,  "//input[@value='Receipt']").click()
    time.sleep(3)
    #danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Back to Goods Receipt List')]").click()
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Cancel GR ')]").send_keys(Keys.ESCAPE)
    print("<<END: createGoodReceipt")
    return BillNo


def editInventoryGoodsReceipt(danpheEMR, BillNo):
    print("START>>editInventoryGoodsReceipt")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(BillNo)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'View')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//button[contains(text(),' Edit Receipt ')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "qtyip0").clear()  # Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
    danpheEMR.find_element(By.ID, "qtyip0").send_keys(2)
    danpheEMR.find_element(By.ID, "SaveGoodsReceiptbtn").click()
    print("END>>editInventoryGoodsReceipt")


def consumptionStore(danpheEMR, itemName, qty, store):
    print("START>>consumptionStore")
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(9)
    try:
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'" + store + "')]").click()
        # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'Billing Store')]").click()
    except:
        pass
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Consumption").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "New Consumption").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "itemName0").clear()
    danpheEMR.find_element(By.ID, "itemName0").send_keys(itemName)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH,  "//input[@id='qtyip0']").clear()
    danpheEMR.find_element(By.XPATH,  "//input[@id='qtyip0']").send_keys(qty)
    danpheEMR.find_element(By.CSS_SELECTOR,   ".btn-success").click()
    time.sleep(2)
    print("END>>consumptionStore")


def activateInventory(danpheEMR, inventory='General Inventory' or 'Medical Inventory'):
    print("Inventory Selection Start")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(5)
    if inventory == 'General Inventory':
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    else:
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'Medical Inventory')]").click()
    print("Inventory Selection End")


def createInventoryDirectDispatch(danpheEMR, itemname, qty, inventory, store):
    print("START>>createInventoryDirectDispatch")
    global RequsitionNo
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(9)
    try:
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'" + inventory + "')]").click()
    except:
        pass
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,  "//button[contains(.,'Direct Dispatch  ')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "store").send_keys(store)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "store").send_keys(Keys.ENTER)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(itemname)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.ENTER)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "qtyip0").send_keys(qty)
    danpheEMR.find_element(By.ID, "qtyip0").send_keys(Keys.ENTER)
    time.sleep(5)
    Quantity = danpheEMR.find_element(By.XPATH,  "//input[@name='availableQuantity']").get_attribute("value")
    print("Available Quantity :", Quantity)
    Quantity = int(Quantity)
    print("Available Quantity :", Quantity)
    # danpheEMR.find_element(By.ID, "qtyip0").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "remarks").send_keys("Direct dispatch test")
    time.sleep(5)
    danpheEMR.find_element(By.ID, "directDispatchButton").click()
    time.sleep(5)
    if AppName == 'LPH':
        RequsitionNo = danpheEMR.find_element(By.XPATH,  "//div[contains(text(),'निकासा नं:')]").text
        RequsitionNo = int(str(RequsitionNo).replace("निकासा नं:", ""))
        print(RequsitionNo)
    else:
        RequsitionNo = danpheEMR.find_element(By.XPATH,  "//div[contains(text(),'Requisition No:')]/child::b").text
    print("Requisition Number is :", RequsitionNo)
    danpheEMR.find_element(By.XPATH,  "//button[contains(.,'Back to Requisition List')]").click()
    return RequsitionNo
    print("END>>createInventoryDirectDispatch")
    return RequsitionNo


def countStock(danpheEMR, itemname):
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(2)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemname)
    time.sleep(2)
    itemstock = danpheEMR.find_element(By.CSS_SELECTOR,   "span > div").text
    time.sleep(5)
    print(itemstock)
    time.sleep(5)
    danpheEMR.find_element(By.CSS_SELECTOR,   ".fa-sign-out")
    danpheEMR.find_element(By.CSS_SELECTOR,   ".fa-sign-out").click()
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
    print("START>>verifyInventoryDirectDispatch")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(2)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,  "//label[2]/span").click()
    time.sleep(3)
    ReqNo = danpheEMR.find_element(By.XPATH,  "(//div[@col-id='RequisitionNo'])[2]").text
    time.sleep(2)
    assert ReqNo == RequisitionNo
    print("END>>verifyInventoryDirectDispatch")


def dispatchRequisition(danpheEMR, ssReqNo, GeneralInventory, itemname, qty):
    print("START>>DispatchRequisition")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(9)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Requisition").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,
        "//a[contains(text(),'Dispatch Requisition')]").click()  # This step can get failed if "AllowSubstoreDispatchWithoutVerification" = false.
    time.sleep(2)
    danpheEMR.find_element(By.ID, "remarks").send_keys("dispatching req")
    danpheEMR.find_element(By.ID, "DispatchBtn").click()
    time.sleep(9)
    danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Back to Requisition List')]").click()
    print("END>>dispatchRequisition")


def verifyDispatchRequisition(danpheEMR, ssReqNo):
    print("START>>verifyDispatchRequisition")
    danpheEMR.find_element(By.XPATH,  "//label[2]/span").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'View')]").click()
    time.sleep(4)
    ssReqNo1 = danpheEMR.find_element(By.XPATH,  "//div[contains(text(),'Requisition No:')]/child::b").text
    print("ssReqNo1:", ssReqNo1)
    print("ssReqNo:", ssReqNo)
    assert ssReqNo1 == ssReqNo
    print("END>>verifyDispatchRequisition")


def createPurchaseRequest(danpheEMR, ItemName, qty):
    print("START>>createPurchaseRequest")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(9)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Purchase Request").click()
    time.sleep(2)
    PRNo = int(danpheEMR.find_element(By.XPATH,  "(//div[@col-id='PRNumber'])[2]").text)
    print("PRNo:", PRNo)
    danpheEMR.find_element(By.XPATH,  "//button[contains(.,'Create Purchase Request')]").click()
    time.sleep(4)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(ItemName)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "qty0").send_keys(qty)
    danpheEMR.find_element(By.ID, "RequestPORequisition").click()
    PRNo = PRNo + 1
    return PRNo
    print("END>>createPurchaseRequest")


def verifyPurchaseRequest(danpheEMR, PRNo, ItemName, qty):
    print("START>>verifyPurchaseRequest")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(9)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Purchase Request").click()
    time.sleep(3)
    PRNo1 = int(danpheEMR.find_element(By.XPATH,  "(//div[@col-id='PRNumber'])[2]").text)
    assert PRNo1 == PRNo
    print("END>>veriifyPurchaseRequest")


def InventoryStockManage(danpheEMR, managetype, itemName):
    print(">>START: InventoryStockManage")
    global actualAvailableQty
    global grNo
    global UnitPrice
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemName)
    time.sleep(2)
    actualAvailableQty = danpheEMR.find_element(By.XPATH,  
        "(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
    actualAvailableQty = int(actualAvailableQty)
    print("actualAvailableQty", actualAvailableQty)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'View')]").click()
    time.sleep(6)
    grNo = danpheEMR.find_element(By.XPATH,  "(//div[@col-id='GoodsReceiptNo'])[2]").text
    print("Goods Receipt No", grNo)
    UnitPrice = danpheEMR.find_element(By.XPATH,  "(//div[@col-id='ItemRate'])[2]").text
    print("Unit Price", UnitPrice)
    danpheEMR.find_element(By.XPATH,  "//i[@class='fa fa-backward']").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemName)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Manage Stock')]").click()
    time.sleep(3)
    grNoTemp = danpheEMR.find_element(By.XPATH,  
        "//td[contains(text(),'GR No.')]/parent::tr/parent::thead/following-sibling::tbody/child::tr/child::td").text
    assert grNo == grNoTemp
    currentQty = danpheEMR.find_element(By.XPATH,  "//input[@name='ModQuantity']").get_attribute("value")
    print("currentQty", currentQty)
    currentQty = int(currentQty)
    assert currentQty == actualAvailableQty
    modifyin = currentQty + 1
    modifyOut = currentQty - 1
    print("modifyin", modifyin)
    print("modifyOut", modifyOut)
    danpheEMR.find_element(By.XPATH,  "//input[@name='ModQuantity']").clear()
    time.sleep(3)
    if managetype == "in":
        danpheEMR.find_element(By.XPATH,  "//input[@name='ModQuantity']").send_keys(modifyin)
        time.sleep(3)
        print("Manage In done")
    if managetype == "out":
        danpheEMR.find_element(By.XPATH,  "//input[@name='ModQuantity']").send_keys(modifyOut)
        time.sleep(3)
        print("Manage Out done")
        time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//input[@value='Update Stock']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemName)
    time.sleep(2)
    newavailableQty = danpheEMR.find_element(By.XPATH,  "(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
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


def verifyInventoryDailyItemDispatchReport(danpheEMR, itemname, qty, storeName):
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//i[contains(.,'Daily Item Dispatch')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//button[contains(.,' Show Report')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(storeName)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//span[contains(.,'Requisition ID')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//span[contains(.,'Requisition ID')]").click()
    time.sleep(2)
    element1 = danpheEMR.find_element(By.XPATH,  "//div[2]/div/div/div/div[4]").text
    assert element1 == itemname
    element2 = danpheEMR.find_element(By.XPATH,  "//div[2]/div/div/div/div[7]").text
    print(element2)
    print(qty)
    assert element2 == str(qty)


def getInventoryStoreCurrentStockLevelReport(danpheEMR, inventory, store):
    global actualTotalStockQuantityInventory
    global actualTotalStockValueInventory
    global actualTotalStockQuantityStore
    global actualTotalStockValueStore
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    try:
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    except:
        pass
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,  "//i[contains(.,'Current Stock Level')]").click()
    time.sleep(2)
    ### for main inventory stock
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-remove").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".c-btn > .fa").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(2)").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(2)").send_keys("general inventory")
    danpheEMR.find_element(By.CSS_SELECTOR, "span > .pure-checkbox > label").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".btn > .fa").click()
    time.sleep(5)
    actualTotalStockQuantityInventory = danpheEMR.find_element(By.XPATH,  
        "//b[contains(text(),' Total Stock Quantity ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockQuantityInventory = float(actualTotalStockQuantityInventory)
    print("actualTotalStockQuantityInventory-:", actualTotalStockQuantityInventory)
    actualTotalStockValueInventory = danpheEMR.find_element(By.XPATH,  
        "//b[contains(text(),' Total Stock Value ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockValueInventory = actualTotalStockValueInventory.replace(',', '')
    actualTotalStockValueInventory = float(actualTotalStockValueInventory)
    print("actualTotalStockValueInventory:", actualTotalStockValueInventory)
    ### for sub store stock
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-remove").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".c-btn > .fa").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".pure-checkbox:nth-child(30) > label").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//span[contains(text(),'Load')]").click()
    # danpheEMR.driver.find_element(By.CSS_SELECTOR, ".btn > .fa").click()
    # danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(30)").click()
    # danpheEMR.find_element(By.CSS_SELECTOR, ".ng-untouched:nth-child(30)").send_keys("ADMINISTRATION")
    # danpheEMR.find_element(By.CSS_SELECTOR, "span > .pure-checkbox > label").click()
    # danpheEMR.find_element(By.CSS_SELECTOR, ".btn > .fa").click()
    time.sleep(5)
    actualTotalStockQuantityStore = danpheEMR.find_element(By.XPATH,  
        "//b[contains(text(),' Total Stock Quantity ')]/parent::span/parent::td/following-sibling::td[1]").text
    actualTotalStockQuantityStore = float(actualTotalStockQuantityStore)
    print("actualTotalStockQuantityStore-:", actualTotalStockQuantityStore)
    actualTotalStockValueStore = danpheEMR.find_element(By.XPATH,  
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
        expectedTotalStockValueInventory = preTotalStockValueInventory - qty * unitprice
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
        expectedTotalStockValueStore = preTotalStockValueStore - qty * unitprice
        print("expectedTotalStockValueStore:", expectedTotalStockValueStore)
        assert actualTotalStockValueStore == expectedTotalStockValueStore


def selectInventory(danpheEMR, inventory):
    print("START>>selectInventory")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(3)
    print("END>>selectInventory")


def selectDispensary(danpheEMR, dispensary):
    print("START>>selectDispensary")
    danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'MainDispensary')]").click()
    time.sleep(3)
    print("END>>selectDispensary")


def getInventorySummaryReport(danpheEMR):
    print("START>>getInventorySummaryReport")
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
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Reports')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//i[contains(.,'Inventory Summary')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//button[contains(.,' Load')]").click()
    time.sleep(7)
    OpeningValue = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),' Opening Value ')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    OpeningValue = float(OpeningValue.replace(',', ''))
    print("OpeningValue", OpeningValue)
    OpeningQty = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'Opening Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    print("OpeningQty", OpeningQty)
    PurchaseValue = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),' Purchase Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    PurchaseValue = float(PurchaseValue.replace(',', ''))
    print("PurchaseValue", PurchaseValue)
    PurchaseQty = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'Purchase Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    print("PurchaseQty", PurchaseQty)
    StockManageInValue = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'StockManage In-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    StockManageInValue = float(StockManageInValue.replace(',', ''))
    print("StockManageInValue", StockManageInValue)
    StockManageInQty = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'StockManage In-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    print("StockManageInQty", StockManageInQty)
    StockManageOutValue = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'StockManage OUT-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    StockManageOutValue = float(StockManageOutValue.replace(',', ''))
    print("StockManageOutValue", StockManageOutValue)
    StockManageOutQty = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'StockManage OUT-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    print("StockManageOutQty", StockManageOutQty)
    ConsumptionValue = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'Consumption Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    ConsumptionValue = float(ConsumptionValue.replace(',', ''))
    print("ConsumptionValue", ConsumptionValue)
    ConsumptionQty = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'Consumption Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    print("ConsumptionQty", ConsumptionQty)
    ClosingValue = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'Closing Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    ClosingValue = float(ClosingValue.replace(',', ''))
    print("ClosingValue", ClosingValue)
    ClosingQty = danpheEMR.find_element(By.XPATH,
        "(//b[contains(text(),'Closing Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
    print("ClosingQty", ClosingQty)
    print("END>>getInventorySummaryReport")


def preInventorySummaryReport():
    print("START>>preInventorySummaryReport")
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
    print(END>>preInventorySummaryReport)


def verifyInventorySummaryReport(purchaseqty, purchaseamount, consumeqty, consumeamount, manageinqty, manageinamount,
                                 manageoutqty, manageoutamount):
    print("START>>verifyInventorySummaryReport")
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
    assert float(ClosingValue) == float(tempclosing)
    print("ClosingQty", ClosingQty)
    print("preClosingQty", preClosingQty)
    print("purchaseqty", purchaseqty)
    print("consumeqty", consumeqty)
    print("manageinqty", manageinqty)
    tempclosingqty = float(preClosingQty) + purchaseqty + manageinqty - consumeqty - manageoutqty
    print("tempclosingqty", tempclosingqty)
    print("ClosingQty", ClosingQty)
    assert float(ClosingQty) == float(tempclosingqty)
    print("END>>verifyInventorySummaryReport")


def receiveGoodReceipt(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt List").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[11]/span/a").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "ReceivedRemarks").send_keys("Items Received ")
    danpheEMR.find_element(By.ID, "ReceiveButton").click()


def getCancelPoReport(danpheEMR, pono):
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Inventory/Reports/Purchase']").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(text(), 'Cancelled PO and GR')]").click()
    danpheEMR.find_element(By.XPATH, "//b[contains(text(), 'Cancelled PO')]").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(pono)
    view = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[8]/a")
    view.is_displayed()


def getCancelGRReport(danpheEMR, BillNo):
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Inventory/Reports/Purchase']").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(text(), 'Cancelled PO and GR')]").click()
    danpheEMR.find_element(By.XPATH, "//*[@class='btn blue' and @type='button']").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(BillNo)
    view = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[9]/a")
    view.is_displayed


def getPurchaseSummaryReport(danpheEMR):
    print("START>>getPurchaseSummaryReport")
    danpheEMR.implicitly_wait(10)
    global actualCreditSubTotal
    global actualCreditDiscount
    global actualCreditVat
    global actualCreditOtherCharge
    global actualCreditTotalAmount
    global actualCashSubTotal
    global actualCashDiscount
    global actualCashVat
    global actualCashOtherCharge
    global actualCashTotalAmount
    global actualTotalSubTotal
    global actualTotalDiscount
    global actualTotalVat
    global actualTotalOtherCharge
    global actualTotalTotalAmount

    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Inventory/Reports/Purchase']").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(text(), 'Purchase Summary')]").click()
    danpheEMR.find_element(By.XPATH, "//*[@class='btn green btn-success' and @type='button']").click()
    time.sleep(3)

    actualCreditSubTotal = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[2]/span").text
    actualCreditSubTotal = int(str(actualCreditSubTotal).replace(",", ""))
    print("actualCreditSubTotal", actualCreditSubTotal)

    actualCreditDiscount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[3]/span").text
    actualCreditDiscount = actualCreditDiscount.replace(',', '')
    actualCreditDiscount = int(actualCreditDiscount)
    print("actualCreditDiscount:", actualCreditDiscount)

    actualCreditVat = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[4]/span").text
    actualCreditVat = actualCreditVat.replace(',', '')
    actualCreditVat = int(actualCreditVat)
    print("actualCreditVat:", actualCreditVat)

    actualCreditOtherCharge = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[5]/span").text
    actualCreditOtherCharge = actualCreditOtherCharge.replace(',', '')
    actualCreditOtherCharge = int(actualCreditOtherCharge)
    print("actualCreditOtherCharge:", actualCreditOtherCharge)

    actualCreditTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[6]/span").text
    actualCreditTotalAmount = actualCreditTotalAmount.replace(',', '')
    actualCreditTotalAmount = int(str(actualCreditTotalAmount).replace(",", ""))
    print("actualCreditTotalAmount:", actualCreditTotalAmount)

    actualCashSubTotal = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[2]/span").text
    actualCashSubTotal = actualCashSubTotal.replace(',', '')
    actualCashSubTotal = int(actualCashSubTotal)
    print("actualCashSubTotal:", actualCashSubTotal)

    actualCashDiscount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[3]/span").text
    actualCashDiscount = actualCashDiscount.replace(',', '')
    actualCashDiscount = int(actualCashDiscount)
    print("actualCashDiscount:", actualCashDiscount)

    actualCashVat = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[4]/span").text
    actualCashVat = actualCashVat.replace(',', '')
    actualCashVat = int(actualCashVat)
    print("actualCashVat:", actualCashVat)

    actualCashOtherCharge = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[5]/span").text
    actualCashOtherCharge = actualCashOtherCharge.replace(',', '')
    actualCashOtherCharge = int(actualCashOtherCharge)
    print("actualCashOtherCharge:", actualCashOtherCharge)

    actualCashTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[6]/span").text
    actualCashTotalAmount = actualCashTotalAmount.replace(',', '')
    actualCashTotalAmount = int(actualCashTotalAmount)
    print("actualCashTotalAmount:", actualCashTotalAmount)

    actualTotalSubTotal = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[2]/span").text
    actualTotalSubTotal = actualTotalSubTotal.replace(',', '')
    actualTotalSubTotal = int(str(actualTotalSubTotal).replace(",",""))
    print("actualTotalSubTotal:", actualTotalSubTotal)

    actualTotalDiscount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[3]/span").text
    actualTotalDiscount = actualTotalDiscount.replace(',', '')
    actualTotalDiscount = int(actualTotalDiscount)
    print("actualTotalDiscount:", actualTotalDiscount)

    actualTotalVat = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[4]/span").text
    actualTotalVat = actualTotalVat.replace(',', '')
    actualTotalVat = int(actualTotalVat)
    print("actualTotalVat:", actualTotalVat)

    actualTotalOtherCharge = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[5]/span").text
    actualTotalOtherCharge = actualTotalOtherCharge.replace(',', '')
    actualTotalOtherCharge = int(actualTotalOtherCharge)
    print("actualTotalOtherCharge:", actualTotalOtherCharge)

    actualTotalTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[6]/span").text
    actualTotalTotalAmount = actualTotalTotalAmount.replace(',', '')
    actualTotalTotalAmount = int(str(actualTotalTotalAmount).replace(",", ""))
    print("actualTotalTotalAmount:", actualTotalTotalAmount)
    print("END>>getPurchaseSummaryReport")


def prePurchaseSummaryReport():
    print("START>>prePurchaseSummaryReport")
    global preCreditSubTotal
    global preCreditDiscount
    global preCreditVat
    global preCreditOtherCharge
    global preCreditTotalAmount
    global preCashSubTotal
    global preCashDiscount
    global preCashVat
    global preCashOtherCharge
    global preCashTotalAmount
    global preTotalSubTotal
    global preTotalDiscount
    global preTotalVat
    global preTotalOtherCharge
    global preTotalTotalAmount

    preCreditSubTotal = actualCreditSubTotal
    preCreditDiscount = actualCreditDiscount
    preCreditVat = actualCreditVat
    preCreditOtherCharge = actualCreditOtherCharge
    preCreditTotalAmount = actualCreditTotalAmount
    preCashSubTotal = actualCashSubTotal
    preCashDiscount = actualCashDiscount
    preCashVat = actualCashVat
    preCashOtherCharge = actualCashOtherCharge
    preCashTotalAmount = actualCashTotalAmount
    preTotalSubTotal = actualTotalSubTotal
    preTotalDiscount = actualTotalDiscount
    preTotalVat = actualTotalVat
    preTotalOtherCharge = actualTotalOtherCharge
    preTotalTotalAmount = actualTotalTotalAmount

    print("END>>prePurchaseSummaryReport")


def verifyPurchaseSummaryReportAfterGR(qty, rate, amountCashEntryGR, amountCreditEntryGR, amountCashCancelGR, amountCreditCancelGR):
    print("START>>verifyPurchaseSummaryReportAfterGR")
    global expectedCreditSubTotal
    global expectedCreditDiscount
    global expectedCreditVat
    global expectedCreditOtherCharge
    global expectedCreditTotalAmount
    global expectedCashSubTotal
    global expectedCashDiscount
    global expectedCashVat
    global expectedCashOtherCharge
    global expectedCashTotalAmount
    global expectedTotalSubTotal
    global expectedTotalDiscount
    global expectedTotalVat
    global expectedTotalOtherCharge
    global expectedTotalTotalAmount

    print("amountCashEntryGR:", amountCashEntryGR)
    print("amountCashCancelGR:", amountCashCancelGR)
    print("amountCreditEntryGR:", amountCreditEntryGR)
    print("amountCreditCancelGR:", amountCreditCancelGR)
    expectedCreditSubTotal = preCreditSubTotal + amountCreditEntryGR - amountCreditCancelGR
    print("expectedCreditSubTotal:", expectedCreditSubTotal)
    assert expectedCreditSubTotal == actualCreditSubTotal
    expectedCreditDiscount = preCreditDiscount + 0
    print("expectedCreditDiscount:", expectedCreditDiscount)
    assert expectedCreditDiscount == actualCreditDiscount
    expectedCreditVat = preCreditVat + 0
    print("expectedCreditVat:", expectedCreditVat)
    assert expectedCreditVat == actualCreditVat
    expectedCreditOtherCharge = preCreditOtherCharge + 0
    print("expectedCreditOtherCharge:", expectedCreditOtherCharge)
    assert expectedCreditOtherCharge == actualCreditOtherCharge
    expectedCreditTotalAmount = preCreditTotalAmount + amountCreditEntryGR - amountCreditCancelGR
    print("expectedCreditTotalAmount:", expectedCreditTotalAmount)
    assert expectedCreditTotalAmount == actualCreditTotalAmount

    expectedCashSubTotal = preCashSubTotal + amountCashEntryGR - amountCashCancelGR
    print("expectedCashSubTotal:", expectedCashSubTotal)
    assert expectedCashSubTotal == actualCashSubTotal
    expectedCashDiscount = preCashDiscount + 0
    print("expectedCashDiscount:", expectedCashDiscount)
    assert expectedCashDiscount == actualCashDiscount
    expectedCashVat = preCashVat + 0
    print("expectedCashVat:", expectedCashVat)
    assert expectedCashVat == actualCashVat
    expectedCashOtherCharge = preCashOtherCharge + 0
    print("expectedCashOtherCharge:", expectedCashOtherCharge)
    assert expectedCashOtherCharge == actualCashOtherCharge
    expectedCashTotalAmount = preCashTotalAmount + amountCashEntryGR - amountCashCancelGR
    print("expectedCashTotalAmount:", expectedCashTotalAmount)
    assert expectedCashTotalAmount == actualCashTotalAmount

    expectedTotalSubTotal = preTotalSubTotal + amountCashEntryGR + amountCreditEntryGR - amountCashCancelGR - amountCreditCancelGR
    print("expectedTotalSubTotal:", expectedTotalSubTotal)
    assert expectedTotalSubTotal == actualTotalSubTotal
    expectedTotalDiscount = preTotalDiscount + 0
    print("expectedTotalDiscount:", expectedTotalDiscount)
    assert expectedTotalDiscount == actualTotalDiscount
    expectedTotalVat = preTotalVat + 0
    print("expectedTotalVat:", expectedTotalVat)
    assert expectedTotalVat == actualTotalVat
    expectedTotalOtherCharge = preTotalOtherCharge + 0
    print("expectedTotalOtherCharge:", expectedTotalOtherCharge)
    assert expectedTotalOtherCharge == actualTotalOtherCharge
    expectedTotalTotalAmount = preTotalTotalAmount + amountCashEntryGR + amountCreditEntryGR - amountCashCancelGR - amountCreditCancelGR
    print("expectedTotalTotalAmount:", expectedCashSubTotal)
    assert expectedTotalTotalAmount == expectedTotalTotalAmount

    print("END>> Verifying Purchase Summary Report After Good Receipt")


def verifyPurchaseSummaryReportAfterGRCancellation():
    print("START>> Verifying Purchase Summary Report after GR Cancelation")
    global creditSubTotal
    global creditDiscount
    global creditVat
    global creditOtherCharge
    global creditTotalAmount
    global cashSubTotal
    global cashDiscount
    global cashVat
    global cashOtherCharge
    global cashTotalAmount
    global totalSubTotal
    global totalDiscount
    global totalVat
    global totalOtherCharge
    global totalTotalAmount

    global precreditSubTotal
    global precreditDiscount
    global precreditVat
    global precreditOtherCharge
    global precreditTotalAmount
    global precashSubTotal
    global precashDiscount
    global precashVat
    global precashOtherCharge
    global precashTotalAmount
    global pretotalSubTotal
    global pretotalDiscount
    global pretotalVat
    global pretotalOtherCharge
    global pretotalTotalAmount

    assert creditSubTotal == precreditSubTotal
    assert creditDiscount == precreditDiscount
    assert creditVat == precreditVat
    assert creditOtherCharge == precreditOtherCharge
    assert creditTotalAmount == precreditTotalAmount

    assert cashSubTotal == precashSubTotal
    assert cashDiscount == precashDiscount
    assert cashVat == precashVat
    assert cashOtherCharge == precashOtherCharge
    assert cashTotalAmount == precashTotalAmount

    assert totalSubTotal == pretotalSubTotal
    assert totalSubTotal == cashSubTotal + creditSubTotal
    assert totalDiscount == cashDiscount + creditDiscount
    assert totalVat == cashVat + creditVat
    assert totalOtherCharge == cashOtherCharge + creditOtherCharge
    assert totalTotalAmount == pretotalTotalAmount
    assert totalTotalAmount == cashTotalAmount + creditTotalAmount
    print("END>> Verifying Purchase Summary Report after GR cancellation")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
