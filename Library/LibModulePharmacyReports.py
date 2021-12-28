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
      #global TotalSale
      # global TotalReturn
      #global CreditReturn
      #global CashReturn
      #global NetCashCollection
      #global DepositAmount
      #global DepositReturned
      #global ProvisionalItems
      #global UnpaidInvoices
      global userCollection
      time.sleep(5)
      if AppName == "LPH":
            danpheEMR.find_element_by_link_text("Store").click()
      else:
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(9)
      danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Dashboard')]").click()
      time.sleep(3)
      '''
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
      '''
      user = GSV.pharmacyUserName

      time.sleep(9)
      userCollection = danpheEMR.find_element_by_xpath("//h4[contains(text(),'"+user+"')]/following-sibling::b").text
      print("User Collection:", userCollection)
      userCollection = userCollection.partition(": ")[2]
      print("User Collection:", userCollection)
      print("<<END: getPharmacyDashboard")
def preSystemPharmacyDashboard():
      #global xTotalSale
      # global xTotalReturn
      #global xCashReturn
      #global xCreditReturn
      #global xNetCashCollection
      #global xDepositAmount
      #global xDepositReturned
      #global xProvisionalItems
      #global xUnpaidInvoices
      global preUserCollection
      preUserCollection = userCollection
      '''
      xTotalSale = TotalSale
      xCashReturn = CashReturn
      xCreditReturn = CreditReturn
      xNetCashCollection = NetCashCollection
      xDepositAmount = DepositAmount
      xDepositReturned = DepositReturned
      xProvisionalItems = ProvisionalItems
      xUnpaidInvoices = UnpaidInvoices
      '''
def verifyPharmacyDashboard(cash, cashreturn, credit, creditreturn, deposit, depositreturn, provisional,
                            provisionacancel):
      print(">>START: verifyPharmacyDashboard:")
      if AppName =='SNCH' or AppName == 'MPH':
            '''
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
            '''
            x = float(preUserCollection) + float(cash) + float(deposit) - float(cashreturn) - float(depositreturn)
            x = str(x)
            print("X:", x)
            #x = x.replace(" ", "")
            x = x.partition(".")[0]
            print("X final:", x)
            print("userCollection:", userCollection)
            y = str(userCollection)
            #y = y.replace(" ", "")
            y = y.partition(".")[0]
            print("y final:", y)
            assert y == x
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
def getPharmacyUserCollectionReport(danpheEMR, user):
      print(">>START: getPharmacyUserCollectionReport")
      global sysPnetcashcollection
      global sysPgrosstotalsales
      global sysPdiscount
      global sysPreturnsubtotal
      global sysPreturndiscount
      global sysPreturnamount
      global sysPnetsales
      global sysPlesscreditamount
      global sysPadddepositreceived
      global sysPdepositdeducted
      global sysPlessdepositrefund
      global sysPaddcollectionfromreceivables
      global sysPlesscashdiscount
      global sysPtotalcollection
      if AppName == 'LPH':
            danpheEMR.find_element_by_link_text("Store").click()
      else:
            danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(3)
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
      sysPnetcashcollection = danpheEMR.find_element_by_css_selector(".blinkAmount").text
      print("sysPnetcashcollection:", sysPnetcashcollection)
      sysPnetcashcollection = sysPnetcashcollection.partition("(")[2]
      sysPnetcashcollection = sysPnetcashcollection.partition(")")[0]
      sysPnetcashcollection = float(sysPnetcashcollection)
      print("sysPnetcashcollection the final:", sysPnetcashcollection)
      sysPgrosstotalsales = danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td[2]").text
      print("sysPgrosstotalsales:", sysPgrosstotalsales)
      sysPdiscount = danpheEMR.find_element_by_xpath("//tr[2]/td[2]").text
      print("sysPdiscount:", sysPdiscount)
      sysPreturnsubtotal = danpheEMR.find_element_by_xpath("//tr[3]/td[2]").text
      print("sysPreturnsubtotal:", sysPreturnsubtotal)
      sysPreturndiscount = danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
      print("sysPreturndiscount:", sysPreturndiscount)
      sysPreturnamount = danpheEMR.find_element_by_xpath("//tr[5]/td[2]").text
      print("sysPreturnamount:", sysPreturnamount)
      sysPnetsales = danpheEMR.find_element_by_xpath("//tr[6]/td[2]").text
      print("sysPnetsales:", sysPnetsales)
      sysPlesscreditamount = danpheEMR.find_element_by_xpath("//tr[7]/td[2]").text
      print("sysPlesscreditamount:", sysPlesscreditamount)
      sysPadddepositreceived = danpheEMR.find_element_by_xpath("//tr[8]/td[2]").text
      print("sysPadddepositreceived:", sysPadddepositreceived)
      sysPdepositdeducted = danpheEMR.find_element_by_xpath("//tr[9]/td[2]").text
      print("sysPdepositdeducted:", sysPdepositdeducted)
      sysPlessdepositrefund = danpheEMR.find_element_by_xpath("//tr[10]/td[2]").text
      print("sysPlessdepositrefund:", sysPlessdepositrefund)
      sysPaddcollectionfromreceivables = danpheEMR.find_element_by_xpath("//tr[11]/td[2]").text
      print("sysPaddcollectionfromreceivables:", sysPaddcollectionfromreceivables)
      sysPlesscashdiscount = danpheEMR.find_element_by_xpath("//tr[12]/td[2]").text
      print("sysPlesscashdiscount:", sysPlesscashdiscount)
      sysPtotalcollection = danpheEMR.find_element_by_xpath("//tr[13]/td[2]").text
      print("sysPtotalcollection:", sysPtotalcollection)
      print("<<END: getPharmacyUserCollectionReport")
