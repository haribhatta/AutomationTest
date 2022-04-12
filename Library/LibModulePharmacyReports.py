import time
from selenium.webdriver.common.keys import Keys
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By

########
AppName = GSV.appName


########
# Module:Pharmacy_Reports: User Collection Report*********
def getPharmacyDashboard(danpheEMR):
    print(">>START: getPharmacyDashboard")
    global TotalSale
    # global TotalReturn
    global CreditReturn
    global CashReturn
    global NetCashCollection
    global DepositAmount
    global DepositReturned
    global ProvisionalItems
    global UnpaidInvoices
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Dashboard')]").click()
    time.sleep(3)
    TotalSale = danpheEMR.find_element(By.XPATH, "//h4[contains(text(),'Total Sale')]/following-sibling::b").text
    print("Total Sale", TotalSale)
    TotalSale = TotalSale.partition(": ")[2]
    TotalSale = float(TotalSale)
    print("Total Sale", TotalSale)
    CashReturn = danpheEMR.find_element(By.XPATH, "//h4[contains(text(),'Cash Return')]/following-sibling::b").text
    print("CashReturn", CashReturn)
    CashReturn = CashReturn.partition(": ")[2]
    CashReturn = float(CashReturn)
    print("CashReturn", CashReturn)
    CreditReturn = danpheEMR.find_element(By.XPATH, "//h4[contains(text(),'Credit Return')]/following-sibling::b").text
    print("CreditReturn", CreditReturn)
    CreditReturn = CreditReturn.partition(": ")[2]
    CreditReturn = float(CreditReturn)
    print("CreditReturn", CreditReturn)
    NetCashCollection = danpheEMR.find_element(By.XPATH,
                                               "//h4[contains(text(),'Net Cash Collection')]/following-sibling::b").text
    print("NetCashCollection", NetCashCollection)
    NetCashCollection = NetCashCollection.partition(": ")[2]
    NetCashCollection = float(NetCashCollection)
    print("NetCashCollection", NetCashCollection)
    DepositAmount = danpheEMR.find_element(By.XPATH,
                                           "//h4[contains(text(),'Deposit Amount')]/following-sibling::b").text
    print("Deposit Amount", DepositAmount)
    DepositAmount = DepositAmount.partition(": ")[2]
    DepositAmount = float(DepositAmount)
    print("DepositAmount", DepositAmount)
    DepositReturned = danpheEMR.find_element(By.XPATH,
                                             "//h4[contains(text(),'Deposit Returned')]/following-sibling::b").text
    print("Deposit Returned", DepositReturned)
    DepositReturned = DepositReturned.partition(": ")[2]
    DepositReturned = float(DepositReturned)
    print("DepositReturned", DepositReturned)
    ProvisionalItems = danpheEMR.find_element(By.XPATH,
                                              "//td[contains(text(),'PROVISIONAL ITEMS')]/following-sibling::td").text
    print("PROVISIONAL ITEMS", ProvisionalItems)
    ProvisionalItems = ProvisionalItems.partition("Rs.")[2]
    ProvisionalItems = float(ProvisionalItems)
    print("ProvisionalItems", ProvisionalItems)
    UnpaidInvoices = danpheEMR.find_element(By.XPATH,
                                            "//td[contains(text(),'UNPAID INVOICES')]/following-sibling::td").text
    print("UNPAID INVOICES", UnpaidInvoices)
    UnpaidInvoices = UnpaidInvoices.partition("Rs.")[2]
    UnpaidInvoices = float(UnpaidInvoices)
    print("UnpaidInvoices", UnpaidInvoices)
    print("<<END: getPharmacyDashboard")


def preSystemPharmacyDashboard():
    global xTotalSale
    # global xTotalReturn
    global xCashReturn
    global xCreditReturn
    global xNetCashCollection
    global xDepositAmount
    global xDepositReturned
    global xProvisionalItems
    global xUnpaidInvoices
    xTotalSale = TotalSale
    xCashReturn = CashReturn
    xCreditReturn = CreditReturn
    xNetCashCollection = NetCashCollection
    xDepositAmount = DepositAmount
    xDepositReturned = DepositReturned
    xProvisionalItems = ProvisionalItems
    xUnpaidInvoices = UnpaidInvoices


def verifyPharmacyDashboard(cash, cashreturn, credit, creditreturn, deposit, depositreturn, provisional,
                            provisionacancel):
    print(">>START: verifyPharmacyDashboard:")
    if AppName == 'SNCH':
        temp = round(xTotalSale + cash + credit)
        print("temp", temp)
        print("temp", float(temp))
        print("TotalSale", TotalSale)
        assert float(round(TotalSale)) == float(round(xTotalSale + cash + credit))
        print("CashReturn", CashReturn)
        print("xCashReturn", xCashReturn)
        # a = float(round(xTotalReturn + cashreturn + creditreturn))
        a = float(round(xCashReturn + cashreturn))
        print("a", a)
        print("CashReturn", CashReturn)
        b = float(round(xCreditReturn + creditreturn))
        print("b", b)
        print("CreditReturn", CreditReturn)
        assert CashReturn == a
        assert CreditReturn == b

        print("xNetCollection", xNetCashCollection)
        x = int(xNetCashCollection + cash - cashreturn)
        print("x:", x)
        y = int(NetCashCollection)
        print("Y", y)
        assert y == x
        assert DepositAmount == xDepositAmount + deposit
        assert DepositReturned == xDepositReturned + depositreturn
        assert ProvisionalItems == xProvisionalItems + provisional - provisionacancel
        c = float(round(xUnpaidInvoices + credit - creditreturn))
        print("c", c)
        print("UnpaidInvoices", UnpaidInvoices)
        assert float(round(UnpaidInvoices)) == c
    print("<<END: verifyPharmacyDashboard")


def getPharmacyCashCollectionSummary(danpheEMR, user):
    print(">>START: getPharmacyCashCollectionSummary")
    global actualInvoiceAmount
    global actualInvocieReturned
    global actualDiscountAmount
    global actualDeposit
    global actualDepositReturn
    global actualNetAmount
    if AppName != 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    elif AppName != 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Cash Collection Summary')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(user)
    time.sleep(2)
    username = danpheEMR.find_element(By.XPATH, "(//div[@col-id='UserName'])[2]").text
    actualInvoiceAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='TotalAmount'])[2]").text
    actualInvoiceAmount = float(actualInvoiceAmount)
    print("actualInvoiceAmount:", actualInvoiceAmount)
    ##
    actualInvocieReturned = danpheEMR.find_element(By.XPATH, "(//div[@col-id='ReturnedAmount'])[2]").text
    actualInvocieReturned = float(actualInvocieReturned)
    print("actualInvocieReturned:", actualInvocieReturned)
    ##
    actualDiscountAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='DiscountAmount'])[2]").text
    actualDiscountAmount = float(actualDiscountAmount)
    print("actualDiscountAmount:", actualDiscountAmount)
    ##
    actualDeposit = danpheEMR.find_element(By.XPATH, "(//div[@col-id='DepositAmount'])[2]").text
    actualDeposit = float(actualDeposit)
    print("actualDeposit:", actualDeposit)
    ##
    actualDepositReturn = danpheEMR.find_element(By.XPATH, "(//div[@col-id='DepositReturn'])[2]").text
    actualDepositReturn = float(actualDepositReturn)
    print("actualDepositReturn:", actualDepositReturn)
    ##
    actualNetAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='NetAmount'])[2]").text
    actualNetAmount = float(actualNetAmount)
    print("actualNetAmount:", actualNetAmount)
    ##
    print("<<END: getPharmacyCashCollectionSummary")


