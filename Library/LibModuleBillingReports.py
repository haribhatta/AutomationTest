import time
from selenium.webdriver.common.keys import Keys
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By

########
# danpheEMR = AC.danpheEMR
AppName = GSV.appName


######## Dashboard
def getBillingDashboard(danpheEMR):
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
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(7)
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-home").click()
    time.sleep(9)

    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        sysgrosstotal = danpheEMR.find_element(By.XPATH, "//div[contains(text(),'i. Subtotal :')]").text
        print("sysgrosstotal:", sysgrosstotal)
        syssubtotal = sysgrosstotal.partition("Subtotal : ")[2]
        print("System subTotal-1:", syssubtotal)
        syssubtotal = syssubtotal.partition("\nii")[0]
        sysdiscountamount = sysgrosstotal.partition("ii. Discount Amount : ")[2]
        print(sysdiscountamount)
        sysdiscountamount = sysdiscountamount.partition(".")[0]
        sysdiscountamount = sysdiscountamount.replace(',', '')
        print("System discountAmount:", sysdiscountamount)

        sysreturnamount = danpheEMR.find_element(By.CSS_SELECTOR, "#totalsales > div:nth-child(4)").text
        print("sysreturnamount:", sysreturnamount)
        print("sysreturnamount:", sysreturnamount)
        sysreturnamount = sysreturnamount.partition(" : ")[2]
        # sysreturnamount = sysreturnamount.partition(".")[0]
        # sysreturnamount = sysreturnamount.replace(',', '')
        print("System returnAmount:", sysreturnamount)

        systotalamount = danpheEMR.find_element(By.XPATH, "//div[@id='totalsales']/div[5]/b").text
        print(systotalamount)
        systotalamount = systotalamount.partition("Rs. ")[2]
        # systotalamount = systotalamount.partition(".")[0]
        print("System totalAmount:", systotalamount)
        # systotalamount = systotalamount.replace(',', '')
        print("System totalAmount:", systotalamount)

        sysnetcashcollection = danpheEMR.find_element(By.CSS_SELECTOR, ".blinkAmount").text
        sysnetcashcollection = sysnetcashcollection.partition("(")[2]
        sysnetcashcollection = sysnetcashcollection.partition(")")[0]
        sysnetcashcollection = sysnetcashcollection.replace(',', '')
        print("System NetCashCollection:", sysnetcashcollection)

        sysprovisionalitems = danpheEMR.find_element(By.XPATH,
            "//td[contains(text(),'PROVISIONAL ITEMS')]/following-sibling::td").text
        sysprovisionalitems = sysprovisionalitems.partition("Rs. ")[2]
        sysprovisionalitems = sysprovisionalitems.partition(".")[0]
        sysprovisionalitems = sysprovisionalitems.replace(',', '')
        print("System Provisional Item:", sysprovisionalitems)

        sysunpaidcreditinvoices = danpheEMR.find_element(By.XPATH,
            "//td[contains(text(),'UNPAID CREDIT INVOICES')]/following-sibling::td").text
        sysunpaidcreditinvoices = sysunpaidcreditinvoices.partition("Rs. ")[2]
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
    print("Cash:", cash)
    print("discountpc:", discountpc)
    print("cashReturn:", cashReturn)
    print("Credit:", credit)
    print("CreditReturn:", creditReturn)
    print("settlement:", settlement)
    print("Provisional:", provisional)
    print("Provisionalcancel:", provisionalcancel)

    cash = int(cash)
    discountpc = int(discountpc)
    cashReturn = int(cashReturn)
    credit = int(credit)
    creditReturn = int(creditReturn)
    settlement = int(settlement)
    provisional = int(provisional)
    provisionalcancel = int(provisionalcancel)

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
        if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
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


########SalesDayBook
def getSalesDayBook(danpheEMR):
    print(">>START: getSalesDayBook")
    global syssales
    # global returnamount
    global sysgrosssales
    global syscreditsalestotal
    # global creditcancel
    global sysnetsalesamount
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Sales DayBook')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    syssales = danpheEMR.find_element(By.XPATH, "//div/div/table/tbody/tr/td").text
    print(syssales)
    sysgrosssales = danpheEMR.find_element(By.XPATH, "//div/div/table/tbody/tr/td[7]").text
    print(sysgrosssales)
    syscreditsalestotal = danpheEMR.find_element(By.XPATH, "//tr[2]/td[3]").text
    print(syscreditsalestotal)
    sysnetsalesamount = danpheEMR.find_element(By.XPATH, "//tr[2]/td[7]").text
    print(sysnetsalesamount)
    print("<<END: getSalesDayBook")


def preSystemSalesDayBook():
    print(">>START: preSystemSalesDayBook")
    global presyssales
    # global returnamount
    global presysgrosssales
    global presyscreditsalestotal
    # global presyscreditcancel
    global presysnetsalesamount
    presyssales = int(syssales)
    presysgrosssales = int(sysgrosssales)
    presyscreditsalestotal = int(syscreditsalestotal)
    presysnetsalesamount = int(sysnetsalesamount)
    print("<<END: preSystemSalesDayBook")


def verifySalesDayBook(cash, credit, cashreturn, creditreturn):
    print(">>START: verifySalesDayBook")
    assert int(syssales) == presyssales + cash + credit - cashreturn - creditreturn
    # assert int(sysgrosssales) == presysgrosssales + cash + credit
    assert int(syscreditsalestotal) == presyscreditsalestotal + credit - creditreturn
    # assert int(sysnetsalesamount) == presysnetsalesamount + cash + credit - cashreturn - creditreturn
    print("<<END: verifySalesDayBook")


# Module:Report: PatientCensus***************
def getPatientCensus(danpheEMR):
    print(">>START: getPatientCensus")
    global sysnoofcount
    global sysamount
    global sysunconfirmedcount
    global sysunconfirmedamount
    global sysconfirmedcount
    global sysconfirmedamount
    global systotalcount
    global systotalamount
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Patient Census')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    sysnoofcount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[1]").text
    print("sysnoofcount", sysnoofcount)
    sysamount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[2]").text
    print("sysamount", sysamount)
    sysunconfirmedcount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[3]").text
    print("sysunconfirmedcount", sysunconfirmedcount)
    sysunconfirmedamount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[4]").text
    print("sysunconfirmedamount", sysunconfirmedamount)
    sysconfirmedcount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[5]").text
    print("sysconfirmedcount", sysconfirmedcount)
    sysconfirmedamount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[6]").text
    print("sysconfirmedamount", sysconfirmedamount)
    systotalcount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[7]").text
    print("systotalcount", systotalcount)
    systotalamount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[8]").text
    print("systotalamount", systotalamount)
    print("<<END: getPatientCensus")


