from selenium import webdriver
import time
import Library.GlobalShareVariables as GSV
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

########
AppName = GSV.appName


########
def addPharmacyItem(danpheEMR, genericName):  # incomplete
    print(">>START: addPharmacyItem")
    global DrugName
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Setting").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Item").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
    time.sleep(3)
    salesCategory = GSV.salesCategoyType
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(
        salesCategory)
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(
        Keys.RETURN)
    drugMGtemp = random.randint(10, 1000)
    drugMG = str(drugMGtemp)
    DrugName = ('Autodrug' + drugMG)
    print("DrugName:", DrugName)
    danpheEMR.find_element(By.XPATH, "//input[@value='']").send_keys(DrugName)
    danpheEMR.find_element(By.XPATH, "//input[@value='']").send_keys(Keys.RETURN)
    time.sleep(3)
    # danpheEMR.find_element(By.CSS_SELECTOR, "//select").click()
    drugCompany = GSV.drugCompany
    danpheEMR.find_element(By.XPATH, "//div[4]/div/div/div/input").send_keys(drugCompany)  # Company
    danpheEMR.find_element(By.XPATH, "//div[4]/div/div/div/input").send_keys(Keys.RETURN)
    itemType = GSV.drugType
    danpheEMR.find_element(By.XPATH, "//div[5]/div/div/div/input").send_keys(itemType)  # itemType
    danpheEMR.find_element(By.XPATH, "//div[5]/div/div/div/input").send_keys(Keys.RETURN)  # itemType
    # danpheEMR.find_element(By.CSS_SELECTOR, ".ng-touched:nth-child(1)").send_keys("ABGEL")
    danpheEMR.find_element(By.XPATH, "//div[6]/div/div/div/input").send_keys("TAB")  # unit
    danpheEMR.find_element(By.XPATH, "//div[6]/div/div/div/input").send_keys(Keys.RETURN)  # unit
    danpheEMR.find_element(By.XPATH, "//div[7]/div/div/div/input").send_keys(genericName)  # genericName
    danpheEMR.find_element(By.XPATH, "//div[7]/div/div/div/input").send_keys(Keys.RETURN)  # genericName
    time.sleep(3)
    danpheEMR.find_element(By.ID, "save").click()
    time.sleep(9)
    print("End>>addPharmacyItem")


def verifyPharmacyItem(danpheEMR):
    print(">>Start:verifyPharmacyItem")
    time.sleep(2)
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Setting").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(DrugName)
    time.sleep(9)
    assert DrugName == danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div").text
    print("End>>verifyPharmacyItem")


def getPharmacyStockDetail(danpheEMR, drugname):
    print(">>Start: getPharmacyStockDetail")
    global drugqtyMS
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Pharmacy/Store' and contains(text(),'Store')]").click()
    time.sleep(3)
    try:
        danpheEMR.find_element(By.XPATH, "(//input[@id='quickFilterInput'])[1]").send_keys(drugname)
    except:
        danpheEMR.find_element(By.XPATH, "(//input[@id='quickFilterInput'])[2]").send_keys(drugname)
    time.sleep(5)
    drugnameMS = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[20]/div[2]").text
    print("drugnameMS:", drugnameMS)
    print("drugname:", drugname)
    assert drugnameMS == drugname
    sysdrugqty = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[20]/div[5]").text
    drugqtyMS = int(sysdrugqty)
    print("drugqtyMS:", drugqtyMS)
    print("End>>getPharmacyStockDetail")


def verifyPharmacyStockDetail(danpheEMR, drugname):
    print(">>Start:verifyDispensaryStockDetail")
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Pharmacy/Store' and contains(text(),'Store')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "(//input[@id='quickFilterInput'])[2]").clear()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "(//input[@id='quickFilterInput'])[2]").send_keys(drugname)
    time.sleep(2)
    sysdrugname = danpheEMR.find_element(By.XPATH,
                                         "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[20]/div[2]").text
    print("sysdrugname:", sysdrugname)
    assert drugname == sysdrugname
    sysdrugqty = danpheEMR.find_element(By.XPATH,
                                        "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[20]/div[5]").text
    print("sysdrugqty", sysdrugqty)
    print("newdrugqtyMS", drugqtyMScalc)
    assert int(drugqtyMScalc) == int(sysdrugqty)
    print("End>>verifyDispensaryStockDetail")


