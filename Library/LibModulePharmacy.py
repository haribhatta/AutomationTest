from selenium import webdriver
import time
import Library.ApplicationConfiguration as AC
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
########
danpheEMR = AC.danpheEMR
AppName = AC.appName
########
def addPharmacyItem(genericName):  # incomplete
    print(">>START: addPharmacyItem")
    global DrugName
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Setting").click()
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Item").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success']").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(
        "Pharmay Unit")
    danpheEMR.find_element_by_xpath("//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(
        Keys.RETURN)
    drugMGtemp = random.randint(10, 1000)
    drugMG = str(drugMGtemp)
    DrugName = ('Autodrug' + drugMG)
    print(DrugName)
    danpheEMR.find_element_by_xpath("//input[@value='']").send_keys(DrugName)
    danpheEMR.find_element_by_xpath("//input[@value='']").send_keys(Keys.RETURN)
    time.sleep(3)
    # danpheEMR.find_element_by_css_selector("//select").click()
    danpheEMR.find_element_by_xpath("//div[4]/div/div/div/input").send_keys("HIMALAYAN")  # Company
    danpheEMR.find_element_by_xpath("//div[4]/div/div/div/input").send_keys(Keys.RETURN)
    danpheEMR.find_element_by_xpath("//div[5]/div/div/div/input").send_keys(genericName)  # itemType
    danpheEMR.find_element_by_xpath("//div[5]/div/div/div/input").send_keys(Keys.RETURN)  # itemType
    # danpheEMR.find_element_by_css_selector(".ng-touched:nth-child(1)").send_keys("ABGEL")
    danpheEMR.find_element_by_xpath("//div[6]/div/div/div/input").send_keys("Tablet")  # unit
    danpheEMR.find_element_by_xpath("//div[6]/div/div/div/input").send_keys(Keys.RETURN)  # unit
    danpheEMR.find_element_by_xpath("//div[7]/div/div/div/input").send_keys(genericName)  # genericName
    danpheEMR.find_element_by_xpath("//div[7]/div/div/div/input").send_keys(Keys.RETURN)  # genericName
    time.sleep(3)
    danpheEMR.find_element_by_id("save").click()
    time.sleep(9)
    print("End>>addPharmacyItem")
def verifyPharmacyItem():
    print(">>Start:verifyPharmacyItem")
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Setting").click()
    time.sleep(5)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(9)
    assert DrugName == danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
    print("End>>verifyPharmacyItem")
def getStoreDetail(drugname):
    print(">>Start: getStoreDetail")
    global drugqtyMS
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Store").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
        time.sleep(5)
        drugnameMS = danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
        print("drugnameMS:", drugnameMS)
        print("drugname:", drugname)
        assert drugnameMS == drugname
        sysdrugqty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
        drugqtyMS = int(sysdrugqty)
        print("drugqtyMS:", drugqtyMS)
    print("End>>getStoreDetail")
def getStockDetail(drugname):
    print(">>Start: getStockDetail")
    global drugqtySS
    if AppName == 'SNCH':
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Dispensary").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Stock").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
        time.sleep(3)
        drugnameSS = danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
        print("drugnameSS:", drugnameSS)
        sysdrugqty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
        drugqtySS = int(sysdrugqty)
        print("drugqtySS:", drugqtySS)
    print("End>>getStockDetail")
def verifyStoreDetail(drugname):
    print(">>Start:verifyStoreDetail")
    danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").clear()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(2)
    sysdrugname = danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[2]").text
    print("sysdrugname:", sysdrugname)
    assert drugname == sysdrugname
    sysdrugqty = danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    print("sysdrugqty", sysdrugqty)
    print("newdrugqtyMS", drugqtyMScalc)
    assert int(drugqtyMScalc) == int(sysdrugqty)
    print("End>>verifyStoreDetail")
def verifyStockDetail(drugname):
    print(">>Start: verifyStockDetail")
    danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(5)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(2)
    sysdrugname = danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div").text
    print("sysdrugname", sysdrugname)
    assert drugname == sysdrugname
    sysdrugqty = danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    print("drugqtySS:", drugqtySS)
    print("sysdrugqty", sysdrugqty)
    assert int(drugqtySS) == int(sysdrugqty)
    print("End>>: verifyStockDetail")