def preSystemPatientCensus():
    print(">>START: preSystemPatientCensus")
    global presysnoofcount
    global presysamount
    global presysunconfirmedcount
    global presysunconfirmedamount
    global presysconfirmedcount
    global presysconfirmedamount
    global presystotalcount
    global presystotalamount
    presysnoofcount = int(sysnoofcount)
    presysamount = int(sysamount)
    presysunconfirmedcount = int(sysunconfirmedcount)
    presysunconfirmedamount = int(sysunconfirmedamount)
    presysconfirmedcount = int(sysconfirmedcount)
    presysconfirmedamount = int(sysconfirmedamount)
    presystotalcount = int(systotalcount)
    presystotalamount = int(systotalamount)
    print("<<END: preSystemPatientCensus")


def verifyPatientCensus(cash, cashreturn, credit, creditreturn, provisional):
    print(">>START: verifyPatientCensus")
    assert int(sysnoofcount) == presysnoofcount + cash / cash
    print("presysamount", presysamount)
    print("sysamount", sysamount)
    print("cash", cash)
    assert int(sysamount) == int(int(presysamount) + int(cash))
    assert int(sysunconfirmedcount) == presysunconfirmedcount + provisional
    assert int(sysunconfirmedamount) == presysunconfirmedamount + provisional
    assert int(sysconfirmedcount) == presysconfirmedcount + credit
    assert int(sysconfirmedamount) == presysconfirmedamount + credit
    assert int(systotalcount) == presystotalcount + cash / cash + credit
    assert int(systotalamount) == presystotalamount + cash + credit
    print("<<END: verifyPatientCensus")


# Module:Report: Income Segregation Report*****************
def getIncomeSegregation(danpheEMR):
    print(">>START: getIncomeSegregation")
    global actualCashSales  # A
    global actualCreditSales  # B
    global actualGrossSales  # C
    global actualCashDiscount  # D
    global actualCreditDiscount  # E
    global actualTotalDiscount  # F
    global actualReturnCashSales  # G
    global actualReturnCreditSales  # H
    global actualTotalSalesReturn  # I
    global actualReturnCashDiscount  # J
    global actualReturnCreditDiscount  # K
    global actualTotalReturnDiscount  # L
    global actualNetSales  # M
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Income Segregation')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(15)
    # A
    actualCashSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Cash Sales')]/following-sibling::td)[1]").text
    actualCashSales = float(actualCashSales)
    print("actualCashSales", actualCashSales)
    # B
    actualCreditSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Credit Sales')]/following-sibling::td)[1]").text
    actualCreditSales = float(actualCreditSales)
    print("actualCreditSales", actualCreditSales)
    # C
    actualGrossSales = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Gross Sales')]/following-sibling::td").text
    actualGrossSales = float(actualGrossSales)
    print("actualGrossSales", actualGrossSales)
    # D
    actualCashDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Cash Discount')]/following-sibling::td)[1]").text
    actualCashDiscount = float(actualCashDiscount)
    print("actualCashDiscount", actualCashDiscount)
    # E
    actualCreditDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Credit Discount')]/following-sibling::td)[1]").text
    actualCreditDiscount = float(actualCreditDiscount)
    print("actualCreditDiscount", actualCreditDiscount)
    # F
    actualTotalDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Discount')]/following-sibling::td").text
    actualTotalDiscount = float(actualTotalDiscount)
    print("actualTotalDiscount", actualTotalDiscount)
    # G
    actualReturnCashSales = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return Cash Sales')]/following-sibling::td").text
    actualReturnCashSales = float(actualReturnCashSales)
    print("actualReturnCashSales", actualReturnCashSales)
    # H
    actualReturnCreditSales = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return Credit Sales')]/following-sibling::td").text
    actualReturnCreditSales = float(actualReturnCreditSales)
    print("actualReturnCreditSales", actualReturnCreditSales)
    # I
    actualTotalSalesReturn = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Sales Return')]/following-sibling::td").text
    actualTotalSalesReturn = float(actualTotalSalesReturn)
    print("actualTotalSalesReturn", actualTotalSalesReturn)
    # j
    actualReturnCashDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return Cash Discount')]/following-sibling::td").text
    actualReturnCashDiscount = float(actualReturnCashDiscount)
    print("actualReturnCashDiscount", actualReturnCashDiscount)
    # k
    actualReturnCreditDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return Credit Discount')]/following-sibling::td").text
    actualReturnCreditDiscount = float(actualReturnCreditDiscount)
    print("actualReturnCreditDiscount", actualReturnCreditDiscount)
    # l
    actualTotalReturnDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Return Discount')]/following-sibling::td").text
    actualTotalReturnDiscount = float(actualTotalReturnDiscount)
    print("actualTotalReturnDiscount", actualTotalReturnDiscount)
    # m
    actualNetSales = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Net Sales')]/following-sibling::td").text
    actualNetSales = float(actualNetSales)
    print("actualNetSales", actualNetSales)
    print("<<END getIncomeSegregation")


def preSystemIncomeSegregation():
    print(">>START: preSystemIncomeSegregation")
    global preCashSales  # A
    global preCreditSales  # B
    global preGrossSales  # C
    global preCashDiscount  # D
    global preCreditDiscount  # E
    global preTotalDiscount  # F
    global preReturnCashSales  # G
    global preReturnCreditSales  # H
    global preTotalSalesReturn  # I
    global preReturnCashDiscount  # J
    global preReturnCreditDiscount  # K
    global preTotalReturnDiscount  # L
    global preNetSales  # M
    preCashSales = actualCashSales
    preCreditSales = actualCreditSales
    preGrossSales = actualGrossSales
    preCashDiscount = actualCashDiscount
    preCreditDiscount = actualCreditDiscount
    preTotalDiscount = actualTotalDiscount
    preReturnCashSales = actualReturnCashSales
    preReturnCreditSales = actualReturnCreditSales
    preTotalSalesReturn = actualTotalSalesReturn
    preReturnCashDiscount = actualReturnCashDiscount
    preReturnCreditDiscount = actualReturnCreditDiscount
    preTotalReturnDiscount = actualTotalReturnDiscount
    preNetSales = actualNetSales
    print("<<END preSystemIncomeSegregation")


