import time
import Library.GlobalShareVariables as GSV
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

AppName = GSV.appName


# Module:Inventory---------------------------------------------------------
def createInventoryGoodReceipt(danpheEMR, qty, item, rate):
    print(">>START: createGoodReceipt")
    global BillNo
    if AppName == 'SNCH':
        danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[contains(.,' Create Goods Receipt')]").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select();']").click()
        time.sleep(2)
        danpheEMR.find_element(By.CSS_SELECTOR, ".danphe-auto-complete-wrapper > .form-control").send_keys(Keys.RETURN)
        BillNo = random.randint(100, 99999)
        print("Bill No", BillNo)
        danpheEMR.find_element(By.XPATH, "//input[@formcontrolname='BillNo']").send_keys(BillNo)  # LPH-934, LPH_V1.9.3
        danpheEMR.find_element(By.ID, "itemName0").send_keys(item)
        danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.TAB)
        danpheEMR.find_element(By.ID, "qtyip0").send_keys(qty)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "rateip0").clear()
        danpheEMR.find_element(By.ID, "rateip0").send_keys(rate)
        danpheEMR.find_element(By.XPATH, "//input[@value='Receipt']").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Back to Goods Receipt List')]").click()
        return BillNo
    print("<<END: createGoodReceipt")


def editInventoryGoodsReceipt(danpheEMR, BillNo):
    print(">>START: edit GoodReceipt")
    time.sleep(2)
    if AppName == 'SNCH':
        danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(BillNo)
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Edit Receipt ')]").click()
        time.sleep(2)
        danpheEMR.find_element(By.ID, "qtyip0").clear()  # Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
        danpheEMR.find_element(By.ID, "qtyip0").send_keys(2)
        danpheEMR.find_element(By.ID, "SaveGoodsReceiptbtn").click()


def consumptionStore(danpheEMR, itemName, qty, store):
    time.sleep(5)
    if AppName == 'SNCH' or AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
        time.sleep(9)
        try:
            danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + store + "')]").click()
            # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Billing Store')]").click()
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
        danpheEMR.find_element(By.XPATH, "//input[@id='qtyip0']").clear()
        danpheEMR.find_element(By.XPATH, "//input[@id='qtyip0']").send_keys(qty)
        danpheEMR.find_element(By.CSS_SELECTOR, ".btn-success").click()
        time.sleep(2)


def activateInventory(danpheEMR, inventory='General Inventory' or 'Medical Inventory'):
    print("Inventory Selection Start")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(2)
    if inventory == 'General Inventory':
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
    else:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Medical Inventory')]").click()
    print("Inventory Selection End")


def createInventoryDirectDispatch(danpheEMR, itemname, qty, inventory, store):
    print(">>START: directDispatch")
    global RequsitionNo
    if AppName == 'SNCH' or AppName == 'LPH' or AppName == 'MPH':
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(9)
        try:
            danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + inventory + "')]").click()
        except:
            pass
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Direct Dispatch  ')]").click()
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
        Quantity = danpheEMR.find_element(By.XPATH, "//input[@name='availableQuantity']").get_attribute("value")
        print("Available Quantity :", Quantity)
        Quantity = int(Quantity)
        print("Available Quantity :", Quantity)
        # danpheEMR.find_element(By.ID, "qtyip0").send_keys(Keys.ENTER)
        danpheEMR.find_element(By.ID, "remarks").send_keys("Direct dispatch test")
        time.sleep(5)
        danpheEMR.find_element(By.ID, "directDispatchButton").click()
        time.sleep(5)
        if AppName == 'LPH':
            RequsitionNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'निकासा नं:')]").text
            RequsitionNo = int(str(RequsitionNo).replace("निकासा नं:", ""))
            print(RequsitionNo)
        else:
            RequsitionNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'Requisition No:')]/child::b").text
        print("Requisition Number is :", RequsitionNo)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Back to Requisition List')]").click()
    print("<<END: directDispatch")
    return RequsitionNo


def countStock(danpheEMR, itemname):
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(2)
    # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemname)
    time.sleep(2)
    itemstock = danpheEMR.find_element(By.CSS_SELECTOR, "span > div").text
    time.sleep(5)
    print(itemstock)
    time.sleep(5)
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-sign-out")
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-sign-out").click()
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
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(2)
        # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//label[2]/span").click()
        time.sleep(3)
        ReqNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='RequisitionNo'])[2]").text
        time.sleep(2)
        assert ReqNo == RequisitionNo
    print("<<End: verifyInventoryDirectDispatch")


def dispatchRequisition(danpheEMR, ssReqNo, GeneralInventory, itemname, qty):
    print(">>START: DispatchRequisition")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(9)
        # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
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
        danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Back to Requisition List')]").click()
    print("<<END: dispatchRequisition")


