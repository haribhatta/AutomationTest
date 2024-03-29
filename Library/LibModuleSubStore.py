import time
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

AppName = GSV.appName


# Module: SubStore Test Actions
def selectSubStore(danpheEMR, substore='Administration Store' or 'Emergency Store'):
    print("Start>> selectSubStore")
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(5)
    if substore == "Administration Store":
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Administration Store')]").click()
    elif substore == 'Emergency Store':
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Emergency Store')]").click()
    else:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'ACCOUNT')]").click()
    print("End<<selectSubStore")


def createSubStoreRequisition(danpheEMR, InventoryName, ItemName, Qty):
    print("Start>> createSubStoreRequisition")
    time.sleep(6)
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(5)
    if AppName == "SNCH":
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Administration Store')]").click()
        time.sleep(2)
    elif AppName == "LPH":
        danpheEMR.find_element(By.XPATH, "//html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/ul/li[2]/a").click()
        time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Inventory Requisition')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "activeInventory").send_keys(InventoryName)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "activeInventory").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(ItemName)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "qtyip0").send_keys(Qty)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "save_requisition").click()
    time.sleep(2)
    if AppName == "LPH":
        ssReqNo = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div[3]/div[2]/div[2]").text
        ssReqNo = ssReqNo.replace('माग नं:', '')
        print("Sub Store Requisition No", ssReqNo)
    else:
        ssReqNo = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div/div/div[2]/p/b").text
        print("Sub Store Requisition No", ssReqNo)
    danpheEMR.find_element(By.ID, "backToList").click()
    print("End<<createSubStoreRequisition")
    return ssReqNo


def verifySubStoreRequisition(danpheEMR, ssReqNo, InventoryName, ItemName, Qty):
    print("Start>> verifySubStoreRequisition")
    # time.sleep(6)
    # danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    # time.sleep(5)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'Administration Store')]").click()
    # time.sleep(5)
    # danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'Inventory Requisition')]").click()
    time.sleep(5)
    ssReqNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='RequisitionNo'])[2]").text
    assert ssReqNo == ssReqNo
    # danpheEMR.find_element(By.XPATH,  "//label[2]/span").click()
    # time.sleep(3)
    # ssReqNo1 =
    print("<<END: verifySubStoreRequisition")


def receiveInventoryDispatch(danpheEMR, substore, ssReqNo):
    print("Start>> createSubStoreRequisition")
    time.sleep(6)
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(5)
    try:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
    except:
        pass
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Inventory')]").click()
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'Administration Store')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Inventory Requisition')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Receive Items')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "ReceiveButton").click()
    #time.sleep(5)
    #danpheEMR.find_element(By.ID, "backToList").click()
    danpheEMR.find_element(By.XPATH, "/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[3]/ng-component/div[2]/app-inventory-ward-receive-stock/div/div/div[1]/div[1]/button").click()


def verifyReceivedInventoryDispatch(danpheEMR, ssReqNo):
    print(">>START: verifyReceivedInventoryDispatch")
    time.sleep(6)
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(5)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'Administration Store')]").click()
    # time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Inventory')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Inventory Requisition')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//label[2]/span").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
    time.sleep(3)
    ssReqNo1 = danpheEMR.find_element(By.XPATH, "//p[contains(text(),'Requisition No:')]/child::b").text
    assert ssReqNo1 == ssReqNo
    danpheEMR.find_element(By.ID, "backToList").click()
    print("<<END: verifyReceivedInventoryDispatch")


def countStockSub(danpheEMR, substore, itemname):
    print(">>START: Counting Sub-store's Stock of :", itemname)
    global stock
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(3)
    # since store is choosen no need to choose this
    try:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
    except:
        pass
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemname)
    time.sleep(2)
    stock = danpheEMR.find_element(By.CSS_SELECTOR, "span > div").text
    print("Stock of item is :", stock)
    danpheEMR.find_element(By.XPATH, "//i[@class = 'fa fa-sign-out']").click()
    print(">>END: End of Sub-store stock count")
    return stock


def prestockcountSub():
    global preStock
    preStock = int(stock)
    print("previous Stock of Item is :", preStock)
    return preStock