def verifyStockDetailTC():
    print(">>Start: verifyStockDetailTC")
    danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(5)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(2)
    sysdrugqty = danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    assert sysdrugqty == '0'
    print("End>>verifyStockDetailTC")
def transferStore2Dispensary(drugname, tqty):
    print(">>Start:transferStore2Dispensary")
    global drugqtyMS
    global drugqtySS
    danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").clear()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Transfer Item").click()
    danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(tqty)
    time.sleep(2)
    danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys("MainDispensary")
    time.sleep(1)
    danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    drugqtyMS = drugqtyMS - tqty
    print("drugqtyMS", drugqtyMS)
    drugqtySS = drugqtySS + tqty
    print("drugqtySS", drugqtySS)
    print("End>>transferStore2Dispensary")
def transferStore2DispensaryTC(tqty, DrugName):
    print(">>Start:transferStore2DispensaryTC")
    danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").clear()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Transfer Item").click()
    danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(tqty)
    time.sleep(2)
    danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys("MainDispensary")
    time.sleep(1)
    danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    print("End>>transferStore2DispensaryTC")
def transferDispensary2Store(drugname, tqty):
    print(">>Start: transferDispensary2Store")
    global drugqtySS
    global drugqtyMS
    danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Store Transfer").click()
    time.sleep(2)
    danpheEMR.find_element_by_id("transfertoStoreQty").send_keys(tqty)
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    drugqtySS = int(drugqtySS) - tqty
    print("drugqtySS", drugqtySS)
    drugqtyMS = int(drugqtyMS) + tqty
    print("drugqtyMS", drugqtyMS)
    # danpheEMR.find_element_by_link_text("Store").click()
    print("End>>transferDispensary2Store")
def transferDispensary2StoreTC(tqty):
    print(">>Start: transferDispensary2StoreTC")
    danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Store Transfer").click()
    time.sleep(2)
    danpheEMR.find_element_by_id("transfertoStoreQty").send_keys(tqty)
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    print("End>>transferDispensary2StoreTC")
def manageStoreStock(drugname, type, qty):
    print(">>START: Manage Store Stock")
    global drugqtyMScalc
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Manage Item").click()
    time.sleep(2)
    if type == "In":
        danpheEMR.find_element_by_css_selector(".mt-checkbox:nth-child(1) > span").click()
        drugqtyMScalc = int(drugqtyMS) + qty
    elif type == "Out":
        danpheEMR.find_element_by_css_selector(".mt-checkbox:nth-child(2) > span").click()
        drugqtyMScalc = int(drugqtyMS) - qty
    danpheEMR.find_element_by_xpath("//input[@name='UpdatedQty']").send_keys(qty)
    danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys("Stock adjusted")
    danpheEMR.find_element_by_xpath("//input[@value='Update Stock']").click()
    time.sleep(2)
def createPharmacyInvoice(HospitalNo, qty, paymentmode):
    print(">>Create Pharmacy OPD Invoice: START")
    global pInvoiceNo
    danpheEMR.find_element_by_link_text("Sale").click()
    danpheEMR.find_element_by_id("patient-search").click()
    danpheEMR.find_element_by_id("patient-search").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
    danpheEMR.find_element_by_id("patient-search").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").click()
    danpheEMR.find_element_by_id("item-box0").clear()
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").send_keys()
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    drugavlqty = danpheEMR.find_element_by_xpath("(//input[@value=''])[6]").get_attribute("Value")
    print("Drug Available qty:", drugavlqty)
    drugavlqty = danpheEMR.find_element_by_css_selector("td:nth-child(8) > .form-control").text
    print("Drug Available qty:", drugavlqty)
    danpheEMR.find_element_by_id("qty-box0").click()
    danpheEMR.find_element_by_id("qty-box0").clear()
    danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
    drugremainingqty = int(drugqtySS) - qty
    print("Remaining qty:", drugremainingqty)
    newdrugqtySS = drugremainingqty
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text("CREDIT")
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")

    danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]

    print("Create Pharmacy OPD Invoice: END<<")