def transferMainStore2MainDispensary(danpheEMR, drugname, qty):
    print(">>Start:transferMainStore2MainDispensary")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    # danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    danpheEMR.find_element(By.XPATH, "//a[@href='#/Pharmacy/Store' and contains(text(),'Store')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Dispensary Request").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@class = 'btn btn-primary']").click()
    time.sleep(3)
    mainDispensary = GSV.dispensaryName1
    danpheEMR.find_element(By.ID, "dispensary").send_keys(mainDispensary)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "dispensary").send_keys(Keys.TAB)
    time.sleep(2)
    ##danpheEMR.find_element(By.ID, "itemName0")
    danpheEMR.find_element(By.ID, "itemName0").click()
    # time.sleep(2)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(drugname)
    # time.sleep(3)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "qtyip0").send_keys(qty)
    danpheEMR.find_element(By.ID, "remarks").send_keys("Transfer to Main Dispensary")
    danpheEMR.find_element(By.ID, "directDispatch").click()
    time.sleep(2)
    requisitionView = danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Requisition View')]")
    requisitionView.is_displayed()


def createPharmacyPurchaseOrder(danpheEMR, supplierName, drugName):
    print(">>Start: Create purchase order in pharmacy")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Order')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[@href='#/Pharmacy/Order/PurchaseOrderItems']").click()

    elif AppName == "SNCH":
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "(//a[@href='#/Pharmacy/Order'])[2]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[@href='#/Pharmacy/Order/PurchaseOrderItems']").click()
        time.sleep(3)
        #danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Purchase')]").click()
    # time.sleep(3)
    # danpheEMR.find_element(By.XPATH, "/html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/ng-component/div/ul/li[1]/a").click()
    # time.sleep(3)
    # danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    # danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderItems')]").click()
    # danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-9 > .form-control").click()
    # time.sleep(9)
    # dropdown = danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-9 > .form-control")
    # time.sleep(3)
    # dropdown.find_element(By.XPATH, "//option[. = 'Shremad Tech.']").click()
    danpheEMR.find_element(By.ID, "SupplierName").send_keys(supplierName)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "SupplierName").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "ItemName0").send_keys(drugName)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "ItemName0").send_keys(Keys.TAB)
    danpheEMR.find_element(By.NAME, "quantity").click()
    time.sleep(3)
    danpheEMR.find_element(By.NAME, "quantity").send_keys("100")
    danpheEMR.find_element(By.NAME, "price").click()
    danpheEMR.find_element(By.NAME, "price").send_keys("1")
    # danpheEMR.find_element(By.CSS_SELECTOR, ".page-content").click()
    danpheEMR.find_element(By.CSS_SELECTOR, ".text-right > .btn-success").click()
    time.sleep(5)


def verifyCreatePharmacyPurchaseOrder(danpheEMR, supplierName, drugName):
    print(">>START: verifyCreatePharmacyPurchaseOrder")
    danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Order List").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(supplierName)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
    time.sleep(3)
    if AppName == "LPH":
        appSupplierName = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'श्री')]").text
        appSupplierName = appSupplierName.partition("श्री ")[2]
    else:
        appSupplierName = danpheEMR.find_element(By.XPATH, "//p[contains(text(),'Supplier Name :')]/child::b").text
    print("SupplierName:", appSupplierName)
    assert supplierName == appSupplierName
    appItemName = danpheEMR.find_element(By.XPATH, "//td[2]/b").text
    print("app Item name:", appItemName)
    assert drugName == appItemName
    danpheEMR.find_element(By.XPATH, "//a[@title='Cancel' and @class='btn btn-danger history-del-btn']").click()
    time.sleep(3)

def addPharmacyGRfromPO(danpheEMR):
    print(">>Start: Create GR from purchase order in pharmacy")
    danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderList')]").click()
    danpheEMR.find_element(By.LINK_TEXT, "Add Goods Receipt").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@value='Receipt']").click()


