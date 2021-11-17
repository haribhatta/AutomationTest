import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.LibModuleAppointment as LA
danpheEMR = AC.danpheEMR
AppName = AC.appName

def counteractivation():
    print(">>Activate Billing Counter: START")
    time.sleep(8)
    danpheEMR.find_element_by_link_text("Billing").click()
    time.sleep(15)
    danpheEMR.find_element_by_xpath("(//a[contains(@href, '#/Billing/CounterActivate')])[2]").click()
    danpheEMR.find_element_by_css_selector(".col-md-2:nth-child(1) img").click()
    print("Activate Billing Counter: END<<")

def verifyopdinvoice(deposit, billamt):
    print(">>Verify OPD Invoice Details: START")
    if AppName == "SNCH":
        syscontactno = danpheEMR.find_element_by_xpath("//p[contains(text(),'Contact No:')]").text
        syscontactno = syscontactno.partition("No: ")[2]
        print(syscontactno)
        if deposit < billamt and deposit > 0:
            DepositDeductorReturn = danpheEMR.find_element_by_xpath(
                "//div[@id='printpage']/div/div[5]/div[10]/span").text  # Deposit Deduct/Return:
            DepositDeductorReturn = DepositDeductorReturn.partition("n: ")[2]
            print("1: Deposit Deduct/Return: ", DepositDeductorReturn)
            assert int(DepositDeductorReturn) == deposit
            systender = danpheEMR.find_element_by_xpath(
                "//div[@id='printpage']/div/div[5]/div[10]/span[2]").text  # Tender
            systender = systender.partition("r: ")[2]
            systender = systender.partition(".00")[0]
            Tender = int(billamt) - int(deposit)
            print("Expected Tender: ", Tender)
            print("Actual Tender:", systender)
            assert int(Tender) == int(systender)
            sysdepositbalance = danpheEMR.find_element_by_xpath(
                "//div[@id='printpage']/div/div[5]/div[10]/span[3]").text  # Deposit Balance
            print("3:", sysdepositbalance)
            sysdepositbalance = sysdepositbalance.partition("e: ")[2]
            assert sysdepositbalance == "0"
    print(">>>Verify OPD Invoice. >>End")

def returnBillingInvoice(returnmsg):
    print(">>START: Returning OPD Invoice.", InvoiceNo)
    global returnTotalAmount
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_link_text("Return Bills").click()
        time.sleep(3)
        danpheEMR.find_element_by_name("TransactionId").clear()
        danpheEMR.find_element_by_name("TransactionId").send_keys(InvoiceNo)
        time.sleep(2)
        danpheEMR.find_element_by_css_selector(".fa-search").click()
        time.sleep(9)
        danpheEMR.find_element_by_id("txtRetQty_0").send_keys(1)
        danpheEMR.find_element_by_id("txtReturnRemarks").send_keys(returnmsg)
        danpheEMR.find_element_by_id("btnSubmit").click()
        time.sleep(3)
        returnremark = danpheEMR.find_element_by_xpath("//div[contains(text(), ' Remarks:')]").text
        returnTotalAmount = danpheEMR.find_element_by_xpath(
            "//td[contains(text(),'Total Amount ')]/following-sibling::td").text
        # danpheEMR.find_element_by_id("btnPrintRecipt").click()
        time.sleep(2)
        danpheEMR.find_element_by_xpath(
            "//a[@class='btn btn-danger del-btn']").click()  # This is to close print window.
        time.sleep(3)
        print("returnmsgTemp", returnremark)
        returnremark = returnremark.partition("Remarks: ")[2]
        print("returnremark", returnremark)
        print("returnmsg", returnmsg)
        assert returnremark == returnmsg
        print("returnTotalAmount", returnTotalAmount)
    print("<<END: Return OPD Invoice.")

def returnBillingInvoicePartial(returnmsg):
    print(">>START: Partial Return of billing invoice.", InvoiceNo)
    global returnTotalAmount
    danpheEMR.find_element_by_link_text("Billing").click()
    danpheEMR.find_element_by_link_text("Return Bills").click()
    time.sleep(3)
    danpheEMR.find_element_by_name("TransactionId").clear()
    danpheEMR.find_element_by_name("TransactionId").send_keys(InvoiceNo)
    time.sleep(2)
    danpheEMR.find_element_by_css_selector(".fa-search").click()
    time.sleep(9)
    danpheEMR.find_element_by_id("txtRetQty_0").send_keys(1)
    danpheEMR.find_element_by_id("txtReturnRemarks").send_keys(returnmsg)
    danpheEMR.find_element_by_id("btnSubmit").click()
    time.sleep(3)
    # returnremark = danpheEMR.find_element_by_xpath("//div[contains(text(), ' Remarks:')]").text
    # returnTotalAmount = danpheEMR.find_element_by_xpath("//td[contains(text(),'Total Amount ')]/following-sibling::td").text
    # danpheEMR.find_element_by_id("btnPrintRecipt").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath(
        "//a[@class='btn btn-danger del-btn']").click()  # This is to close print window.