def preSystemPharmacyCashCollectionSummary():
    print(">>START: preSystemPharmacyCashCollectionSummary")
    global preInvoiceAmount
    global preInvocieReturned
    global preDiscountAmount
    global preDeposit
    global preDepositReturn
    global preNetAmount
    preInvoiceAmount = actualInvoiceAmount
    preInvocieReturned = actualInvocieReturned
    preDiscountAmount = actualDiscountAmount
    preDeposit = actualDeposit
    preDepositReturn = actualDepositReturn
    preNetAmount = actualNetAmount
    print("<<END: preSystemPharmacyCashCollectionSummary")


def verifyPharmacyCashCollectionSummary(cash, cashreturn, credit, creditreturn, deposit, depositreturn, discount):
    print(">>START: verifyPharmacyCashCollectionSummary")
    global expectedInvoiceAmount
    global expectedInvocieReturned
    global expectedDiscountAmount
    global expectedDeposit
    global expectedDepositReturn
    global expectedNetAmount
    ##
    print("cash:", cash)
    print("credit:", credit)
    print("cashreturn:", cashreturn)
    print("creditreturn:", creditreturn)
    ##
    expectedInvoiceAmount = preInvoiceAmount + cash
    assert expectedInvoiceAmount == actualInvoiceAmount
    ##
    expectedInvocieReturned = preInvocieReturned + cashreturn
    print("expectedInvocieReturned:", expectedInvocieReturned)
    assert expectedInvocieReturned == actualInvocieReturned
    ##
    expectedDiscountAmount = preDiscountAmount + discount
    print("expectedDiscountAmount:", expectedDiscountAmount)
    assert expectedDiscountAmount == preDiscountAmount
    ##
    expectedDeposit = preDeposit + deposit
    print("expectedDeposit:", expectedDeposit)
    assert expectedDeposit == actualDeposit
    ##
    expectedDepositReturn = preDepositReturn + depositreturn
    print("expectedDepositReturn:", expectedDepositReturn)
    assert expectedDepositReturn == actualDepositReturn
    ##
    expectedNetAmount = preNetAmount + cash - cashreturn + deposit - depositreturn - discount
    print("expectedNetAmount:", expectedNetAmount)
    assert expectedNetAmount == actualNetAmount
    print("<<END: verifyPharmacyCashCollectionSummary")


def getPharmacyDepositBalanceReport(danpheEMR, HospitalNo):
    print(">>START: getPharmacyDepositBalanceReport")
    global sysdepositamt
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Deposit Balance Report ')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(9)
    assert HospitalNo == danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div[2]").text
    sysdepositamt = int(danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[4]").text)
    print("<<END: getPharmacyDepositBalanceReport")


def verifyPharmacyDepositBalanceReport(danpheEMR, HospitalNo, deposit, depositreturn):
    print(">>START: verifyPharmacyDepositBalanceReport")
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Deposit Balance Report ')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(9)
    assert HospitalNo == danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div[2]").text
    depositbalance = int(danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[4]").text)
    assert depositbalance == sysdepositamt + deposit - depositreturn
    print("<<END: verifyPharmacyDepositBalanceReport")


def getPharmacyOpeningEndingStockSummaryReport(danpheEMR, drugname):
    print(">>START: getPharmacyOpeningEndingStockSummaryReport")
    global sysdrugname
    global sysopeningstock
    global sysendingstock
    global sysdrugbatch
    global sysdrugexpiry
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Opening and Ending Stock Summary')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(drugname)
    time.sleep(3)
    sysdrugname = danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div").text
    print("sysdrugname", sysdrugname)
    assert sysdrugname == drugname
    sysopeningstock = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[7]").text
    print("sysopeningstock", sysopeningstock)
    sysendingstock = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[8]").text
    print("sysendingstock", sysendingstock)
    print("<<END: getPharmacyOpeningEndingStockSummaryReport")


def preSystemPharmacyOpeningEndingStockSummaryReport():
    print(">>START: preSystemPharmacyOpeningEndingStockSummaryReport")
    global presysdrugname
    global presysdrugbatch
    global presysdrugexpiry
    global presysopeningstock
    global presysendingstock
    presysopeningstock = sysopeningstock
    presysendingstock = sysendingstock
    presysdrugname = sysdrugname
    presysdrugbatch = sysdrugbatch
    presysdrugexpiry = sysdrugexpiry
    print("<<END: preSystemPharmacyOpeningEndingStockSummaryReport")


def verifyPharmacyOpeningEndingStockSummaryReport(danpheEMR, qty):
    print(">>START: verifyPharmacyOpeningEndingStockSummaryReport")
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Opening and Ending Stock Summary')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(presysdrugname, ' ', presysdrugbatch)
    time.sleep(7)
    assert presysdrugname == danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div").text
    assert presysdrugbatch == danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div[2]").text
    assert presysdrugexpiry == danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[4]/span").text
    assert presysopeningstock == danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[7]").text
    sysendingstock = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[8]").text
    assert int(sysendingstock) == int(presysendingstock) - qty
    print("<<END: verifyPharmacyOpeningEndingStockSummaryReport")


def getPharmacyStockManageDetailReport(danpheEMR, drugname):
    print(">>START: getPharmacyStockManageDetailReport")
    global ManageQuantity
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Stock Manage Detail Report')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(drugname)
    time.sleep(5)
    ManageQuantity = danpheEMR.find_element(By.XPATH,
                                            "(//div[@col-id='Quantity'])[2]").text  # There is open bug (EMR-2588) to list down latest manage record to top.
    print("Manage Quantity", ManageQuantity)
    print("<<END: getPharmacyStockManageDetailReport")


def preSystemPharmacyStockManageDetailReport():
    print(">>START: preSystemPharmacyStockManageDetailReport")
    global xManageQuantity
    xManageQuantity = ManageQuantity


def verifyPharmacyStockManageDetailReport(In, Out):
    assert int(ManageQuantity) == int(xManageQuantity) + In - Out
    print("<<END: preSystemPharmacyStockManageDetailReport")


def verifyStockItemsReport(danpheEMR, drugname):
    print(">>START: verifyStockItemsReport")
    if AppName == 'LPH':
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, 'Pharmacy').click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Stock Items')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='--Select Item--']").send_keys(drugname)
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='--Select Item--']").send_keys(Keys.ARROW_DOWN)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='--Select Item--']").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//select").send_keys("Dispensary")
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    sysqty = danpheEMR.find_element(By.XPATH, "(//div[@col-id='AvailableQuantity'])[2]").text
    print(sysqty)
    print("<<END: verifyStockItemsReport")


