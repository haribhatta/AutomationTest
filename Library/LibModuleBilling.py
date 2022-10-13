import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AppName = GSV.appName


def counteractivation(danpheEMR):
    print(">>Activate Billing Counter: START")
    time.sleep(7)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Counter Activate").click()
    time.sleep(3)
    danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(1) img").click()
    time.sleep(5)
    print("Activate Billing Counter: END<<")


def verifyopdinvoice(danpheEMR, deposit, billamt):
    print(">>Verify OPD Invoice Details: START")
    syscontactno = danpheEMR.find_element(By.XPATH, "//p[contains(text(),'Contact No:')]").text
    syscontactno = syscontactno.partition("No: ")[2]
    print(syscontactno)
    if deposit < billamt and deposit > 0:
        DepositDeductorReturn = danpheEMR.find_element(By.XPATH,
            "//div[@id='printpage']/div/div[5]/div[10]/span").text  # Deposit Deduct/Return:
        DepositDeductorReturn = DepositDeductorReturn.partition("n: ")[2]
        print("1: Deposit Deduct/Return: ", DepositDeductorReturn)
        assert int(DepositDeductorReturn) == deposit
        systender = danpheEMR.find_element(By.XPATH,
            "//div[@id='printpage']/div/div[5]/div[10]/span[2]").text  # Tender
        systender = systender.partition("r: ")[2]
        systender = systender.partition(".00")[0]
        Tender = int(billamt) - int(deposit)
        print("Expected Tender: ", Tender)
        print("Actual Tender:", systender)
        assert int(Tender) == int(systender)
        sysdepositbalance = danpheEMR.find_element(By.XPATH,
            "//div[@id='printpage']/div/div[5]/div[10]/span[3]").text  # Deposit Balance
        print("3:", sysdepositbalance)
        sysdepositbalance = sysdepositbalance.partition("e: ")[2]
        assert sysdepositbalance == "0"
    print(">>>Verify OPD Invoice. >>End")


def returnBillingInvoice(danpheEMR, InvoiceNo, returnmsg):
    print(">>START: Returning OPD Invoice.", InvoiceNo)
    global returnTotalAmount
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.LINK_TEXT, "Return Bills").click()
    time.sleep(4)
    danpheEMR.find_element(By.NAME, "TransactionId").clear()
    danpheEMR.find_element(By.NAME, "TransactionId").send_keys(InvoiceNo)
    time.sleep(2)
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-search").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "txtRetQty_0").send_keys(1)
    danpheEMR.find_element(By.ID, "txtReturnRemarks").send_keys(returnmsg)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnSubmit").click()
    time.sleep(3)
    returnremark = danpheEMR.find_element(By.XPATH, "//div[contains(text(), ' Remarks:')]").text
    returnTotalAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Amount ')]/following-sibling::td").text
    # danpheEMR.find_element(By.ID, "btnPrintRecipt").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,
        "//a[@class='btn btn-danger del-btn']").click()  # This is to close print window.
    time.sleep(3)
    print("returnmsgTemp", returnremark)
    returnremark = returnremark.partition("Remarks: ")[2]
    print("returnremark", returnremark)
    print("returnmsg", returnmsg)
    assert returnremark == returnmsg
    print("returnTotalAmount", returnTotalAmount)
    print("<<END: Return OPD Invoice.")


def returnBillingInvoicePartial(danpheEMR, InvoiceNo, returnmsg):
    print(">>START: Partial Return of billing invoice.", InvoiceNo)
    global returnTotalAmount
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.LINK_TEXT, "Return Bills").click()
    time.sleep(3)
    danpheEMR.find_element(By.NAME, "TransactionId").clear()
    danpheEMR.find_element(By.NAME, "TransactionId").send_keys(InvoiceNo)
    time.sleep(2)
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-search").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "txtRetQty_0").send_keys(1)
    danpheEMR.find_element(By.ID, "txtReturnRemarks").send_keys(returnmsg)
    danpheEMR.find_element(By.ID, "btnSubmit").click()
    time.sleep(3)
    # returnremark = danpheEMR.find_element(By.XPATH, "//div[contains(text(), ' Remarks:')]").text
    # returnTotalAmount = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'Total Amount ')]/following-sibling::td").text
    # danpheEMR.find_element(By.ID, "btnPrintRecipt").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH,
        "//a[@class='btn btn-danger del-btn']").click()  # This is to close print window.

def verifyReturnBillingInvoice(danpheEMR, InvoiceNo, itemRate):
    print("START>>verifyReturnBillingInvoice")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Duplicate Prints')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Returned Invoice')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(InvoiceNo)
    time.sleep(5)
    RefInvoiceNumber = danpheEMR.find_element(By.XPATH, "(//div[@col-id='RefInvoiceNum'])[2]").text
    print("RefInvoiceNumber", RefInvoiceNumber)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Show Details')]").click()
    time.sleep(3)
    returnAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Amount')]/following-sibling::td").text
    returnAmount = int(returnAmount.partition(".")[0])
    print("returnAmount:", returnAmount)
    print("ItemRate:", itemRate)
    assert returnAmount == itemRate
    danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']").click()
    time.sleep(2)
    print("END>>verifyReturnBillingInvoice")