def createPharmacyGoodsReceipt(danpheEMR, supplier, qty, DrugName, grPrice, NepaliReceipt):
    print("START>>createPharmacyGoodsReceipt")
    global goodsReceiptNo
    time.sleep(2)
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Order')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt").click()
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Select Supplier']").send_keys(supplier)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
    gRNo = random.randint(1000, 999999)
    print("GR No:", gRNo)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Invoice No']").send_keys(gRNo)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Invoice No']").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btn_AddNew").click()
    time.sleep(7)
    danpheEMR.find_element(By.ID, "txt_ItemName").send_keys(DrugName)
    danpheEMR.find_element(By.ID, "txt_ItemName").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "txt_BatchNo").send_keys(gRNo)
    danpheEMR.find_element(By.ID, "ItemQTy").send_keys(qty)
    print("grPrice", grPrice)
    grPrice = int(grPrice)
    danpheEMR.find_element(By.ID, "GRItemPrice").send_keys(grPrice)
    danpheEMR.find_element(By.ID, "Margin").send_keys(14)
    #danpheEMR.find_element(By.ID, "VATPercentage").send_keys(13): removing VAT amount fr drug sale.
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btn_Save").click()
    # danpheEMR.find_element(By.XPATH, "//select[contains(.,'Main Store')]").send_keys("Main Store") Temporary disable due to issue.
    danpheEMR.find_element(By.XPATH, "//button[@class='btn green btn-success tooltip']").click()
    time.sleep(5)
    if AppName == 'RTM' or AppName == "SNCH":
        # danpheEMR.find_element(By.ID, "saveGr").click()
        time.sleep(3)
        # assert danpheEMR.switch_to.alert.text == "Similar GR found with these Invoices: \n Invoice No.: 262049\n Invoice No.: 303568\n Invoice No.: 99999999\n Want to continue?"
        danpheEMR.switch_to.alert.accept()
        time.sleep(3)
    else:
        # danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE) ## not working @LPH
        # danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE) ## working @LPH
        danpheEMR.switch_to.alert.accept()  ## to close alert msg box for similiar GR items already entered.
    time.sleep(2)
    # obj = danpheEMR.switch_to.alert
    # obj.accept()
    time.sleep(2)
    if NepaliReceipt == "true":
        goodsReceiptNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'दाखिला प्रतिवेदन नम्बर')]").text
        # goodsReceiptNo = goodsReceiptNo.replace("-", "")
        goodsReceiptNo = goodsReceiptNo.partition(": ")[2]
        print("goodsReceiptNo:", goodsReceiptNo)
        danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    else:
        goodsReceiptNo = danpheEMR.find_element(By.XPATH, "//div[@id='print-good-reciept']/div/div/div[5]/p/b").text
        goodsReceiptNo = goodsReceiptNo.replace("-", "")
        print("goodsReceiptNo:", goodsReceiptNo)
        danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("END>>createPharmacyGoodsReceipt")
    return gRNo


def createPharmacyGrwithSameInvoiceNumberAfterGrCancel(danpheEMR, invoiceNumber, supplier, qty, DrugName, grPrice, NepaliReceipt):
    print("START>>Good Receipt after GR cancel with previously cancelled Invoice Number")
    global goodsReceiptNo
    time.sleep(2)
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Order')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt").click()
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Select Supplier']").send_keys(supplier)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Invoice No']").send_keys(invoiceNumber)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Invoice No']").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btn_AddNew").click()
    time.sleep(7)
    danpheEMR.find_element(By.ID, "txt_ItemName").send_keys(DrugName)
    danpheEMR.find_element(By.ID, "txt_ItemName").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "txt_BatchNo").send_keys(invoiceNumber)
    danpheEMR.find_element(By.ID, "ItemQTy").send_keys(qty)
    print("grPrice", grPrice)
    grPrice = int(grPrice)
    danpheEMR.find_element(By.ID, "GRItemPrice").send_keys(grPrice)
    danpheEMR.find_element(By.ID, "Margin").send_keys(14)
    danpheEMR.find_element(By.ID, "VATPercentage").send_keys(13)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btn_Save").click()
    danpheEMR.find_element(By.XPATH, "//button[@class='btn green btn-success tooltip']").click()
    time.sleep(5)
    danpheEMR.switch_to.alert.accept()
    time.sleep(2)
    if NepaliReceipt == "true":
        goodsReceiptNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'दाखिला प्रतिवेदन नम्बर')]").text
        goodsReceiptNo = goodsReceiptNo.partition(": ")[2]
        print("goodsReceiptNo:", goodsReceiptNo)
        danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    else:
        goodsReceiptNo = danpheEMR.find_element(By.XPATH, "//div[@id='print-good-reciept']/div/div/div[5]/p/b").text
        goodsReceiptNo = goodsReceiptNo.replace("-", "")
        print("goodsReceiptNo:", goodsReceiptNo)
        danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("END>>createPharmacyGoodsReceipt")
    return invoiceNumber

