from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
#Module:Report: SalesDayBook******************
   def getSalesDayBook(self):
      print(">>START: getSalesDayBook")
      global syssales
      #global returnamount
      global sysgrosssales
      global syscreditsalestotal
      #global creditcancel
      global sysnetsalesamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Sales DayBook')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      syssales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td").text
      print(syssales)
      sysgrosssales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td[7]").text
      print(sysgrosssales)
      syscreditsalestotal = self.danpheEMR.find_element_by_xpath("//tr[2]/td[3]").text
      print(syscreditsalestotal)
      sysnetsalesamount = self.danpheEMR.find_element_by_xpath("//tr[2]/td[7]").text
      print(sysnetsalesamount)
      print("<<END: getSalesDayBook")
   def preSystemSalesDayBook(self):
      print(">>START: preSystemSalesDayBook")
      global presyssales
      #global returnamount
      global presysgrosssales
      global presyscreditsalestotal
      #global presyscreditcancel
      global presysnetsalesamount
      presyssales = int(syssales)
      presysgrosssales = int(sysgrosssales)
      presyscreditsalestotal = int(syscreditsalestotal)
      presysnetsalesamount = int(sysnetsalesamount)
      print("<<END: preSystemSalesDayBook")
   def verifySalesDayBook(self, cash, credit, cashreturn, creditreturn):
      print(">>START: verifySalesDayBook")
      assert int(syssales) == presyssales + cash + credit - cashreturn - creditreturn
      #assert int(sysgrosssales) == presysgrosssales + cash + credit
      assert int(syscreditsalestotal) == presyscreditsalestotal + credit - creditreturn
      #assert int(sysnetsalesamount) == presysnetsalesamount + cash + credit - cashreturn - creditreturn
      print("<<END: verifySalesDayBook")
#Module:Report: PatientCensus***************
   def getPatientCensus(self):
      print(">>START: getPatientCensus")
      global sysnoofcount
      global sysamount
      global sysunconfirmedcount
      global sysunconfirmedamount
      global sysconfirmedcount
      global sysconfirmedamount
      global systotalcount
      global systotalamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Patient Census')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysnoofcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[1]").text
      print("sysnoofcount", sysnoofcount)
      sysamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[2]").text
      print("sysamount", sysamount)
      sysunconfirmedcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[3]").text
      print("sysunconfirmedcount", sysunconfirmedcount)
      sysunconfirmedamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[4]").text
      print("sysunconfirmedamount", sysunconfirmedamount)
      sysconfirmedcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[5]").text
      print("sysconfirmedcount", sysconfirmedcount)
      sysconfirmedamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[6]").text
      print("sysconfirmedamount", sysconfirmedamount)
      systotalcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[7]").text
      print("systotalcount", systotalcount)
      systotalamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[8]").text
      print("systotalamount", systotalamount)
      print("<<END: getPatientCensus")
   def preSystemPatientCensus(self):
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
   def verifyPatientCensus(self, cash, cashreturn, credit, creditreturn, provisional):
      print(">>START: verifyPatientCensus")
      assert int(sysnoofcount) == presysnoofcount + cash/cash
      print("presysamount", presysamount)
      print("sysamount", sysamount)
      print("cash", cash)
      assert int(sysamount) == int(int(presysamount) + int(cash))
      assert int(sysunconfirmedcount) == presysunconfirmedcount + provisional
      assert int(sysunconfirmedamount) == presysunconfirmedamount + provisional
      assert int(sysconfirmedcount) == presysconfirmedcount + credit
      assert int(sysconfirmedamount) == presysconfirmedamount + credit
      assert int(systotalcount) == presystotalcount + cash/cash + credit
      assert int(systotalamount) == presystotalamount + cash + credit
      print("<<END: verifyPatientCensus")
