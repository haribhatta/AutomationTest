import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.LibModuleAppointment as LA
import Library.GlobalShareVariables as GSV

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
      time.sleep(5)
      danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Dashboard')]").click()
      time.sleep(3)
      TotalSale = danpheEMR.find_element_by_xpath("//h4[contains(text(),'Total Sale')]/following-sibling::b").text
      print("Total Sale", TotalSale)
      TotalSale = TotalSale.partition(": ")[2]
      TotalSale = float(TotalSale)
      print("Total Sale", TotalSale)
      CashReturn = danpheEMR.find_element_by_xpath("//h4[contains(text(),'Cash Return')]/following-sibling::b").text
      print("CashReturn", CashReturn)
      CashReturn = CashReturn.partition(": ")[2]
      CashReturn = float(CashReturn)
      print("CashReturn", CashReturn)
      CreditReturn = danpheEMR.find_element_by_xpath("//h4[contains(text(),'Credit Return')]/following-sibling::b").text
      print("CreditReturn", CreditReturn)
      CreditReturn = CreditReturn.partition(": ")[2]
      CreditReturn = float(CreditReturn)
      print("CreditReturn", CreditReturn)
      NetCashCollection = danpheEMR.find_element_by_xpath(
            "//h4[contains(text(),'Net Cash Collection')]/following-sibling::b").text
      print("NetCashCollection", NetCashCollection)
      NetCashCollection = NetCashCollection.partition(": ")[2]
      NetCashCollection = float(NetCashCollection)
      print("NetCashCollection", NetCashCollection)
      DepositAmount = danpheEMR.find_element_by_xpath(
            "//h4[contains(text(),'Deposit Amount')]/following-sibling::b").text
      print("Deposit Amount", DepositAmount)
      DepositAmount = DepositAmount.partition(": ")[2]
      DepositAmount = float(DepositAmount)
      print("DepositAmount", DepositAmount)
      DepositReturned = danpheEMR.find_element_by_xpath(
            "//h4[contains(text(),'Deposit Returned')]/following-sibling::b").text
      print("Deposit Returned", DepositReturned)
      DepositReturned = DepositReturned.partition(": ")[2]
      DepositReturned = float(DepositReturned)
      print("DepositReturned", DepositReturned)
      ProvisionalItems = danpheEMR.find_element_by_xpath(
            "//td[contains(text(),'PROVISIONAL ITEMS')]/following-sibling::td").text
      print("PROVISIONAL ITEMS", ProvisionalItems)
      ProvisionalItems = ProvisionalItems.partition("Rs.")[2]
      ProvisionalItems = float(ProvisionalItems)
      print("ProvisionalItems", ProvisionalItems)
      UnpaidInvoices = danpheEMR.find_element_by_xpath(
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
      if AppName =='SNCH':
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
      global sysinvoiceamount
      global sysinvoicereturned
      global sysdeposit
      global sysdepositreturn
      global sysnetamount
      global sysdiscountamount
      if AppName =='SNCH':
            danpheEMR.find_element_by_link_text("Pharmacy").click()
            time.sleep(2)
            danpheEMR.find_element_by_link_text("Report").click()
            time.sleep(2)
            danpheEMR.find_element_by_link_text("Sales").click()
            time.sleep(2)
            danpheEMR.find_element_by_xpath("//i[contains(.,'Cash Collection Summary')]").click()
            time.sleep(2)
            danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
            time.sleep(9)
            danpheEMR.find_element_by_id("quickFilterInput").send_keys(user)
            time.sleep(2)
            username = danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
            sysinvoiceamount = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
            print(sysinvoiceamount)
            sysinvoicereturned = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
            print(sysinvoicereturned)
            sysdeposit = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
            print(sysdeposit)
            sysdepositreturn = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
            print(sysdepositreturn)
            sysnetamount = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
            print(sysnetamount)
            sysdiscountamount = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
            print(sysdiscountamount)
      print("<<END: getPharmacyCashCollectionSummary")
def preSystemPharmacyCashCollectionSummary():
      print(">>START: preSystemPharmacyCashCollectionSummary")
      global presysinvoiceamount
      global presysinvoicereturned
      global presysdeposit
      global presysdepositreturn
      global presysnetamount
      global presysdiscountamount
      presysinvoiceamount = int(sysinvoiceamount)
      presysinvoicereturned = float(sysinvoicereturned)
      presysdeposit = int(sysdeposit)
      presysdepositreturn = int(sysdepositreturn)
      presysnetamount = float(sysnetamount)
      presysdiscountamount = int(sysdiscountamount)
      print("<<END: preSystemPharmacyCashCollectionSummary")
def verifyPharmacyCashCollectionSummary(cash, cashreturn, credit, creditreturn, deposit, depositreturn, discount):
      print(">>START: verifyPharmacyCashCollectionSummary")
      print("presysinvoiceamount:", presysinvoiceamount)
      print("sysinvoiceamount:", sysinvoiceamount)
      print("cash:", cash)
      print("credit:", credit)
      print("presysinvoicereturned:", presysinvoicereturned)
      print("sysinvoicereturned:", sysinvoicereturned)
      print("cashreturn:", cashreturn)
      print("creditreturn:", creditreturn)
      assert int(sysinvoiceamount) == presysinvoiceamount + cash + credit
      assert float(sysinvoicereturned) == float(presysinvoicereturned + cashreturn + creditreturn)
      assert int(sysdeposit) == presysdeposit + deposit
      assert int(sysdepositreturn) == presysdepositreturn + depositreturn
      result = float(sysinvoiceamount) - float(sysinvoicereturned) - float(sysdeposit) - float(sysdepositreturn)
      print("result:", result)
      netamount = float(result)
      print("netamount", netamount)
      assert float(sysnetamount) == float(netamount)
      assert int(sysdiscountamount) == presysdiscountamount + discount
      print("<<END: verifyPharmacyCashCollectionSummary")
def getPharmacyDepositBalanceReport(danpheEMR, HospitalNo):
      print(">>START: getPharmacyDepositBalanceReport")
      global sysdepositamt
      danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'Deposit Balance Report ')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(9)
      assert HospitalNo == danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      sysdepositamt = int(danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text)
      print("<<END: getPharmacyDepositBalanceReport")