def verifyIncomeSegregation(cash, cashReturn, credit, creditReturn, discount, provision):
    print(">>START: verifyIncomeSegregation")
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        expectedCashSales = preCashSales + cash
        print("expectedCashSales:", expectedCashSales)
        assert expectedCashSales == actualCashSales
        expectedCreditSales = preCreditSales + credit
        assert expectedCreditSales == actualCreditSales
        expectedGrossSales = preGrossSales + cash + credit
        assert expectedGrossSales == actualGrossSales
        expectedCashDiscount = preCashDiscount + discount
        assert expectedCashDiscount == actualCashDiscount
        expectedCreditDiscount = preCreditDiscount + discount
        assert expectedCreditDiscount == actualCreditDiscount
        expectedTotalDiscount = preTotalDiscount + discount
        assert expectedTotalDiscount == actualTotalDiscount
        expectedReturnCashSales = preReturnCashSales + cashReturn
        assert expectedReturnCashSales == actualReturnCashSales
        expectedReturnCreditSales = preReturnCreditSales + creditReturn
        assert expectedReturnCreditSales == actualReturnCreditSales
        expectedTotalSalesReturn = preTotalSalesReturn + cashReturn + creditReturn
        assert expectedTotalSalesReturn == actualTotalSalesReturn
        expectedReturnCashDiscount = preReturnCashDiscount + discount
        assert expectedReturnCashDiscount == actualReturnCashDiscount
        expectedReturnCreditDiscount = preReturnCreditDiscount + discount
        assert expectedReturnCreditDiscount == actualReturnCreditDiscount
        expectedTotalReturnDiscount = preTotalReturnDiscount + discount
        assert expectedTotalReturnDiscount == actualTotalReturnDiscount
        expectedNetSales = preNetSales + cash + credit - cashReturn - creditReturn
        assert expectedNetSales == actualNetSales
        print("<<END verifyIncomeSegregation")


######## Patient Credit Summary Report
def getPatientCreditSummary(danpheEMR):
    print(">>START: getPatientCreditSummary")
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Patient Credit Summary')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    print("<<END: getPatientCreditSummary")


def preSystemPatientCreditSummary():
    print(">>START: preSystemPatientCreditSummary")
    print("<<END: preSystemPatientCreditSummary")


def verifyPatientCreditSummary():
    print(">>START: verifyPatientCreditSummary")
    print("<<END: verifyPatientCreditSummary")


######## Doctor Summary Report
def getDoctorSummary(danpheEMR, doctor):
    print(">>START: getDoctorSummary")
    global sysgrosstotal
    global sysdiscountamount
    global sysreturnamount
    global sysnetsales
    global sysprovisionalamount
    global syscancelamount
    global syscreditamount
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(7)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Doctor Summary')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/input").send_keys(doctor)
    danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/input").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    sysgrosstotal = danpheEMR.find_element(By.CSS_SELECTOR, ".table tr:nth-child(1) > td:nth-child(2)").text
    print("sysgrosstotal", sysgrosstotal)
    sysdiscountamount = danpheEMR.find_element(By.CSS_SELECTOR, ".table tr:nth-child(1) > td:nth-child(4)").text
    print("sysdiscountamount", sysdiscountamount)
    sysreturnamount = danpheEMR.find_element(By.CSS_SELECTOR, ".table tr:nth-child(1) > td:nth-child(6)").text
    print("sysreturnamount", sysreturnamount)
    sysnetsales = danpheEMR.find_element(By.CSS_SELECTOR, "tbody:nth-child(1) td:nth-child(8)").text
    print("sysnetsales", sysnetsales)
    sysprovisionalamount = danpheEMR.find_element(By.CSS_SELECTOR,
        "tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)").text
    print("sysprovisionalamount", sysprovisionalamount)
    syscancelamount = danpheEMR.find_element(By.CSS_SELECTOR,
        "tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4)").text
    print("cancel amount", syscancelamount)
    syscreditamount = danpheEMR.find_element(By.CSS_SELECTOR,
        "tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6)").text
    print("syscreditamount", syscreditamount)
    print("<<END: getDoctorSummary")


def preSystemDoctorSummary():
    print(">>START: preSystemDoctorSummary")
    global presysgrosstotal
    global presysdiscountamount
    global presysreturnamount
    global presysnetsales
    global presysprovisionalamount
    global presyscancelamount
    global presyscreditamount
    presysgrosstotal = int(sysgrosstotal)
    presysdiscountamount = int(sysdiscountamount)
    presysreturnamount = int(sysreturnamount)
    presysnetsales = int(sysnetsales)
    presysprovisionalamount = int(sysprovisionalamount)
    presyscancelamount = int(syscancelamount)
    presyscreditamount = int(syscreditamount)
    print("<<END: preSystemDoctorSummary")


def verifyDoctorSummary(cash, cashreturn, credit, creditreturn, discount, provisional, provisionalcancel):
    print(">>START: verifyDoctorSummary")
    assert int(sysgrosstotal) == presysgrosstotal + cash + credit
    assert int(sysdiscountamount) == presysdiscountamount + discount
    assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
    assert int(sysnetsales) == presysnetsales + cash + credit - discount - cashreturn - creditreturn
    assert int(sysprovisionalamount) == presysprovisionalamount + provisional
    assert int(syscancelamount) == presyscancelamount + provisionalcancel
    assert int(syscreditamount) == presyscreditamount + credit - creditreturn
    print("<<END: verifyDoctorSummary")


# Module:Billing_Report: Discount Report**********************
def verifyDiscountReport(danpheEMR, HospitalNo, cash, discountpc):
    print(">>START: verifyDiscountReport")
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'DiscountReport')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    date = danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div/span").text
    print(date)
    systemReceiptNo = danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div[2]").text
    print("systemReceiptNo:", systemReceiptNo)
    systemHospitalNo = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[3]").text
    print("systemHospitalNo", systemHospitalNo)
    assert HospitalNo == systemHospitalNo
    systemSubTotal = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[5]").text
    print("systemSubTotal:", systemSubTotal)
    systemSubTotal = int(systemSubTotal)
    assert cash == systemSubTotal
    systemDiscount = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[6]").text
    print("systemDiscount:", systemDiscount)
    systemDiscount = int(systemDiscount)
    ###
    print("discountpc:", discountpc)
    discountpc = discountpc.partition("%)")[0]
    discountpc = discountpc.partition("(")[2]
    discountpc = int(discountpc)
    print("discountpc:", discountpc)
    ###
    expectedDiscount = (discountpc * cash / 100)
    print("expectedDiscount:", expectedDiscount)
    assert systemDiscount == expectedDiscount
    tax = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[7]").text
    print(tax)
    systemTotalAmount = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[8]/span").text
    print("systemTotalAmount:", systemTotalAmount)
    systemTotalAmount = int(systemTotalAmount)
    expectedTotalAmount = int(systemSubTotal) - int(systemDiscount)
    assert systemTotalAmount == expectedTotalAmount
    user = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[9]").text
    print("user:", user)
    print("<<END: verifyDiscountReport")


# Module:Billing report: Deposit Report*********************
def verifyDepositBalanceReport(danpheEMR, HospitalNo, deposit):
    print(">>START: verifyDepositBalanceReport")
    # if appPort == '81':
    #    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    #    time.sleep(3)
    #    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    #    time.sleep(2)
    #    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Deposit Balance')]").click()
    #    time.sleep(3)
    #    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    #    time.sleep(3)
    #    hospitalno = danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div[2]").text
    #    #assert HospitalNo == hospitalno
    #    depositamt = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[4]").text
    #    x = int(depositamt)
    #    y = int(deposit)
    #    print("x", x)
    #    print("y", y)
    #    assert x == y
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
        time.sleep(3)
        danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//i[contains(.,'Deposit Balance')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        hospitalno = danpheEMR.find_element(By.XPATH, "//div[3]/div[2]/div/div/div/div[2]").text
        # assert HospitalNo == hospitalno
        time.sleep(4)
        depositamt = danpheEMR.find_element(By.XPATH, "(//div[@col-id='DepositBalance'])[2]").text
        x = int(depositamt)
        y = int(deposit)
        print("x", x)
        print("y", y)
        assert x == y
    print("<<END: BalanceReport")