def verifyCreditNoteDuplicateInvoice(danpheEMR, InvoiceNo):
    print("Verify partial return of bill invoice")
    # global returnTotalAmount
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Duplicate Prints')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Returned Invoice')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(InvoiceNo)
    time.sleep(5)
    HospitalNo = danpheEMR.find_element(By.ID, "PatientCode").text
    print("HospitalNo:", HospitalNo)
    RefInvoiceNumber = danpheEMR.find_element(By.XPATH, "(//div[@col-id='RefInvoiceNum'])[2]").text
    print("RefInvoiceNumber", RefInvoiceNumber)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Show Details')]").click()
    time.sleep(3)
    ReturnAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Amount')]/following-sibling::td").text
    print("ReturnAmount", ReturnAmount)
    danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']").click()
    time.sleep(2)
    return HospitalNo


def createlabxrayinvoice(danpheEMR, HospitalNo, labtest, imagingtest):
    print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")
    print("Hospital Number:", HospitalNo)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.implicitly_wait(10)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.ENTER)
    element = WebDriverWait(danpheEMR, 10)
    element.until(
        EC.element_to_be_clickable((By.ID, "btn_billRequest"))
    ).click()

    # danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    wait = WebDriverWait(danpheEMR, 20)
    wait.until(
        EC.element_to_be_clickable((By.ID, "srchbx_ItemName_0"))
    ).click()

    # danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(imagingtest)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    danpheEMR.find_element(By.CSS_SELECTOR, "a > .btn-success").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(labtest)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(Keys.RETURN)
    price = WebDriverWait(danpheEMR, 10)
    price.until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@name='total'])[2]"))
    )
    price2 = danpheEMR.find_element(By.XPATH, "(//input[@name='total'])[2]").get_attribute('value')
    totalprice = int(price1) + int(price2)
    print("Total Price:", totalprice)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    InNo = WebDriverWait(danpheEMR, 10)
    InNo.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Invoice No:')]")))
    # InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    print("Create OPD Invoice: 1 Lab + 1 Xray Items: END<<")


def multiplebillingclick(danpheEMR, HospitalNo, labtest, imagingtest):
    print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")
    print("Hospital Number:", HospitalNo)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(imagingtest)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    time.sleep(1)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    time.sleep(1)
    danpheEMR.find_element(By.CSS_SELECTOR, "a > .btn-success").click()
    time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(labtest)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(Keys.RETURN)
    time.sleep(2)
    price2 = danpheEMR.find_element(By.XPATH, "(//input[@name='total'])[2]").get_attribute('value')
    totalprice = int(price1) + int(price2)
    print("Total Price:", totalprice)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(3)
    # InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)

    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    print("Create OPD Invoice: 1 Lab + 1 Xray Items: END<<")
    return InvoiceNo


def verifymultipleclickbilling(danpheEMR, InvoiceNo):
    print("START>>verifymultipleclickbilling")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Duplicate Prints ')]").click()
    time.sleep(5)
    print("InvoiceNo:", InvoiceNo)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(InvoiceNo)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Load Invoices')]").click()
    time.sleep(2)
    searchResult = danpheEMR.find_element(By.XPATH, "//div[@class='page-items']").text
    print("searchResult:", searchResult)
    searchResult = searchResult.partition("Showing ")[2]
    print("searchResult:", searchResult)
    searchResult = searchResult.partition(" /")[0]
    print("searchResult:", searchResult)
    assert searchResult == "1"
    danpheEMR.find_element(By.XPATH, "(//a[contains(text(),'Show Details')])[1]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    # element = danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']")
    time.sleep(2)
    print("END>>verifymultipleclickbilling")


def createLabInvoice(danpheEMR, HospitalNo, labtest):
    print("START>>createLabInvoice")
    print("Hospital Number:", HospitalNo)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(5)
    if AppName == 'LPH':
        labType = Select(danpheEMR.find_element(By.ID, "lab_type"))
        labType.select_by_visible_text("OP-LAB")
    time.sleep(4)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(labtest)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "txtQuantity_0").send_keys(1)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    time.sleep(1)
    totalprice = int(price1)
    print("Total Price:", totalprice)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(9)
    # InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)

    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    print("END>>createLabInvoice")


def createERlabInvoice(danpheEMR, HospitalNo, labtest, labtype):
    print("START>>createERlabInvoice")
    global InvoiceNo
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "lab_type").send_keys(labtype)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(labtest)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    time.sleep(1)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    time.sleep(1)
    danpheEMR.find_element(By.CSS_SELECTOR, "a > .btn-success").click()
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(9)
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    print("END>>createERlabInvoice")


def verifylabxrayinvoice():
    print("START>>verifylabxrayinvoice")
    ## code goes here
    print("END>>verifylabxrayinvoice")


def verifySampleCollectionDuplicateEntry():
    print("START>>verifySampleCollectionDuplicateEntry")
    ## code goes here
    print("START>>verifySampleCollectionDuplicateEntry")


def createProvisionalBill(danpheEMR, HospitalNo, usgtest):
    print("START>>createProvisionalBill")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(usgtest)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Print Provisional Slip ')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "btnPrintProvisionalSlip").send_keys(Keys.ESCAPE)
    time.sleep(2)
    print("END>>createProvisionalBill")