def verifyCreditNoteDuplicateInvoice():
    print("Verify partial return of bill invoice")
    # global returnTotalAmount
    danpheEMR.find_element_by_link_text("Billing").click()
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Duplicate Prints')]").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Returned Invoice')]").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(InvoiceNo)
    time.sleep(5)
    RefInvoiceNumber = danpheEMR.find_element_by_xpath("(//div[@col-id='RefInvoiceNum'])[2]").text
    print("RefInvoiceNumber", RefInvoiceNumber)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Show Details')]").click()
    time.sleep(3)
    ReturnAmount = danpheEMR.find_element_by_xpath(
        "//td[contains(text(),'Total Amount')]/following-sibling::td").text
    print("ReturnAmount", ReturnAmount)
    danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']").click()
    time.sleep(2)

def creditPayment(HospitalNo):
    print(">>START: Credit Payment")
    danpheEMR.find_element_by_link_text("Billing").click()
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Settlements").click()
    time.sleep(2)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element_by_link_text("Show Details").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//input[@value='Proceed']").click()

def createlabxrayinvoice(HospitalNo, labtest, imagingtest):
    print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")
    global InvoiceNo
    print("Hospital Number:", HospitalNo)
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(5)
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
        time.sleep(5)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").click()
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(imagingtest)
        time.sleep(1)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(Keys.TAB)
        time.sleep(1)
        price1 = danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
        time.sleep(1)
        danpheEMR.find_element_by_css_selector("a > .btn-success").click()
        time.sleep(1)
        danpheEMR.find_element_by_id("srchbx_ItemName_1").send_keys(labtest)
        time.sleep(1)
        danpheEMR.find_element_by_id("srchbx_ItemName_1").send_keys(Keys.RETURN)
        time.sleep(2)
        price2 = danpheEMR.find_element_by_xpath("(//input[@name='total'])[2]").get_attribute('value')
        totalprice = int(price1) + int(price2)
        print("Total Price:", totalprice)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
        time.sleep(9)
        # InvoiceNo = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]/child::span").text
        InvoiceNo = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]").text
        danpheEMR.find_element_by_id("btnPrintRecipt").send_keys(Keys.ESCAPE)

        print("InvoiceNoTemp", InvoiceNo)
        InvoiceNo = InvoiceNo.partition("BL")[2]
        print("InvoiceNo", InvoiceNo)

    print("Create OPD Invoice: 1 Lab + 1 Xray Items: END<<")


def createERlabInvoice(HospitalNo, labtest, labtype):
    print(">>Create ER LAB Invoice: START")
    global InvoiceNo
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(5)
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
        time.sleep(5)
        danpheEMR.find_element_by_id("lab_type").send_keys(labtype)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").click()
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(labtest)
        time.sleep(1)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(Keys.TAB)
        time.sleep(1)
        price1 = danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
        time.sleep(1)
        danpheEMR.find_element_by_css_selector("a > .btn-success").click()
        danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
        time.sleep(9)
        InvoiceNo = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]").text
        danpheEMR.find_element_by_id("btnPrintRecipt").send_keys(Keys.ESCAPE)
        print("InvoiceNoTemp", InvoiceNo)
        InvoiceNo = InvoiceNo.partition("BL")[2]
        print("InvoiceNo", InvoiceNo)
    print("Create ER LAB Invoice: 1 Lab: END<<")


def verifylabxrayinvoice():
    # if appPort == "81":
    #    print(">>Verify OPD Invoice: 1 Lab + 1 Xray Items: START")
    #    invoiceNo = danpheEMR.find_element_by_css_selector(".no-margin:nth-child(1) > span").text
    #    hospitalNoT = danpheEMR.find_element_by_css_selector("span > strong").text
    #    assert HospitalNo == hospitalNoT
    if AppName == "SNCH":
        print(">>Verify OPD Invoice: 1 Lab + 1 Xray Items: START")
        # InvoiceNoTemp = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]").text
        # hospitalNoTemp = danpheEMR.find_element_by_css_selector("span > strong").text
        # assert HospitalNo == hospitalNoT
    # print("Verify OPD Invoice: 1 Lab + 1 Xray Items: END<<", "HospitalNo", hospitalNoT, "InvoiceNo", invoiceNo)


def verifySampleCollectionDuplicateEntry():
    if AppName == "SNCH":
        print("Start: verifySampleCollectionDuplicateEntry")


def createProvisionalBill(HospitalNo, usgtest):
    print(">>START: Create USG Provisional bill")
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").click()
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(usgtest)
        time.sleep(1)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[contains(text(),' Print Provisional Slip ')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("btnPrintProvisionalSlip").send_keys(Keys.ESCAPE)
        time.sleep(2)

    print("<<END")

def verifyDuplicateBill(HospitalNo):
    if AppName == "SNCH":
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//a[contains(text(),'Duplicate Prints ')]").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        # danpheEMR.find_element_by_link_text("Show Details").click()
        danpheEMR.find_element_by_xpath("(//a[contains(text(),'Show Details')])[1]").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)
        time.sleep(3)