def verifyDispatchRequisition(danpheEMR, ssReqNo):
    print(">>START: verifyDispatchRequisition")
    if AppName == 'SNCH':
        danpheEMR.find_element(By.XPATH, "//label[2]/span").click()
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
        time.sleep(4)
        ssReqNo1 = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'Requisition No:')]/child::b").text
        print("ssReqNo1:", ssReqNo1)
        print("ssReqNo:", ssReqNo)
        assert ssReqNo1 == ssReqNo
    print("<<END: verifyDispatchRequisition")


def createPurchaseRequest(danpheEMR, ItemName, qty):
    print(">>START: createPurchaseRequest")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(9)
        # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "Purchase Request").click()
        time.sleep(2)
        PRNo = int(danpheEMR.find_element(By.XPATH, "(//div[@col-id='PRNumber'])[2]").text)
        print("PRNo:", PRNo)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,'Create Purchase Request')]").click()
        time.sleep(4)
        danpheEMR.find_element(By.ID, "itemName0").send_keys(ItemName)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "qty0").send_keys(qty)
        danpheEMR.find_element(By.ID, "RequestPORequisition").click()
        PRNo = PRNo + 1
        return PRNo
    print("<<END: createPurchaseRequest")


def verifyPurchaseRequest(danpheEMR, PRNo, ItemName, qty):
    print(">>START: verifyPurchaseRequest")
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(9)
        # danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "Purchase Request").click()
        time.sleep(3)
        PRNo1 = int(danpheEMR.find_element(By.XPATH, "(//div[@col-id='PRNumber'])[2]").text)
        assert PRNo1 == PRNo
    print(">>END: veriifyPurchaseRequest")


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
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
    time.sleep(6)
    grNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='GoodsReceiptNo'])[2]").text
    print("Goods Receipt No", grNo)
    UnitPrice = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ItemRate'])[2]").text
    print("Unit Price", UnitPrice)
    danpheEMR.find_element(By.XPATH, "//i[@class='fa fa-backward']").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemName)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Manage Stock')]").click()
    time.sleep(3)
    grNoTemp = danpheEMR.find_element(By.XPATH, 
        "//td[contains(text(),'GR No.')]/parent::tr/parent::thead/following-sibling::tbody/child::tr/child::td").text
    assert grNo == grNoTemp
    currentQty = danpheEMR.find_element(By.XPATH, "//input[@name='ModQuantity']").get_attribute("value")
    print("currentQty", currentQty)
    currentQty = int(currentQty)
    assert currentQty == actualAvailableQty
    modifyin = currentQty + 1
    modifyOut = currentQty - 1
    print("modifyin", modifyin)
    print("modifyOut", modifyOut)
    danpheEMR.find_element(By.XPATH, "//input[@name='ModQuantity']").clear()
    time.sleep(3)
    if managetype == "in":
        danpheEMR.find_element(By.XPATH, "//input[@name='ModQuantity']").send_keys(modifyin)
        time.sleep(3)
        print("Manage In done")
    if managetype == "out":
        danpheEMR.find_element(By.XPATH, "//input[@name='ModQuantity']").send_keys(modifyOut)
        time.sleep(3)
        print("Manage Out done")
        time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@value='Update Stock']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemName)
    time.sleep(2)
    newavailableQty = danpheEMR.find_element(By.XPATH, "(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
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
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Daily Item Dispatch')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(storeName)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//span[contains(.,'Requisition ID')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//span[contains(.,'Requisition ID')]").click()
    time.sleep(2)
    element1 = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[4]").text
    assert element1 == itemname
    element2 = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[7]").text
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
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
    except:
        pass
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Current Stock Level')]").click()
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
    danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Load')]").click()
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
    time.sleep(5)
    if AppName == 'SNCH':
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'General Inventory')]").click()
        time.sleep(3)


def selectDispensary(danpheEMR, dispensary):
    time.sleep(5)
    if AppName == 'SNCH':
        danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'MainDispensary')]").click()
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
        danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//i[contains(.,'Inventory Summary')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,' Load')]").click()
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
    print(">>Start : Verifying the Inventory Summary Report")
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
    print("END>> Verifying Inventory Summary Report")


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
    view.is_displayed()