# Module: Billing report: Department Summary Report**********
def getDepartmentSummary(danpheEMR):
    global sysgrosstotal
    global sysdiscountamount
    global sysreturnamount
    global sysnetsales
    global sysprovisionalamount
    global syscancelamount
    global syscreditamount
    # if appPort == '81':
    #    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    #    time.sleep(2)
    #    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    #    time.sleep(2)
    #    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Department Summary')]").click()
    #    time.sleep(3)
    #    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").clear()
    #    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys("OPD")
    #    time.sleep(3)
    #    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(
    #       Keys.ARROW_DOWN)
    #    time.sleep(2)
    #    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(Keys.TAB)
    #    time.sleep(3)
    #    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(
    #       Keys.RETURN)
    #    time.sleep(2)
    #    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    #    time.sleep(9)
    #    sysgrosstotal = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td").text
    #    print(sysgrosstotal)
    #    sysdiscountamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td[2]").text
    #    print(sysdiscountamount)
    #    sysreturnamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td[3]").text
    #    print(sysreturnamount)
    #    sysnetsales = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td[4]").text
    #    print(sysnetsales)
    #    sysprovisionalamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr[2]/td").text
    #    print(sysprovisionalamount)
    #    syscancelamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr[2]/td[2]").text
    #    print(syscancelamount)
    #    syscreditamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr[2]/td[3]").text
    #    print(syscreditamount)
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//i[contains(.,'Department Summary')]").click()
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").clear()
        danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(
            "Department OPD")
        time.sleep(3)
        # danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(
        #   Keys.ARROW_DOWN)
        # time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(Keys.TAB)
        time.sleep(3)
        danpheEMR.find_element(By.XPATH, "//input[@placeholder='Enter Service Department Name']").send_keys(
            Keys.RETURN)
        time.sleep(2)
        danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
        time.sleep(9)
        sysgrosstotal = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td").text
        print(sysgrosstotal)
        sysdiscountamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td[2]").text
        print(sysdiscountamount)
        sysreturnamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td[3]").text
        print(sysreturnamount)
        sysnetsales = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr/td[4]").text
        print(sysnetsales)
        sysprovisionalamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr[2]/td").text
        print(sysprovisionalamount)
        syscancelamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr[2]/td[2]").text
        print(syscancelamount)
        syscreditamount = danpheEMR.find_element(By.XPATH, "//table[2]/tbody/tr[2]/td[3]").text
        print(syscreditamount)


def preSystemDepartmentSummary():
    global presysgrosstotal
    global presysdiscountamount
    global presysreturnamount
    global presysnetsales
    global presysprovisionalamount
    global presyscancelamount
    global presyscreditamount
    presysgrosstotal = int(sysgrosstotal)
    presysdiscountamount = int(sysdiscountamount)
    presysreturnamount = int(sysreturnamount)
    presysnetsales = int(sysnetsales)
    presysprovisionalamount = int(sysprovisionalamount)
    presyscancelamount = int(syscancelamount)
    presyscreditamount = int(syscreditamount)


def verifyDepartmentSummary(cash, cashreturn, credit, creditreturn, discount, provisional, provisionalcancel):
    assert int(sysgrosstotal) == presysgrosstotal + cash + credit
    assert int(sysdiscountamount) == presysdiscountamount + discount
    assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
    assert int(sysnetsales) == presysnetsales - discount - cashreturn - creditreturn + cash + credit
    assert int(sysprovisionalamount) == presysprovisionalamount + provisional
    assert int(syscancelamount) == presyscancelamount + provisionalcancel
    assert int(syscreditamount) == presyscreditamount + credit - creditreturn


# Module:Billing_Report: User Collection Report***********
def getUserCollectionReport(danpheEMR, user):
    global actualNetCashCollection
    global actualGrossTotalSales
    global actualDiscount
    global actualReturnSubTotal
    global actualReturnDiscount
    global actualReturnAmount
    global actualNetSales
    global actualLessCreditAmount
    global actualAddDepositReceived
    global actualLessDepositRefund
    global actualAddCollectionFromReceivables
    global actualLessCashDiscount
    global actualOtherPaymentsGiven
    global actualTotalCollection
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'User Collection')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/input").send_keys(user)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/input").send_keys(Keys.TAB)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    # actualNetCashCollection = danpheEMR.find_element(By.CSS_SELECTOR, ".blinkAmount").text
    actualNetCashCollection = danpheEMR.find_element(By.XPATH, "//h4[contains(text(),'Net Cash Collection')]").text
    print("actualNetCashCollection:", actualNetCashCollection)
    actualNetCashCollection = actualNetCashCollection.partition("( ")[2]
    actualNetCashCollection = actualNetCashCollection.partition(")")[0]
    actualNetCashCollection = float(actualNetCashCollection)
    print("actualNetCashCollection:", actualNetCashCollection)
    actualGrossTotalSales = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Gross Total Sales')]//following-sibling::td").text
    print("actualGrossTotalSales:", actualGrossTotalSales)
    actualGrossTotalSales = float(actualGrossTotalSales)
    print("actualGrossTotalSales:", actualGrossTotalSales)
    actualDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Discount')])[1]//following-sibling::td").text
    print("actualDiscount:", actualDiscount)
    actualDiscount = float(actualDiscount)
    print("actualDiscount:", actualDiscount)
    actualReturnSubTotal = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return SubTotal')]//following-sibling::td").text
    print("actualReturnSubTotal:", actualReturnSubTotal)
    actualReturnSubTotal = float(actualReturnSubTotal)
    print("actualReturnSubTotal:", actualReturnSubTotal)
    actualReturnDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return Discount')]//following-sibling::td").text
    print("actualReturnDiscount:", actualReturnDiscount)
    actualReturnDiscount = float(actualReturnDiscount)
    print("actualReturnDiscount:", actualReturnDiscount)
    actualReturnAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Return Amount')]//following-sibling::td").text
    print("actualReturnAmount:", actualReturnAmount)
    actualReturnAmount = float(actualReturnAmount)
    print("actualReturnAmount:", actualReturnAmount)
    actualNetSales = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'Net Sales')]//following-sibling::td").text
    print("actualNetSales:", actualNetSales)
    actualNetSales = float(actualNetSales)
    print("actualNetSales:", actualNetSales)
    actualLessCreditAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Less Credit Amount')]//following-sibling::td").text
    print("actualLessCreditAmount:", actualLessCreditAmount)
    actualLessCreditAmount = float(actualLessCreditAmount)
    print("actualLessCreditAmount:", actualLessCreditAmount)
    actualAddDepositReceived = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Add Deposit Received')]//following-sibling::td").text
    print("actualAddDepositReceived:", actualAddDepositReceived)
    actualAddDepositReceived = float(actualAddDepositReceived)
    print("actualAddDepositReceived:", actualAddDepositReceived)
    actualLessDepositRefund = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Less Deposit Refund')]//following-sibling::td").text
    print("actualLessDepositRefund:", actualLessDepositRefund)
    actualLessDepositRefund = float(actualLessDepositRefund)
    print("actualLessDepositRefund:", actualLessDepositRefund)
    actualAddCollectionFromReceivables = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Add Collection From Receivables')]//following-sibling::td").text
    print("actualAddCollectionFromReceivables:", actualAddCollectionFromReceivables)
    actualAddCollectionFromReceivables = float(actualAddCollectionFromReceivables)
    print("actualAddCollectionFromReceivables:", actualAddCollectionFromReceivables)
    actualLessCashDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Less Cash Discount')]//following-sibling::td").text
    print("actualLessCashDiscount:", actualLessCashDiscount)
    actualLessCashDiscount = float(actualLessCashDiscount)
    print("actualLessCashDiscount:", actualLessCashDiscount)
    actualOtherPaymentsGiven = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Other Payments Given')]//following-sibling::td").text
    print("actualOtherPaymentsGiven:", actualOtherPaymentsGiven)
    actualOtherPaymentsGiven = float(actualOtherPaymentsGiven)
    print("actualOtherPaymentsGiven:", actualOtherPaymentsGiven)
    actualTotalCollection = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),' Total Collection ')]//following-sibling::td").text
    print("actualTotalCollection:", actualTotalCollection)
    actualTotalCollection = float(actualTotalCollection)
    print("actualTotalCollection:", actualTotalCollection)