#Module:Report: Income Segregation Report*****************
   def getIncomeSegregation(self):
      print(">>START: getIncomeSegregation")
      global sysunit
      global syscashgrosssales
      global syscashdiscount
      global syscreditgrosssales
      global syscreditdiscount
      global sysreturnqty
      global sysreturnamount
      global sysreturndiscount
      global systotalgrosssales
      global systotaldiscount
      global systotalnetsales
      time.sleep(3)
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Reports").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Income Segregation')]").click()
      #    time.sleep(5)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      #    time.sleep(15)
      #    sysunit = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[1]").text
      #    print("sysunit", sysunit)
      #    syscashgrosssales = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[2]").text
      #    print("syscashgrosssales", syscashgrosssales)
      #    syscashdiscount = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[3]").text
      #    print("syscashdiscount", syscashdiscount)
      #    syscreditgrosssales = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[4]").text
      #    print("syscreditgrosssales", syscreditgrosssales)
      #    syscreditdiscount = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[5]").text
      #    print("syscreditdiscount", syscreditdiscount)
      #    sysreturnqty = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[6]").text
      #    print("sysreturnqty", sysreturnqty)
      #    sysreturnamount = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[7]").text
      #    print("sysreturnamount", sysreturnamount)
      #    sysreturndiscount = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[8]").text
      #    print("sysreturndiscount", sysreturndiscount)
      #    systotalgrosssales = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[9]").text
      #    print("systotalgrosssales", systotalgrosssales)
      #    systotaldiscount = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[10]").text
      #    print("systotaldiscount", systotaldiscount)
      #    systotalnetsales = self.danpheEMR.find_element_by_xpath(
      #       "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[11]").text
      #    print("systotalnetsales", systotalnetsales)
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Reports").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Billing Reports").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//i[contains(.,'Income Segregation')]").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
         time.sleep(15)
         #sysunit = self.danpheEMR.find_element_by_xpath(
         #   "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[1]").text
         #print("sysunit", sysunit)
         #syscashgrosssales = self.danpheEMR.find_element_by_xpath(
         #   "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[2]").text
         #print("syscashgrosssales", syscashgrosssales)
         syscashdiscount = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[3]").text
         print("syscashdiscount", syscashdiscount)
         syscreditgrosssales = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[4]").text
         print("syscreditgrosssales", syscreditgrosssales)
         syscreditdiscount = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[5]").text
         print("syscreditdiscount", syscreditdiscount)
         sysreturnqty = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[6]").text
         print("sysreturnqty", sysreturnqty)
         sysreturnamount = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[7]").text
         print("sysreturnamount", sysreturnamount)
         sysreturndiscount = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[8]").text
         print("sysreturndiscount", sysreturndiscount)
         systotalgrosssales = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[9]").text
         print("systotalgrosssales", systotalgrosssales)
         systotaldiscount = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[10]").text
         print("systotaldiscount", systotaldiscount)
         systotalnetsales = self.danpheEMR.find_element_by_xpath(
            "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[11]").text
         print("systotalnetsales", systotalnetsales)
      print("<<END getIncomeSegregation")
   def preSystemIncomeSegregation(self):
      print(">>START: preSystemIncomeSegregation")
      global presysunit
      global presyscashgrosssales
      global presyscashdiscount
      global presyscreditgrosssales
      global presyscreditdiscount
      global presysreturnqty
      global presysreturnamount
      global presysreturndiscount
      global presystotalgrosssales
      global presystotaldiscount
      global presystotalnetsales
      presysunit = float(sysunit)
      print("presysunit", presysunit)
      presyscashgrosssales = int(syscashgrosssales)
      print("presyscashgrosssales", presyscashgrosssales)
      presyscashdiscount = int(syscashdiscount)
      print("presyscashdiscount", presyscashdiscount)
      presyscreditgrosssales = int(syscreditgrosssales)
      print("presyscreditgrosssales", presyscreditgrosssales)
      presyscreditdiscount = int(syscreditdiscount)
      print("presyscreditdiscount", presyscreditdiscount)
      presysreturnqty = int(sysreturnqty)
      print("presysreturnqty", presysreturnqty)
      presysreturnamount = int(sysreturnamount)
      print("presysreturnamount", presysreturnamount)
      presysreturndiscount = int(sysreturndiscount)
      print("presysreturndiscount", presysreturndiscount)
      presystotalgrosssales = int(systotalgrosssales)
      print("presystotalgrosssales", presystotalgrosssales)
      presystotaldiscount = int(systotaldiscount)
      print("presystotaldiscount", presystotaldiscount)
      presystotalnetsales = int(systotalnetsales)
      print("presystotalnetsales", presystotalnetsales)
      print("<<END preSystemIncomeSegregation")
   def verifyIncomeSegregation(self, cash, cashreturn, credit, creditreturn, provision):
      print(">>START: verifyIncomeSegregation")
      unit = 0
      returnqty = 0
      if cash > 0 or credit > 0:
         returnqty = 0
         unit = 1
      elif cashreturn > 0 or creditreturn > 0:
         returnqty = 1
         unit = 0
      # if appPort == '81':
      #    calcUnit = presysunit + unit - returnqty
      #    print("calcUnit", calcUnit)
      #    print("sysunit", sysunit)
      #    assert int(sysunit) == int(calcUnit)
      #    print("syscashgrosssales", syscashgrosssales)
      #    calcCashGrossSales = int(presyscashgrosssales + cash)
      #    print("calcCashGrossSales", calcCashGrossSales)
      #    assert int(syscashgrosssales) == int(presyscashgrosssales + cash) #Issues: LPH-866,...  .Issue on: V1.9.0,.....
      #    assert int(syscashdiscount) == presyscashdiscount + 0
      #    assert int(syscreditgrosssales) == presyscreditgrosssales + credit
      #    assert int(syscreditdiscount) == presyscreditdiscount + 0
      #    assert int(sysreturnqty) == presysreturnqty + returnqty
      #    assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
      #    assert int(sysreturndiscount) == presysreturndiscount + 0
      #    assert int(systotalgrosssales) == presystotalgrosssales + cash - cashreturn + credit - creditreturn
      #    assert int(systotaldiscount) == presystotaldiscount + 0
      #    assert int(systotalnetsales) == presystotalnetsales + cash - cashreturn + credit - creditreturn
      #    print("<<END verifyIncomeSegregation")
      if appPort == '82':
         calcUnit = presysunit + unit
         print("calcUnit", calcUnit)
         print("sysunit", sysunit)
         assert int(sysunit) == int(calcUnit)
         print("syscashgrosssales", syscashgrosssales)
         calcCashGrossSales = int(presyscashgrosssales + cash)
         print("calcCashGrossSales", calcCashGrossSales)
         assert int(syscashgrosssales) == int(presyscashgrosssales + cash) #Issues: LPH-866,...  .Issue on: V1.9.0,.....
         assert int(syscashdiscount) == presyscashdiscount + 0
         assert int(syscreditgrosssales) == presyscreditgrosssales + credit
         assert int(syscreditdiscount) == presyscreditdiscount + 0
         assert int(sysreturnqty) == presysreturnqty + returnqty
         assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
         assert int(sysreturndiscount) == presysreturndiscount + 0
         assert int(systotalgrosssales) == presystotalgrosssales + cash - cashreturn + credit - creditreturn
         assert int(systotaldiscount) == presystotaldiscount + 0
         assert int(systotalnetsales) == presystotalnetsales + cash - cashreturn + credit - creditreturn
         print("<<END verifyIncomeSegregation")
   def getPatientCreditSummary(self):
      print(">>START: getPatientCreditSummary")
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Patient Credit Summary')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      print("<<END: getPatientCreditSummary")
   def preSystemPatientCreditSummary(self):
      print(">>START: preSystemPatientCreditSummary")
      print("<<END: preSystemPatientCreditSummary")
   def verifyPatientCreditSummary(self):
      print(">>START: verifyPatientCreditSummary")
      print("<<END: verifyPatientCreditSummary")
   def getDoctorSummary(self, doctor):
      print(">>START: getDoctorSummary")
      global sysgrosstotal
      global sysdiscountamount
      global sysreturnamount
      global sysnetsales
      global sysprovisionalamount
      global syscancelamount
      global syscreditamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(7)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Doctor Summary')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysgrosstotal = self.danpheEMR.find_element_by_css_selector(".table tr:nth-child(1) > td:nth-child(2)").text
      print("sysgrosstotal", sysgrosstotal)
      sysdiscountamount = self.danpheEMR.find_element_by_css_selector(".table tr:nth-child(1) > td:nth-child(4)").text
      print("sysdiscountamount", sysdiscountamount)
      sysreturnamount = self.danpheEMR.find_element_by_css_selector(".table tr:nth-child(1) > td:nth-child(6)").text
      print("sysreturnamount", sysreturnamount)
      sysnetsales = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) td:nth-child(8)").text
      print("sysnetsales", sysnetsales)
      sysprovisionalamount = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)").text
      print("sysprovisionalamount", sysprovisionalamount)
      syscancelamount = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4)").text
      print("cancel amount", syscancelamount)
      syscreditamount = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6)").text
      print("syscreditamount", syscreditamount)
      print("<<END: getDoctorSummary")
   def preSystemDoctorSummary(self):
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
   def verifyDoctorSummary(self, cash, cashreturn, credit, creditreturn, discount, provisional, provisionalcancel):
      print(">>START: verifyDoctorSummary")
      assert int(sysgrosstotal) == presysgrosstotal + cash + credit
      assert int(sysdiscountamount) == presysdiscountamount + discount
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
      assert int(sysnetsales) == presysnetsales + cash + credit - discount - cashreturn - creditreturn
      assert int(sysprovisionalamount) == presysprovisionalamount + provisional
      assert int(syscancelamount) == presyscancelamount + provisionalcancel
      assert int(syscreditamount) == presyscreditamount + credit - creditreturn
      print("<<END: verifyDoctorSummary")