def getPurchaseSummaryReport(danpheEMR):
    global purchase
    global purchaseReturn
    global balance
    time.sleep(3)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Report/Purchase')]").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Purchase Summary')]").click()
    time.sleep(5)
    purchase = danpheEMR.find_element(By.XPATH,
                                      "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div").text
    purchase = int(purchase)
    print("Purchase value of a item is : ", purchase)
    purchaseReturn = danpheEMR.find_element(By.XPATH,
                                            "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[2]").text
    purchaseReturn = int(purchaseReturn)
    print("Purchase Return of the Items :", purchaseReturn)
    balance = danpheEMR.find_element(By.XPATH,
                                     "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[3]").text
    balance = int(balance)
    print("Balance of the Item is : ", balance)


def prePurchaseSummaryReport():
    global prePurchase
    global prepurchaseReturn
    global prebalance

    prePurchase = purchase
    prePurchase = int(prePurchase)
    print("PrePurchase amount is :", prePurchase)
    prepurchaseReturn = purchaseReturn
    prepurchaseReturn = int(prepurchaseReturn)
    print("Pre Purchase Return is :", prepurchaseReturn)
    prebalance = balance
    prebalance = int(prebalance)
    print("Pre Balance is :", prebalance)


def verifypurchasesummarybeforeReturn():
    print("START>>verifying the Purchase Summary before Return ")
    assert prePurchase == purchase
    assert prepurchaseReturn == purchaseReturn
    assert prebalance == balance
    print("END>> Verifying Purchase Summary Report before Return")


def verifypurchaseSummaryAfterReturn(retamt):
    print("START>>verifying the Purchase Summary After Return ")
    assert prepurchaseReturn == purchaseReturn - retamt
    print("END>> Verifying Purchase Summary Report After Return")

def getItemWisePurchaseReport(danpheEMR):
    print("get ItemWise Purchase Report")
    global TotalPurchaseQuantity
    global TotalPurchaseValueExcludingVAT
    global TotalVATAmount
    global TotalPurchaseValue
    time.sleep(3)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Report/Purchase')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Item Wise Purchase Report')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(5)
    TotalPurchaseQuantity = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[2]/span").text
    TotalPurchaseQuantity = TotalPurchaseQuantity.replace(",", "")
    TotalPurchaseQuantity = int(TotalPurchaseQuantity)
    print("Total Purchase Quantity is : ", TotalPurchaseQuantity)

    TotalPurchaseValueExcludingVAT = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[2]/td[2]/span").text
    TotalPurchaseValueExcludingVAT = TotalPurchaseValueExcludingVAT.replace(",", "")
    TotalPurchaseValueExcludingVAT = int(TotalPurchaseValueExcludingVAT)
    print("Total Purchase Value ExcludingVAT is : ", TotalPurchaseValueExcludingVAT)

    TotalVATAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[3]/td[2]/span").text
    TotalVATAmount = float(TotalVATAmount)
    print("Total VAT Amount is : ", TotalVATAmount)

    TotalPurchaseValue = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[4]/td[2]/span").text
    TotalPurchaseValue = TotalPurchaseValue.replace(",", "")
    TotalPurchaseValue = float(TotalPurchaseValue)
    print("Total Purchase Value is : ", TotalPurchaseValue)


def preItemWisePurchaseReport():
    print("Pre Itemwise Purchase Report")
    global preTotalPurchaseQuantity
    global preTotalPurchaseValueExcludingVAT
    global preTotalVATAmount
    global preTotalPurchaseValue

    preTotalPurchaseQuantity = TotalPurchaseQuantity
    preTotalPurchaseQuantity = int(preTotalPurchaseQuantity)
    print("PreTotal Purchase Quantity amount is :", preTotalPurchaseQuantity)

    preTotalPurchaseValueExcludingVAT = TotalPurchaseValueExcludingVAT
    preTotalPurchaseValueExcludingVAT = int(preTotalPurchaseValueExcludingVAT)
    print("PreTotal Purchase Value Excluding VAT is :", preTotalPurchaseValueExcludingVAT)

    preTotalVATAmount = TotalVATAmount
    print("PreTotal VAT Amount is :", preTotalVATAmount)

    preTotalPurchaseValue = TotalPurchaseValue
    preTotalPurchaseValue = float(preTotalPurchaseValue)
    print("PreTotal Purchase Value is :", preTotalPurchaseValue)


def verifyItemWisePurchaseReport(qty, purchaseValue):
    print("START>>verifying the Item Wise Purchase Report ")
    assert TotalPurchaseQuantity == preTotalPurchaseQuantity + qty
    assert TotalPurchaseValueExcludingVAT == preTotalPurchaseValueExcludingVAT + purchaseValue
    assert preTotalVATAmount == TotalVATAmount
    assert TotalPurchaseValue == preTotalPurchaseValue + purchaseValue
    print("END>> Verifying Item Wise Purchase Report")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


########Purchase Reports:

########Sales Reports:
###User Collection Report-
def getPharmacyUserCollectionReport(danpheEMR, user):
    print(">>START: getPharmacyUserCollectionReport")
    global actualNetCashCollection
    global actualGrossTotalSales
    global actualDiscount
    global actualReturnSubTotal
    global actualReturnDiscount
    global actualReturnAmount
    global actualNetSales
    global actualVATAmount
    global actualLessCreditAmount
    global actualAddDepositReceived
    global actualDepositDeducted
    global actualLessDepositRefund
    global actualAddCollectionFromReceivables
    global actualLessCashDiscount
    global actualTotalCashCollection
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'User Collection')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(user)
    time.sleep(9)
    # 1
    actualNetCashCollection = danpheEMR.find_element(By.CSS_SELECTOR, ".blinkAmount").text
    print("actualNetCashCollection", actualNetCashCollection)
    actualNetCashCollection = actualNetCashCollection.partition("(")[2]
    actualNetCashCollection = actualNetCashCollection.partition(")")[0]
    actualNetCashCollection = float(actualNetCashCollection)
    print("actualNetCashCollection", actualNetCashCollection)
    # 2
    actualGrossTotalSales = danpheEMR.find_element(By.XPATH,
                                                   "//td[contains(text(),'Gross Total Sales')]/following-sibling::td").text
    actualGrossTotalSales = float(actualGrossTotalSales)
    print("actualGrossTotalSales", actualGrossTotalSales)
    # 3
    actualDiscount = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'Discount')]/following-sibling::td").text
    actualDiscount = float(actualDiscount)
    print("actualDiscount", actualDiscount)
    # 4
    actualReturnSubTotal = danpheEMR.find_element(By.XPATH,
                                                  "//td[contains(text(),'Return SubTotal')]/following-sibling::td").text
    actualReturnSubTotal = float(actualReturnSubTotal)
    print("actualReturnSubTotal", actualReturnSubTotal)
    # 5
    actualReturnDiscount = danpheEMR.find_element(By.XPATH,
                                                  "//td[contains(text(),'Return Discount')]/following-sibling::td").text
    actualReturnDiscount = float(actualReturnDiscount)
    print("actualReturnDiscount", actualReturnDiscount)
    # 6
    actualReturnAmount = danpheEMR.find_element(By.XPATH,
                                                "//td[contains(text(),'Return Amount')]/following-sibling::td").text
    actualReturnAmount = float(actualReturnAmount)
    print("actualReturnAmount", actualReturnAmount)
    # 7
    actualNetSales = danpheEMR.find_element(By.XPATH,
                                            "//strong[contains(text(),'Net Sales')]/parent::td/following-sibling::td").text
    actualNetSales = float(actualNetSales)
    print("actualNetSales", actualNetSales)
    # 8
    if AppName != 'RTM':
        actualVATAmount = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'VAT Amount')]/following-sibling::td").text
        actualVATAmount = float(actualVATAmount)
        print("actualVATAmount", actualVATAmount)
    # 9
    actualLessCreditAmount = danpheEMR.find_element(By.XPATH,
                                                    "//td[contains(text(),'Less Credit Amount')]/following-sibling::td").text
    actualLessCreditAmount = float(actualLessCreditAmount)
    print("actualLessCreditAmount", actualLessCreditAmount)
    # 10
    actualAddDepositReceived = danpheEMR.find_element(By.XPATH,
                                                      "//td[contains(text(),'Add Deposit Received')]/following-sibling::td").text
    actualAddDepositReceived = float(actualAddDepositReceived)
    print("actualAddDepositReceived", actualAddDepositReceived)
    # 11
    actualDepositDeducted = danpheEMR.find_element(By.XPATH,
                                                   "//td[contains(text(),'Deposit Deducted')]/following-sibling::td").text
    actualDepositDeducted = float(actualDepositDeducted)
    print("actualDepositDeducted", actualDepositDeducted)
    # 12
    actualLessDepositRefund = danpheEMR.find_element(By.XPATH,
                                                     "//td[contains(text(),'Less Deposit Refund')]/following-sibling::td").text
    actualLessDepositRefund = float(actualLessDepositRefund)
    print("actualLessDepositRefund", actualLessDepositRefund)
    # 13
    actualAddCollectionFromReceivables = danpheEMR.find_element(By.XPATH,
                                                                "//td[contains(text(),'Add Collection From Receivables')]/following-sibling::td").text
    actualAddCollectionFromReceivables = float(actualAddCollectionFromReceivables)
    print("actualAddCollectionFromReceivables", actualAddCollectionFromReceivables)
    # 14
    actualLessCashDiscount = danpheEMR.find_element(By.XPATH,
                                                    "//td[contains(text(),'Less Cash Discount')]/following-sibling::td").text
    actualLessCashDiscount = float(actualLessCashDiscount)
    print("actualLessCashDiscount", actualLessCashDiscount)
    # 15
    actualTotalCashCollection = danpheEMR.find_element(By.XPATH,
                                                       "//td[contains(text(),'Total Cash Collection')]/following-sibling::td").text
    actualTotalCashCollection = float(actualTotalCashCollection)
    print("actualTotalCashCollection", actualTotalCashCollection)
    print("<<END: getPharmacyUserCollectionReport")


def preSystemPharmacyUserCollectionReport():
    print(">START: preSystemPharmacyUserCollectionReport")
    global preNetCashCollection
    global preGrossTotalSales
    global preDiscount
    global preReturnSubTotal
    global preReturnDiscount
    global preReturnAmount
    global preNetSales
    global preVATAmount
    global preLessCreditAmount
    global preAddDepositReceived
    global preDepositDeducted
    global preLessDepositRefund
    global preAddCollectionFromReceivables
    global preLessCashDiscount
    global preTotalCashCollection
    preNetCashCollection = actualNetCashCollection
    preGrossTotalSales = actualGrossTotalSales
    preDiscount = actualDiscount
    preReturnSubTotal = actualReturnSubTotal
    preReturnDiscount = actualReturnDiscount
    preReturnAmount = actualReturnAmount
    preNetSales = actualNetSales
    if AppName != "RTM":
        preVATAmount = actualVATAmount
    preLessCreditAmount = actualLessCreditAmount
    preAddDepositReceived = actualAddDepositReceived
    preDepositDeducted = actualDepositDeducted
    preLessDepositRefund = actualLessDepositRefund
    preAddCollectionFromReceivables = actualAddCollectionFromReceivables
    preLessCashDiscount = actualLessCashDiscount
    preTotalCashCollection = actualTotalCashCollection
    print("<<END: preSystemPharmacyUserCollectionReport")


def verifySystemPharmacyUserCollectionReport(cash, cashreturn, credit, creditreturn, creditsettlement, discount,
                                             deposit, depositreturn, provisional, provisionalcancel):
    print(">>START: verifySystemPharmacyUserCollectionReport")
    print("cash", cash)
    print("cashreturn", cashreturn)
    # 1
    expectedNetCashCollection = preNetCashCollection + cash - cashreturn + creditsettlement
    print("expectedNetCashCollection:", expectedNetCashCollection)
    assert actualNetCashCollection == expectedNetCashCollection
    # 2
    expectedGrossTotalSales = preGrossTotalSales + cash + credit
    assert actualGrossTotalSales == expectedGrossTotalSales
    # 3
    expectedDiscount = preDiscount + discount
    assert actualDiscount == expectedDiscount
    # 4
    expectedReturnSubTotal = preReturnSubTotal + cashreturn + creditreturn
    assert actualReturnSubTotal == expectedReturnSubTotal
    # 5
    expectedReturnDiscount = preReturnDiscount - discount
    assert actualReturnDiscount == expectedReturnDiscount
    # 6
    expectedReturnAmount = preReturnAmount + cashreturn + creditreturn
    assert actualReturnAmount == expectedReturnAmount
    # 7
    expectedNetSales = preNetSales + cash - cashreturn + credit - creditreturn
    assert actualNetSales == expectedNetSales
    # 8
    if AppName != 'RTM':
        expectedVATAmount = preVATAmount
        assert actualVATAmount == expectedVATAmount
    # 9
    expectedLessCreditAmount = preLessCreditAmount + credit - creditreturn
    assert actualLessCreditAmount == expectedLessCreditAmount
    # 10
    expectedAddDepositReceived = preAddDepositReceived + deposit
    assert actualAddDepositReceived == expectedAddDepositReceived
    # 11
    expectedDepositDeducted = preDepositDeducted
    assert actualDepositDeducted == expectedDepositDeducted
    # 12
    expectedLessDepositRefund = preLessDepositRefund
    assert actualLessDepositRefund == expectedLessDepositRefund
    # 13
    expectedAddCollectionFromReceivables = preAddCollectionFromReceivables + creditsettlement
    assert actualAddCollectionFromReceivables == expectedAddCollectionFromReceivables
    # 14
    expectedLessCashDiscount = preLessCashDiscount
    assert actualLessCashDiscount == expectedLessCashDiscount
    # 15
    expectedTotalCashCollection = preTotalCashCollection + cash - cashreturn + deposit - depositreturn + creditsettlement
    assert actualTotalCashCollection == expectedTotalCashCollection

    print("<<END: verifySystemPharmacyUserCollectionReport")