def createCopyItemInvoice(paymentmode):
    print(">>START: CreateCopyItemInvoice")
    global InvoiceNo
    danpheEMR.find_element_by_xpath("//button[contains(.,'Create Copy Of Items ')]").click()
    time.sleep(3)
    if paymentmode == 'CREDIT':
        danpheEMR.find_element_by_id("pay_mode").send_keys('CREDIT')
        danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("Credit in request of chairman")
        time.sleep(5)
    danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
    time.sleep(13)
    InvoiceNo = danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]/child::span").text
    print("NewInvoiceNo", InvoiceNo)
    InvoiceNo = InvoiceNo.partition("BL")[2]
    print("NewInvoiceNo", InvoiceNo)
    CopyItemTotalAmount = danpheEMR.find_element_by_xpath(
        "//td[contains(text(),'Total Amount ')]/following-sibling::td").text
    print("CopyItemTotalAmount:", CopyItemTotalAmount)
    print("returnTotalAmount", returnTotalAmount)
    assert CopyItemTotalAmount == returnTotalAmount  # LPH-865 : LPH_V1.9.0
    print("<<END: CreateCopyItemInvoice")

def getBillingDashboard():
    print(">>START: getBillingDashboard")
    global sysgrosstotal
    global syssubtotal
    global sysdiscountamount
    global sysreturnamount
    global systotalamount
    global sysnetcashcollection
    global sysprovisionalitems
    global sysunpaidcreditinvoices

    time.sleep(8)
    danpheEMR.find_element_by_link_text("Billing").click()
    time.sleep(7)
    danpheEMR.find_element_by_css_selector(".fa-home").click()
    time.sleep(9)

    if AppName == "SNCH":
        sysgrosstotal = danpheEMR.find_element_by_xpath("//div[contains(text(),'i. Subtotal :')]").text
        print("sysgrosstotal:", sysgrosstotal)
        syssubtotal = sysgrosstotal.partition("Subtotal : ")[2]
        print("System subTotal-1:", syssubtotal)
        syssubtotal = syssubtotal.partition("\nii")[0]
        sysdiscountamount = sysgrosstotal.partition("ii. Discount Amount : ")[2]
        print(sysdiscountamount)
        sysdiscountamount = sysdiscountamount.partition(".")[0]
        sysdiscountamount = sysdiscountamount.replace(',', '')
        print("System discountAmount:", sysdiscountamount)

        sysreturnamount = danpheEMR.find_element_by_css_selector("#totalsales > div:nth-child(4)").text
        print("sysreturnamount:", sysreturnamount)
        print("sysreturnamount:", sysreturnamount)
        sysreturnamount = sysreturnamount.partition(" : ")[2]
        # sysreturnamount = sysreturnamount.partition(".")[0]
        # sysreturnamount = sysreturnamount.replace(',', '')
        print("System returnAmount:", sysreturnamount)

        systotalamount = danpheEMR.find_element_by_xpath("//div[@id='totalsales']/div[5]/b").text
        print(systotalamount)
        systotalamount = systotalamount.partition(": NRs. ")[2]
        # systotalamount = systotalamount.partition(".")[0]
        print("System totalAmount:", systotalamount)
        # systotalamount = systotalamount.replace(',', '')
        print("System totalAmount:", systotalamount)

        sysnetcashcollection = danpheEMR.find_element_by_css_selector(".blinkAmount").text
        sysnetcashcollection = sysnetcashcollection.partition("(")[2]
        sysnetcashcollection = sysnetcashcollection.partition(")")[0]
        sysnetcashcollection = sysnetcashcollection.replace(',', '')
        print("System NetCashCollection:", sysnetcashcollection)

        sysprovisionalitems = danpheEMR.find_element_by_xpath(
            "//td[contains(text(),'PROVISIONAL ITEMS')]/following-sibling::td").text
        sysprovisionalitems = sysprovisionalitems.partition("NRs. ")[2]
        sysprovisionalitems = sysprovisionalitems.partition(".")[0]
        sysprovisionalitems = sysprovisionalitems.replace(',', '')
        print("System Provisional Item:", sysprovisionalitems)

        sysunpaidcreditinvoices = danpheEMR.find_element_by_xpath(
            "//td[contains(text(),'UNPAID CREDIT INVOICES')]/following-sibling::td").text
        sysunpaidcreditinvoices = sysunpaidcreditinvoices.partition("NRs. ")[2]
        sysunpaidcreditinvoices = sysunpaidcreditinvoices.partition(".")[0]
        sysunpaidcreditinvoices = sysunpaidcreditinvoices.replace(',', '')
        print("System Unpaid Credit Invoice:", sysunpaidcreditinvoices)
    print(">>End: getBillingDashboard")
    print("syssubtotal", syssubtotal)

