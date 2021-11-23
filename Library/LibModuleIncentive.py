import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Library.LibModuleAppointment as LA
########
danpheEMR = AC.danpheEMR
AppName = AC.appName
########
#Module:Incentive ******************
def synchBilingIncentive():
      danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Bill Sync").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//button[contains(.,' Sync Billing to Incentives')]").click()
      time.sleep(5)
def getIncentiveTransactionReport(doctorName):
      global quantity
      global incentiveAmt
      global tdsAmount
      global netPayable
      danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//a[text()='Transaction Report']").click()
      time.sleep(1)
      danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(doctorName)
      time.sleep(1)
      danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
      danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.TAB)
      danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      quantity = danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[3]").text
      print("quantity", quantity)
      incentiveAmt = danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[4]").text
      print("incentiveAmt", incentiveAmt)
      tdsAmount = danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[5]").text
      print("tdsAmount", tdsAmount)
      netPayable = danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[6]").text
      print("netPayable", netPayable)
def preIncentiveTransactionReport():
      global xquantity
      global xincentiveAmt
      global xtdsAmount
      global xnetPayable
      xquantity = int(quantity)
      xincentiveAmt = float(incentiveAmt)
      xtdsAmount = float(tdsAmount)
      xnetPayable = float(netPayable)
def verifyIncentiveTransactionReport(cash, credit):
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
def IncentivePayment(doctorName):
      danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Payment").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctorName)
      danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.ARROW_DOWN)
      danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
      danpheEMR.find_element_by_xpath("//button[contains(text(), ' Search ')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//input[@placeholder='Ledger Name']").send_keys("Nisha & Dharam")
      danpheEMR.find_element_by_xpath("//textarea").send_keys("This is test payment")
      danpheEMR.find_element_by_xpath("//button[contains(.,'Make Payment')]").click()
      time.sleep(5)
def createLedgerIncentivePayment(doctorName):
      danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(2)
      danpheEMR.find_element_by_link_text("Payment").click()
      danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(doctorName)
      danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
      danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.TAB)
      danpheEMR.find_element_by_xpath("//strong[contains(.,'Create ledger for selected doctor')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Create New Ledger").click()
def getIncentivePaymentReport(doctorName):
      global TotalIncome
      global TDSAmt
      global NetIncome
      global AdjustedAmount
      time.sleep(9)
      danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(5)
      danpheEMR.find_element_by_xpath("//a[contains(.,' Reports ')]").click()
      time.sleep(5)
      danpheEMR.find_element_by_link_text("Payment Report").click()
      danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(doctorName)
      time.sleep(5)
      TotalIncome = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      TDSAmt = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
      NetIncome = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
      AdjustedAmount = danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
def preIncentivePaymentReport():
      global xTotalIncome
      global xTDSAmt
      global xNetIncome
      global xAdjustedAmount
      xTotalIncome = TotalIncome
      xTDSAmt = TDSAmt
      xNetIncome = NetIncome
      xAdjustedAmount = AdjustedAmount
def verifyIncentivePaymentReport():
      assert TotalIncome == xTotalIncome # + totalIncomeCalc
      assert TDSAmt == xTDSAmt # + tdsAmtCalc
      assert NetIncome == xNetIncome # + netIncomeCalc
      assert AdjustedAmount == xAdjustedAmount # + adjustAmtCalc
def getIncentivePatientVsServiceReport(doctorName):
      global IncentiveAmt
      global TDSAmt
      global NetPayable
      danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(.,' Reports ')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Patient Vs Service Report").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctorName)
      danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
      #danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      IncentiveAmt = danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[1]").text
      print("IncentiveAmt", IncentiveAmt)
      TDSAmt = danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[2]").text
      print("TDSAmt", TDSAmt)
      NetPayable = danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[3]").text
      print("NetPayable", NetPayable)
      time.sleep(5)
def preIncentivePatientVsServiceReport():
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

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