def verifyDuplicateBill(danpheEMR, HospitalNo):
    print("START>>verifyDuplicateBill")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Duplicate Prints ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Load Invoices')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    #sysHospitalNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'" + HospitalNo + "')]").text
    sysHospitalNo = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'" + HospitalNo + "')]").text

    assert HospitalNo == sysHospitalNo  # to check double click issue on invoice creation.
    # danpheEMR.find_element(By.LINK_TEXT, "Show Details").click()
    danpheEMR.find_element(By.XPATH, "(//a[contains(text(),'Show Details')])[1]").click()
    time.sleep(2)
    #danpheEMR.find_element(By.ID, "btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)
    danpheEMR.find_element(By.ID, "btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("END>>verifyDuplicateBill")


def createCopyItemInvoice(danpheEMR, paymentmode):
    print(">>START: CreateCopyItemInvoice")
    global InvoiceNo
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Create Copy Of Items ')]").click()
    time.sleep(3)
    if paymentmode == 'CREDIT':
        danpheEMR.find_element(By.ID, "pay_mode").send_keys('CREDIT')
        danpheEMR.find_element(By.XPATH, "//input[@name='Remarks']").send_keys("Credit in request of chairman")
        time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(13)
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    print("NewInvoiceNo", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("NewInvoiceNo", InvoiceNo)
    CopyItemTotalAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Amount ')]/following-sibling::td").text
    print("CopyItemTotalAmount:", CopyItemTotalAmount)
    print("returnTotalAmount", returnTotalAmount)
    assert CopyItemTotalAmount == returnTotalAmount  # LPH-865 : LPH_V1.9.0
    print("<<END: CreateCopyItemInvoice")


# Module:Billing_OP -----------------
def opDeposit(danpheEMR, HospitalNo, amount):
    print("START>>opDeposit")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btn_addDeposit").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@name='amount']").send_keys(amount)
    danpheEMR.find_element(By.XPATH, "//input[@value='Add Deposit and Print']").click()
    time.sleep(3)
    print("END>>opDeposit")


def opDepositDbiling(danpheEMR, HospitalNo, deposit, testname):
    print("START>>opDepositDbiling")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(2)
    if AppName == "LPH":
        labType = Select(danpheEMR.find_element(By.ID, "lab_type"))
        labType.select_by_visible_text("OP-LAB")
    else:
        time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(testname)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    itemAprice = danpheEMR.find_element(By.XPATH, "//input[@name='price']").get_attribute("value")
    SubTotal = itemAprice
    DepositBalance = danpheEMR.find_element(By.XPATH, "//tr[4]/td[2]").text
    assert deposit == int(DepositBalance)
    # BalanceAmount = danpheEMR.find_element(By.XPATH, "//td[2]/span").text
    # assert deposit == int(BalanceAmount)
    TotalAmount = danpheEMR.find_element(By.XPATH, "//tr[4]/td[2]/input").get_attribute("value")
    print("TotalAmount", TotalAmount)
    assert TotalAmount == SubTotal
    Tender = danpheEMR.find_element(By.XPATH, "//input[@name='Tender']").get_attribute("value")
    print("Tender before deposit deduction: ", Tender)
    assert Tender == TotalAmount
    time.sleep(2)
    paymentMode = Select(danpheEMR.find_element(By.NAME, "pay_mode"))
    paymentMode.select_by_visible_text("Others")
    time.sleep(3)
    # Need to maintain the Display sequence from Setting > Payment Mode Settings make Pos m
    if int(DepositBalance) >= int(TotalAmount):
        dep = danpheEMR.find_element(By.ID, "mode_0")
    # Use Java script executioner click instead of click method.
        danpheEMR.execute_script("arguments[0].click();", dep)
        time.sleep(2)
    else:
        remaining = int(TotalAmount) - int(DepositBalance)
        print("Remaining amount after deducting deposite is :", remaining)
        dep = danpheEMR.find_element(By.ID, "mode_0")
        # Use Java script executioner click instead of click method.
        danpheEMR.execute_script("arguments[0].click();", dep)
        danpheEMR.find_element(By.ID, "input_amount1").send_keys(remaining)
        time.sleep(2)
    danpheEMR.find_element(By.ID, "Add").click()
    danpheEMR.find_element(By.NAME, "Remarks").send_keys("Deducted full from deposite")
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    time.sleep(3)
    print("END>>opDepositDbiling")


def opDepositDbilingTenderCashReturn(danpheEMR, HospitalNo, deposit, testname):
    global ChangeReturn
    print("START>>opDepositDbilingTenderCashReturn")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(2)
    if AppName == 'LPH':
        labType = Select(danpheEMR.find_element(By.ID, "lab_type"))
        labType.select_by_visible_text("OP-LAB")
        time.sleep(3)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(testname)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    itemAprice = danpheEMR.find_element(By.XPATH, "//input[@name='price']").get_attribute("value")
    SubTotal = itemAprice
    DepositBalance = danpheEMR.find_element(By.XPATH, "//tr[4]/td[2]").text
    print("DepositBalance", DepositBalance)
    print("Deposit", deposit)
    assert int(deposit) == int(DepositBalance)
    BalanceAmount = danpheEMR.find_element(By.XPATH, "//td[2]/span").text
    print("BalanceAmount", BalanceAmount)
    # assert int(deposit) == int(BalanceAmount)
    TotalAmount = danpheEMR.find_element(By.XPATH, "//tr[4]/td[2]/input").get_attribute("value")
    print("TotalAmount", TotalAmount)
    assert TotalAmount == SubTotal
    print("subtotal", SubTotal)
    Tender = danpheEMR.find_element(By.XPATH, "//input[@name='Tender']").get_attribute("value")
    print("Tender before deposit deduction: ", Tender)
    assert Tender == TotalAmount
    time.sleep(2)
    paymentMode = Select(danpheEMR.find_element(By.NAME, "pay_mode"))
    paymentMode.select_by_visible_text("Others")
    time.sleep(3)
    # Need to maintain the Display sequence from Setting > Payment Mode Settings make Pos m
    if int(DepositBalance) >= int(TotalAmount):
        dep = danpheEMR.find_element(By.ID, "mode_1")
        # Use Java script executioner click instead of click method.
        danpheEMR.execute_script("arguments[0].click();", dep)
        time.sleep(2)
    else:
        remaining = int(TotalAmount) - int(DepositBalance)
        dep0 = danpheEMR.find_element(By.ID, "mode_0")
        # Use Java script executioner click instead of click method.
        danpheEMR.execute_script("arguments[0].click();", dep0)
        time.sleep(2)
        print("Remaining amount after deducting deposite is :", remaining)
        dep = danpheEMR.find_element(By.ID, "mode_1")
        # Use Java script executioner click instead of click method.
        danpheEMR.execute_script("arguments[0].click();", dep)
        danpheEMR.find_element(By.ID, "input_amount1").send_keys(remaining)
        time.sleep(2)
    danpheEMR.find_element(By.ID, "Add").click()
    danpheEMR.find_element(By.NAME, "Remarks").send_keys("Deducted full from deposite")
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    print("END>>opDepositDbilingTenderCashReturn")
    # danpheEMR.find_element(By.XPATH, "//input[@ng-checked='deductDeposit']").click()  # Click on Deduct from Deposit

    # Tender = danpheEMR.find_element(By.XPATH, "//input[@name='Tender']").get_attribute("value")
    # print("Tender after deposit deduction: ", Tender)
    #
    # DepositDeduction = danpheEMR.find_element(By.XPATH, "//td/table/tbody/tr[2]/td[2]").text
    # print("DepositDeduction", DepositDeduction)
    #
    # if int(DepositBalance) < int(TotalAmount):
    #     assert DepositDeduction == DepositBalance
    #     assert int(Tender) == int(TotalAmount) - int(DepositBalance)
    #
    # else:
    #     assert DepositDeduction == TotalAmount
    #     assert Tender == "0"
    #
    # NewDepositBalance = danpheEMR.find_element(By.XPATH, "//td/table/tbody/tr[3]/td[2]").text
    # assert NewDepositBalance == str(int(DepositBalance) - int(DepositDeduction))
    # print("NewDepositBalance", NewDepositBalance)
    #
    # # if 200 < int(Tender) < 500:
    # if int(Tender) % 100 > 0:
    #     Tender = int(Tender) * 2
    #     danpheEMR.find_element(By.XPATH, "//input[@name='Tender']").clear()
    #     danpheEMR.find_element(By.XPATH, "//input[@name='Tender']").send_keys(Tender)
    #
    # ChangeReturn = danpheEMR.find_element(By.XPATH,
    #     "//td[contains(text(),'Change/Return :')]/following-sibling::td").text
    # print("ChangeReturn", ChangeReturn)
    # ChangeReturn = ChangeReturn.partition("NRs.")[2]
    # print("Change Return:", ChangeReturn)
    # actualChangeReturn = int(ChangeReturn)
    # expectedChangeReturn = int(Tender) + int(DepositBalance) - int(TotalAmount)
    # assert actualChangeReturn == expectedChangeReturn
    #
    # danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    # time.sleep(7)
    # # DepositDeductorReturn = danpheEMR.find_element(By.XPATH, "//div[10]/span").text
    # DepositDeductorReturn = danpheEMR.find_element(By.XPATH,
    #     "//span[contains(text(),' Deposit: [Deducted: ')]").text
    # print("DepositDeductorReturn:", DepositDeductorReturn)
    # DepositDeductorReturn = DepositDeductorReturn.partition("Deducted: ")[2]
    # print("DepositDeductorReturn", DepositDeductorReturn)
    # DepositDeductorReturn = DepositDeductorReturn.partition("/Balance")[0]
    # print("DepositDeductorReturn", DepositDeductorReturn)
    #
    # assert DepositDeductorReturn == DepositDeduction
    # billTender = danpheEMR.find_element(By.XPATH,
    #     "//span[contains(text(),'Tender: ')]").text  # Tender
    # billTender = billTender.partition("r: ")[2]
    # billTender = billTender.partition(".")[0]
    # print("billTender:", billTender)
    # # Tender = int(TotalAmount) - int(DepositDeduction)
    # print("Tender", Tender)
    # assert int(Tender) == int(billTender)
    #
    # if actualChangeReturn >= 1:
    #     eChangeReturn = danpheEMR.find_element(By.XPATH,
    #         "//span[contains(text(),' Change/Return:')]").text  # Change/Return
    #     print("eChangeReturn", eChangeReturn)
    #     eChangeReturn = eChangeReturn.partition("n: ")[2]
    #     print("eChangeReturn", eChangeReturn)
    #     assert eChangeReturn == str(actualChangeReturn)
    #     DepositBalance = danpheEMR.find_element(By.XPATH,
    #         "//span[contains(text(),'Balance:')]").text  # Deposit Balance
    #     print("DepositBalance", DepositBalance)
    #     DepositBalance = DepositBalance.partition("Balance:")[2]
    #     DepositBalance = DepositBalance.partition("]")[0]
    #     print("DepositBalance", DepositBalance)
    #     print("NewDepositBalance", NewDepositBalance)
    #     assert DepositBalance == NewDepositBalance
    # danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)



def createUSGinvoice(danpheEMR, HospitalNo, USGtest):
    print("START>>createUSGinvoice")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(USGtest)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    time.sleep(2)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    totalprice = int(price1)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    print("END>>createUSGinvoice")


# Module:Billing_IP -----------------
def createIPprovisionalBill(danpheEMR, HospitalNo, test):
    global testrate
    print(">>START: Cancel Admitted Provisional bill")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' New Item')]").click()
    danpheEMR.find_element(By.XPATH, "//input[@id='items-box0']").send_keys(test)
    time.sleep(2)
    testrate = int(danpheEMR.find_element(By.XPATH, "//input[@name='price']").get_attribute("value"))
    print("testrate", testrate)
    danpheEMR.find_element(By.XPATH, "//input[@value='Request']").click()
    time.sleep(9)
    print("<<END")