def verifyPharmacyDepositBalanceReport(danpheEMR, HospitalNo, deposit, depositreturn):
      print(">>START: verifyPharmacyDepositBalanceReport")
      danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'Deposit Balance Report ')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(9)
      assert HospitalNo == danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      depositbalance = int(danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text)
      assert depositbalance == sysdepositamt + deposit - depositreturn
      print("<<END: verifyPharmacyDepositBalanceReport")
def getPharmacyOpeningEndingStockSummaryReport(danpheEMR, drugname):
      print(">>START: getPharmacyOpeningEndingStockSummaryReport")
      global sysdrugname
      global sysopeningstock
      global sysendingstock
      danpheEMR.find_element_by_link_text('Pharmacy').click()
      time.sleep(2)
      danpheEMR.find_element_by_link_text('Report').click()
      danpheEMR.find_element_by_xpath("//i[contains(.,'Opening and Ending Stock Summary')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
      time.sleep(3)
      sysdrugname = danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
      print("sysdrugname", sysdrugname)
      assert sysdrugname == drugname
      sysopeningstock = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
      print("sysopeningstock", sysopeningstock)
      sysendingstock = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
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
      danpheEMR.find_element_by_link_text('Pharmacy').click()
      time.sleep(2)
      danpheEMR.find_element_by_link_text('Report').click()
      danpheEMR.find_element_by_xpath("//i[contains(.,'Opening and Ending Stock Summary')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(presysdrugname, ' ', presysdrugbatch)
      time.sleep(7)
      assert presysdrugname == danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
      assert presysdrugbatch == danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      assert presysdrugexpiry == danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]/span").text
      assert presysopeningstock == danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
      sysendingstock = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
      assert int(sysendingstock) == int(presysendingstock) - qty
      print("<<END: verifyPharmacyOpeningEndingStockSummaryReport")
def getPharmacyStockManageDetailReport(danpheEMR, drugname):
      print(">>START: getPharmacyStockManageDetailReport")
      global ManageQuantity
      danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Stock Manage Detail Report')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(9)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
      time.sleep(5)
      ManageQuantity = danpheEMR.find_element_by_xpath(
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
      danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//i[contains(text(),'Stock Items')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//input[@placeholder='--Select Item--']").send_keys(drugname)
      time.sleep(1)
      danpheEMR.find_element_by_xpath("//input[@placeholder='--Select Item--']").send_keys(Keys.ARROW_DOWN)
      danpheEMR.find_element_by_xpath("//input[@placeholder='--Select Item--']").send_keys(Keys.TAB)
      danpheEMR.find_element_by_xpath("//select").send_keys("Dispensary")
      danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      sysqty = danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
      print("sysqty", sysqty)
      print("drugqtySS", drugqtySS)
      assert int(drugqtySS) == int(sysqty)
      print("<<END: verifyStockItemsReport")
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
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
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Sales").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'User Collection')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(user)
      time.sleep(9)
      #1
      actualNetCashCollection = danpheEMR.find_element_by_css_selector(".blinkAmount").text
      print("actualNetCashCollection", actualNetCashCollection)
      actualNetCashCollection = actualNetCashCollection.partition("(")[2]
      actualNetCashCollection = actualNetCashCollection.partition(")")[0]
      actualNetCashCollection = float(actualNetCashCollection)
      print("actualNetCashCollection", actualNetCashCollection)
      #2
      actualGrossTotalSales = danpheEMR.find_element_by_xpath("//td[contains(text(),'Gross Total Sales')]/following-sibling::td").text
      actualGrossTotalSales = float(actualGrossTotalSales)
      print("actualGrossTotalSales", actualGrossTotalSales)
      #3
      actualDiscount = danpheEMR.find_element_by_xpath("//td[contains(text(),'Discount')]/following-sibling::td").text
      actualDiscount = float(actualDiscount)
      print("actualDiscount", actualDiscount)
      #4
      actualReturnSubTotal = danpheEMR.find_element_by_xpath("//td[contains(text(),'Return SubTotal')]/following-sibling::td").text
      actualReturnSubTotal = float(actualReturnSubTotal)
      print("actualReturnSubTotal", actualReturnSubTotal)
      #5
      actualReturnDiscount = danpheEMR.find_element_by_xpath("//td[contains(text(),'Return Discount')]/following-sibling::td").text
      actualReturnDiscount = float(actualReturnDiscount)
      print("actualReturnDiscount", actualReturnDiscount)
      #6
      actualReturnAmount = danpheEMR.find_element_by_xpath("//td[contains(text(),'Return Amount')]/following-sibling::td").text
      actualReturnAmount = float(actualReturnAmount)
      print("actualReturnAmount", actualReturnAmount)
      #7
      actualNetSales = danpheEMR.find_element_by_xpath("//strong[contains(text(),'Net Sales')]/parent::td/following-sibling::td").text
      actualNetSales = float(actualNetSales)
      print("actualNetSales", actualNetSales)
      #8
      actualVATAmount = danpheEMR.find_element_by_xpath("//td[contains(text(),'VAT Amount')]/following-sibling::td").text
      actualVATAmount = float(actualVATAmount)
      print("actualVATAmount", actualVATAmount)
      #9
      actualLessCreditAmount = danpheEMR.find_element_by_xpath("//td[contains(text(),'Less Credit Amount')]/following-sibling::td").text
      actualLessCreditAmount = float(actualLessCreditAmount)
      print("actualLessCreditAmount", actualLessCreditAmount)
      #10
      actualAddDepositReceived = danpheEMR.find_element_by_xpath("//td[contains(text(),'Add Deposit Received')]/following-sibling::td").text
      actualAddDepositReceived = float(actualAddDepositReceived)
      print("actualAddDepositReceived", actualAddDepositReceived)
      #11
      actualDepositDeducted = danpheEMR.find_element_by_xpath("//td[contains(text(),'Deposit Deducted')]/following-sibling::td").text
      actualDepositDeducted = float(actualDepositDeducted)
      print("actualDepositDeducted", actualDepositDeducted)
      #12
      actualLessDepositRefund = danpheEMR.find_element_by_xpath("//td[contains(text(),'Less Deposit Refund')]/following-sibling::td").text
      actualLessDepositRefund = float(actualLessDepositRefund)
      print("actualLessDepositRefund", actualLessDepositRefund)
      #13
      actualAddCollectionFromReceivables = danpheEMR.find_element_by_xpath("//td[contains(text(),'Add Collection From Receivables')]/following-sibling::td").text
      actualAddCollectionFromReceivables = float(actualAddCollectionFromReceivables)
      print("actualAddCollectionFromReceivables", actualAddCollectionFromReceivables)
      #14
      actualLessCashDiscount = danpheEMR.find_element_by_xpath("//td[contains(text(),'Less Cash Discount')]/following-sibling::td").text
      actualLessCashDiscount = float(actualLessCashDiscount)
      print("actualLessCashDiscount", actualLessCashDiscount)
      #15
      actualTotalCashCollection = danpheEMR.find_element_by_xpath("//td[contains(text(),'Total Cash Collection')]/following-sibling::td").text
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
      #1
      expectedNetCashCollection = preNetCashCollection + cash - cashreturn
      assert actualNetCashCollection == expectedNetCashCollection
      #2
      expectedGrossTotalSales = preGrossTotalSales + cash + credit
      assert actualGrossTotalSales == expectedGrossTotalSales
      #3
      expectedDiscount = preDiscount + discount
      assert actualDiscount == expectedDiscount
      #4
      expectedReturnSubTotal = preReturnSubTotal + cashreturn + creditreturn
      assert actualReturnSubTotal == expectedReturnSubTotal
      #5
      expectedReturnDiscount = preReturnDiscount - discount
      assert actualReturnDiscount == expectedReturnDiscount
      #6
      expectedReturnAmount = preReturnAmount + cashreturn + creditreturn
      assert actualReturnAmount == expectedReturnAmount
      #7
      expectedNetSales = preNetSales + cash - cashreturn + credit - creditreturn
      assert actualNetSales == expectedNetSales
      #8
      expectedVATAmount = preVATAmount
      assert actualVATAmount == expectedVATAmount
      #9
      expectedLessCreditAmount = preLessCreditAmount + credit - creditreturn
      assert actualLessCreditAmount == expectedLessCreditAmount
      #10
      expectedAddDepositReceived = preAddDepositReceived + deposit
      assert actualAddDepositReceived == expectedAddDepositReceived
      #11
      expectedDepositDeducted = preDepositDeducted
      assert actualDepositDeducted == expectedDepositDeducted
      #12
      expectedLessDepositRefund = preLessDepositRefund
      assert actualLessDepositRefund == expectedLessDepositRefund
      #13
      expectedAddCollectionFromReceivables = preAddCollectionFromReceivables + creditsettlement
      assert actualAddCollectionFromReceivables == expectedAddCollectionFromReceivables
      #14
      expectedLessCashDiscount = preLessCashDiscount
      assert actualLessCashDiscount == expectedLessCashDiscount
      #15
      expectedTotalCashCollection = preTotalCashCollection + cash - cashreturn + deposit - depositreturn + creditsettlement
      assert actualTotalCashCollection == expectedTotalCashCollection

      print("<<END: verifySystemPharmacyUserCollectionReport")
###Narcotic Daily Sales Report-
def verifySystemPharmacyNarcoticDailySalesReport(danpheEMR, invoiceNo, totalAmount):
      print(">>START: verifySystemPharmacyNarcoticDailySalesReport")
      if AppName == "LPH":
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Sales").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Narcotics Daily Sales')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(15) # Due to performance issue there is open bug in Jira: EMR-4775
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(invoiceNo)
      time.sleep(9)
      sysInvoiceNo = danpheEMR.find_element_by_xpath("(//div[@col-id='InvoicePrintId'])[2]").text
      print("sysInvoiceNo:", sysInvoiceNo)
      print("invoiceNo:", invoiceNo)
      assert sysInvoiceNo == invoiceNo
      sysTotalAmount = danpheEMR.find_element_by_xpath("(//div[@col-id='TotalAmount'])[2]").text
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
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Sales").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Bill-wise Sales')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(3)
      actualSubTotalAmount = danpheEMR.find_element_by_xpath("(//td[contains(text(),'MainDispensary')]/following-sibling::td)[1]").text
      actualSubTotalAmount = float(actualSubTotalAmount)
      print("actualSubTotalAmount:", actualSubTotalAmount)
      actualDiscountAmount = danpheEMR.find_element_by_xpath("(//td[contains(text(),'MainDispensary')]/following-sibling::td)[2]").text
      actualDiscountAmount = float(actualDiscountAmount)
      print("actualDiscountAmount:", actualDiscountAmount)
      actualTotalAmount = danpheEMR.find_element_by_xpath("(//td[contains(text(),'MainDispensary')]/following-sibling::td)[3]").text
      actualTotalAmount = float(actualTotalAmount)
      print("actualTotalAmount:", actualTotalAmount)
def preSystemPharmacyBillWiseSalesReport():
      global preSubTotalAmount
      global preDiscountAmount
      global preTotalAmount
      preSubTotalAmount = actualSubTotalAmount
      preDiscountAmount = actualDiscountAmount
      preTotalAmount = actualTotalAmount
def verifySystemPharmacyBillWiseSalesReport(danpheEMR, invoiceNo, cash, cashReturn, credit, creditReturn, totalAmount, discountAmount):
      print(">>START: verifySystemPharmacyBillWiseSalesReport")
      if AppName == "LPH":
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Sales").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Bill-wise Sales')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(15) # Due to performance issue there is open bug in Jira: EMR-4775
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(invoiceNo)
      time.sleep(9)
      sysInvoiceNo = danpheEMR.find_element_by_xpath("(//div[@col-id='InvoicePrintId'])[2]").text
      print("sysInvoiceNo:", sysInvoiceNo)
      print("invoiceNo:", invoiceNo)
      assert sysInvoiceNo == invoiceNo
      sysTotalAmount = danpheEMR.find_element_by_xpath("(//div[@col-id='TotalAmount'])[2]").text
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
###Sales Summary Report-
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
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Sales").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Sales Summary')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(3)
      actualCashSales = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Cash Sales')])[1]/following-sibling::td").text
      actualCashSales = float(actualCashSales)
      print("actualCashSales", actualCashSales)
      actualCashSalesRefund = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Cash Sales Refund')])[1]/following-sibling::td").text
      actualCashSalesRefund = float(actualCashSalesRefund)
      print("actualCashSalesRefund", actualCashSalesRefund)
      actualNetCashSales = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Net Cash Sales')])[1]/following-sibling::td").text
      actualNetCashSales = float(actualNetCashSales)
      print("actualNetCashSales", actualNetCashSales)
      actualCreditSales = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Credit Sales')])[1]/following-sibling::td").text
      actualCreditSales = float(actualCreditSales)
      print("actualCreditSales", actualCreditSales)
      actualCreditSalesRefund = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Credit Sales Refund')])[1]/following-sibling::td").text
      actualCreditSalesRefund = float(actualCreditSalesRefund)
      print("actualCreditSalesRefund", actualCreditSalesRefund)
      actualNetCreditSales = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Net Credit Sales')])[1]/following-sibling::td").text
      actualNetCreditSales = float(actualNetCreditSales)
      print("actualNetCreditSales", actualNetCreditSales)
      actualTotalSales = danpheEMR.find_element_by_xpath("(//td[contains(text(),'Total Sales')])[1]/following-sibling::td").text
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
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Return From Customer Report')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(3)
      actualTotalReturnedAmount = danpheEMR.find_element_by_xpath("//td[contains(text(),' Total Returned Amount ')]/following-sibling::td").text
      actualTotalReturnedAmount = float(actualTotalReturnedAmount)
      print("End: getPharmacyReturnFromCustomerReport:")
def prePharmacyReturnFromCustomerReport():
      print("Start: prePharmacyReturnFromCustomerReport:")
      global preTotalReturnedAmount
      preTotalReturnedAmount = actualTotalReturnedAmount
      print("End: prePharmacyReturnFromCustomerReport:")
def verifyPharmacyReturnFromCustomerReport(danpheEMR, invoiceNo, cashReturn):
      print("Start: verifyPharmacyReturnFromCustomerReport:")
      if AppName == "LPH":
            danpheEMR.find_element_by_link_text("Store").click()
      elif AppName == "MPH" or AppName == "SNCH":
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Report").click()
      time.sleep(4)
      danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(4)
      danpheEMR.find_element_by_xpath("//i[contains(.,'Return From Customer Report')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(invoiceNo)
      time.sleep(3)
      sysInvoiceNo = danpheEMR.find_element_by_xpath("(//div[@col-id='IssueNo'])[2]").text
      sysInvoiceNo = sysInvoiceNo.partition("PH")[2]
      print("sysInvoiceNo", sysInvoiceNo)
      assert sysInvoiceNo == invoiceNo
      expectedTotalReturnedAmount = preTotalReturnedAmount + cashReturn
      assert actualTotalReturnedAmount == expectedTotalReturnedAmount
      print("End: verifyPharmacyReturnFromCustomerReport:")
########Supplier Reports:

def __str__():
      return