#Module:Billing_Report: Discount Report**********************
   def verifyDiscountReport(self, cash, discountpc):
      print(">>START: verifyDiscountReport")
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'DiscountReport')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      date = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div/span").text
      print(date)
      receiptno = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      print(receiptno)
      hospitalno = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      print(hospitalno)
      assert HospitalNo == hospitalno
      subtotal = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
      print(subtotal)
      assert cash == int(subtotal)
      discount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
      print(discount)
      assert int(discount) == (discountpc*cash/100)
      tax = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
      print(tax)
      totalamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]/span").text
      print(totalamount)
      assert int(totalamount) == int(subtotal) - int(discount)
      user = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[9]").text
      print(user)
      print("<<END: verifyDiscountReport")
#Module:Billing report: Deposit Report*********************
   def verifyDepositBalanceReport(self, deposit):
      print(">>START: verifyDepositBalanceReport")
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Reports").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Deposit Balance')]").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      #    time.sleep(3)
      #    hospitalno = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      #    #assert HospitalNo == hospitalno
      #    depositamt = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
      #    x = int(depositamt)
      #    y = int(deposit)
      #    print("x", x)
      #    print("y", y)
      #    assert x == y
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Reports").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Billing Reports").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//i[contains(.,'Deposit Balance')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(3)
         hospitalno = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
         #assert HospitalNo == hospitalno
         time.sleep(4)
         depositamt = self.danpheEMR.find_element_by_xpath("(//div[@col-id='DepositBalance'])[2]").text
         x = int(depositamt)
         y = int(deposit)
         print("x", x)
         print("y", y)
         assert x == y
      print("<<END: verifyDepositBalanceReport")