def verifyPharmacyGoodsReceipt(danpheEMR, brandName, genericName, grno, NepaliReceipt):
    print("START>>verifyPharmacyGoodsReceipt")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt List").click()
    time.sleep(5)
    # danpheEMR.find_element(By.LINK_TEXT, "View").click()  ## not working on LPH
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(grno)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "View").click()
    time.sleep(3)
    if NepaliReceipt == "true":
        sysdrugname = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div[2]/table/tbody/tr[1]/td[3]").text
        print("sysdrugname:", sysdrugname)
        danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    else:
        sysdrugname = danpheEMR.find_element(By.XPATH, "//*[@id='print-good-reciept']/div/div/div[10]/table/tbody/tr/td[2]/b").text
        print("sysdrugname:", sysdrugname)
        danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE)

    print("END>>verifyPharmacyGoodsReceipt")


def cancelPharmacyGoodsReceipt(danpheEMR, grNo, NepaliReceipt):
    print("START>>cancelPharmacyGoodsReceipt")
    time.sleep(2)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt List").click()
    time.sleep(5)
    print("goodsReceiptNo:", grNo)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(grNo)
    danpheEMR.find_element(By.XPATH, "(//a[contains(text(), 'View')])[1]").click()
    time.sleep(3)
    if NepaliReceipt == 'true':
        sysGRno = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'दाखिला प्रतिवेदन नम्बर')]").text
        print("sysGRno", sysGRno)
    else:
        sysGRno = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Goods Receipt No.:')]").text
        sysGRno = sysGRno.replace("-", "")
        print("sysGRno", sysGRno)
    danpheEMR.find_element(By.XPATH, "//button[@title='Cancel Goods Receipt']").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "CancelRemarks").send_keys("Cancel to test")
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Proceed')]").click()
    time.sleep(4)
    if NepaliReceipt == 'true':
       danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    else:
        danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE)
    print("END>>cancelPharmacyGoodsReceipt")


def verifyCancelledGoodReceipt(danpheEMR, grno):
    print("START>>verify cancelled GoodsReceipt")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt List").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(grno)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "View").click()
    time.sleep(2)
    cancel = danpheEMR.find_element(By.XPATH, "//*[@id='print-good-reciept']/div/div/div[11]/div[1]/div/p[3]/b").text
    print("Cancelled Text is ", cancel)
    text = "CANCELLED"
    assert cancel == text
    danpheEMR.find_element(By.ID, "printButton")
    danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE)
    print("END Verifying cancelling Good Receipt")


def getPharmacyGoodsReceiptListAmount(danpheEMR):
    print("START>>getPharmacyGoodsReceiptListAmount")
    global SubTotal
    global DiscountTotal
    global TotalAmount
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    #danpheEMR.find_element(By.LINK_TEXT, "Order").click()
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Order')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt List").click()
    time.sleep(2)
    SubTotal = danpheEMR.find_element(By.XPATH,
                                      "(//b[contains(text(),'Sub Total')]//parent::span//parent::td//following-sibling::td)[1]").text
    print("SubTotal", SubTotal)
    DiscountTotal = danpheEMR.find_element(By.XPATH,
                                           "(//b[contains(text(),'Discount Total')]//parent::span//parent::td//following-sibling::td)[1]").text
    print("DiscountTotal", DiscountTotal)
    TotalAmount = danpheEMR.find_element(By.XPATH,
                                         "(//b[contains(text(),' Total Amount ')]//parent::span//parent::td//following-sibling::td)[1]").text
    print("TotalAmount", TotalAmount)
    print("END>>getPharmacyGoodsReceiptListAmount")