def cancelIPprovisionalBill(danpheEMR, HospitalNo, canceltest):
    print(">>START: Cancel IP Provisional bill")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(Keys.RETURN)
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(canceltest)
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Edit").click()
    danpheEMR.find_element(By.XPATH, "//div/textarea").send_keys("Auto cancel of IP provisional bill items")
    time.sleep(9)
    danpheEMR.find_element(By.XPATH, "//div[3]/button[2]").click()
    time.sleep(3)
    assert danpheEMR.switch_to.alert.text == "This item will be cancelled. Are you sure you want to continue ?"
    time.sleep(3)
    danpheEMR.switch_to.alert.accept()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger history-del-btn' and @title='Cancel']").click()
    time.sleep(3)
    print("End of cancel IP Provisional Bill")


def getIPbillingDetails(danpheEMR, HospitalNo, paymentmode):
    print("Start>>getIPbillingDetails")
    global actualBillingTotal
    global actualNetTotal
    global actualToBePaid
    global actualTender
    global actualChangeReturn
    actualTender = 0
    actualChangeReturn = 0
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(5)
    if paymentmode == "CREDIT":
        paymentoptions = Select(
            #danpheEMR.find_element(By.XPATH, "//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
            danpheEMR.find_element(By.XPATH, "//select[@id='pay_mode']"))
        paymentoptions.select_by_visible_text("Credit")
    actualBillingTotal = danpheEMR.find_element(By.XPATH,
        "//td[contains(.,' Sub Total ')]/following-sibling::td").text
    actualBillingTotal = actualBillingTotal.replace(',', '')
    actualBillingTotal = float(actualBillingTotal)
    print("actualBillingTotal", actualBillingTotal)
    actualNetTotal = danpheEMR.find_element(By.XPATH, "//td[contains(.,'Total Amount')]/following-sibling::td").text
    actualNetTotal = actualNetTotal.replace(',', '')
    actualNetTotal = float(actualNetTotal)
    print("actualNetTotal", actualNetTotal)

    if paymentmode != "CREDIT":
        actualToBePaid = danpheEMR.find_element(By.XPATH,
            "//td[contains(.,'To Be Paid')]/following-sibling::td").text
        actualToBePaid = actualToBePaid.replace(',', '')
        actualToBePaid = float(actualToBePaid)
        print("actualToBePaid", actualToBePaid)
        actualTender = danpheEMR.find_element(By.NAME, "Tender").get_attribute("value")
        actualTender = float(actualTender)
        print("actualTender", actualTender)
        actualChangeReturn = danpheEMR.find_element(By.XPATH,
            "//td[contains(.,'Change/Return :')]/following-sibling::td").text
        actualChangeReturn = float(actualChangeReturn)
        print("actualChangeReturn", actualChangeReturn)
    print("End<<getIPbillingDetails")


