import time
import Library.GlobalShareVariables as GSV
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

AppName = GSV.appName


# Module:Inventory---------------------------------------------------------

def getpurchaseitemreport(danpheEMR):
    print("START: Purchase Item report")
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "(//a[@href='#/Inventory/Reports'])[2]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Inventory/Reports/Purchase']").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//*[text()='Purchase Items']").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//span[contains(text(), 'Load')]").click()
    time.sleep(2)
    btn = danpheEMR.find_element(By.XPATH, "//input[@value = 'Capital Goods']")
    print(btn.is_selected())
    danpheEMR.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    check = danpheEMR.find_element(By.XPATH, "//input[@value = 'Capital Goods']")
    print(check.is_selected())
    time.sleep(3)
    if check.is_selected:
        danpheEMR.find_element(By.XPATH, "//span[contains(text(), 'Load')]").click()
        time.sleep(5)
    check_after_update = danpheEMR.find_element(By.XPATH, "//input[@value = 'Capital Goods']")
    if check_after_update.get_attribute("checked") != "True":
        danpheEMR.execute_script("arguments[0].click();", check_after_update)
        time.sleep(5)


def createInventoryGoodReceipt(danpheEMR, qty, item, rate, paymentMode, NepaliReceipt):
    print(">>START: createGoodReceipt")
    global BillNo
    #if AppName == 'SNCH':
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    time.sleep(6)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH,"//a[contains(.,' Create Goods Receipt')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,"//input[@onclick='this.select();']").click()
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
    if NepaliReceipt == 'false':
        totalrate = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div/div[9]/div/table/tbody/tr/td[11]").text
        totalrate = float(totalrate)
        print(totalrate)
        rate = float(rate)
        print(rate)

    else:
        totalrate = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[2]/table/tbody/tr[1]/td[11]").text
        print(totalrate)
        rate = float(rate)
        print(rate)
        totalrate = float(totalrate)
    assert rate == totalrate
    #danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Back to Goods Receipt List')]").click()
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Cancel GR ')]").send_keys(Keys.ESCAPE)
    print("<<END: createGoodReceipt")
    return BillNo


def verifyGoodReceiptNumberInGridAndShow(danpheEMR, billno, totalAmount, NepaliReceipt):
    print("Start Verifying the Goods Receipt Number in Grid and View Page")
    time.sleep(1)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(billno)
    time.sleep(1)
    if NepaliReceipt == "true":
        text = "दाखिला प्रतिवेदन नम्बरः"
        grno = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").text
        grno = text + " " + grno
        print("Good Receipt Number in Grid is :", grno)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
        time.sleep(2)
        goodReceiptNo = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div[2]/div[2]").text
        print("Good Receipt Number is :", goodReceiptNo)
        print(type(goodReceiptNo))
        assert grno == goodReceiptNo
    else:
        text = "2079/2080-"
        grno = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").text
        grno = text+grno
        print("Good Receipt Number in Grid is :", grno)
        vendor = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[5]").text
        print("Vendor Name in the grid is ", vendor)
        vendorContact = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[6]").text
        print("Vendor contact in the Grid is :", vendorContact)
        totalAmt = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[8]").text
        print("Total amount in the grid is ", totalAmt)
        totalAmt = int(totalAmt)
        print(totalAmt)
        assert totalAmt == totalAmount
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
        time.sleep(2)
        billNumber = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div/div[4]/p[3]/b").text
        billNumber = int(billNumber)
        print("Bill number in view is :", billNumber)
        goodReceiptNo = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div/div[3]/p[1]/b").text
        print("Good Receipt Number is :", goodReceiptNo)
        print(type(goodReceiptNo))
        vendorName = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div/div[3]/p[3]/b").text
        print("Vendor name in the view is :", vendorName)
        vendorNo = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div/div[3]/p[5]/b").text
        print("Vendor contact in View page is ", vendorNo)
        assert vendorNo == vendorContact
        assert vendor == vendorName
        assert billno == billNumber
        assert grno == goodReceiptNo
#def PurchaseItemReport (danpheEMR):
#danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
#time.sleep(2)
#click on Purchase
#danpheEMR.find_element(By. LINK_TEXT, "Purchase").click()
#danpheEMR.find_element(By. XPATH,"/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/div/ng-component/div[2]/app-inv-purchase-report-main/div/div/div[3]/a/div/span[2]/i[1]").click()