def XgetPharmacyGoodsReceiptListAmount():
    global xSubTotal
    global xDiscountTotal
    global xTotalAmount
    xSubTotal = SubTotal
    xDiscountTotal = DiscountTotal
    xTotalAmount = TotalAmount


def verifygetPharmacyGoodsReceiptListAmount(amount, discount):
    x = float(xSubTotal) + amount
    print("x", x)
    print("amount", amount)
    print("xSubTotal", xSubTotal)
    print("SubTotal", SubTotal)
    assert float(SubTotal) == float(x)
    assert float(DiscountTotal) == float(xDiscountTotal) + discount
    calTotalAmount = float(xTotalAmount) + amount - discount
    print("calculation Total Amount", calTotalAmount)
    assert float(TotalAmount) == calTotalAmount


def closePopupApplication(danpheEMR):
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger history-del-btn']").click()
    time.sleep(2)


def return_to_supplier(danpheEMR, grno, rqty):
    print(">>START: Returning to Supplier")
    time.sleep(2)
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
        danpheEMR.find_element(By.XPATH, '//a[@href="#/Pharmacy/Store" and contains(text(),"Store")]').click()
        danpheEMR.find_element(By.XPATH, '//a[contains(text(),"New Return Order")]').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
        danpheEMR.find_element(By.XPATH, '//a[@href="#/Pharmacy/Store" and contains(text(),"Store")]').click()
        danpheEMR.find_element(By.LINK_TEXT, "Return To Supplier").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(grno)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[8]/a[1]").click()
    creditnote = random.randint(1, 1000)
    print("Credit Note Of the Given Patient is ", creditnote)
    time.sleep(3)
    danpheEMR.find_element(By.NAME, "CreditNoteId").send_keys(creditnote)
    danpheEMR.find_element(By.CSS_SELECTOR, "th > input").click()
    danpheEMR.find_element(By.NAME, "returnquantity").send_keys(rqty)
    time.sleep(2)
    vatamount = danpheEMR.find_element(By.XPATH, "//*[@name = 'VATAmount']").text
    print("Vat amount of returned items is :", vatamount)
    returnstatus = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname = 'ReturnStatus']"))
    returnstatus.select_by_visible_text("Breakage")
    danpheEMR.find_element(By.XPATH, "//input[@value= 'Return']").click()
    time.sleep(6)
    danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[8]/a").click()
    time.sleep(2)
    vatamount = danpheEMR.find_element(By.XPATH, "//*[@id='print-credit-note']/div/div[9]/div[1]/div/table/tbody/tr[3]/td[2]/b").text
    vatamount = vatamount.replace(".", "")
    vatamount = int(vatamount)
    vatamount = float(vatamount * 0.01)
    print("Vat Amount removing dot is ", vatamount)
    assert vatamount > 0
    danpheEMR.find_element(By.XPATH, "//a[@title = 'Cancel']").click()
    return creditnote
    print("END>>Return to supplier")


def addPharmacyCreditOrganization(danpheEMR):
    print("START: Adding Pharmacy Credit Organization")
    time.sleep(1)
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Setting')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Credit Organizations").click()
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Add Organization')]").click()
    number = random.randint(0, 100)
    print(number)
    danpheEMR.find_element(By.ID, "OrganizationName").send_keys("Hospital Ward", + number)
    danpheEMR.find_element(By.ID, "save").click()


### Below Test Actions are currently deprecated
def manageStoreStock(danpheEMR, drugname, type, qty):
    print(">>START: Manage Store Stock")
    global drugqtyMScalc
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(drugname)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Manage Item").click()
    time.sleep(2)
    if type == "In":
        danpheEMR.find_element(By.CSS_SELECTOR, ".mt-checkbox:nth-child(1) > span").click()
        drugqtyMScalc = int(drugqtyMS) + qty
    elif type == "Out":
        danpheEMR.find_element(By.CSS_SELECTOR, ".mt-checkbox:nth-child(2) > span").click()
        drugqtyMScalc = int(drugqtyMS) - qty
    danpheEMR.find_element(By.XPATH, "//input[@name='UpdatedQty']").send_keys(qty)
    danpheEMR.find_element(By.XPATH, "//textarea[@name='Remark']").send_keys("Stock adjusted")
    danpheEMR.find_element(By.XPATH, "//input[@value='Update Stock']").click()
    time.sleep(2)