def preIPbillingDetails(paymentmode):
    print("START>>preIPbillingDetails")
    global preBillingTotal
    global preNetTotal
    global preToBePaid
    global preTender
    preTender = 0
    global preChangeReturn
    preChangeReturn = 0
    preBillingTotal = actualBillingTotal
    preNetTotal = actualNetTotal
    if paymentmode != "CREDIT":
        preToBePaid = actualToBePaid
    preTender = actualTender
    preChangeReturn = actualChangeReturn
    print("END>>preIPbillingDetails")


def verifyIPbillingDetails(testrate, canceltest, paymentmode):
    print("START>>verifyIPbillingDetails")
    expectedBillingTotal = float(preBillingTotal + testrate - canceltest)
    print("expectedBillingTotal", expectedBillingTotal)
    assert actualBillingTotal == expectedBillingTotal
    expectedNetTotal = preNetTotal + testrate - canceltest
    assert actualNetTotal == expectedNetTotal

    if paymentmode != "CREDIT":
        expectedToBePaid = preToBePaid + testrate - canceltest
        assert actualToBePaid == expectedToBePaid
        expectedTender = preTender + testrate - canceltest
        assert actualTender == expectedTender
        expectedChangeReturn = preChangeReturn
        assert actualChangeReturn == expectedChangeReturn
    print("END>>verifyIPbillingDetails")