def RetunToVendor(danpheEMR, vendorName, billNo, GRno, item, purchaseQuantity, returnqty, purchaseRate, returnRate):
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    time.sleep(5)
    #click on Stock
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Stock')]").click()
    time.sleep(4)
    #click on good receipt list
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Goods Receipt List')]").click()

    #search by using bill no.
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(billNo)
    time.sleep(5)
    #click on receive view
    danpheEMR.find_element(By.XPATH, "//a[@title='View']").click()
    #Add the remark
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//textarea[@id='ReceivedRemarks']").send_keys("receive")
    danpheEMR.find_element(By.XPATH, "//i[@class='fa fa-check-square-o']").click()
    time.sleep(5)
    #GRNno. can be taken from Good receipt list aswell
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(billNo)
    GRno = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[1]").text
    print(GRno)
    print("Good Receipt number :", GRno)
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Return To Vendor')]").click()
    danpheEMR.find_element(By.XPATH, "//a[@class='btn primary-btn btn-sm m1']").click()
    danpheEMR.find_element(By.XPATH, "//input[@id='vendor']").send_keys(vendorName)
    danpheEMR.find_element(By.XPATH, "//input[@id='GrNo']").send_keys(GRno)
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[@id='searchBtn']").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(item)
    time.sleep(7)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.ENTER)
    time.sleep(6)
    danpheEMR.find_element(By.XPATH, "//input[@id='returnrate0']").send_keys(returnRate)
    if returnRate > purchaseRate:
        actual_RateMessage = danpheEMR.find_element(By.XPATH,"//span[normalize-space()='must be less than Standard Rate']").text
        print("Actual Error message is :", actual_RateMessage)
        expected_RateMessage = "must be less than Standard Rate"
        assert actual_RateMessage == expected_RateMessage
        print("The return rate is grater than available rate")
        danpheEMR.find_element(By.XPATH, "//input[@value='Cancel']").click()
        return

    danpheEMR.find_element(By.XPATH, "//input[@id='qtyip0']").send_keys(returnqty)
    if returnqty > purchaseQuantity:
        actual_QTYmessage = danpheEMR.find_element(By.XPATH, "//span[normalize-space()='No more Qty is Available']").text
        print("Actual Error messge is :", actual_QTYmessage)
        expected_QtyMessage = "No more Qty is Available"
        assert actual_QTYmessage == expected_QtyMessage
        print("The return quantity is grater than available quantity")
        danpheEMR.find_element(By.XPATH, "//input[@value='Cancel']").click()
        return
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//input[@id='remark0']").send_keys("return to vendor")
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//input[@id='Request']").click()



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
    ## Edit on quantity feeature has been deprecated
    #danpheEMR.find_element(By.ID, "qtyip0").clear()  # Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
    #danpheEMR.find_element(By.ID, "qtyip0").send_keys(2)
    ##
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
    time.sleep(3)
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


def dispatchRequisition(danpheEMR, ssReqNo, dispatchQuantity):
    print("START>>DispatchRequisition")
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Inventory").click()
    # time.sleep(5)
    # danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Internal").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Requisition").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Dispatch Requisition')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "dispatchQty0").send_keys(dispatchQuantity)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "remarks").send_keys("dispatching req")
    danpheEMR.find_element(By.ID, "DispatchBtn").click()
    time.sleep(9)
    danpheEMR.find_element(By.XPATH,  "//button[contains(text(),'Back to Requisition List')]").click()
    print("END>>dispatchRequisition")


def verifyInventorypartialStatusofPartialDispatch(danpheEMR, ssReqNo, status):
    print("START: Verifying Partial Dispatch of Items requisition from substore")
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(2)
    Status = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[4]").text
    print("Status in the Requisition page is ", Status)
    print("Expected status is ", status)
    assert Status == status
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//i[@class = 'fa fa-sign-out']").click()
    print("END : Verifying Partial Dispatch of items")


def verifyDispatchRequisition(danpheEMR, ssReqNo):
    print("START>>verifyDispatchRequisition")
    danpheEMR.find_element(By.XPATH,  "//label[2]/span").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(ssReqNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "//a[contains(text(),'View')]").click()
    time.sleep(4)
    if AppName == 'LPH':
        ssReqNo1 = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[1]/div[3]/div[2]/div[2]").text
        print("Sub Store Requisition No", ssReqNo1)
        ssReqNo1 = ssReqNo.replace('माग नं:', '')
    else:
        ssReqNo1 = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'Requisition No:')]").text
        print("Sub Store Requisition No", ssReqNo1)
        ssReqNo1 = ssReqNo.replace('Requisition No:', '')
    print("Sub Store Requisition No", ssReqNo1)
    # ssReqNo1 = danpheEMR.find_element(By.XPATH,  "//div[contains(text(),'Requisition No:')]/child::b").text
    # print("ssReqNo1:", ssReqNo1)
    # print("ssReqNo:", ssReqNo)
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

def createPurchaseRequestByAddingNewItem(danpheEMR, qty):
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
    danpheEMR.find_element(By.XPATH,  "//button[contains(.,'Create Purchase Request')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,  "/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/div/ng-component/ng-component/div/div/div[2]/div/div[3]/table/tbody/tr/td[3]/div/form/a").click()
    time.sleep(3)
    ItemCategory = Select(danpheEMR.find_element(By.ID, "ddlItemCategory"))
    ItemCategory.select_by_visible_text("Consumables")
    print("PR Category While Creating New Item =", ItemCategory)
    time.sleep(4)
    Iname = str(random.randint(1111, 9999))
    danpheEMR.find_element(By.ID, "ItemName").send_keys("auto", Iname)
    time.sleep(3)
    ItemSubCategory = Select(danpheEMR.find_element(By.ID, "ddlSubItemCategory"))
    ItemSubCategory.select_by_visible_text("Consumables")
    time.sleep(3)
    UnitOfMeasurement = Select(danpheEMR.find_element(By.ID, "ddlUnitOfMeasurement"))
    UnitOfMeasurement.select_by_visible_text("N/A")
    time.sleep(3)
    danpheEMR.find_element(By.ID, "MinStockQuantity").send_keys("25")
    time.sleep(3)
    ItemCompany = Select(danpheEMR.find_element(By.XPATH, "/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/div/ng-component/ng-component/item-add/div/div/div/div/div/form/div/div[1]/div[2]/div[2]/div[2]/div/div/select"))
    ItemCompany.select_by_visible_text("N/A")
    time.sleep(3)
    danpheEMR.find_element(By.ID, "AddItem").click()
    time.sleep(3)
    AfterAdding = danpheEMR.find_element(By.XPATH, "/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/div/ng-component/ng-component/div/div/div[2]/div/div[3]/table/tbody/tr/td[2]/select")
    print("PR Category After Adding New Item =", AfterAdding)
    time.sleep(4)
    danpheEMR.find_element(By.ID, "RequestPORequisition").click()
    PRNo = PRNo + 1
    return PRNo
    print("PRNo:", PRNo)
    assert ItemCategory == AfterAdding

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
    try:
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    except:
        pass
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
    print("END>>preInventorySummaryReport")


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
