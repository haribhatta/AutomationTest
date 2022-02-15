import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By

# danpheEMR = AC.danpheEMR
# print("DanpheEMR", danpheEMR)
AppName = GSV.appName


# Module:Dispensary ------------------
def activatePharmacyCounter(danpheEMR, dispensaryName):
    print(">>Start: Pharmacy Counter Activate: START")
    time.sleep(7)
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
        time.sleep(7)
        danpheEMR.find_element(By.XPATH, "//i[contains(text(),'" + dispensaryName + "')]").click()
        time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Counter").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//h5").click()
    time.sleep(2)
    print("Pharmacy Counter Activate: END")


def createDispensarySale(danpheEMR, HospitalNo, qty, drugName, paymentmode):
    print(">>Create Dispensary Sale to Hospital Patient: START")
    danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Sale").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "patient-search").click()
    danpheEMR.find_element(By.ID, "patient-search").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "patient-search").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "patient-search").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "item-box0").click()
    danpheEMR.find_element(By.ID, "item-box0").clear()
    time.sleep(3)
    print("drugName:", drugName)
    danpheEMR.find_element(By.ID, "item-box0").send_keys(drugName)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    # drugavlqty = danpheEMR.find_element(By.XPATH, "(//input[@value=''])[6]").get_attribute("Value")
    # print("Drug Available qty:", drugavlqty)
    danpheEMR.find_element(By.ID, "qty0").click()
    danpheEMR.find_element(By.ID, "qty0").clear()
    danpheEMR.find_element(By.ID, "qty0").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(danpheEMR.find_element(By.XPATH, "//select"))
        paymentoptions.select_by_visible_text("credit")
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//input[@name='Remarks']").send_keys("This is credit bill")
    danpheEMR.find_element(By.XPATH, "//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element(By.XPATH, "//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    danpheEMR.find_element(By.ID, "btnPrintPhrmInvoice").send_keys(Keys.ESCAPE)
    print("Create Pharmacy OPD Invoice: END<<")
    return pInvoiceNo


def createDispensarySaleRandomPatient(danpheEMR, drugname, qty, paymentmode):
    print("<<START: Create Dispensary sales to random customer.")
    global pInvoiceNo
    danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
    time.sleep(2)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "item-box0").click()
    danpheEMR.find_element(By.ID, "item-box0").clear()
    danpheEMR.find_element(By.ID, "item-box0").send_keys(drugname)
    danpheEMR.find_element(By.ID, "item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//input[@formcontrolname= 'Quantity']").click()
    danpheEMR.find_element(By.XPATH, "//input[@formcontrolname= 'Quantity']").clear()
    danpheEMR.find_element(By.XPATH, "//input[@formcontrolname= 'Quantity']").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(danpheEMR.find_element(By.XPATH, "//select"))
        paymentoptions.select_by_visible_text("credit")
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//input[@name='Remarks']").send_keys("This is credit bill")
    danpheEMR.find_element(By.XPATH, "//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element(By.XPATH, "//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    danpheEMR.find_element(By.ID, "btnPrintPhrmInvoice").send_keys(Keys.ESCAPE)
    print("END>> Create Pharmacy OPD Invoice.", pInvoiceNo)


def returnPharmacyInvoice(danpheEMR, pInvoiceNo, qty, returnremark):
    print(">>Return Pharmacy Invoice: START")
    if AppName == 'SNCH' or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.XPATH, "//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        # danpheEMR.find_element(By.XPATH, "//i[contains(.,'MainDispensary')]").click()
        # time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "Return From Customer").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "invoiceId").send_keys(pInvoiceNo)
        print("pInvoiceNo is getting returned", pInvoiceNo)
        time.sleep(2)
        danpheEMR.find_element(By.ID, "invoiceId").send_keys(Keys.TAB)
        time.sleep(3)
        danpheEMR.find_element(By.ID, "invoiceId").send_keys(Keys.ENTER)
        time.sleep(9)
        danpheEMR.find_element(By.ID, "ReturnedQty0").clear()
        danpheEMR.find_element(By.ID, "ReturnedQty0").send_keys(qty)
        danpheEMR.find_element(By.XPATH, "//textarea[@name='Remark']").send_keys(returnremark)
        danpheEMR.find_element(By.ID, "return").click()
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger']").click()
        time.sleep(5)
    print("<<Return Pharmacy Invoice: END")


def verifyReturnPharmacyInvoice(danpheEMR, InvoiceNo, paymentmode, returnRemark):
    print("<<Verify Return Pharmacy Invoice: START")
    if AppName == 'SNCH' or AppName == 'LPH' or AppName == 'MPH':
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Return Sale List").click()
        time.sleep(9)
        # danpheEMR.find_element(By.XPATH, "//button[contains(.,'Load Data')]").click()
        danpheEMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(InvoiceNo)
        time.sleep(5)
        danpheEMR.find_element(By.LINK_TEXT, "Print").click()
        time.sleep(3)
        syspaymentmode = danpheEMR.find_element(By.XPATH, "//p[contains(text(),'Method of payment: ')]").text
        print("syspaymentmode:", syspaymentmode)
        syspaymentmode = syspaymentmode.partition("t: ")[2]
        # print("syspaymentmode1:", syspaymentmode)
        # assert syspaymentmode == paymentmode  # as per the comment on bug:EMR-2699 payment mode need to be cash on credit note.
        ReturnremarkTemp = danpheEMR.find_element(By.XPATH, "//div[@id='pharma-pat-info']/div[12]").text
        print("ReturnremarkTemp", ReturnremarkTemp)
        ReturnremarkTemp = ReturnremarkTemp.partition("s : ")[2]
        print("ReturnremarkTemp", ReturnremarkTemp)
        assert ReturnremarkTemp == returnRemark
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger history-del-btn']").click()
        # danpheEMR.find_element(By.CSS_SELECTOR, ".fa-close").click()

    print(">>Verify Return Pharmacy Invoice: END")


def settlePharmacyCreditInvoice(danpheEMR, HospitalNo, InvoiceNo):
    print(">>Create Dispensary Sale to Hospital Patient: START")
    danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Sale").click()
    danpheEMR.find_element(By.LINK_TEXT, "Settlement").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[@danphe-grid-action='showDetails']").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@value='Proceed']").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@class='btn btn-danger' and contains(text(),'X')]").click()
    time.sleep(3)


def transfer2MainStore(danpheEMR, itemName, qty):
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    danpheEMR.find_element(By.LINK_TEXT, "Transfer").click()
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'New Transfer')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "selectedStore").click()
    danpheEMR.find_element(By.ID, "selectedStore").send_keys("Main Store")
    danpheEMR.find_element(By.ID, "selectedStore").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(itemName)
    danpheEMR.find_element(By.ID, "itemName0").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.NAME, "quantity").send_keys(qty)
    danpheEMR.find_element(By.ID, "remarks").send_keys("Transfer to Main Store")
    danpheEMR.find_element(By.ID, "stockTransfer").click()

# quantity is for Varifying the Requested Quantity
def receiveItem(danpheEMR,qty):
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    danpheEMR.find_element(By.LINK_TEXT, "Requisition").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[6]/span/a[2]").click()
    time.sleep(3)
    requestedQty = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div/div[2]/div/div[2]/table/tbody/tr/td[2]").text
    requestedQty = int(requestedQty)
    print("Requested Quantity is : ", requestedQty)
    assert qty == requestedQty
    remark = danpheEMR.find_element(By.ID, "remarks")
    remark.send_keys("Received a Quantity of ", +qty)
    danpheEMR.find_element(By.ID, "btn_Add").click()


def wait_for_window(danpheEMR,timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