def modifyDischargeDate(danpheEMR, HospitalNo):
    print(">>START:modifyDischargeDate")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(5)
    print("END>>modifyDischargeDate")


def verifyConfirmDischarge(danpheEMR, HospitalNo, paymentmode):
    print("START>>verifyConfirmDischarge")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(3)
    if paymentmode == "CREDIT":
        paymentoptions = Select(danpheEMR.find_element(By.XPATH,
            #"//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
            "//select[@id='pay_mode']"))
        paymentoptions.select_by_visible_text("Credit")
        time.sleep(2)
        creditOrganization = Select(danpheEMR.find_element(By.XPATH, "//select[@class='form-control mb-8']"))
        creditOrganization.select_by_visible_text(GSV.creditOrganization)
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//td[contains(text(),'Billing Remarks')]/following-sibling::td/child::textarea").send_keys("This is credit bill")
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Discharge')]").click()
    time.sleep(3)
    if paymentmode == "CREDIT":
        assert danpheEMR.switch_to.alert.text == "Are you sure to discharge this patient on CREDIT?"
        time.sleep(3)
        danpheEMR.switch_to.alert.accept()
        time.sleep(5)
        # danpheEMR.find_element(By.CSS_SELECTOR, ".btn-danger").click()
        # time.sleep(2)
    global tobepaid
    tobepaid = danpheEMR.find_element(By.XPATH, "(//td[text()='To Be Paid :']/following-sibling::td)[1]").text
    print("tobepaid", tobepaid)
    # print("ToBePaid", ToBePaid)
    # assert int(ToBePaid) == int(tobepaid)
    tender = danpheEMR.find_element(By.XPATH, "(//td[text()='Tender']/following-sibling::td)[1]").text
    print("tender:", tender)
    # assert int(Tender) == int(tender)
    change = danpheEMR.find_element(By.XPATH, "(//td[text()='Change']/following-sibling::td)[1]").text
    print("change:", change)
    # assert int(ChangeReturn) == int(change)
    danpheEMR.find_element(By.XPATH, "//textarea[@placeholder='Remarks']").send_keys("Patient discharge")
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@type='button' and text()=' Confirm Discharge ']").click()
    time.sleep(7)
    print("END>>verifyConfirmDischarge")


def verifyDischargeInvoice(danpheEMR, paymentmode):
    time.sleep(3)
    print("START>>verifyDischargeInvoice")
    AMOUNT = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Amount:')]//parent::div").text
    print("AMOUNT", AMOUNT)
    AMOUNT = AMOUNT.partition(": ")[2]
    AMOUNT = AMOUNT.partition(".")[0]
    AMOUNT = AMOUNT.replace(',', '')
    AMOUNT = float(AMOUNT)
    print("AMOUNT", AMOUNT)
    GRANDTOTAL = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Grand Total:')]//parent::div").text
    print("GRANDTOTAL", GRANDTOTAL)
    GRANDTOTAL = GRANDTOTAL.partition(": ")[2]
    GRANDTOTAL = GRANDTOTAL.partition(".")[0]
    GrandTotal = GRANDTOTAL.replace(',', '')
    GrandTotal = float(GrandTotal)
    print("GRANDTOTAL:", GRANDTOTAL)
    if paymentmode == "Cash":
        TOBEPAID = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'To Be Paid:')]//parent::div").text
        print("TOBEPAID:", TOBEPAID)
        TOBEPAID = TOBEPAID.partition(": ")[2]
        TOBEPAID = TOBEPAID.partition(".")[0]
        TOBEPAID = TOBEPAID.replace(',', '')
        print("TOBEPAID:", TOBEPAID)
        ''' # commenting this due to removal of Tender/Change field in IP Invoice.
        tender = danpheEMR.find_element(By.XPATH, 
            "//td/strong[text()='Tender']//parent::td//following-sibling::td").text
        print("tender", tender)
        tender = float(tender)
        assert tender == actualTender
        '''

    element = danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']")
    time.sleep(2)
    danpheEMR.execute_script("arguments[0].click();", element)
    print("End>>verifyDischargeInvoice")


def creditSettlements(danpheEMR, creditOrganization, HospitalNo, ProvisionalSlip, cashdiscount):
    print("Start: creditSettlements")
    if ProvisionalSlip == "Yes":
        danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
        danpheEMR.find_element(By.LINK_TEXT, "Settlements").click()
        time.sleep(2)
        crOrg = Select(danpheEMR.find_element(By.ID, "id_creditOrganization"))
        crOrg.select_by_visible_text(creditOrganization)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Show Details')]").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//i[@title= 'Click to Generate receipt of these items']").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//input[@value = 'Print Invoice']").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'X') and @class='btn btn-danger del-btn']").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
        danpheEMR.find_element(By.LINK_TEXT, "Settlements").click()
        time.sleep(2)
        crOrg = Select(danpheEMR.find_element(By.ID, "id_creditOrganization"))
        crOrg.select_by_visible_text(creditOrganization)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(5)
        danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Show Details')]").click() ## Jira has existing bug: EMR-4898
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//input[@type = 'number']").send_keys(cashdiscount)
        danpheEMR.find_element(By.XPATH, "//input[@value='Proceed']").click()
    time.sleep(4)
    print("End: creditSettlements")