def preSystemPharmacyUserCollectionReport():
      print(">START: preSystemPharmacyUserCollectionReport")
      global presysPnetcashcollection
      global presysPgrosstotalsales
      global presysPdiscount
      global presysPreturnsubtotal
      global presysPreturndiscount
      global presysPreturnamount
      global presysPnetsales
      global presysPlesscreditamount
      global presysPadddepositreceived
      global presysPdepositdeducted
      global presysPlessdepositrefund
      global presysPaddcollectionfromreceivables
      global presysPlesscashdiscount
      global presysPtotalcollection
      print("sysPnetcashcollection: Hari", sysPnetcashcollection)
      presysPnetcashcollection = float(sysPnetcashcollection)
      presysPgrosstotalsales = float(sysPgrosstotalsales)
      presysPdiscount = float(sysPdiscount)
      presysPreturnsubtotal = float(sysPreturnsubtotal)
      presysPreturndiscount = float(sysPreturndiscount)
      presysPreturnamount = float(sysPreturnamount)
      presysPnetsales = float(sysPnetsales)
      presysPlesscreditamount = float(sysPlesscreditamount)
      presysPadddepositreceived = float(sysPadddepositreceived)
      presysPdepositdeducted = float(sysPdepositdeducted)
      presysPlessdepositrefund = float(sysPlessdepositrefund)
      presysPaddcollectionfromreceivables = float(sysPaddcollectionfromreceivables)
      presysPlesscashdiscount = float(sysPlesscashdiscount)
      presysPtotalcollection = float(sysPtotalcollection)
      print("<<END: preSystemPharmacyUserCollectionReport")
def verifySystemPharmacyUserCollectionReport(cash, cashreturn, credit, creditreturn, creditsettlement, discount,
                                             deposit, depositreturn, provisional, provisionalcancel):
      print(">>START: verifySystemPharmacyUserCollectionReport")
      global sysPgrosstotalsales
      if AppName =='SNCH':
            print(">>START: verifySystemPharmacyUserCollectionReport")
            print("cash", cash)
            print("cashreturn", cashreturn)
            print("presysPnetcashcollection", presysPnetcashcollection)
            print("sysPnetcashcollection", sysPnetcashcollection)
            newCashCollection = presysPnetcashcollection + cash - cashreturn
            print("newCashCollection", newCashCollection)
            assert round(float(sysPnetcashcollection)) == round(float(newCashCollection))
            result = str(float(presysPgrosstotalsales) + cash + credit)
            print("result", result)
            print("sysPgrosstotalsales", sysPgrosstotalsales)
            print("presysPgrosstotalsales", presysPgrosstotalsales)
            # sysPgrosstotalsales = sysPgrosstotalsales.partition(".")[0]
            # result = result.partition(".")[0]
            # print("result", result)
            print("sysPgrosstotalsales", sysPgrosstotalsales)
            assert sysPgrosstotalsales == result
            assert float(sysPdiscount) == presysPdiscount + discount
            print("sysPreturnsubtotal", sysPreturnsubtotal)
            print("presysPreturnsubtotal", presysPreturnsubtotal)
            assert round(float(sysPreturnsubtotal)) == round(float(presysPreturnsubtotal + cashreturn + creditreturn))
            assert float(sysPreturndiscount) == presysPreturndiscount + discount
            assert round(float(sysPreturnamount)) == round(
                  float(presysPreturnamount + cashreturn + creditreturn + discount))
            print("presysPnetsales", presysPnetsales)
            print("sysPnetsales", sysPnetsales)
            assert round(float(sysPnetsales)) == round(
                  float(presysPnetsales + cash + credit - cashreturn - creditreturn - discount))
            print("sysPlesscreditamount", sysPlesscreditamount)
            print("presysPlesscreditamount", presysPlesscreditamount)
            print("Credit", credit)
            assert round(float(sysPlesscreditamount)) == round(presysPlesscreditamount + credit)
            assert float(sysPadddepositreceived) == presysPadddepositreceived + deposit
            assert float(sysPdepositdeducted) == presysPdepositdeducted
            assert float(sysPlessdepositrefund) == presysPlessdepositrefund - depositreturn
            assert float(sysPaddcollectionfromreceivables) == presysPaddcollectionfromreceivables + creditsettlement
            assert float(sysPlesscashdiscount) == presysPlesscashdiscount + discount
            print("sysPtotalcollection", sysPtotalcollection)
            result2 = presysPtotalcollection + cash - cashreturn + deposit - depositreturn + creditsettlement
            print("result2", result2)
            x = str(sysPtotalcollection)
            x = x.replace(" ", "")
            print("X", x)
            y = str(result2)
            y = y.replace(" ", "")
            print("Y", x)
            assert x == y
      print("<<END: verifySystemPharmacyUserCollectionReport")
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

def __str__():
      return