###Patient Wise Sales Report-
def getPatientWiseSalesDetails(danpheEMR, HospitalNo):
    print(">>Start: getPatientWise Sales Details")
    global TotalSalesValue
    global TotalSalesRefund
    global TotalNetSales
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Patient-wise Sales Detail')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "SearchPatientBox").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "SearchPatientBox").send_keys(Keys.DOWN)
    danpheEMR.find_element(By.ID, "SearchPatientBox").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Show Report')]").click()
    time.sleep(2)
    TotalSalesValue = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[2]").text
    TotalSalesValue = float(TotalSalesValue)
    print("Total Sales Value of selected date of given patient is  : ", TotalSalesValue)
    TotalSalesRefund = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[4]").text
    TotalSalesRefund = float(TotalSalesRefund)
    print("Total Sales Refund of selected date of given patient is  : ", TotalSalesRefund)
    TotalNetSales = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[6]").text
    TotalNetSales = float(TotalNetSales)
    print("Total Net Sales of selected date of given patient is  : ", TotalNetSales)


def prePatientWiseSalesDetails():
    global preTotalSalesValue
    global preTotalSalesRefund
    global preTotalNetSales
    preTotalSalesValue = TotalSalesValue
    preTotalSalesRefund = TotalSalesRefund
    preTotalNetSales = TotalNetSales


def VerifyPatientWiseSalesDetail(danpheEMR, HospitalNo, cash, credit, cashreturn, creditreturn):
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Patient-wise Sales Detail')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "SearchPatientBox").send_keys(HospitalNo)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "SearchPatientBox").send_keys(Keys.DOWN)
    danpheEMR.find_element(By.ID, "SearchPatientBox").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Show Report')]").click()
    time.sleep(2)
    print("Start:  Verifing Patient wise Sales Detail")
    expectedTotalSalesValue = preTotalSalesValue + cash + credit
    assert TotalSalesValue == expectedTotalSalesValue
    expectedTotalSalesRefund = preTotalSalesRefund + cashreturn + creditreturn
    assert TotalSalesRefund == expectedTotalSalesRefund
    expectedTotalNetSales = preTotalNetSales + cash - cashreturn + credit - creditreturn
    assert TotalNetSales == expectedTotalNetSales
    print("END>> Verify Patient wise Sales Detail")


###Narcotic Daily Sales Report-
def verifySystemPharmacyNarcoticDailySalesReport(danpheEMR, invoiceNo, totalAmount):
    print(">>START: verifySystemPharmacyNarcoticDailySalesReport")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Narcotics Daily Sales')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(15)  # Due to performance issue there is open bug in Jira: EMR-4775
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(invoiceNo)
    time.sleep(9)
    sysInvoiceNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='InvoicePrintId'])[2]").text
    print("sysInvoiceNo:", sysInvoiceNo)
    print("invoiceNo:", invoiceNo)
    assert sysInvoiceNo == invoiceNo
    sysTotalAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='TotalAmount'])[2]").text
    try:
        sysTotalAmount = sysTotalAmount.partition(".")[0]
    except:
        pass
    sysTotalAmount = int(sysTotalAmount)
    print("sysTotalAmount:", sysTotalAmount)
    print("totalAmount:", totalAmount)
    assert sysTotalAmount == totalAmount
    print("<<END: verifySystemPharmacyNarcoticDailySalesReport")


###Bill-Wise Sales Report-
def getSystemPharmacyBillWiseSalesReport(danpheEMR):
    print(">>START: verifySystemPharmacyBillWiseSalesReport")
    global actualSubTotalAmount
    global actualDiscountAmount
    global actualTotalAmount

    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Bill-wise Sales')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    actualSubTotalAmount = danpheEMR.find_element(By.XPATH,
                                                  "(//td[contains(text(),'MainDispensary')]/following-sibling::td)[1]").text
    actualSubTotalAmount = float(actualSubTotalAmount)
    print("actualSubTotalAmount:", actualSubTotalAmount)
    actualDiscountAmount = danpheEMR.find_element(By.XPATH,
                                                  "(//td[contains(text(),'MainDispensary')]/following-sibling::td)[2]").text
    actualDiscountAmount = float(actualDiscountAmount)
    print("actualDiscountAmount:", actualDiscountAmount)
    actualTotalAmount = danpheEMR.find_element(By.XPATH,
                                               "(//td[contains(text(),'MainDispensary')]/following-sibling::td)[3]").text
    actualTotalAmount = float(actualTotalAmount)
    print("actualTotalAmount:", actualTotalAmount)


def preSystemPharmacyBillWiseSalesReport():
    global preSubTotalAmount
    global preDiscountAmount
    global preTotalAmount
    preSubTotalAmount = actualSubTotalAmount
    preDiscountAmount = actualDiscountAmount
    preTotalAmount = actualTotalAmount


def verifySystemPharmacyBillWiseSalesReport(danpheEMR, invoiceNo, cash, cashReturn, credit, creditReturn, totalAmount,
                                            discountAmount):
    print(">>START: verifySystemPharmacyBillWiseSalesReport")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Bill-wise Sales')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(15)  # Due to performance issue there is open bug in Jira: EMR-4775
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(invoiceNo)
    time.sleep(9)
    sysInvoiceNo = danpheEMR.find_element(By.XPATH, "(/sale").text
    print("sysInvoiceNo:", sysInvoiceNo)
    print("invoiceNo:", invoiceNo)
    assert sysInvoiceNo == invoiceNo
    sysTotalAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='TotalAmount'])[2]").text
    sysTotalAmount = int(sysTotalAmount)
    print("sysTotalAmount:", sysTotalAmount)
    print("totalAmount:", totalAmount)
    assert sysTotalAmount == totalAmount

    expectedSubTotalAmount = preSubTotalAmount + cash - cashReturn + credit - creditReturn
    print("expectedSubTotalAmount:", expectedSubTotalAmount)
    assert expectedSubTotalAmount == actualSubTotalAmount
    expectedDiscountAmount = preDiscountAmount + discountAmount
    print("expectedDiscountAmount:", expectedDiscountAmount)
    assert expectedDiscountAmount == actualDiscountAmount
    expectedTotalAmount = preTotalAmount + cash - cashReturn + credit - creditReturn - discountAmount
    print("expectedTotalAmount:", expectedTotalAmount)
    assert expectedTotalAmount == actualTotalAmount

    print("<<END: verifySystemPharmacyBillWiseSalesReport")