def createPharmacyInvoiceRandomPatient(drugname, qty, paymentmode):
    print("<<START: Create Pharmacy OPD Invoice.")
    global pInvoiceNo
    if AppName == 'SNCH':
        danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//a[contains(text(),' Sale ')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("patient-search").click()
        danpheEMR.find_element_by_id("patient-search").send_keys('Auto Test')
        time.sleep(5)
        danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_id("item-box0").click()
        danpheEMR.find_element_by_id("item-box0").clear()
        danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
        danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
        time.sleep(5)
        danpheEMR.find_element_by_id("qty0").click()
        danpheEMR.find_element_by_id("qty0").clear()
        danpheEMR.find_element_by_id("qty0").send_keys(qty)
        time.sleep(3)
        if paymentmode == 'CREDIT':
            paymentoptions = Select(danpheEMR.find_element_by_xpath("//select"))
            paymentoptions.select_by_visible_text("CREDIT")
            time.sleep(2)
            danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
        danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
        time.sleep(5)
        pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
        pInvoiceNo = pInvoiceNo.partition("PH")[2]
        danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()

    time.sleep(3)
    print("END>> Create Pharmacy OPD Invoice.", pInvoiceNo)
def createPharmacyInvoiceTC(HospitalNo, drugname, qty, paymentmode):
    print(">>Create Pharmacy OPD Invoice: START")
    global pInvoiceNo
    danpheEMR.find_element_by_link_text("Sale").click()
    danpheEMR.find_element_by_id("patient-search").click()
    danpheEMR.find_element_by_id("patient-search").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
    danpheEMR.find_element_by_id("patient-search").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").click()
    danpheEMR.find_element_by_id("item-box0").clear()
    danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    if AppName == "SNCH":
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").send_keys(qty)
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    print("pInvoiceNo", pInvoiceNo)
    danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    epInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("Create Pharmacy OPD Invoice: END<<")
def createPharmacyInvoiceAnonymous(drugname, qty, paymentmode):
    print(">>Create Pharmacy OPD Invoice: START")
    global pInvoiceNo
    danpheEMR.find_element_by_link_text("Sale").click()
    danpheEMR.find_element_by_xpath("//button[contains(.,'Anonymous Patient')]").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").click()
    danpheEMR.find_element_by_id("item-box0").clear()
    danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    if AppName == "SNCH":
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").send_keys(qty)
        danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    print("pInvoiceNo", pInvoiceNo)
    danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("END>>: Create Pharmacy OPD Invoice.", pInvoiceNo)
def createPharmacyPurchaseOrder():
    print(">>Start: Create purchase order in pharmacy")
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    danpheEMR.find_element_by_link_text("Order").click()
    danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderItems')]").click()
    danpheEMR.find_element_by_css_selector(".col-md-9 > .form-control").click()
    time.sleep(9)
    dropdown = danpheEMR.find_element_by_css_selector(".col-md-9 > .form-control")
    time.sleep(3)
    dropdown.find_element_by_xpath("//option[. = 'AARATI MEDITCHA PVT']").click()
    time.sleep(2)
    danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .form-control").send_keys(
        "ABEN SUSPENSION 10ML")
    danpheEMR.find_element_by_name("quantity").click()
    time.sleep(2)
    danpheEMR.find_element_by_name("quantity").send_keys("100")
    danpheEMR.find_element_by_name("price").click()
    danpheEMR.find_element_by_name("price").send_keys("1")
    # danpheEMR.find_element_by_css_selector(".page-content").click()
    danpheEMR.find_element_by_css_selector(".text-right > .btn-success").click()
    time.sleep(5)
def verifyPharmacyPurchaseOrder():
    print(">>Start: Verify purchase order in pharmacy")
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Order").click()
    danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderList')]").click()
    # Jira ticket EMR-3297 need to deploy to search the purchase order with PO number.