def preSystemDataBillingDashboard():
    print(">>START: preSystemDataBillingDashboard")
    global presyssubtotal
    global presysdiscountamount
    global presysreturnamount
    global presystotalamount
    global presysnetcashcollection
    global presysprovisionalitems
    global presysunpaidcreditinvoices

    presyssubtotal = float(syssubtotal)
    presyssubtotal = int(syssubtotal)
    print("presyssubtotal", presyssubtotal)
    presysdiscountamount = float(sysdiscountamount)
    print("presysdiscountamount", presysdiscountamount)
    presysreturnamount = float(sysreturnamount)
    print("presysreturnamount", presysreturnamount)
    presystotalamount = float(systotalamount)
    print("presystotalamount", presystotalamount)
    presysnetcashcollection = float(sysnetcashcollection)
    print("presysnetcashcollection", presysnetcashcollection)
    presysprovisionalitems = float(sysprovisionalitems)
    print("presysprovisionalitems", presysprovisionalitems)
    presysunpaidcreditinvoices = float(sysunpaidcreditinvoices)
    print("presysunpaidcreditinvoices", presysunpaidcreditinvoices)
    print("<<END:")


def verifyBillingDashboard(cash, discountpc, cashReturn, credit, creditReturn, settlement, provisional,
                           provisionalcancel):
    print(">>START: Verify Billing Dashboard new updated amounts")

    # 1. Cash Invoice (Check subTotal & totalAmount is increased in Total Sales area).
    if cash > 0 and cashReturn == 0 and discountpc == 0 and credit == 0 and creditReturn == 0:
        expectedsubtotal = presyssubtotal + cash
        print("expectedsubtotal", expectedsubtotal)
        print("syssubtotal", syssubtotal)
        assert float(syssubtotal) == expectedsubtotal
        assert float(systotalamount) == presystotalamount + cash
        assert float(sysnetcashcollection) == presysnetcashcollection + cash

    # 2. Return Cash Invoice (Check ReturnAmount is increased and TotalAmount is decreased on returning opd cash invoice).
    elif cash == 0 and cashReturn > 0 and discountpc == 0 and credit == 0 and creditReturn == 0:
        time.sleep(3)
        print("syssubtotal", syssubtotal)
        print("presyssubtotal", presyssubtotal)
        assert int(syssubtotal) == int(presyssubtotal)  # LPH-864: Prio-1 bug in LPH_V1.9.0
        tempresult = presysreturnamount + cashReturn
        print("tempresult", tempresult)
        print("sysreturnamount", sysreturnamount)
        print("presysreturnamount", presysreturnamount)
        assert float(sysreturnamount) == presysreturnamount + cashReturn
        assert float(systotalamount) == presystotalamount - cashReturn
        assert float(sysnetcashcollection) == presysnetcashcollection - cashReturn

    # 3. Cash Discount Invoice (Check Billing Dashboard for discount in OPD cash sale invoice).
    elif cash > 0 and cashReturn == 0 and discountpc > 0 and credit == 0 and creditReturn == 0:
        time.sleep(3)
        assert int(syssubtotal) == presyssubtotal + cash
        calctemp = presysdiscountamount + (discountpc * cash / 100)
        print("calctemp", calctemp)
        print("sysdiscountamount", sysdiscountamount)
        assert float(sysdiscountamount) == calctemp
        assert float(sysreturnamount) == presysreturnamount
        assert float(systotalamount) == presystotalamount + cash - (discountpc * cash / 100)
        assert float(sysnetcashcollection) == presysnetcashcollection + cash - (discountpc * cash / 100)

    # 4. Return Cash Discount Invoice (Check Billing Dashboard for return of discounted OPD cash sale invoice).
    elif cash == 0 and cashReturn > 0 and discountpc > 0 and credit == 0 and creditReturn == 0:
        assert int(syssubtotal) == presyssubtotal
        assert int(sysdiscountamount) == presysdiscountamount
        print("sysreturnamount", sysreturnamount)
        print("presysreturnamount", presysreturnamount)
        print("cashReturn*discountpc", cashReturn * discountpc)
        assert int(sysreturnamount) == presysreturnamount + (cashReturn * (100 - discountpc) / 100)
        assert int(systotalamount) == presystotalamount - (cashReturn * (100 - discountpc) / 100)
        assert int(sysnetcashcollection) == presysnetcashcollection - (cashReturn * (100 - discountpc) / 100)

    # 5. Credit Invoice
    elif cash == 0 and cashReturn == 0 and discountpc == 0 and credit > 0 and creditReturn == 0:
        time.sleep(7)
        # if appPort == '81':
        #    assert int(syssubtotal) == presyssubtotal + credit
        #    assert int(sysdiscountamount) == presysdiscountamount
        #    assert int(sysreturnamount) == presysreturnamount
        #    assert int(systotalamount) == presystotalamount + credit
        #    print("presysnetcashcollection", presysnetcashcollection)
        #    print("sysnetcashcollection", sysnetcashcollection)
        #    assert int(sysnetcashcollection) == presysnetcashcollection
        #    print("End of credit invoice check")
        if AppName == "SNCH":
            assert int(syssubtotal) == presyssubtotal + credit
            assert int(sysdiscountamount) == presysdiscountamount
            assert int(sysreturnamount) == presysreturnamount
            assert int(systotalamount) == presystotalamount + credit
            print("presysnetcashcollection", presysnetcashcollection)
            print("sysnetcashcollection", sysnetcashcollection)
            assert int(sysnetcashcollection) == presysnetcashcollection
            print("End of credit invoice check")

    # 6. Return Credit Invoice (Check ReturnAmount is increased and TotalAmount is decreased on returning opd cash invoice).
    elif cash == 0 and cashReturn == 0 and discountpc == 0 and credit == 0 and creditReturn > 0:
        time.sleep(3)
        print(syssubtotal)
        print(presyssubtotal)
        assert int(syssubtotal) == presyssubtotal
        print("sysreturnamount", sysreturnamount)
        print("presysreturnamount", presysreturnamount)
        print("creditReturn", creditReturn)
        assert int(sysreturnamount) == presysreturnamount + creditReturn
        assert int(systotalamount) == presystotalamount - creditReturn
        assert int(sysnetcashcollection) == presysnetcashcollection

    # 7. Credit Payment/Settlement
    elif credit > 0 and settlement == "CREDIT":
        assert int(sysnetcashcollection) == presysnetcashcollection + credit

    # 8. Provisional bill
    elif cash == 0 and credit == 0 and discountpc == 0 and cashReturn == 0 and provisional > 0:
        print("presysprovisionalitems:", presysprovisionalitems)
        print("provisional:", provisional)
        print(float(sysprovisionalitems))
        testvalu = presysprovisionalitems + provisional
        print(testvalu)
        # assert float(sysprovisionalitems) == presysprovisionalitems + provisional

    # 9. Cancel Provisional bill
    elif cash == 0 and credit == 0 and provisional == 0 and provisionalcancel > 0:
        print(presysprovisionalitems)


