from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)

#Module:Incentive ******************
   def synchBilingIncentive(self):
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Bill Sync").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Sync Billing to Incentives')]").click()
      time.sleep(5)
   def getIncentiveTransactionReport(self):
      global quantity
      global incentiveAmt
      global tdsAmount
      global netPayable
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[text()='Transaction Report']").click()
      time.sleep(1)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(doctor1)
      time.sleep(1)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      quantity = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[3]").text
      print("quantity", quantity)
      incentiveAmt = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[4]").text
      print("incentiveAmt", incentiveAmt)
      tdsAmount = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[5]").text
      print("tdsAmount", tdsAmount)
      netPayable = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[6]").text
      print("netPayable", netPayable)
   def preIncentiveTransactionReport(self):
      global xquantity
      global xincentiveAmt
      global xtdsAmount
      global xnetPayable
      xquantity = int(quantity)
      xincentiveAmt = float(incentiveAmt)
      xtdsAmount = float(tdsAmount)
      xnetPayable = float(netPayable)
   def verifyIncentiveTransactionReport(self, cash, credit):
      assert int(quantity) == int(xquantity) + 1
      incentiveAmtCalc = cash*0.6 + credit
      print("incentiveAmtCalc", int(incentiveAmtCalc))
      assert int(incentiveAmt) == int(incentiveAmtCalc) + int(xincentiveAmt)
      tdsAmtCalc = incentiveAmtCalc*0.15
      print("tdsAmtCalc", int(tdsAmtCalc))
      assert float(tdsAmount) == float(xtdsAmount) + tdsAmtCalc
      netPayableCalc = incentiveAmtCalc - tdsAmtCalc
      print("netPayableCalc", netPayableCalc)
      assert float(netPayable) == float(xnetPayable) + netPayableCalc
   def IncentivePayment(self):
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Payment").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//button[contains(text(), ' Search ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Ledger Name']").send_keys("Nisha & Dharam")
      self.danpheEMR.find_element_by_xpath("//textarea").send_keys("This is test payment")
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Make Payment')]").click()
      time.sleep(5)
   def createLedgerIncentivePayment(self):
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Payment").click()
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//strong[contains(.,'Create ledger for selected doctor')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Create New Ledger").click()
   def getIncentivePaymentReport(self):
      global TotalIncome
      global TDSAmt
      global NetIncome
      global AdjustedAmount
      time.sleep(9)
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//a[contains(.,' Reports ')]").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Payment Report").click()
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(doctor1)
      time.sleep(5)
      TotalIncome = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      TDSAmt = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
      NetIncome = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
      AdjustedAmount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
   def preIncentivePaymentReport(self):
      global xTotalIncome
      global xTDSAmt
      global xNetIncome
      global xAdjustedAmount
      xTotalIncome = TotalIncome
      xTDSAmt = TDSAmt
      xNetIncome = NetIncome
      xAdjustedAmount = AdjustedAmount
   def verifyIncentivePaymentReport(self):
      assert TotalIncome == xTotalIncome # + totalIncomeCalc
      assert TDSAmt == xTDSAmt # + tdsAmtCalc
      assert NetIncome == xNetIncome # + netIncomeCalc
      assert AdjustedAmount == xAdjustedAmount # + adjustAmtCalc
   def verifyAcMasterMapping(self):
      print(" ##Start of ACC_MST_Hospital table mapping with AccPrimaryHospitalShortName core cfg parameter value ##")
   def getIncentivePatientVsServiceReport(self):
      global IncentiveAmt
      global TDSAmt
      global NetPayable
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(.,' Reports ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Patient Vs Service Report").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
      #self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      IncentiveAmt = self.danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[1]").text
      print("IncentiveAmt", IncentiveAmt)
      TDSAmt = self.danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[2]").text
      print("TDSAmt", TDSAmt)
      NetPayable = self.danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[3]").text
      print("NetPayable", NetPayable)
      time.sleep(5)
   def preIncentivePatientVsServiceReport(self):
      global xIncentiveAmt
      global xTDSAmt
      global xNetPayable
      xIncentiveAmt = float(IncentiveAmt)
      xTDSAmt = float(TDSAmt)
      xNetPayable = float(NetPayable)
   def verifyIncentivePatientVsServiceReport(self, amount):
       calcIncentive = amount * .60
       calcTDS = calcIncentive * .15
       print("IncentiveAmt", IncentiveAmt)
       print("xIncentiveAmt", xIncentiveAmt)
       print("calcIncentive", calcIncentive)
       assert float(IncentiveAmt) == xIncentiveAmt + calcIncentive   # incentive %
       assert float(TDSAmt) == xTDSAmt + calcTDS         # TDS 15%
       print("xNetPayable", xNetPayable)
       print("NetPayable", NetPayable)
       print("TDSAmt", TDSAmt)
       assert  float(NetPayable) == float(IncentiveAmt) - float(TDSAmt)
       assert float(NetPayable) == xNetPayable + float(calcIncentive) - float(calcTDS) # incentive after deducting TDS
   def insurancePatientRegistration(self):
      global NSHI
      print("Start >> Insurance Patient Registration")
      self.danpheEMR.find_element_by_link_text("GovInsurance").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Patient List").click()
      self.danpheEMR.find_element_by_id("btnNewInsurancePat").click()
      fname = str(random.randint(1111, 9999))
      self.danpheEMR.find_element_by_id("aptPatFirstName").send_keys("insu", fname)
      #self.danpheEMR.find_element_by_id("middleName").send_keys("Patient")
      self.danpheEMR.find_element_by_id("lastName").send_keys("registration")
      dropdown = self.danpheEMR.find_element_by_id("selGender")
      dropdown.find_element_by_xpath("//option[. = 'Male']").click()
      self.danpheEMR.find_element_by_id("selGender").click()
      self.danpheEMR.find_element_by_id("age").send_keys(5)
      NSHI = str(random.randint(11111, 99999))
      self.danpheEMR.find_element_by_id("Ins_NshiNumber").send_keys(NSHI)
      self.danpheEMR.find_element_by_id("Ins_InsuranceBalance").send_keys(50000)
      dropdown = self.danpheEMR.find_element_by_id("firstServicePoint")
      dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
      self.danpheEMR.find_element_by_id("firstServicePoint").click()
      time.sleep(3)
      dropdown = self.danpheEMR.find_element_by_id("IsFamilyHead")
      dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
      self.danpheEMR.find_element_by_id("IsFamilyHead").click()
      self.danpheEMR.find_element_by_id("register").click()
   def insuranceNewVisit(self):
      global NSHI
      print(">> Start: Create insurance patient new visit")
      self.danpheEMR.find_element_by_link_text("GovInsurance").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Patient List").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(NSHI)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'New Visit')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("txtDepartment").send_keys("GYNAE & OBS")
      time.sleep(3)
      self.danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.RETURN)
      time.sleep(2)
      self.danpheEMR.find_element_by_id("btnPrintInvoice").click()
   def receivedStoreDispatch(self, store):
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(8)
      a = "//i[contains(.,'"
      b = store
      c = "')]"
      d = a + b + c
      self.danpheEMR.find_element_by_xpath(d).click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Inventory Requisition").click()
      #ReqNo = 750
      #self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(ReqNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//a[contains(.,'Receive Items')])[1]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Receive')]").click()
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Back to Requisition List')]").click()
   def createManualVoucher(self):
      self.danpheEMR.find_element_by_link_text("Accounting").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Transaction").click()
      self.danpheEMR.find_element_by_link_text("Voucher Entry").click()
      dropdown = self.danpheEMR.find_element_by_id("voucher")
      dropdown.find_element_by_xpath("//option[. = 'Purchase Voucher']").click()
      assert self.danpheEMR.switch_to.alert.text == "Are you sure you want to change the Voucher Type?"
      self.danpheEMR.switch_to.alert.accept()
      self.danpheEMR.find_element_by_css_selector(".fa-question").click()
      assert self.danpheEMR.switch_to.alert.text == "Do you want to create new Ledger?"
      self.danpheEMR.switch_to.alert.accept()
      time.sleep(4)
      self.danpheEMR.find_element_by_id("primarygroup").click()
      time.sleep(3)
      dropdown = self.danpheEMR.find_element_by_id("primarygroup")
      time.sleep(3)
      dropdown.find_element_by_xpath("//option[. = 'Assets']").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("primarygroup").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("primarygroup").click()
      self.danpheEMR.find_element_by_css_selector(".div-relative .ng-untouched").click()
      self.danpheEMR.find_element_by_css_selector(".col-md-8 > .danphe-auto-complete-wrapper > .ng-untouched").click()
      self.danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .ng-dirty").send_keys("Test Dr. 1")
      self.danpheEMR.find_element_by_css_selector(".btn-primary").click()
      self.danpheEMR.find_element_by_id("Amount_1").send_keys(100)
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".fa-plus").click()
      self.danpheEMR.find_element_by_id("DrCr_2").click()
   #def insuranceBilling(self, itemName):
     # Emergency Module
   def EmergencyRegistration(self):
       self.danpheEMR.find_element_by_link_text("Emergency").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'New patient')]").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'New Registration ')]").click()
       time.sleep(5)
       # self.danpheEMR.find_element_by_id("erPatFirstName").send_keys("ram")
       self.danpheEMR.find_element_by_xpath("//span[contains(text(),'Add Unknown ER-Patient')]").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_id("erPatGender").send_keys("M")
       self.danpheEMR.find_element_by_xpath("//button[@id='register']").click()
   # Setting Module
   # Adding user
   def Setting_add_employee(self):
       global randomnum
       self.danpheEMR.find_element_by_link_text("Settings").click()
       time.sleep(5)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Employee')]").click()
       time.sleep(5)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Add Employee')]").click()
       time.sleep(5)
       randomnum = str(random.randint(1111, 9999))
       self.danpheEMR.find_element_by_id("FirstName").send_keys("DR. Ankit", randomnum)
       self.danpheEMR.find_element_by_id("LastName").send_keys("lastname")
       dropdown = self.danpheEMR.find_element_by_id("Gender")
       dropdown.send_keys("M")
       self.danpheEMR.find_element_by_id("EmployeeDepartment").send_keys("admin")
       # self.danpheEMR.find_element_by_id("isApptApplicable").click()
       self.danpheEMR.find_element_by_id("Add").click()

   def Setting_Adding_User(self):
       global randomnum

       self.danpheEMR.find_element_by_link_text("Settings").click()
       time.sleep(5)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Security')]").click()
       time.sleep(5)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Add User')]").click()
       time.sleep(5)
       Select_emp= self.danpheEMR.find_element_by_id("EmployeeId")
       Select_emp.send_keys(Keys.TAB)
       user_name = self.danpheEMR.find_element_by_id("UserName")
       user_name.send_keys("Ankit", randomnum)
       Email = self.danpheEMR.find_element_by_id("EmailId")
       Email.send_keys("ankit", randomnum, "@gmail.com")
       password = self.danpheEMR.find_element_by_id("Password").send_keys("pass123")
       self.danpheEMR.find_element_by_id("Addbtn").click()


def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