def addPharmacyGRfromPO():
    print(">>Start: Create GR from purchase order in pharmacy")
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    danpheEMR.find_element_by_link_text("Order").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderList')]").click()
    danpheEMR.find_element_by_link_text("Add Goods Receipt").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
def verifyPharmacyInvoice(qty):
    print(">>Verify Pharmacy Invoice: START")
    assert str(qty) == danpheEMR.find_element_by_xpath("//tr[2]/td[3]").text
    totalamount = danpheEMR.find_element_by_xpath("//table[@id='pharma-bill-sum']/tbody/tr[3]/td[2]").text
    totalamount = totalamount.partition("Rs. ")[2]
    totalamount = totalamount.partition(".00")[0]
    print("Verify Pharmacy Invoice: END<<", "Pharmacy Invoice No: ", pInvoiceNo)
def verifyPharmacyInvoice3(drugname, qty, rate):
    time.sleep(7)
    print(">>Verify Pharmacy Invoice: START")
    danpheEMR.find_element_by_xpath("//i[@class='fa fa-close']").click()
def returnPharmacyInvoice(qty, returnremark):
    print(">>Return Pharmacy Invoice: START")
    if AppName == 'SNCH':
        danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        # danpheEMR.find_element_by_xpath("//i[contains(.,'MainDispensary')]").click()
        # time.sleep(2)
        danpheEMR.find_element_by_link_text("Return From Customer").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("invoiceId").send_keys(pInvoiceNo)
        print("pInvoiceNo is getting returned", pInvoiceNo)
        time.sleep(2)
        danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.TAB)
        time.sleep(3)
        danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.ENTER)
        time.sleep(2)
        danpheEMR.find_element_by_id("ReturnedQty0").clear()
        danpheEMR.find_element_by_id("ReturnedQty0").send_keys(qty)
        danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys(returnremark)
        danpheEMR.find_element_by_id("return").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger']").click()
        time.sleep(5)

    print("<<Return Pharmacy Invoice: END")
def verifyReturnPharmacyInvoice(HospitalNo, paymentmode, returnRemark):
    print("<<Verify Return Pharmacy Invoice: START")
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Return Sale List").click()
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Print").click()
        time.sleep(3)
        syspaymentmode = danpheEMR.find_element_by_xpath("//p[contains(text(),'Method of payment: ')]").text
        print("syspaymentmode:", syspaymentmode)
        syspaymentmode = syspaymentmode.partition("t: ")[2]
        # print("syspaymentmode1:", syspaymentmode)
        assert syspaymentmode == "Cash"  # as per the comment on bug:EMR-2699 payment mode need to be cash on credit note.
        ReturnremarkTemp = danpheEMR.find_element_by_xpath("//div[@id='pharma-pat-info']/div[12]").text
        print("ReturnremarkTemp", ReturnremarkTemp)
        ReturnremarkTemp = ReturnremarkTemp.partition("s : ")[2]
        print("ReturnremarkTemp", ReturnremarkTemp)
        assert ReturnremarkTemp == returnRemark
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
        # danpheEMR.find_element_by_css_selector(".fa-close").click()

    print(">>Verify Return Pharmacy Invoice: END")
def addPharmacyDeposit(HospitalNo, deposit):
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//a[contains(text(),'Patient')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Deposit").click()
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//input[@name='DepositAmount']").send_keys(deposit)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//input[@value='Add Deposit']").click()
        time.sleep(3)
def returnPharmacyDeposit(HospitalNo, depositreturn):
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Patient')]").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Deposit").click()
    time.sleep(5)
    deposittype = Select(danpheEMR.find_element_by_xpath("//select"))
    deposittype.select_by_visible_text("Return Deposit")
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//input[@name='DepositAmount']").send_keys(depositreturn)
    danpheEMR.find_element_by_xpath("//input[@value='Return Deposit']").click()
    time.sleep(3)