# Module:Billing_OP -----------------
def opDeposit(HospitalNo, amount):
    print(">>>opDeposit>>Start")
    if AppName == "SNCH":
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(5)
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_id("btn_addDeposit").click()
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//input[@name='amount']").send_keys(amount)
        danpheEMR.find_element_by_xpath("//input[@value='Add Deposit and Print']").click()
        time.sleep(3)
    print(">>>opDeposit>>End")

def opDepositDbiling(HospitalNo, deposit, testname):
    print("lets issue OPD invoice deducting amount from deposit.")
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").click()
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(testname)
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(Keys.TAB)
        itemAprice = danpheEMR.find_element_by_xpath("//input[@name='price']").get_attribute("value")
        SubTotal = itemAprice
        DepositBalance = danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
        assert deposit == int(DepositBalance)
        BalanceAmount = danpheEMR.find_element_by_xpath("//td[2]/span").text
        assert deposit == int(BalanceAmount)
        TotalAmount = danpheEMR.find_element_by_xpath("//tr[4]/td[2]/input").get_attribute("value")
        print("TotalAmount", TotalAmount)
        assert TotalAmount == SubTotal
        Tender = danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
        print("Tender before deposit deduction: ", Tender)
        assert Tender == TotalAmount
        danpheEMR.find_element_by_xpath(
            "//input[@ng-checked='deductDeposit']").click()  # Click on Deduct from Deposit
        Tender = danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
        print("Tender after deposit deduction: ", Tender)

        if int(DepositBalance) >= int(TotalAmount):
            assert Tender == "0"

        else:
            assert int(Tender) == int(TotalAmount) - int(DepositBalance)

        DepositDeduction = danpheEMR.find_element_by_xpath("//td/table/tbody/tr[2]/td[2]").text
        print("DepositDeduction:", DepositDeduction)

        if int(DepositBalance) < int(TotalAmount):
            assert DepositDeduction == DepositBalance

        else:
            assert DepositDeduction == TotalAmount

        NewDepositBalance = danpheEMR.find_element_by_xpath("//td/table/tbody/tr[3]/td[2]").text
        assert NewDepositBalance == str(int(DepositBalance) - int(DepositDeduction))
        print("NewDepositBalance:", NewDepositBalance)

        danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
        time.sleep(9)
        danpheEMR.find_element_by_id("btnPrintRecipt").send_keys(Keys.ESCAPE)
        time.sleep(3)