def verifyCreditSettlement(danpheEMR, HospitalNo, itemRate):
    print("START>>verifyCreditSettlement")
    # global returnTotalAmount
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Duplicate Prints')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Settlement Receipts')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Show Details')]").click()
    time.sleep(3)
    netAmount = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'Net Amount:')]/following-sibling::td").text
    netAmount = int(netAmount)
    print("netAmount:", netAmount)
    assert netAmount == itemRate
    print("END>>verifyCreditSettlement")


def generateDischargeInvoice(danpheEMR, creditOrganization, HospitalNo, paymentmode):
    print(">>START: generateDischargeInvoice")
    global InvoiceNo
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(7)
    if paymentmode == "CREDIT":
        paymentoptions = Select(danpheEMR.find_element(By.ID, "pay_mode"))
        paymentoptions.select_by_visible_text("Credit")
        time.sleep(2)
        crOrg = Select(danpheEMR.find_element(By.XPATH, "//select[@class='form-control mb-8']"))
        crOrg.select_by_visible_text(creditOrganization)
        time.sleep(1)
        danpheEMR.find_element(By.XPATH, "//textarea").send_keys("This is credit bill")
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Discharge')]").click()
    if paymentmode == "CREDIT":
        time.sleep(4)
        assert danpheEMR.switch_to.alert.text == "Are you sure to discharge this patient on CREDIT?"
        time.sleep(3)
        danpheEMR.switch_to.alert.accept()
        time.sleep(2)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//textarea[@placeholder='Remarks']").send_keys("Patient discharge")
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@type='button' and text()=' Confirm Discharge ']").click()
    time.sleep(7)
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//span[contains(text(),'2079/2080-')]").text
    print("InvoiceNo:", InvoiceNo)
    #InvoiceNo = InvoiceNo.partition("- ")[2] ## This is not working in RTM
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    time.sleep(2)
    element = danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']")
    time.sleep(2)
    danpheEMR.execute_script("arguments[0].click();", element)
    print("END>>: generateDischargeInvoice")
    return InvoiceNo


def billingIP(danpheEMR, HospitalNo, admitCharge, deposit):
    print("START>>billingIP:")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "IPBilling").click()
    time.sleep(1)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "View Details").click()
    time.sleep(9)
    if deposit >= 1:
        danpheEMR.find_element(By.XPATH, "//button[contains(.,' Add Deposit ')]").click()
        danpheEMR.find_element(By.ID, "txtAmount").send_keys(deposit)
        danpheEMR.find_element(By.ID, "btnAddDeposit").click()
        time.sleep(2)
        danpheEMR.find_element(By.ID, "btn_PrintReceipt").send_keys(Keys.ESCAPE)
    time.sleep(2)
    billingTotalExp = admitCharge
    billingTotalAct = danpheEMR.find_element(By.XPATH, "//td[2]/label").text
    print(billingTotalAct)
    totalDiscountExp = 0  # discount is zero
    totalDiscountAct = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),' Discount Amt.')]/following-sibling::td").text
    print("totalDiscountAct", totalDiscountAct)
    print("totalDiscountExp", totalDiscountExp)
    netTotalExp = int(billingTotalExp) - int(totalDiscountExp)
    netTotalAct = danpheEMR.find_element(By.XPATH, "//tr[5]/td[2]/label").text
    print(netTotalAct)
    depositBalanceExp = int(deposit)
    depositBalanceAct = danpheEMR.find_element(By.XPATH, "//tr[6]/td[2]/label").text
    print("depositBalanceAct", depositBalanceAct)
    depositBalanceAct = depositBalanceAct.replace(',', '')
    print("depositBalanceAct", depositBalanceAct)
    print("depositBalanceExp", depositBalanceExp)
    assert depositBalanceExp == int(depositBalanceAct)
    if depositBalanceExp > netTotalExp:
        toBeRefundExp = depositBalanceExp - netTotalExp
        toBeRefundAct = danpheEMR.find_element(By.CSS_SELECTOR, "tr:nth-child(7) label").text
        print("To be refund:", toBeRefundAct)
    elif depositBalanceExp < netTotalExp:
        toBePaidExp = netTotalExp - depositBalanceExp
        toBePaidAct = danpheEMR.find_element(By.CSS_SELECTOR, "tr:nth-child(7) label").text
        print("To be paid:", toBePaidAct)
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Discharge')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//div[3]/textarea").send_keys("Patient discharging")
    danpheEMR.find_element(By.XPATH, "(//button[@type='button'])[5]").click()
    time.sleep(10)
    element = danpheEMR.find_element(By.XPATH, "//a[@class='btn btn-danger del-btn']")
    time.sleep(2)
    danpheEMR.execute_script("arguments[0].click();", element)
    time.sleep(5)
    print(">>END:billingIP")