def getSystemPharmacyItemWiseSalesReport(danpheEMR, drugName):
    print(">>START: GetSystemPharmacyItemWiseSalesReport")
    global TotalSalesQuantity
    global TotalSalesValue
    global TotalStockValue
    global Net

    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Item-wise Sales')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH,
                           "//html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/ng-component/div[2]/my-app/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/input").send_keys(
        drugName)
    danpheEMR.find_element(By.XPATH,
                           "//html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/ng-component/div[2]/my-app/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/input").send_keys(
        Keys.DOWN)
    danpheEMR.find_element(By.XPATH,
                           "//html/body/my-app/div/div/div[3]/div[2]/div/div/ng-component/div[2]/ng-component/div[2]/my-app/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div/input").send_keys(
        Keys.ENTER)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    TotalSalesQuantity = danpheEMR.find_element(By.XPATH, "//table/tbody/tr/td[2]/span").text
    TotalSalesQuantity = float(TotalSalesQuantity)
    print("TotalSalesQuantity:", TotalSalesQuantity)
    TotalSalesValue = danpheEMR.find_element(By.XPATH, "//table/tbody/tr/td[4]/span").text
    TotalSalesValue = float(TotalSalesValue)
    print("TotalSalesValue:", TotalSalesValue)
    TotalStockValue = danpheEMR.find_element(By.XPATH, "//table/tbody/tr/td[6]/span").text
    TotalStockValue = float(TotalStockValue)
    print("TotalStockValue:", TotalStockValue)
    Net = danpheEMR.find_element(By.XPATH, "//table/tbody/tr/td[8]/span").text
    Net = float(Net)
    print("Net:", Net)


def preSystemPharmacyItemWiseSalesReport():
    print(">>START: PreSystemPharmacyItemWiseSalesReport")
    global preTotalSalesQuantity
    global preTotalSalesValue
    global preTotalStockValue
    global preNet

    preTotalSalesQuantity = TotalSalesQuantity
    preTotalSalesValue = TotalSalesValue
    preTotalStockValue = TotalStockValue
    preNet = Net


def VerifySystemPharmacyItemWiseSalesReport(danpheEMR, drugName, cash, credit, qty):
    print(">>START: Verifying System Pharmacy ItemWiseSalesReport")
    expectedTotalSalesQuantity = preTotalSalesQuantity + qty
    assert TotalSalesQuantity == expectedTotalSalesQuantity
    expectedTotalSalesValue = preTotalSalesValue + cash + credit
    assert TotalSalesValue == expectedTotalSalesValue
    print(">> Verified System Pharmacy Item-wise Sales Report ")


def getSystemPharmacySalesSummaryReport(danpheEMR):
    print("Start: getSystemPharmacySalesSummaryReport:")
    global actualCashSales
    global actualCashSalesRefund
    global actualNetCashSales
    global actualCreditSales
    global actualCreditSalesRefund
    global actualNetCreditSales
    global actualTotalSales
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Sales Summary')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    actualCashSales = danpheEMR.find_element(By.XPATH,
                                             "(//td[contains(text(),'Cash Sales')])[1]/following-sibling::td").text
    actualCashSales = float(actualCashSales)
    print("actualCashSales", actualCashSales)
    actualCashSalesRefund = danpheEMR.find_element(By.XPATH,
                                                   "(//td[contains(text(),'Cash Sales Refund')])[1]/following-sibling::td").text
    actualCashSalesRefund = float(actualCashSalesRefund)
    print("actualCashSalesRefund", actualCashSalesRefund)
    actualNetCashSales = danpheEMR.find_element(By.XPATH,
                                                "(//td[contains(text(),'Net Cash Sales')])[1]/following-sibling::td").text
    actualNetCashSales = float(actualNetCashSales)
    print("actualNetCashSales", actualNetCashSales)
    actualCreditSales = danpheEMR.find_element(By.XPATH,
                                               "(//td[contains(text(),'Credit Sales')])[1]/following-sibling::td").text
    actualCreditSales = float(actualCreditSales)
    print("actualCreditSales", actualCreditSales)
    actualCreditSalesRefund = danpheEMR.find_element(By.XPATH,
                                                     "(//td[contains(text(),'Credit Sales Refund')])[1]/following-sibling::td").text
    actualCreditSalesRefund = float(actualCreditSalesRefund)
    print("actualCreditSalesRefund", actualCreditSalesRefund)
    actualNetCreditSales = danpheEMR.find_element(By.XPATH,
                                                  "(//td[contains(text(),'Net Credit Sales')])[1]/following-sibling::td").text
    actualNetCreditSales = float(actualNetCreditSales)
    print("actualNetCreditSales", actualNetCreditSales)
    actualTotalSales = danpheEMR.find_element(By.XPATH,
                                              "(//td[contains(text(),'Total Sales')])[1]/following-sibling::td").text
    actualTotalSales = float(actualTotalSales)
    print("actualTotalSales", actualTotalSales)
    print("End: getSystemPharmacySalesSummaryReport:")


def preSystemPharmacySalesSummaryReport():
    print("Start: getSystemPharmacySalesSummaryReport:")
    global preCashSales
    global preCashSalesRefund
    global preNetCashSales
    global preCreditSales
    global preCreditSalesRefund
    global preNetCreditSales
    global preTotalSales
    preCashSales = actualCashSales
    preCashSalesRefund = actualCashSalesRefund
    preNetCashSales = actualNetCashSales
    preCreditSales = actualCreditSales
    preCreditSalesRefund = actualCreditSalesRefund
    preNetCreditSales = actualNetCreditSales
    preTotalSales = actualTotalSales
    print("End: getSystemPharmacySalesSummaryReport:")


def verifySystemPharmacySalesSummaryReport(danpheEMR, cash, cashReturn, credit, creditReturn):
    print("Start: getSystemPharmacySalesSummaryReport:")
    expectedCashSales = preCashSales + cash
    assert actualCashSales == expectedCashSales
    expectedCashSalesRefund = preCashSalesRefund + cashReturn
    assert actualCashSalesRefund == expectedCashSalesRefund
    expectedNetCashSales = preNetCashSales + cash - cashReturn
    assert actualNetCashSales == expectedNetCashSales
    expectedCreditSales = preCreditSales + credit
    assert actualCreditSales == expectedCreditSales
    expectedCreditSalesRefund = preCreditSalesRefund + creditReturn
    assert actualCreditSalesRefund == expectedCreditSalesRefund
    expectedNetCreditSales = preNetCreditSales + credit - creditReturn
    assert actualNetCreditSales == expectedNetCreditSales
    expectedTotalSales = preTotalSales + cash - cashReturn + credit - creditReturn
    assert actualTotalSales == expectedTotalSales
    print("End: getSystemPharmacySalesSummaryReport:")