def opDepositDbilingTenderCashReturn(HospitalNo, deposit, testname):
    global ChangeReturn
    print(">>>opDepositDbilingTenderCashReturn>>Start")
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").click()
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(testname)
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(Keys.TAB)
        itemAprice = danpheEMR.find_element_by_xpath("//input[@name='price']").get_attribute("value")
        SubTotal = itemAprice
        DepositBalance = danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
        print("DepositBalance", DepositBalance)
        print("Deposit", deposit)
        assert int(deposit) == int(DepositBalance)
        BalanceAmount = danpheEMR.find_element_by_xpath("//td[2]/span").text
        print("BalanceAmount", BalanceAmount)
        assert int(deposit) == int(BalanceAmount)
        TotalAmount = danpheEMR.find_element_by_xpath("//tr[4]/td[2]/input").get_attribute("value")
        print("TotalAmount", TotalAmount)
        assert TotalAmount == SubTotal
        print("subtotal", SubTotal)
        Tender = danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
        print("Tender before deposit deduction: ", Tender)
        assert Tender == TotalAmount

        danpheEMR.find_element_by_xpath(
            "//input[@ng-checked='deductDeposit']").click()  # Click on Deduct from Deposit

        Tender = danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
        print("Tender after deposit deduction: ", Tender)

        DepositDeduction = danpheEMR.find_element_by_xpath("//td/table/tbody/tr[2]/td[2]").text
        print("DepositDeduction", DepositDeduction)

        if int(DepositBalance) < int(TotalAmount):
            assert DepositDeduction == DepositBalance
            assert int(Tender) == int(TotalAmount) - int(DepositBalance)

        else:
            assert DepositDeduction == TotalAmount
            assert Tender == "0"

        NewDepositBalance = danpheEMR.find_element_by_xpath("//td/table/tbody/tr[3]/td[2]").text
        assert NewDepositBalance == str(int(DepositBalance) - int(DepositDeduction))
        print("NewDepositBalance", NewDepositBalance)

        # if 200 < int(Tender) < 500:
        if int(Tender) % 100 > 0:
            Tender = int(Tender) * 2
            danpheEMR.find_element_by_xpath("//input[@name='Tender']").clear()
            danpheEMR.find_element_by_xpath("//input[@name='Tender']").send_keys(Tender)

        ChangeReturn = danpheEMR.find_element_by_xpath(
            "//td[contains(text(),'Change/Return :')]/following-sibling::td").text
        print("ChangeReturn", ChangeReturn)
        ChangeReturn = ChangeReturn.partition("NRs.")[2]
        print("Change Return:", ChangeReturn)
        ChangeReturn = int(ChangeReturn)
        assert ChangeReturn == int(Tender) + int(DepositBalance) - int(TotalAmount)

        danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
        time.sleep(7)
        # DepositDeductorReturn = danpheEMR.find_element_by_xpath("//div[10]/span").text
        DepositDeductorReturn = danpheEMR.find_element_by_xpath(
            "//span[contains(text(),' Deposit: [Deducted: ')]").text
        print("DepositDeductorReturn:", DepositDeductorReturn)
        DepositDeductorReturn = DepositDeductorReturn.partition("Deducted: ")[2]
        print("DepositDeductorReturn", DepositDeductorReturn)
        DepositDeductorReturn = DepositDeductorReturn.partition("/Balance")[0]
        print("DepositDeductorReturn", DepositDeductorReturn)

        assert DepositDeductorReturn == DepositDeduction
        billTender = danpheEMR.find_element_by_xpath(
            "//span[contains(text(),'Tender: ')]").text  # Tender
        billTender = billTender.partition("r: ")[2]
        billTender = billTender.partition(".")[0]
        print("billTender:", billTender)
        # Tender = int(TotalAmount) - int(DepositDeduction)
        print("Tender", Tender)
        assert int(Tender) == int(billTender)

        if ChangeReturn >= 1:
            eChangeReturn = danpheEMR.find_element_by_xpath(
                "//span[contains(text(),' Change/Return:')]").text  # Change/Return
            print("eChangeReturn", eChangeReturn)
            eChangeReturn = eChangeReturn.partition("n: ")[2]
            print("eChangeReturn", eChangeReturn)
            print("ChangeReturn", ChangeReturn)
            assert eChangeReturn == str(ChangeReturn)
            DepositBalance = danpheEMR.find_element_by_xpath(
                "//span[contains(text(),'Balance:')]").text  # Deposit Balance
            print("DepositBalance", DepositBalance)
            DepositBalance = DepositBalance.partition("Balance:")[2]
            DepositBalance = DepositBalance.partition("]")[0]
            print("DepositBalance", DepositBalance)
            print("NewDepositBalance", NewDepositBalance)
            assert DepositBalance == NewDepositBalance
        danpheEMR.find_element_by_id("btnPrintRecipt").send_keys(Keys.ESCAPE)
    print(">>>opDepositDbilingTenderCashReturn>>End")

def createUSGinvoice(HospitalNo, USGtest):
    print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_id("srch_PatientList").click()
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").click()
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(USGtest)
        time.sleep(2)
        danpheEMR.find_element_by_id("srchbx_ItemName_0").send_keys(Keys.TAB)
        time.sleep(2)
        price1 = danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
        totalprice = int(price1)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("btnPrintRecipt").send_keys(Keys.ESCAPE)

    print("Create OPD Invoice: USG Items: END<<")

# Module:Billing_IP -----------------
def createIPprovisionalBill(HospitalNo, test):
    global testrate
    print(">>START: Cancel Admitted Provisional bill")
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_link_text("IPBilling").click()
        danpheEMR.find_element_by_id("quickFilterInput").click()
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
        time.sleep(3)
        danpheEMR.find_element_by_link_text("View Details").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//button[contains(.,' New Item')]").click()
        danpheEMR.find_element_by_xpath("//input[@id='items-box0']").send_keys(test)
        time.sleep(2)
        testrate = int(danpheEMR.find_element_by_xpath("//input[@name='price']").get_attribute("value"))
        print("testrate", testrate)
        danpheEMR.find_element_by_xpath("//input[@value='Request']").click()
        time.sleep(9)
    print("<<END")