def verifyStockSub(qty):
    time.sleep(2)
    print("Start to Verify Stock")
    print("Prestock of substore's item  is :", int(preStock))
    print("Substore's Item Stock is :", int(stock))
    assert int(qty) == int(preStock) - int(stock)
    print("End of Verifying Stock")


def createNewConsumption(danpheEMR, substore, itemName, isBackDate):
    print(">>Start : Consumption of item by Staff")
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(2)
    # since store is choosen no need to choose this
    try:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
    except:
        pass
    time.sleep(1)
    #danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    #danpheEMR.find_element(By.XPATH, "//div[2]/ul/li[2]/a").click()
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/WardSupply/Inventory/Consumption')]").click()
    danpheEMR.find_element(By.XPATH, " //a[contains(text(),'New Consumption')]").click()
    time.sleep(2)
    if isBackDate == "yes":
        date = danpheEMR.find_element(By.ID, "inputDay").text
        print("date is :", int(date))
        backdate = date-1
        print(backdate)
        danpheEMR.find_element(By.ID, "inputDay").send_keys(Keys.CLEAR)
        danpheEMR.find_element(By.ID, "inputDay").send_keys(backdate)
    danpheEMR.find_element(By.ID, "itemName0").click()
    danpheEMR.find_element(By.ID, "itemName0").send_keys(itemName)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "remark").send_keys("Consumption by  user name Sabitri")
    danpheEMR.find_element(By.ID, "save").click()


def createPatientConsumption(danpheEMR, substore, hospitalNumber, itemName):
    print("START:: Patient Consumption ")
    time.sleep(2)
    # since store is choosen no need to choose this
    try:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
    except:
        pass
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Patient Consumption").click()
    time.sleep(2)
    danpheEMR.find_element(By.NAME, "name").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(hospitalNumber)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(itemName)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.ENTER)
    # danpheEMR.find_element(By.ID, "qtyip0").send_keys(Keys.CLEAR)
    # danpheEMR.find_element(By.ID, "qtyip0").send_keys(quantity)
    time.sleep(1)
    danpheEMR.find_element(By.NAME, "remark").send_keys("consumed by Patient")
    time.sleep(1)
    danpheEMR.find_element(By.ID, "save").click()
    danpheEMR.find_element(By.XPATH, "//i[@class = 'fa fa-sign-out']").click()
    print("END: Patient Consumption")


def getConsumptionReports(danpheEMR, substore, isBackDate, itemName):
    print("START: get consumption report")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "SubStore").click()
    time.sleep(2)
    try:
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + substore + "')]").click()
    except:
        pass
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Dispensary/Reports']").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(text(), 'Consumption Report')]").click()
    if isBackDate == 'yes':
        currentDate = danpheEMR.find_element(By.XPATH, "(//input[@id='inputDay'])[2]").text
        print("Current date is :", int(currentDate))
        backdate = currentDate - 1
        print("back date is :", backdate)
        danpheEMR.find_element(By.XPATH, "(//input[@id='inputDay'])[1]").send_keys(Keys.CLEAR)
        danpheEMR.find_element(By.XPATH, "(//input[@id='inputDay'])[1]").send_keys(backdate)
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "(//input[@id='inputDay'])[2]").send_keys(Keys.CLEAR)
        danpheEMR.find_element(By.XPATH, "(//input[@id='inputDay'])[2]").send_keys(backdate)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemName)

def RequisitionandDispatchReport(danpheEMR, Itemname, qty):
    print("START: Requisition and Dispatch Report")
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[3]/ng-component/div[2]/ng-component/div/div[1]/a/div/span[2]/i[1]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(Itemname)
    time.sleep(3)
    sysItemname = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[3]").text
    print("Itemname in System is :", sysItemname)
    assert sysItemname == Itemname
    sysrequestedQty = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[4]").text
    print("sysrequestedQty in System is :", sysrequestedQty)
    sysrequestedQty = int(sysrequestedQty)
    assert sysrequestedQty == qty
    sysreceivedQty = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[5]").text
    print("sysreceivedQty in System is :", sysreceivedQty)
    sysreceivedQty = int(sysreceivedQty)
    assert sysreceivedQty == qty
    sysdispatchedQty = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[7]").text
    print("sysdispatchedQty in System is :", sysdispatchedQty)
    sysdispatchedQty = int(sysdispatchedQty)
    assert sysdispatchedQty == qty



def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