########Stock Reports:
###Pharmacy>Expiry Report-
def getPharmacyExpiryReport():
    print("Start: getPharmacyExpiryReport:")
    ###### EMR-4779 : ticket need to get deployed to test the expiry report, otherwise it's of no use.
    print("End: getPharmacyExpiryReport:")


def verifyPharmacyExpiryReport():
    print("Start: verifyPharmacyExpiryReport:")
    ###### EMR-4779 : ticket need to get deployed to test the expiry report, otherwise it's of no use.
    print("End: verifyPharmacyExpiryReport:")


###Pharmacy>Return From Customer Report
def getPharmacyReturnFromCustomerReport(danpheEMR, invoiceNo):
    print("Start: getPharmacyReturnFromCustomerReport:")
    global actualTotalReturnedAmount
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Return From Customer Report')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    actualTotalReturnedAmount = danpheEMR.find_element(By.XPATH,
                                                       "//td[contains(text(),' Total Returned Amount ')]/following-sibling::td").text
    actualTotalReturnedAmount = float(actualTotalReturnedAmount)
    print("actualTotalReturnedAmount", actualTotalReturnedAmount)
    print("End: getPharmacyReturnFromCustomerReport:")


def prePharmacyReturnFromCustomerReport():
    print("Start: prePharmacyReturnFromCustomerReport:")
    global preTotalReturnedAmount
    preTotalReturnedAmount = actualTotalReturnedAmount
    print("End: prePharmacyReturnFromCustomerReport:")


def verifyPharmacyReturnFromCustomerReport(danpheEMR, invoiceNo, cashReturn, creditReturn):
    print("Start: verifyPharmacyReturnFromCustomerReport:")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Return From Customer Report')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(invoiceNo)
    time.sleep(3)
    sysInvoiceNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='IssueNo'])[2]").text
    sysInvoiceNo = sysInvoiceNo.partition("PH")[2]
    print("sysInvoiceNo", sysInvoiceNo)
    assert sysInvoiceNo == invoiceNo
    expectedTotalReturnedAmount = preTotalReturnedAmount + cashReturn + creditReturn
    print("expectedTotalReturnedAmount", expectedTotalReturnedAmount)
    assert actualTotalReturnedAmount == expectedTotalReturnedAmount
    print("End: verifyPharmacyReturnFromCustomerReport:")


########Supplier Reports:

def getSupplierStockReport(danpheEMR, supplier):
    global actualTotalAmount
    time.sleep(3)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    elif AppName == "SNCH":
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Report/Stock')]").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Supplier Stock ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "supplierName").send_keys(supplier)
    time.sleep(2)
    danpheEMR.find_element(By.ID, "supplierName").send_keys(Keys.DOWN)
    danpheEMR.find_element(By.ID, "supplierName").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Show Report')]").click()
    time.sleep(2)
    actualTotalAmount = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[1]/td[4]").text
    actualTotalAmount = int(actualTotalAmount)
    print("Total Amount of selected date of given supplier is  : ", actualTotalAmount)


def preSupplierStockReport():
    global pretotalAmount
    pretotalAmount = actualTotalAmount
    print("pre Total Stock amount of given supplier is :", pretotalAmount)


def verifysupplierStockReport(qtyGR, rateGR):
    print("START>>verifying the Stock Summary Report")
    newPurchaseAmount = qtyGR * rateGR
    print("newPurchaseAmount:", newPurchaseAmount)
    expectedTotalAmount = pretotalAmount + newPurchaseAmount
    print("expectedTotalAmount:", expectedTotalAmount)
    assert expectedTotalAmount == actualTotalAmount
    print("END>> Verifying Stock Summary Report")


### Sales Statement ##

def getStockTransferReport(danpheEMR):
    global actualSalesValue
    global actualSalesCost
    global actualSalesReturnCost
    global actualSalesReturnValue
    global actualProfit

    time.sleep(3)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Sales").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Sales Statement')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    actualSalesValue = danpheEMR.find_element(By.XPATH, "(//div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[2]").text
    actualSalesValue = float(actualSalesValue)
    print("actualSalesValue", actualSalesValue)
    actualSalesCost = danpheEMR.find_element(By.XPATH, "(//div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[3])").text
    actualSalesCost = float(actualSalesCost)
    print("actualSalesCost", actualSalesCost)
    actualSalesReturnValue = danpheEMR.find_element(By.XPATH,
                                                    "(//div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[4])").text
    actualSalesReturnValue = float(actualSalesReturnValue)
    print("actualSalesReturnValue", actualSalesReturnValue)
    actualSalesReturnCost = danpheEMR.find_element(By.XPATH,
                                                   "(//div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[5]").text
    actualSalesReturnCost = float(actualSalesReturnCost)
    print("actualSalesReturnCost", actualSalesReturnCost)
    actualProfit = danpheEMR.find_element(By.XPATH, "(//div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[6]").text
    actualProfit = float(actualProfit)
    print("actualProfit", actualProfit)
    print("END>>> Get Sales Statement >>>")


def presalesstatementreport():
    print("START>>>Pre Sales Statement Report >>>")
    global presalesvalue
    global presalescost
    global presalesreturnvalue
    global presalesreturncost
    global preactualProfit

    presalesvalue = actualSalesValue
    presalescost = actualSalesCost
    presalesreturnvalue = actualSalesReturnValue
    presalesreturncost = actualSalesReturnCost
    preactualProfit = actualProfit

    print("END>>> Pre Sales Statement Report >>>")


### Narcotic Stock Report ###

def verifynarcoticstockreport(danpheEMR, qty, DrugName, grNo):
    print("START >>> Verifying Narcotic Stock Report>>")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Store").click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Report").click()
    time.sleep(4)
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Narcotics Stock')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(DrugName, " ", qty, " ", grNo)
    time.sleep(9)
    print("Good Receipt Number / Batch Number: ", grNo)
    batchNo = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[2]").text
    batchNo = int(batchNo)
    print("Batch number of Given medicine is :", batchNo)
    assert batchNo == grNo