def addPharmacyDeposit(danpheEMR, HospitalNo, deposit):
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Patient')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Deposit").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//input[@name='DepositAmount']").send_keys(deposit)
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//input[@value='Add Deposit']").click()
        time.sleep(3)


def returnPharmacyDeposit(danpheEMR, HospitalNo, depositreturn):
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()

    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Patient')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Deposit").click()
    time.sleep(5)
    deposittype = Select(danpheEMR.find_element(By.XPATH, "//select"))
    deposittype.select_by_visible_text("Return Deposit")
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@name='DepositAmount']").send_keys(depositreturn)
    danpheEMR.find_element(By.XPATH, "//input[@value='Return Deposit']").click()
    time.sleep(3)


    ## Edit Pharmacy Goods Receipt
def editPharmacyGoodsReceiptContent(danpheEMR, supplier, qty, DrugName, grPrice):
    print("START>>edit PharmacyGoodsReceipt")
    global goodsReceiptNo
    time.sleep(2)
    if AppName == 'LPH':
      danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
      danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Order')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Goods Receipt").click()
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Select Supplier']").send_keys(supplier)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
    gRNo = random.randint(1000, 999999)
    print("GR No:", gRNo)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Invoice No']").send_keys(gRNo)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Invoice No']").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btn_AddNew").click()
    time.sleep(7)
    danpheEMR.find_element(By.ID, "txt_ItemName").send_keys(DrugName)
    danpheEMR.find_element(By.ID, "txt_ItemName").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "txt_BatchNo").send_keys(gRNo)
    danpheEMR.find_element(By.ID, "ItemQTy").send_keys(qty)
    print("grPrice", grPrice)
    grPrice = int(grPrice)
    danpheEMR.find_element(By.ID, "GRItemPrice").send_keys(grPrice)
    danpheEMR.find_element(By.ID, "Margin").send_keys(14)
    danpheEMR.find_element(By.ID, "btn_Save").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "editButton0").click()
    danpheEMR.find_element(By.ID, "txt_BatchNo").clear()
    gRNo1 = random.randint(1, 9999)
    danpheEMR.find_element(By.ID, "txt_BatchNo").send_keys(gRNo1)
    danpheEMR.find_element(By.ID, "ItemQTy").clear()
    qty1 = random.randint(1, 999)
    danpheEMR.find_element(By.ID, "ItemQTy").send_keys(qty1)
    danpheEMR.find_element(By.ID, "GRItemPrice").clear()
    grPrice1 = random.randint(1, 99)
    danpheEMR.find_element(By.ID, "GRItemPrice").send_keys(grPrice1)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btn_Save").click()
    time.sleep(3)
    # danpheEMR.find_element(By.XPATH, "//select[contains(.,'Main Store')]").send_keys("Main Store") Temporary disable due to issue.
    danpheEMR.find_element(By.XPATH, "//button[@class='btn green btn-success tooltip']").click()
    time.sleep(5)
    #danpheEMR.switch_to.alert.accept()  ## to close alert msg box for similiar GR items already entered.
    #time.sleep(2)

    if AppName == 'LPH':
        goodsReceiptNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'दाखिला प्रतिवेदन नम्बर')]").text
        # goodsReceiptNo = goodsReceiptNo.replace("-", "")
        goodsReceiptNo = goodsReceiptNo.partition(": ")[2]
        print("goodsReceiptNo:", goodsReceiptNo)
        danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    else:
        goodsReceiptNo = danpheEMR.find_element(By.XPATH, "//div[@id='print-good-reciept']/div/div/div[5]/p/b").text
        goodsReceiptNo = goodsReceiptNo.replace("-", "")
        print("goodsReceiptNo:", goodsReceiptNo)
        danpheEMR.find_element(By.ID, "printButton").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("END>>createPharmacyGoodsReceipt")
    return gRNo


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