def createCreditLabInvoice(danpheEMR, HospitalNo, labtest):
    print("START>>createLabInvoice")
    print("Hospital Number:", HospitalNo)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    time.sleep(5)
    if AppName == 'LPH':
        labType = Select(danpheEMR.find_element(By.ID, "lab_type"))
        labType.select_by_visible_text("OP-LAB")
    time.sleep(4)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(labtest)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "txtQuantity_0").send_keys(1)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    time.sleep(1)
    totalprice = int(price1)
    print("Total Price:", totalprice)
    time.sleep(3)
    paymode = Select(danpheEMR.find_element(By.ID, "pay_mode"))
    paymode.select_by_visible_text("Credit")
    time.sleep(2)
    creditorganization = Select(danpheEMR.find_element(By.XPATH, "//select[@class = 'form-control mb-8']"))
    creditorganization.select_by_visible_text(GSV.creditOrganization)
    time.sleep(1)
    danpheEMR.find_element(By.NAME, "Remarks").send_keys("This is Credit bill on demand of CEO")
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    time.sleep(9)
    # InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    InvoiceNo = InvoiceNo.replace("Invoice No: 2079/2080-BL", "")
    print("InvoiceNo:", InvoiceNo)
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    return InvoiceNo


def verifyReferDoctorinInvoice(danpheEMR, HospitalNo, imagingtest, labtest, ReferDoctor):
    print(">>Start Verifying Refer Doctor in Invoice")
    print("Hospital Number:", HospitalNo)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.implicitly_wait(10)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.ENTER)
    element = WebDriverWait(danpheEMR, 10)
    element.until(
        EC.element_to_be_clickable((By.ID, "btn_billRequest"))
    ).click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "currentRequestedByDoctor").clear()
    danpheEMR.find_element(By.ID, "currentRequestedByDoctor").send_keys(ReferDoctor)

    # danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    wait = WebDriverWait(danpheEMR, 20)
    wait.until(
        EC.element_to_be_clickable((By.ID, "srchbx_ItemName_0"))
    ).click()

    # danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(imagingtest)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    danpheEMR.find_element(By.CSS_SELECTOR, "a > .btn-success").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(labtest)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(Keys.RETURN)
    price = WebDriverWait(danpheEMR, 10)
    price.until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@name='total'])[2]"))
    )
    price2 = danpheEMR.find_element(By.XPATH, "(//input[@name='total'])[2]").get_attribute('value')
    totalprice = int(price1) + int(price2)
    print("Total Price:", totalprice)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    InNo = WebDriverWait(danpheEMR, 10)
    InNo.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Invoice No:')]"))
    )
    # InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    Presciber = danpheEMR.find_element(By.XPATH, "//div[@id='divBilInvoicePrintPage']/div/div[9]/div").text
    Presciber = str(Presciber)
    print(Presciber)
    refer = str('Prescribed By:' + " " + ReferDoctor)
    print(refer)
    assert Presciber == refer
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    print("END: Refered By Doctor Passed")


def createlabxrayinvoiceOtherPayment(danpheEMR, HospitalNo, labtest, imagingtest):
    print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")
    print("Hospital Number:", HospitalNo)
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    danpheEMR.implicitly_wait(10)
    danpheEMR.find_element(By.ID, "srch_PatientList").click()
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.TAB)
    danpheEMR.find_element(By.ID, "srch_PatientList").send_keys(Keys.ENTER)
    element = WebDriverWait(danpheEMR, 10)
    element.until(
        EC.element_to_be_clickable((By.ID, "btn_billRequest"))
    ).click()

    # danpheEMR.find_element(By.XPATH, "//button[@id='btn_billRequest']").click()
    wait = WebDriverWait(danpheEMR, 20)
    wait.until(
        EC.element_to_be_clickable((By.ID, "srchbx_ItemName_0"))
    ).click()

    # danpheEMR.find_element(By.ID, "srchbx_ItemName_0").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(imagingtest)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_0").send_keys(Keys.TAB)
    price1 = danpheEMR.find_element(By.XPATH, "//input[@name='total']").get_attribute('value')
    print("Price of Item 1 is :", price1)
    danpheEMR.find_element(By.CSS_SELECTOR, "a > .btn-success").click()
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(labtest)
    danpheEMR.find_element(By.ID, "srchbx_ItemName_1").send_keys(Keys.RETURN)
    price = WebDriverWait(danpheEMR, 10)
    price.until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@name='total'])[2]"))
    )
    price2 = danpheEMR.find_element(By.XPATH, "(//input[@name='total'])[2]").get_attribute('value')
    print("Price of Item 2 is :", price2)
    totalprice = int(price1) + int(price2)
    print("Total Price:", totalprice)
    time.sleep(2)
    otherPaymentmode = Select(danpheEMR.find_element(By.ID, "pay_mode"))
    otherPaymentmode.select_by_visible_text("Others")
    time.sleep(2)
    danpheEMR.find_element(By.ID, "input_amount0").send_keys(price1)
    danpheEMR.find_element(By.ID, "input_amount1").send_keys(price2)
    danpheEMR.find_element(By.ID, "Add").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@value='Print INVOICE']").click()
    InNo = WebDriverWait(danpheEMR, 10)
    InNo.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Invoice No:')]"))
    )
    # InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]/child::span").text
    InvoiceNo = danpheEMR.find_element(By.XPATH, "//p[contains(text(), 'Invoice No:')]").text
    danpheEMR.find_element(By.ID, "btnPrintRecipt").send_keys(Keys.ESCAPE)
    print("InvoiceNoTemp", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("InvoiceNo", InvoiceNo)
    return totalprice
    print("Create OPD Invoice: 1 Lab + 1 Xray Items: END<<")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return