def preSystemUserCollectionReport():
    global presysnetcashcollection
    global presysgrosstotalsales
    global presysdiscount
    global presysreturnsubtotal
    global presysreturndiscount
    global presysreturnamount
    global presysnetsales
    global presyslesscreditamount
    global presysadddepositreceived
    global presyslessdepositrefund
    global presysaddcollectionfromreceivables
    global presyslesscashdiscount
    global preOtherPaymentsGiven
    global presystotalcollection
    presysnetcashcollection = actualNetCashCollection
    presysgrosstotalsales = actualGrossTotalSales
    presysdiscount = actualDiscount
    presysreturnsubtotal = actualReturnSubTotal
    presysreturndiscount = actualReturnDiscount
    presysreturnamount = actualReturnAmount
    presysnetsales = actualNetSales
    presyslesscreditamount = actualLessCreditAmount
    presysadddepositreceived = actualAddDepositReceived
    presyslessdepositrefund = actualLessDepositRefund
    presysaddcollectionfromreceivables = actualAddCollectionFromReceivables
    presyslesscashdiscount = actualLessCashDiscount
    preOtherPaymentsGiven = actualOtherPaymentsGiven
    presystotalcollection = actualTotalCollection


def verifyUserCollectionReport(cash, cashreturn, credit, creditreturn, tradeDiscount, cashDiscount, deposit,
                               depositreturn, creditsettlement, provisional, provisionalcancel):
    expectedNetCashCollection = presysnetcashcollection + cash - cashreturn + deposit - depositreturn + creditsettlement - tradeDiscount - cashDiscount
    print("expectedNetCashCollection:", expectedNetCashCollection)
    assert expectedNetCashCollection == actualNetCashCollection
    expectedGrossTotalSales = presysgrosstotalsales + cash + credit + creditsettlement
    print("expectedGrossTotalSales:", expectedGrossTotalSales)
    assert expectedGrossTotalSales == actualGrossTotalSales
    expectedDiscount = presysdiscount + tradeDiscount
    print("expectedDiscount:", expectedDiscount)
    assert actualDiscount == expectedDiscount
    expectedReturnSubTotal = presysreturnsubtotal + cashreturn + creditreturn
    print("expectedReturnSubTotal:", expectedReturnSubTotal)
    assert expectedReturnSubTotal == actualReturnSubTotal
    expectedReturnDiscount = presysreturndiscount + tradeDiscount
    print("expectedReturnDiscount:", expectedReturnDiscount)
    assert expectedReturnDiscount == actualReturnDiscount
    expectedReturnAmount = presysreturnamount + cashreturn + creditreturn - tradeDiscount
    print("expectedReturnAmount:", expectedReturnAmount)
    assert expectedReturnAmount == actualReturnAmount
    expectedNetSales = presysnetsales + cash - cashreturn + credit - creditreturn - tradeDiscount + creditsettlement
    print("expectedNetSales:", expectedNetSales)
    assert expectedNetSales == actualNetSales
    expectedLessCreditAmount = presyslesscreditamount + credit - creditreturn + creditsettlement
    print("expectedLessCreditAmount:", expectedLessCreditAmount)
    assert expectedLessCreditAmount == actualLessCreditAmount
    expectedAddDepositReceived = presysadddepositreceived + deposit
    print("expectedAddDepositReceived:", expectedAddDepositReceived)
    assert expectedAddDepositReceived == actualAddDepositReceived
    expectedLessDepositRefund = presyslessdepositrefund + depositreturn
    print("expectedLessDepositRefund:", expectedLessDepositRefund)
    assert expectedLessDepositRefund == actualLessDepositRefund
    expectedAddCollectionFromReceivables = presysaddcollectionfromreceivables + creditsettlement
    print("expectedAddCollectionFromReceivables:", expectedAddCollectionFromReceivables)
    assert expectedAddCollectionFromReceivables == actualAddCollectionFromReceivables
    expectedLessCashDiscount = presyslesscashdiscount + cashDiscount
    print("expectedLessCashDiscount:", expectedLessCashDiscount)
    assert expectedLessCashDiscount == actualLessCashDiscount
    expectedOtherPayments = preOtherPaymentsGiven
    print("expectedOtherPayments:", expectedOtherPayments)
    assert expectedOtherPayments == actualOtherPaymentsGiven
    expectedTotalCollection = presystotalcollection + cash - cashreturn + deposit - depositreturn + creditsettlement - tradeDiscount - cashDiscount
    print("expectedTotalCollection:", expectedTotalCollection)
    print("actualTotalCollection:", actualTotalCollection)
    assert actualTotalCollection == expectedTotalCollection


# Module:Admission_Report: Total Admitted Patients Report**********************
def verifyTotalAdmittedPatients(danpheEMR, HospitalNo):
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Admission").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Admitted Patient").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    time.sleep(5)
    hospitalno = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[3]").text
    assert hospitalno == HospitalNo