#Module: Billing report: Department Summary Report**********
   def getDepartmentSummary(self):
      global sysgrosstotal
      global sysdiscountamount
      global sysreturnamount
      global sysnetsales
      global sysprovisionalamount
      global syscancelamount
      global syscreditamount
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Reports").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Department Summary')]").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").clear()
      #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys("OPD")
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(
      #       Keys.ARROW_DOWN)
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(Keys.TAB)
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(
      #       Keys.RETURN)
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      #    time.sleep(9)
      #    sysgrosstotal = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td").text
      #    print(sysgrosstotal)
      #    sysdiscountamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[2]").text
      #    print(sysdiscountamount)
      #    sysreturnamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[3]").text
      #    print(sysreturnamount)
      #    sysnetsales = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[4]").text
      #    print(sysnetsales)
      #    sysprovisionalamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td").text
      #    print(sysprovisionalamount)
      #    syscancelamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td[2]").text
      #    print(syscancelamount)
      #    syscreditamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td[3]").text
      #    print(syscreditamount)
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Reports").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Billing Reports").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//i[contains(.,'Department Summary')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").clear()
         self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys("Department OPD")
         time.sleep(3)
         #self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(
         #   Keys.ARROW_DOWN)
         #time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(Keys.TAB)
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(
            Keys.RETURN)
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
         time.sleep(9)
         sysgrosstotal = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td").text
         print(sysgrosstotal)
         sysdiscountamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[2]").text
         print(sysdiscountamount)
         sysreturnamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[3]").text
         print(sysreturnamount)
         sysnetsales = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[4]").text
         print(sysnetsales)
         sysprovisionalamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td").text
         print(sysprovisionalamount)
         syscancelamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td[2]").text
         print(syscancelamount)
         syscreditamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td[3]").text
         print(syscreditamount)
   def preSystemDepartmentSummary(self):
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
   def verifyDepartmentSummary(self, cash, cashreturn, credit, creditreturn, discount, provisional, provisionalcancel):
      assert int(sysgrosstotal) == presysgrosstotal + cash + credit
      assert int(sysdiscountamount) == presysdiscountamount + discount
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
      assert int(sysnetsales) == presysnetsales - discount - cashreturn - creditreturn + cash + credit
      assert int(sysprovisionalamount) == presysprovisionalamount + provisional
      assert int(syscancelamount) == presyscancelamount + provisionalcancel
      assert int(syscreditamount) == presyscreditamount + credit - creditreturn
#Module:Billing_Report: User Collection Report***********
   def getUserCollectionReport(self, user):
       global sysnetcashcollection
       global sysgrosstotalsales
       global sysdiscount
       global sysreturnsubtotal
       global sysreturndiscount
       global sysreturnamount
       global sysnetsales
       global syslesscreditamount
       global sysadddepositreceived
       global syslessdepositrefund
       global sysaddcollectionfromreceivables
       global syslesscashdiscount
       global systotalcollection
       self.danpheEMR.find_element_by_link_text("Reports").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_link_text("Billing Reports").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//i[contains(.,'User Collection')]").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(user)
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(Keys.TAB)
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
       time.sleep(9)
       sysnetcashcollection = self.danpheEMR.find_element_by_css_selector(".blinkAmount").text
       print(sysnetcashcollection)
       sysnetcashcollection = sysnetcashcollection.partition("( ")[2]
       sysnetcashcollection = sysnetcashcollection.partition(")")[0]
       print(sysnetcashcollection)
       sysgrosstotalsales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td[2]").text
       print(sysgrosstotalsales)
       sysdiscount = self.danpheEMR.find_element_by_xpath("//tr[2]/td[2]").text
       print(sysdiscount)
       sysreturnsubtotal = self.danpheEMR.find_element_by_xpath("//tr[3]/td[2]").text
       print(sysreturnsubtotal)
       sysreturndiscount = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
       print(sysreturndiscount)
       sysreturnamount = self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]").text
       print(sysreturnamount)
       sysnetsales = self.danpheEMR.find_element_by_xpath("//tr[6]/td[2]").text
       print(sysnetsales)
       syslesscreditamount = self.danpheEMR.find_element_by_xpath("//tr[7]/td[2]").text
       print(syslesscreditamount)
       sysadddepositreceived = self.danpheEMR.find_element_by_xpath("//tr[8]/td[2]").text
       print(sysadddepositreceived)
       syslessdepositrefund = self.danpheEMR.find_element_by_xpath("//tr[9]/td[2]").text
       print(syslessdepositrefund)
       sysaddcollectionfromreceivables = self.danpheEMR.find_element_by_xpath("//tr[10]/td[2]").text
       print(sysaddcollectionfromreceivables)
       syslesscashdiscount = self.danpheEMR.find_element_by_xpath("//tr[11]/td[2]").text
       print(syslesscashdiscount)
       systotalcollection = self.danpheEMR.find_element_by_xpath("//tr[12]/td[2]").text
       print(systotalcollection)
   def preSystemUserCollectionReport(self):
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
      global presystotalcollection
      presysnetcashcollection = int(sysnetcashcollection)
      presysgrosstotalsales = int(sysgrosstotalsales)
      presysdiscount = int(sysdiscount)
      presysreturnsubtotal = int(sysreturnsubtotal)
      presysreturndiscount = int(sysreturndiscount)
      presysreturnamount = int(sysreturnamount)
      presysnetsales = int(sysnetsales)
      presyslesscreditamount = int(syslesscreditamount)
      presysadddepositreceived = int(sysadddepositreceived)
      presyslessdepositrefund = int(syslessdepositrefund)
      presysaddcollectionfromreceivables = int(sysaddcollectionfromreceivables)
      presyslesscashdiscount = int(syslesscashdiscount)
      presystotalcollection = int(systotalcollection)
   def verifyUserCollectionReport(self, cash, cashreturn, credit, creditreturn, discount, deposit, depositreturn, creditsettlement, provisional, provisionalcancel):
      assert int(sysnetcashcollection) == presysnetcashcollection + cash - cashreturn + deposit - depositreturn - creditsettlement
      assert int(sysgrosstotalsales) == presysgrosstotalsales + cash + credit
      assert int(sysdiscount) == presysdiscount + discount
      assert int(sysreturnsubtotal) == presysreturnsubtotal + cashreturn + creditreturn
      assert int(sysreturndiscount) == presysreturndiscount + discount
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn - discount
      assert int(sysnetsales) == presysnetsales + cash - cashreturn + credit - creditreturn
      assert int(syslesscreditamount) == presyslesscreditamount + credit - creditreturn
      assert int(sysadddepositreceived) == presysadddepositreceived + deposit
      assert int(syslessdepositrefund) == presyslessdepositrefund + depositreturn
      assert int(sysaddcollectionfromreceivables) == presysaddcollectionfromreceivables + creditsettlement
      assert int(syslesscashdiscount) == presyslesscashdiscount + discount
      assert int(systotalcollection) == presystotalcollection + cash - cashreturn + deposit - depositreturn - creditsettlement
#Module:Admission_Report: Total Admitted Patients Report**********************
   def verifyTotalAdmittedPatients(self):
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Admission").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Admitted Patient").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(5)
      hospitalno = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      assert hospitalno == HospitalNo

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