def createPharmacyGoodsReceipt(qty, DrugName, grPrice):
    global goodsReceiptNo
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Order").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Goods Receipt").click()
        time.sleep(7)
        danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys("Aayush surgichem")
        danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
        gRNo = random.randint(100, 9999)
        print("GR No:", gRNo)
        danpheEMR.find_element_by_xpath("//input[@placeholder='Invoice No']").send_keys(gRNo)
        danpheEMR.find_element_by_id("btn_AddNew").click()
        time.sleep(7)
        danpheEMR.find_element_by_id("txt_ItemName").send_keys(DrugName)
        danpheEMR.find_element_by_id("txt_ItemName").send_keys(Keys.TAB)
        time.sleep(3)
        danpheEMR.find_element_by_id("txt_BatchNo").send_keys(gRNo)
        danpheEMR.find_element_by_id("ItemQTy").send_keys(qty)
        print("grPrice", grPrice)
        grPrice = int(grPrice)
        danpheEMR.find_element_by_id("GRItemPrice").send_keys(grPrice)
        danpheEMR.find_element_by_id("Margin").send_keys(14)
        danpheEMR.find_element_by_id("btn_Save").click()
        # danpheEMR.find_element_by_xpath("//select[contains(.,'Main Store')]").send_keys("Main Store") Temporary disable due to issue.
        danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success tooltip']").click()
        time.sleep(14)
        goodsReceiptNo = danpheEMR.find_element_by_xpath("(//div[@col-id='GoodReceiptPrintId'])[2]").text
    print("goodsReceiptNo:", goodsReceiptNo)
def cancelPharmacyGoodsReceipt():
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Order").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Goods Receipt List").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("(//a[contains(text(), 'View')])[1]").click()
    time.sleep(3)
    sysGRno = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Goods Receipt No.:')]").text
    print("sysGRno", sysGRno)
    danpheEMR.find_element_by_xpath("//button[@title='Cancel Goods Receipt']").click()
    time.sleep(2)
    assert danpheEMR.switch_to.alert.text == "NOTE !!! Do you want to cancel Good Receipt?"
    time.sleep(3)
    danpheEMR.switch_to.alert.accept()
    time.sleep(7)
def getPharmacyGoodsReceiptListAmount():
    print(">>Start:getPharmacyGoodsReceiptListAmount")
    global SubTotal
    global DiscountTotal
    global TotalAmount
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Order").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Goods Receipt List").click()
        time.sleep(2)
        SubTotal = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Sub Total')]//parent::span//parent::td//following-sibling::td)[1]").text
        print("SubTotal", SubTotal)
        DiscountTotal = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Discount Total')]//parent::span//parent::td//following-sibling::td)[1]").text
        print("DiscountTotal", DiscountTotal)
        TotalAmount = danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),' Total Amount ')]//parent::span//parent::td//following-sibling::td)[1]").text
        print("TotalAmount", TotalAmount)
        print(">>Start:getPharmacyGoodsReceiptListAmount")
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
    assert float(TotalAmount) == float(xTotalAmount) + amount - discount
def verifyDispensaryStock(qty):
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(2)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(5)
    drugnameTemp = danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
    assert drugnameTemp == DrugName
    drugqtyTemp = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
    assert drugqtyTemp == str(qty)
def createPharmacyOPDBilling(qty, paymentmode):
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Sale").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//button[contains(.,'Anonymous Patient')]").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").click()
    danpheEMR.find_element_by_id("item-box0").clear()
    danpheEMR.find_element_by_id("item-box0").send_keys(DrugName)
    danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    danpheEMR.find_element_by_id("qty-box0").click()
    danpheEMR.find_element_by_id("qty-box0").clear()
    danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text(paymentmode)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("Create Pharmacy OPD Invoice: END<<")
def verifyPharmacyGoodsReceipt(qty, DrugName):
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Pharmacy").click()
    danpheEMR.find_element_by_link_text("Order").click()
    danpheEMR.find_element_by_link_text("Goods Receipt List").click()
    time.sleep(7)
    danpheEMR.find_element_by_link_text("View").click()
    time.sleep(3)
    sysdrugname = danpheEMR.find_element_by_xpath("//td[2]/b").text
    print("sysdrugname:", sysdrugname)
    assert sysdrugname == DrugName
    danpheEMR.find_element_by_css_selector(".fa-times").click()
def closePopupApplication(saleinvoice):
    time.sleep(7)
    danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    time.sleep(3)

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