def getStockTransferReport(danpheEMR):
    global receivedStockQuantity
    global receivedStockPurchaseValue
    global receivedStockSalesValue
    global notReceivedStockQuantity
    global notReceivedStockPurchaseValue
    global notReceivedSalesValue
    global totalStockQuantity
    global totalStockPurchaseValue
    global totalStockSalesValue

    time.sleep(3)
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    elif AppName == "SNCH" or AppName == "MPH":
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Report/Stock')]").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Stock Transfers')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//span[contains(text(),'Show Report')]").click()

    receivedStockQuantity = danpheEMR.find_element(By.XPATH,
                                                   "//*[@id='print_summary']/table/tbody/tr[2]/td[2]/span").text
    receivedStockQuantity = int(receivedStockQuantity)
    print("Transferred Stocks (Received Stocks) Quantity is : ", receivedStockQuantity)

    receivedStockPurchaseValue = danpheEMR.find_element(By.XPATH,
                                                        "//*[@id='print_summary']/table/tbody/tr[2]/td[3]/span").text
    receivedStockPurchaseValue = int(str(receivedStockPurchaseValue).replace(",", ""))
    print("Transferred Stocks (Received Stocks)Purchase value is : ", receivedStockPurchaseValue)

    receivedStockSalesValue = danpheEMR.find_element(By.XPATH,
                                                     "//*[@id='print_summary']/table/tbody/tr[2]/td[4]/span").text
    receivedStockSalesValue = int(str(receivedStockSalesValue).replace(",", ""))
    print("Transferred Stocks (Received Stocks) Sales Value is : ", receivedStockSalesValue)

    notReceivedStockQuantity = danpheEMR.find_element(By.XPATH,
                                                      "//*[@id='print_summary']/table/tbody/tr[3]/td[2]/span").text
    notReceivedStockQuantity = int(notReceivedStockQuantity)
    print("In-Transition Stocks (Not Received Stocks) Quantity is :  ", notReceivedStockQuantity)

    notReceivedStockPurchaseValue = danpheEMR.find_element(By.XPATH,
                                                           "//*[@id='print_summary']/table/tbody/tr[3]/td[3]/span").text
    notReceivedStockPurchaseValue = int(str(notReceivedStockPurchaseValue).replace(",", ""))
    print("In-Transition Stocks (Not Received Stocks) Purchase value is :  ", notReceivedStockPurchaseValue)

    notReceivedSalesValue = danpheEMR.find_element(By.XPATH,
                                                   "//*[@id='print_summary']/table/tbody/tr[3]/td[4]/span").text
    notReceivedSalesValue = float(str(notReceivedSalesValue).replace(",", ""))
    print("In-Transition Stocks (Not Received Stocks) Sales value is :  ", notReceivedSalesValue)

    totalStockQuantity = danpheEMR.find_element(By.XPATH, "//*[@id='print_summary']/table/tbody/tr[4]/td[2]/span").text
    totalStockQuantity = int(totalStockQuantity)
    print("Total Stocks is : ", totalStockQuantity)

    totalStockPurchaseValue = danpheEMR.find_element(By.XPATH,
                                                     "//*[@id='print_summary']/table/tbody/tr[4]/td[3]/span").text
    totalStockPurchaseValue = int(str(totalStockPurchaseValue).replace(",", ""))
    print("Total Purchase Value is : ", totalStockPurchaseValue)

    totalStockSalesValue = danpheEMR.find_element(By.XPATH,
                                                  "//*[@id='print_summary']/table/tbody/tr[4]/td[4]/span").text
    totalStockSalesValue = str(totalStockSalesValue).replace(",", "")
    totalStockSalesValue = float(totalStockSalesValue)
    print("Total Sales value is : ", totalStockSalesValue)


def preStockTransferReport():
    global prereceivedStockQuantity
    global prereceivedStockPurchaseValue
    global prereceivedStockSalesValue
    global prenotReceivedStockQuantity
    global prenotReceivedStockPurchaseValue
    global prenotReceivedSalesValue
    global pretotalStockQuantity
    global pretotalStockPurchaseValue
    global pretotalStockSalesValue

    prereceivedStockQuantity = receivedStockQuantity
    print("let Transferred Stocks(Received Stock) Quantity be : ", prereceivedStockQuantity)

    prereceivedStockPurchaseValue = receivedStockPurchaseValue
    print("let Transferred Stocks(Received Stock) Purchase Value be : ", prereceivedStockPurchaseValue)

    prereceivedStockSalesValue = receivedStockSalesValue
    print("let Transferred Stocks(Received Stock) Sales Value be : ", prereceivedStockSalesValue)

    prenotReceivedStockQuantity = notReceivedStockQuantity
    print("let In -Transition Stocks(Not Received Stock) Quantity be : ", prenotReceivedStockQuantity)

    prenotReceivedStockPurchaseValue = notReceivedStockPurchaseValue
    print("let In -Transition Stocks(Not Received Stock) Purchase Value be : ", prenotReceivedStockPurchaseValue)

    prenotReceivedSalesValue = notReceivedSalesValue
    print("let In -Transition Stocks(Not Received Stock) Sales Value be : ", prenotReceivedSalesValue)

    pretotalStockQuantity = totalStockQuantity
    print("let Total Stocks Quantity be : ", pretotalStockQuantity)

    pretotalStockPurchaseValue = totalStockPurchaseValue
    print("let Total Stocks Purchase Value be : ", pretotalStockPurchaseValue)

    pretotalStockSalesValue = totalStockSalesValue
    print("let Total Stocks Sales Value be : ", pretotalStockSalesValue)


def verifyStockSummaryReportBeforeReceiving(qty):
    print("START>> Verifying Stock Stock Summary Report Before Item Receiving")
    assert notReceivedStockQuantity == float(prenotReceivedStockQuantity + qty)
    assert totalStockQuantity == receivedStockQuantity + notReceivedStockQuantity
    assert totalStockPurchaseValue == receivedStockPurchaseValue + notReceivedStockPurchaseValue
    assert totalStockSalesValue == receivedStockSalesValue + notReceivedSalesValue
    print("END>> Verifying Stock Stock Summary Report Before Item  Receiving")


def verifyStockSummaryReportAfterReceiving(qty):
    print("START>> Verifying Stock Stock Summary Report After item Receiving")
    assert receivedStockQuantity == prereceivedStockQuantity + qty
    assert totalStockQuantity == receivedStockQuantity + notReceivedStockQuantity
    assert totalStockPurchaseValue == receivedStockPurchaseValue + notReceivedStockPurchaseValue
    assert totalStockSalesValue == receivedStockSalesValue + notReceivedSalesValue
    print("END>> Verifying Stock Stock Summary Report After item Receiving")

def getReturnToSupplierReport(danpheEMR, creditno):
    print("START>> Return to supplier report")
    if AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, 'Store').click()
    else:
        danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, 'Report').click()
    danpheEMR.find_element(By.XPATH, "//a[contains(@href, '#/Pharmacy/Report/Purchase')]").click()
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Return to Supplier')]").click()
    danpheEMR.find_element(By.XPATH, "//span[contains(text(), 'Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, 'quickFilterInput').send_keys(creditno)
    time.sleep(2)
    suppliercredit = danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div/div[11]").text
    suppliercredit = int(suppliercredit)
    print(suppliercredit)
    assert creditno == suppliercredit
    print("END>> Return to supplier report")


def __str__():
    return