######## Report: Total Items Bill
def getTotalItemsBill(danpheEMR):
    print(">>START: getTotalItemsBill")
    global CashSales
    global CreditSales
    global GrossSales
    global CashDiscount
    global CreditDiscount
    global TotalDiscount
    global ReturnCashSales
    global ReturnCreditSales
    global TotalSalesReturn
    global ReturnCashDiscount
    global ReturnCreditDiscount
    global TotalReturnDiscount
    global NetSales
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Total Items Bill')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)

    CashSales = danpheEMR.find_element(By.XPATH, "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[2]/td[3]").text
    CashSales = CashSales.replace(",", "")
    print("Cash Sale is : ", CashSales)
    CreditSales = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[3]/td[3]").text
    CreditSales = CreditSales.replace(",", "")
    print("Credit Sale is :", CreditSales)
    GrossSales = danpheEMR.find_element(By.XPATH, "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[4]/td[3]").text
    GrossSales = GrossSales.replace(",", "")
    print("Gross Sale is :", GrossSales)
    CashDiscount = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[5]/td[3]").text
    CashDiscount = CashDiscount.replace(",", "")
    print("Cash Discount is : ", CashDiscount)
    CreditDiscount = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[6]/td[3]").text
    CreditDiscount = CreditDiscount.replace(",", "")
    print("Credit Discount is : ", CreditDiscount)
    TotalDiscount = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[7]/td[3]").text
    TotalDiscount = TotalDiscount.replace(",", "")
    print("Total Discount is :", TotalDiscount)
    ReturnCashSales = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[8]/td[3]").text
    ReturnCashSales = ReturnCashSales.replace(",", "")
    print("Cash Sale Returned is :", ReturnCashSales)
    ReturnCreditSales = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[9]/td[3]").text
    ReturnCreditSales = ReturnCreditSales.replace(",", "")
    print("Credit Sale Returned is : ", ReturnCreditSales)
    TotalSalesReturn = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[10]/td[3]").text
    TotalSalesReturn = TotalSalesReturn.replace(",", "")
    print("Total Sale Returned is :", TotalSalesReturn)
    ReturnCashDiscount = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[11]/td[3]").text
    ReturnCashDiscount = ReturnCashDiscount.replace(",", "")
    print("Cash Discount Returned is : ", ReturnCashDiscount)
    ReturnCreditDiscount = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[12]/td[3]").text
    ReturnCreditDiscount = ReturnCreditDiscount.replace(",", "")
    print("Credit Discount Returned is ", ReturnCreditDiscount)
    TotalReturnDiscount = danpheEMR.find_element(By.XPATH,
        "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[13]/td[3]").text
    TotalReturnDiscount = TotalReturnDiscount.replace(",", "")
    print("Total Discount Returned is :", TotalReturnDiscount)
    NetSales = danpheEMR.find_element(By.XPATH, "//*[@id='dvSummary_TotalItemBills']/div/table/tbody/tr[14]/td[3]").text
    NetSales = NetSales.replace(",", "")
    print("Net Sales is : ", NetSales)

    # return type('', (object,), {"system return quantiy": sysreturnQty, "Return Subtotal": sysreturnSubtotal})()
    print("<<END: getTotalItemsBill")


def preSystemTotalItemsBill():
    print(">>START: preSystemTotalItemsBill")
    global preCashSales
    global preCreditSales
    global preGrossSales
    global preCashDiscount
    global preCreditDiscount
    global preTotalDiscount
    global preReturnCashSales
    global preReturnCreditSales
    global preTotalSalesReturn
    global preReturnCashDiscount
    global preReturnCreditDiscount
    global preTotalReturnDiscount
    global preNetSales

    preCashSales = int(CashSales)
    print("Previous Cash Sales is :", preCashSales)
    preCreditSales = int(CreditSales)
    print("Previous Credit Sales is :", preCreditSales)
    preGrossSales = int(GrossSales)
    print("Previous Gross Sales is :", preGrossSales)
    preCashDiscount = int(CashDiscount)
    print("Previous Cash Discount is :", preCashDiscount)
    preCreditDiscount = int(CreditDiscount)
    print("Previous Credit Discount is :", preCreditDiscount)
    preTotalDiscount = int(TotalDiscount)
    print("Previous Total Discount is :", preTotalDiscount)
    preReturnCashSales = int(ReturnCashSales)
    print("Previous  Returned Cash Sales is :", preReturnCashSales)
    preReturnCreditSales = int(ReturnCreditSales)
    print("Previous Returned Credit Sales is :", preReturnCreditSales)
    preTotalSalesReturn = int(TotalSalesReturn)
    print("Previous Total Sales Return is :", preTotalSalesReturn)
    preReturnCashDiscount = int(ReturnCashDiscount)
    print("Previous Returned Cash Discount is :", preReturnCashDiscount)
    preReturnCreditDiscount = int(ReturnCreditDiscount)
    print("Previous Returned Credit Discount is :", preReturnCreditDiscount)
    preTotalReturnDiscount = int(TotalReturnDiscount)
    print("Previous Total Returned Discount is :", preTotalReturnDiscount)
    preNetSales = int(NetSales)
    print("Previous Net Cash Sales is :", preNetSales)

    print("<<END: preSystemTotalItemsBill")


def verifyTotalItemsBill(returnamt):
    global CashSales
    global CreditSales
    global GrossSales
    global CashDiscount
    global CreditDiscount
    global TotalDiscount
    global ReturnCashSales
    global ReturnCreditSales
    global TotalSalesReturn
    global ReturnCashDiscount
    global ReturnCreditDiscount
    global TotalReturnDiscount
    global NetSales

    print(">>START: verifyTotalItemsBill")
    if returnamt > 0:
        assert int(GrossSales) == preGrossSales \
            # + int(CashSales) + int(CreditSales)
        assert int(TotalDiscount) == (preTotalDiscount)
        # + CashDiscount + CreditDiscount)
        assert int(TotalSalesReturn) == (preTotalSalesReturn + returnamt)
        # + ReturnCashSales + ReturnCreditSales)
        assert int(TotalReturnDiscount) == preTotalReturnDiscount
        # ReturnCashDiscount + ReturnCreditDiscount)
        assert int(NetSales) == (preNetSales - returnamt)
        # GrossSales - TotalDiscount - TotalSalesReturn + TotalReturnDiscount)
    print("<<END: verifyTotalItemsBill")