def getPurchaseSummaryReport(danpheEMR):
    danpheEMR.implicitly_wait(10)
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

    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Inventory/Reports/Purchase']").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(text(), 'Purchase Summary')]").click()
    danpheEMR.find_element(By.XPATH, "//*[@class='btn green btn-success' and @type='button']").click()
    time.sleep(3)

    creditSubTotal = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[2]/span").text
    creditSubTotal = int(str(creditSubTotal).replace(",", ""))
    print("Sub Total of Credit Purchase is :", creditSubTotal)

    creditDiscount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[3]/span").text
    creditDiscount = int(creditDiscount)
    print("Discount for Credit Purchase is :", creditDiscount)

    creditVat = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[4]/span").text
    creditVat = int(creditVat)
    print("Vat for Credit Purchase is :", creditVat)

    creditOtherCharge = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[5]/span").text
    creditOtherCharge = int(creditOtherCharge)
    print("Other Charge of credit purchase is :", creditOtherCharge)

    creditTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[6]/span").text
    creditTotalAmount = int(str(creditTotalAmount).replace(",", ""))
    print("Total Amount of Credit Sale is :", creditTotalAmount)

    cashSubTotal = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[2]/span").text
    cashSubTotal = int(cashSubTotal)
    print("Subtotal of Cash Purchase is :", cashSubTotal)

    cashDiscount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[3]/span").text
    cashDiscount = int(cashDiscount)
    print("Discount of Cash Purchase is ", cashDiscount)

    cashVat = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[4]/span").text
    cashVat = int(cashVat)
    print("Vat of cash Purchase is :", cashVat)

    cashOtherCharge = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[5]/span").text
    cashOtherCharge = int(cashOtherCharge)
    print(cashOtherCharge)

    cashTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[6]/span").text
    cashTotalAmount = int(cashTotalAmount)
    print("Total Amount of Cash Purchase is :", cashTotalAmount)

    totalSubTotal = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[2]/span").text
    totalSubTotal = int(str(totalSubTotal).replace(",",""))
    print("Total Sum of SubTotal is ", totalSubTotal)

    totalDiscount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[3]/span").text
    totalDiscount = int(totalDiscount)
    print("Total Discount of Cash and Credit Purchase is :", totalDiscount)

    totalVat = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[4]/span").text
    totalVat = int(totalVat)
    print("Total vat of Credit and Cash Purchase is ", totalVat)

    totalOtherCharge = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[5]/span").text
    totalOtherCharge = int(totalOtherCharge)
    print("Total other charge of cash and credit Purchase is :", totalOtherCharge)

    totalTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[6]/span").text
    totalTotalAmount = int(str(totalTotalAmount).replace(",", ""))
    print("Total Amount of Cash and Credit Purchase is :", totalTotalAmount)


def prePurchaseSummaryReport():
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

    precreditSubTotal = creditSubTotal
    print("Previous SubTotal of credit purchase is:", precreditSubTotal)

    precreditDiscount = creditDiscount
    print("Previous Discount of Credit Purchase is :", precreditDiscount)

    precreditVat = creditVat
    print("Previous credit Vat is :", precreditVat)

    precreditOtherCharge = creditOtherCharge
    print("Previous Credit Other Charge is :", precreditOtherCharge)

    precreditTotalAmount = creditTotalAmount
    print("Previous Credit Total Amount is :", precreditTotalAmount)

    precashSubTotal = cashSubTotal
    print("previous cash Sub Total is :", precashSubTotal)

    precashDiscount = cashDiscount
    print("Previous cash Discount is :", precashDiscount)

    precashVat = cashVat
    print("Previous Cash Vat is :", precashVat)

    precashOtherCharge = cashOtherCharge
    print("Previous Cash Other Chagre is :", precashOtherCharge)

    precashTotalAmount = cashTotalAmount
    print("Previous Cash Total Amount is :", precashTotalAmount)

    pretotalSubTotal = totalSubTotal
    print("Previous Total  SubTotal is :", pretotalSubTotal)

    pretotalDiscount = totalDiscount
    print("Previous Total Discount is :", pretotalDiscount)

    pretotalVat = totalVat
    print("Previous Total Vat is :", pretotalVat)

    pretotalOtherCharge = totalOtherCharge
    print("Previous Total Other Charge is :", pretotalOtherCharge)

    pretotalTotalAmount = totalTotalAmount
    print("Previous Total Amount is :", pretotalTotalAmount)


def verifyPurchaseSummaryReportAfterGR(qty, rate):
    print("START>> Verifying Purchase Summary Report After Good Receipt")
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

    itemrate = qty * rate
    itemrate = float(itemrate)
    print(itemrate)
    assert creditSubTotal == precreditSubTotal + itemrate
    assert creditDiscount == precreditDiscount + 0
    assert creditVat == precreditVat + 0
    assert creditOtherCharge == precreditOtherCharge + 0
    assert creditTotalAmount == precreditTotalAmount + itemrate

    assert cashSubTotal == precashSubTotal + 0
    assert cashDiscount == precashDiscount + 0
    assert cashVat == precashVat + 0
    assert cashOtherCharge == precashOtherCharge + 0
    assert cashTotalAmount == precashTotalAmount + 0

    assert totalSubTotal == pretotalSubTotal + itemrate
    assert totalSubTotal == cashSubTotal + creditSubTotal
    assert totalDiscount == cashDiscount + creditDiscount
    assert totalVat == cashVat + creditVat
    assert totalOtherCharge == cashOtherCharge + creditOtherCharge
    assert totalTotalAmount == pretotalTotalAmount + itemrate
    assert totalTotalAmount == cashTotalAmount + creditTotalAmount
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