def cancelIPprovisionalBill(HospitalNo, canceltest):
    print(">>START: Cancel IP Provisional bill")
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        danpheEMR.find_element_by_link_text("IPBilling").click()
        danpheEMR.find_element_by_id("quickFilterInput").click()
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
        time.sleep(2)
        danpheEMR.find_element_by_link_text("View Details").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(canceltest)
        time.sleep(2)
        danpheEMR.find_element_by_link_text("Edit").click()
        danpheEMR.find_element_by_xpath("//div/textarea").send_keys("Auto cancel of IP provisional bill items")
        time.sleep(9)
        danpheEMR.find_element_by_xpath("//div[3]/button[2]").click()
        time.sleep(3)
        assert danpheEMR.switch_to.alert.text == "This item will be cancelled. Are you sure you want to continue ?"
        time.sleep(3)
        danpheEMR.switch_to.alert.accept()
        time.sleep(2)
        danpheEMR.find_element_by_css_selector(".fa-times").click()
    print("End of cancel IP Provisional Bill")

def getIPbillingDetails(HospitalNo, paymentmode):
    print("Start>>getIPbillingDetails")
    global BillingTotal
    global NetTotal
    global ToBePaid
    global Tender
    Tender = 0
    global ChangeReturn
    ChangeReturn = 0
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("IPBilling").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(5)
        danpheEMR.find_element_by_link_text("View Details").click()
        time.sleep(5)
        if paymentmode == "CREDIT":
            paymentoptions = Select(danpheEMR.find_element_by_xpath(
                "//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
            paymentoptions.select_by_visible_text("CREDIT")
        BillingTotal = danpheEMR.find_element_by_xpath(
            "//td[contains(.,' Sub Total ')]/following-sibling::td").text
        print("BillingTotal", BillingTotal)
        NetTotal = danpheEMR.find_element_by_xpath("//td[contains(.,'Total Amount')]/following-sibling::td").text
        print("NetTotal", NetTotal)
        ToBePaid = danpheEMR.find_element_by_xpath("//td[contains(.,'To Be Paid')]/following-sibling::td").text
        print("ToBePaid", ToBePaid)
        if paymentmode != "CREDIT":
            Tender = danpheEMR.find_element_by_name("Tender").get_attribute("value")
            print("Tender1", Tender)
            ChangeReturn = danpheEMR.find_element_by_xpath(
                "//td[contains(.,'Change/Return :')]/following-sibling::td").text
            print("ChangeReturn", ChangeReturn)
    print("End<<getIPbillingDetails")

def preIPbillingDetails():
    global xBillingTotal
    global xNetTotal
    global xToBePaid
    global xTender
    xTender = 0
    global xChangeReturn
    xChangeReturn = 0
    xBillingTotal = int(BillingTotal)
    xNetTotal = int(NetTotal)
    xToBePaid = int(ToBePaid)
    xTender = int(Tender)
    xChangeReturn = int(ChangeReturn)

def verifyIPbillingDetails(testrate, canceltest, paymentmode):
    x = BillingTotal.replace(',', '')
    x = int(x)
    print("x", x)
    print("xBillingTotal", xBillingTotal)
    print("testrate", testrate)
    print("canceltest", canceltest)
    y = int(xBillingTotal + testrate - canceltest)
    print("y", y)
    assert x == y
    assert int(NetTotal) == xNetTotal + testrate - canceltest
    assert int(ToBePaid) == xToBePaid + testrate - canceltest
    if paymentmode != "CREDIT":
        assert int(Tender) == xTender + testrate - canceltest
        assert int(ChangeReturn) == xChangeReturn

def modifyDischargeDate(HospitalNo):
    danpheEMR.find_element_by_link_text("Billing").click()
    time.sleep(3)
    danpheEMR.find_element_by_link_text("IPBilling").click()
    time.sleep(3)
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element_by_link_text("View Details").click()
    time.sleep(5)

def verifyConfirmDischarge(HospitalNo, paymentmode):
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(3)
        danpheEMR.find_element_by_link_text("IPBilling").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element_by_link_text("View Details").click()
        time.sleep(3)
        if paymentmode == "CREDIT":
            paymentoptions = Select(danpheEMR.find_element_by_xpath(
                "//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
            paymentoptions.select_by_visible_text("CREDIT")
            danpheEMR.find_element_by_xpath("//textarea").send_keys("This is credit bill")
        danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
        time.sleep(3)
        if paymentmode == "CREDIT":
            assert danpheEMR.switch_to.alert.text == "Are you sure to discharge this patient on CREDIT?"
            time.sleep(3)
            danpheEMR.switch_to.alert.accept()
            time.sleep(3)
            danpheEMR.find_element_by_css_selector(".btn-danger").click()
            time.sleep(2)
        tobepaid = danpheEMR.find_element_by_xpath("(//td[text()='To Be Paid :']/following-sibling::td)[1]").text
        print("tobepaid", tobepaid)
        print("ToBePaid", ToBePaid)
        assert int(ToBePaid) == int(tobepaid)
        tender = danpheEMR.find_element_by_xpath("(//td[text()='Tender']/following-sibling::td)[1]").text
        assert int(Tender) == int(tender)
        change = danpheEMR.find_element_by_xpath("(//td[text()='Change']/following-sibling::td)[1]").text
        assert int(ChangeReturn) == int(change)
        danpheEMR.find_element_by_xpath("//textarea[@placeholder='Remarks']").send_keys("Patient discharge")
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@type='button' and text()=' Confirm Discharge ']").click()
        time.sleep(7)

def verifyDischargeInvoice(paymentmode):
    time.sleep(3)
    print("Start>>verifyDischargeInvoice")
    if AppName == "SNCH":
        AMOUNT = danpheEMR.find_element_by_xpath("//span[contains(text(),'Amount:')]//parent::div").text
        print("GrandTotal", AMOUNT)
        Amount1 = AMOUNT.partition(": ")[2]
        # grosstotal = grosstotal.replace(',', '')
        print("Amount1", Amount1)
        # randTotal2 = GrandTotal.partition("TOTAL: ")[0]
        print("BillingTotal:", BillingTotal)
        x = int(BillingTotal)
        print("x", x)
        Amount = Amount1.partition(".")[0]
        print("Amount", Amount1)
        y = int(Amount)
        print("y", y)
        assert x == y
        GRANDTOTAL = danpheEMR.find_element_by_xpath("//span[contains(text(),'Grand Total:')]//parent::div").text
        print("GRANDTOTAL", GRANDTOTAL)
        GrandTotal1 = GRANDTOTAL.partition(": ")[2]
        print("GrandTotal1", GrandTotal1)
        GrandTotal = GrandTotal1.partition(".")[0]
        x = int(GrandTotal)
        print("x", x)
        y = int(NetTotal)
        assert y == x
        if paymentmode == "Cash":
            TOBEPAID = danpheEMR.find_element_by_xpath("//span[contains(text(),'To Be Paid:')]//parent::div").text
            ToBePaid = TOBEPAID.partition(": ")[2]
            paidamount = ToBePaid.partition(".")[0]
            x = int(paidamount)
            print("paidamount", x)
            y = int(ToBePaid)
            print("y", y)
            assert x == y
            tender = danpheEMR.find_element_by_xpath(
                "//td/strong[text()='Tender']//parent::td//following-sibling::td").text
            print("tender", tender)
            assert int(Tender) == int(tender)
        else:
            amounttobepaid = danpheEMR.find_element_by_xpath(
                "//td/strong[text()='Amount to be Paid ']//parent::td//following-sibling::td").text
            amounttobepaid = amounttobepaid.partition(".")[0]
            amounttobepaid = amounttobepaid.replace(',', '')
            print("amounttobepaid", amounttobepaid)
            assert int(amounttobepaid) == int(ToBePaid)
        element = danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
        time.sleep(2)
        danpheEMR.execute_script("arguments[0].click();", element)
    print("End>>verifyDischargeInvoice")

def creditSettlements(HospitalNo):
    print("Start: creditSettlements")
    danpheEMR.find_element_by_link_text("Billing").click()
    danpheEMR.find_element_by_link_text("Settlements").click()
    danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element_by_xpath("//a[contains(text(),'Show Details')]").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//input[@value='Proceed']").click()
    print("End: creditSettlements")

def generateDischargeInvoice(HospitalNo, paymentmode):
    print("Start: generateDischargeInvoice")
    global InvoiceNo
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Billing").click()
        time.sleep(2)
        danpheEMR.find_element_by_link_text("IPBilling").click()
        time.sleep(2)
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element_by_link_text("View Details").click()
        time.sleep(7)
        if paymentmode == "CREDIT":
            paymentoptions = Select(danpheEMR.find_element_by_xpath(
                "//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
            paymentoptions.select_by_visible_text("CREDIT")
            danpheEMR.find_element_by_xpath("//textarea").send_keys("This is credit bill")
        danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
        if paymentmode == "CREDIT":
            time.sleep(4)
            assert danpheEMR.switch_to.alert.text == "Are you sure to discharge this patient on CREDIT?"
            time.sleep(3)
            danpheEMR.switch_to.alert.accept()
            time.sleep(2)
        time.sleep(3)
        danpheEMR.find_element_by_xpath("//textarea[@placeholder='Remarks']").send_keys("Patient discharge")
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//button[@type='button' and text()=' Confirm Discharge ']").click()
        time.sleep(7)
        InvoiceNo = danpheEMR.find_element_by_xpath("//span[contains(text(),'2078/2079-')]").text
        InvoiceNo = InvoiceNo.partition("- ")[2]
        print("InvoiceNo", InvoiceNo)
        time.sleep(2)
        element = danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
        time.sleep(2)
        danpheEMR.execute_script("arguments[0].click();", element)
    print("End: generateDischargeInvoice")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