######## Report: Return Bill
def getReturnBillReport(danpheEMR):
    print(">>START: getReturnBillReport")
    global actualTotalReturnAmount
    global actualTotalReturnDiscount
    global actualNetReturnAmount

    global CashSales
    global CreditSales
    global GrossSales
    global CashDiscount
    global CreditDiscount
    global TotalDiscount
    global ReturnCashSales
    global ReturnCreditSales
    global TotalSalesReturn
    global ReturnCashDiscount
    global ReturnCreditDiscount
    global TotalReturnDiscount
    global NetSales
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Return Bills')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    # Summary #
    actualTotalReturnAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Return Amount')]//following-sibling::td").text
    print("actualTotalReturnAmount: ", actualTotalReturnAmount)
    actualTotalReturnAmount = float(actualTotalReturnAmount)
    actualTotalReturnDiscount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Total Return Discount')]//following-sibling::td").text
    print("actualTotalReturnDiscount", actualTotalReturnDiscount)
    actualTotalReturnDiscount = float(actualTotalReturnDiscount)
    actualNetReturnAmount = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),'Net Return Amount')]//following-sibling::td").text
    print("actualNetReturnAmount: ", actualNetReturnAmount)
    actualNetReturnAmount = float(actualNetReturnAmount)
    print("<<END: getReturnBillReport")


def preReturnBillReprot():
    print(">>START: preReturnBillReprot")
    global preTotalReturnAmount
    global preTotalReturnDiscount
    global preNetReturnAmount
    preTotalReturnAmount = actualTotalReturnAmount
    preTotalReturnDiscount = actualTotalReturnDiscount
    preNetReturnAmount = actualNetReturnAmount


def verifyReturnBillReport(returnamt, returnDiscount):
    print(">>START: verifyReturnBillReport")
    expectedTotalReturnAmount = preTotalReturnAmount + returnamt
    assert actualTotalReturnAmount == expectedTotalReturnAmount
    expectedTotalReturnDiscount = preTotalReturnDiscount + returnDiscount
    assert actualTotalReturnDiscount == expectedTotalReturnDiscount
    expectedNetReturnAmount = preNetReturnAmount + returnamt - returnDiscount
    assert actualNetReturnAmount == expectedNetReturnAmount
    print("<<END: verifyReturnBillReport")


######## Report: Cancel Bill
def verifyCancelBillReport(danpheEMR, HospitalNo, expectedTotalCancelAmt):
    print(">>START: verifyCancelBillReport")
    global actualHospitalNo
    expectedTotalCancelAmt = float(expectedTotalCancelAmt)
    print("expectedTotalCancelAmt:", expectedTotalCancelAmt)
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Cancel Bill')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(HospitalNo)
    actualHospitalNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='HospitalNo'])[2]").text
    print("actualHospitalNo : ", actualHospitalNo)
    assert actualHospitalNo == HospitalNo
    actualTotalCancelAmt = danpheEMR.find_element(By.XPATH, "(//div[@col-id='TotalAmount'])[2]").text
    actualTotalCancelAmt = float(actualTotalCancelAmt)
    print("actualTotalCancelAmt:", actualTotalCancelAmt)
    assert actualTotalCancelAmt == expectedTotalCancelAmt
    print("<<END: verifyCancelBillReport")


######## Report: EHS Bill
def getEHSBillReport(danpheEMR):
    print(">>START: getEHSBillReport")
    global actualCashSales  # A
    global actualCreditSales  # B
    global actualGrossSalesApB  # C
    global actualCashDiscount  # D
    global actualCreditDiscount  # E
    global actualTotalDiscountDpE  # F
    global actualReturnCashSales  # G
    global actualReturnCreditSales  # H
    global actualTotalSalesReturn  # I
    global actualReturnCashDiscount  # J
    global actualReturnCreditDiscount  # K
    global actualTotalReturnDiscount  # L
    global actualNetSales  # M
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'EHS Bill')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    # A
    actualCashSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Cash Sales')])[1]//following-sibling::td").text
    print("actualCashSales: ", actualCashSales)
    # B
    actualCreditSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Credit Sales')])[1]//following-sibling::td").text
    print("actualCreditSales: ", actualCreditSales)
    # C
    actualGrossSalesApB = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Gross Sales')])[1]//following-sibling::td").text
    print("actualGrossSalesApB: ", actualGrossSalesApB)
    # D
    actualCashDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Cash Discount')])[1]//following-sibling::td").text
    print("actualCashDiscount: ", actualCashDiscount)
    # E
    actualCreditDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Credit Discount')])[1]//following-sibling::td").text
    print("actualCreditDiscount: ", actualCreditDiscount)
    # F
    actualTotalDiscountDpE = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Total Discount')])[1]//following-sibling::td").text
    print("actualTotalDiscountDpE: ", actualTotalDiscountDpE)
    # G
    actualReturnCashSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Return Cash Sales')])[1]//following-sibling::td").text
    print("actualReturnCashSales: ", actualReturnCashSales)
    # H
    actualReturnCreditSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Return Credit Sales')])[1]//following-sibling::td").text
    print("actualReturnCreditSales: ", actualReturnCreditSales)
    # I
    actualTotalSalesReturn = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Total Sales Return')])[1]//following-sibling::td").text
    print("actualTotalSalesReturn: ", actualTotalSalesReturn)
    # J
    actualReturnCashDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Return Cash Discount')])[1]//following-sibling::td").text
    print("actualReturnCashDiscount: ", actualReturnCashDiscount)
    # K
    actualReturnCreditDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Return Credit Discount')])[1]//following-sibling::td").text
    print("actualReturnCreditDiscount: ", actualReturnCreditDiscount)
    # L
    actualTotalReturnDiscount = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Total Return Discount')])[1]//following-sibling::td").text
    print("actualTotalReturnDiscount: ", actualTotalReturnDiscount)
    # M
    actualNetSales = danpheEMR.find_element(By.XPATH,
        "(//td[contains(text(),'Net Sales')])[1]//following-sibling::td").text
    print("actualNetSales: ", actualNetSales)

    print("<<END: getEHSBillReport")


def preEHSBillReport():
    print(">>START: preEHSBillReport")
    global preCashSales
    global preCreditSales
    global preGrossSalesApB
    global preCashDiscount
    global preCreditDiscount
    global preTotalDiscountDpE
    global preReturnCashSales
    global preReturnCreditSales
    global preTotalSalesReturn
    global preReturnCashDiscount
    global preReturnCreditDiscount
    global preTotalReturnDiscount
    global preNetSales

    preCashSales = actualCashSales
    preCreditSales = actualCreditSales
    preGrossSalesApB = actualGrossSalesApB
    preCashDiscount = actualCashDiscount
    preCreditDiscount = actualCreditDiscount
    preTotalDiscountDpE = actualTotalDiscountDpE
    preReturnCashSales = actualReturnCashSales
    preReturnCreditSales = actualReturnCreditSales
    preTotalSalesReturn = actualTotalSalesReturn
    preReturnCashDiscount = actualReturnCashDiscount
    preReturnCreditDiscount = actualReturnCreditDiscount
    preTotalReturnDiscount = actualTotalReturnDiscount
    preNetSales = actualNetSales

    print("<<END: preEHSBillReport")


def verifyEHSBillReport():
    print(">>START: verifyEHSBillReport")

    print("<<END: verifyEHSBillReport")


def getSummaryReport(danpheEMR):
    global row
    print(">>START: getSummaryReport")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Handover").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Summary Report").click()
    time.sleep(3)
    records = danpheEMR.find_element(By.XPATH, "//div[@class='page-items']").text
    print("records:", records)
    records = records.partition("Showing ")[2]
    print("records:", records)
    records = records.partition(" /")[0]
    records = int(records)
    print("records:", records)
    for x in range(records):
        rowCount = x + 2
        if rowCount < 22:
            row = str(rowCount)
            print("row:", row)
            PreviousDueAmt = danpheEMR.find_element(By.XPATH, "(//div[@col-id='PreviousDueAmount'])[" + row + "]").text
            PreviousDueAmt = float(PreviousDueAmt)
            print("PreviousDueAmt:", PreviousDueAmt)
            CollectionTillDate = danpheEMR.find_element(By.XPATH,
                "(//div[@col-id='CollectionTillDate'])[" + row + "]").text
            CollectionTillDate = float(CollectionTillDate)
            print("CollectionTillDate:", CollectionTillDate)
            HandoverTillDate = danpheEMR.find_element(By.XPATH, "(//div[@col-id='HandoverTillDate'])[" + row + "]").text
            HandoverTillDate = float(HandoverTillDate)
            print("HandoverTillDate:", HandoverTillDate)
            DueAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='DueAmount'])[" + row + "]").text
            DueAmount = float(DueAmount)
            print("DueAmount:", DueAmount)
            expectedDueAmount = PreviousDueAmt + CollectionTillDate - HandoverTillDate
            print("expectedDueAmount:", expectedDueAmount)
            expectedDueAmount = int(expectedDueAmount)
            DueAmount = int(DueAmount)
            assert DueAmount == expectedDueAmount
            assert DueAmount >= 0
        elif rowCount == 22:
            danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Next')]").click()
            time.sleep(5)
        elif rowCount > 22:
            row = str(rowCount - 21)
            print("row:", row)
            PreviousDueAmt = danpheEMR.find_element(By.XPATH, "(//div[@col-id='PreviousDueAmount'])[" + row + "]").text
            PreviousDueAmt = float(PreviousDueAmt)
            print("PreviousDueAmt:", PreviousDueAmt)
            CollectionTillDate = danpheEMR.find_element(By.XPATH,
                "(//div[@col-id='CollectionTillDate'])[" + row + "]").text
            CollectionTillDate = float(CollectionTillDate)
            print("CollectionTillDate:", CollectionTillDate)
            HandoverTillDate = danpheEMR.find_element(By.XPATH, "(//div[@col-id='HandoverTillDate'])[" + row + "]").text
            HandoverTillDate = float(HandoverTillDate)
            print("HandoverTillDate:", HandoverTillDate)
            DueAmount = danpheEMR.find_element(By.XPATH, "(//div[@col-id='DueAmount'])[" + row + "]").text
            DueAmount = float(DueAmount)
            print("DueAmount:", DueAmount)
            expectedDueAmount = PreviousDueAmt + CollectionTillDate - HandoverTillDate
            print("expectedDueAmount:", expectedDueAmount)
            expectedDueAmount = int(expectedDueAmount)
            DueAmount = int(DueAmount)
            assert DueAmount == expectedDueAmount
            assert DueAmount >= 0
        print("<<END: getSummaryReport")


def verifyUserCollectionVsHandOverReport(danpheEMR):
    print("Start: Get Reports>Billing Reports>User Collection Report")
    global TotalCollectionInUserCollection
    global TotalCollectionInHandover
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'User Collection')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//span[@class='icon-range-ddl dropdown-toggle']").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Last 3 Months").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    TotalCollectionInUserCollection = danpheEMR.find_element(By.XPATH,
        "//td[contains(text(),' Total Collection ')]//following-sibling::td").text
    print("TotalCollectionInUserCollection:", TotalCollectionInUserCollection)
    TotalCollectionInUserCollection = float(TotalCollectionInUserCollection)
    print("TotalCollectionInUserCollection:", TotalCollectionInUserCollection)
    ###
    print("Get Billing>Handover>DailyCollection Vs Handover Report")
    danpheEMR.find_element(By.LINK_TEXT, "Billing").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Handover").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "DailyCollection Vs Handover Report").click()
    time.sleep(3)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//span[@class='icon-range-ddl dropdown-toggle']").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Last 3 Months").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[@class='btn green btn-success']").click()
    time.sleep(9)
    TotalCollectionInHandover = danpheEMR.find_element(By.XPATH,
        "//b[contains(text(),'Total')]/parent::td/following-sibling::td[1]").text
    TotalCollectionInHandover = float(TotalCollectionInHandover)
    print("TotalCollectionInHandover:", TotalCollectionInHandover)
    assert TotalCollectionInHandover == TotalCollectionInUserCollection
    print("End: Get Reports>Billing Reports>User Collection Report")


def verifydepositbalancereportall(danpheEMR):
    global row
    print(">>START: verify Deposit Balance Report")
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Deposit Balance')]").click()
    time.sleep(3)
    records = danpheEMR.find_element(By.XPATH, "//div[@class='page-items']").text
    print("records:", records)
    records = records.partition("Showing ")[2]
    print("records:", records)
    records = records.partition(" /")[0]
    records = int(records)
    print("records:", records)
    for x in range(records):
        rowCount = x + 2
        if rowCount < 20:
            row = str(rowCount)
            print("row:", row)
            Balance = danpheEMR.find_element(By.XPATH, "(//div[@col-id='Balance'])[" + row + "]").text
            Balance = float(Balance)
            print("Balance:", Balance)
            if Balance >= 0:
                print("Total Balance: ", Balance)
            elif Balance < 0:
                print("Amount Cannot be negative: ", Balance)


### To test Total Refund < Total Deposit ###

def RefundCheckOfDepositBalanceReport(danpheEMR):
    global row
    print(">>START: verify Deposit Balance Report")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Reports").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Billing Reports").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//i[contains(.,'Deposit Balance')]").click()
    time.sleep(5)
    records = danpheEMR.find_element(By.XPATH, "//div[@class='page-items']").text
    print("records:", records)
    records = records.partition("Showing ")[2]
    print("records:", records)
    records = records.partition(" /")[0]
    records = int(records)
    print("records:", records)
    for x in range(records):
        rowCount = x + 2
        if rowCount < 20:
            row = str(rowCount)
            print("row:", row)
            Deposit = danpheEMR.find_element(By.XPATH, "(//div[@col-id='TotalDeposit'])[" + row + "]").text
            Deposit = float(Deposit)
            print("Total Deposit:", Deposit)
            Refunded = danpheEMR.find_element(By.XPATH, "(//div[@col-id='TotalRefunded'])[" + row + "]").text
            Refunded = float(Refunded)
            print("Total Refunded :", Refunded)
            assert float(Deposit) >= float(Refunded)
            print(" Actual Refunded : ", Refunded)


def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
