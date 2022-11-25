import time
from selenium.webdriver.common.by import By
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
########
AppName = GSV.appName


########
# Module:Incentive ******************
def synchBilingIncentive(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Bill Sync").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Sync Billing to Incentives')]").click()
    time.sleep(5)


def getIncentiveTransactionReport(danpheEMR, doctorName):
    global actualQuantity
    global actualIncentiveAmt
    global actualTDSAmt
    global actualNetPayable
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'Reports')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[text()='Transaction Report']").click()
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select()']").send_keys(doctorName)
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select()']").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    #actualQuantity = danpheEMR.find_element(By.XPATH, "//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[3]").text
    actualQuantity = danpheEMR.find_element(By.XPATH, "(//td[contains(text(),'CONSULTATION CHARGE')]/following-sibling::td)[1]").text
    actualQuantity = int(actualQuantity)
    print("actualQuantity", actualQuantity)
    #actualIncentiveAmt = danpheEMR.find_element(By.XPATH, "//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[4]").text
    actualIncentiveAmt = danpheEMR.find_element(By.XPATH, "(//td[contains(text(),'CONSULTATION CHARGE')]/following-sibling::td)[2]").text
    actualIncentiveAmt = float(actualIncentiveAmt)
    print("actualIncentiveAmt", actualIncentiveAmt)
    #actualTDSAmt = danpheEMR.find_element(By.XPATH, "//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[5]").text
    actualTDSAmt = danpheEMR.find_element(By.XPATH, "(//td[contains(text(),'CONSULTATION CHARGE')]/following-sibling::td)[3]").text
    actualTDSAmt = float(actualTDSAmt)
    print("actualTDSAmt", actualTDSAmt)
    #actualNetPayable = danpheEMR.find_element(By.XPATH, "//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[6]").text
    actualNetPayable = danpheEMR.find_element(By.XPATH, "(//td[contains(text(),'CONSULTATION CHARGE')]/following-sibling::td)[4]").text
    actualNetPayable = float(actualNetPayable)
    print("actualNetPayable", actualNetPayable)


def preIncentiveTransactionReport():
    global preQuantity
    global preIncentiveAmt
    global preTDSAmt
    global preNetPayable
    preQuantity = actualQuantity
    preIncentiveAmt = actualIncentiveAmt
    preTDSAmt = actualTDSAmt
    preNetPayable = actualNetPayable


def verifyIncentiveTransactionReport(cash, credit):
    global expectedQuantity
    global expectedIncentiveAmt
    global expectedTDSAmt
    global expectedNetPayable
    expectedQuantity = preQuantity + 1
    print("expectedQuantity:", expectedQuantity)
    assert expectedQuantity == actualQuantity
    #
    incentiveAmtCalc = cash * 0.421 + credit
    expectedIncentiveAmt = preIncentiveAmt + incentiveAmtCalc
    expectedIncentiveAmt = int(expectedIncentiveAmt)
    #actualIncentiveAmt = int(actualIncentiveAmt)
    print("actualIncentiveAmt:", actualIncentiveAmt)
    print("expectedIncentiveAmt:", expectedIncentiveAmt)
    assert expectedIncentiveAmt == actualIncentiveAmt
    #
    tdsAmtCalc = incentiveAmtCalc * 0.15
    expectedTDSAmt = preTDSAmt + tdsAmtCalc
    expectedTDSAmt = int(expectedTDSAmt)
    actualTDSAmt = int(actualTDSAmt)
    print("actualTDSAmt:", actualTDSAmt)
    print("expectedTDSAmt:", expectedTDSAmt)
    assert expectedTDSAmt == actualTDSAmt
    #
    netPayableCalc = incentiveAmtCalc - tdsAmtCalc
    expectedNetPayable = preNetPayable + netPayableCalc
    expectedNetPayable = int(expectedNetPayable)
    actualNetPayable = int(actualNetPayable)
    print("actualNetPayable:", actualNetPayable)
    print("expectedNetPayable:", expectedNetPayable)
    assert expectedNetPayable == actualNetPayable


def IncentivePayment(danpheEMR, doctorName):
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Payment").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(doctorName)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(Keys.ARROW_DOWN)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), ' Search ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Ledger Name']").send_keys("Nisha & Dharam")
    danpheEMR.find_element(By.XPATH, "//textarea").send_keys("This is test payment")
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Make Payment')]").click()
    time.sleep(5)


def createLedgerIncentivePayment(danpheEMR, doctorName):
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Payment").click()
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select()']").send_keys(doctorName)
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
    danpheEMR.find_element(By.XPATH, "//input[@onclick='this.select()']").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//strong[contains(.,'Create ledger for selected doctor')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Create New Ledger").click()


def getIncentivePaymentReport(danpheEMR, doctorName):
    global TotalIncome
    global TDSAmt
    global NetIncome
    global AdjustedAmount
    time.sleep(9)
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//a[contains(.,' Reports ')]").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Payment Report").click()
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(doctorName)
    time.sleep(5)
    TotalIncome = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[3]").text
    TDSAmt = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[4]").text
    NetIncome = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[5]").text
    AdjustedAmount = danpheEMR.find_element(By.XPATH, "//div[2]/div/div/div/div[6]").text


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
    assert TotalIncome == xTotalIncome  # + totalIncomeCalc
    assert TDSAmt == xTDSAmt  # + tdsAmtCalc
    assert NetIncome == xNetIncome  # + netIncomeCalc
    assert AdjustedAmount == xAdjustedAmount  # + adjustAmtCalc


def getIncentivePatientVsServiceReport(danpheEMR, doctorName):
    global IncentiveAmt
    global TDSAmt
    global NetPayable
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//a[contains(.,' Reports ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Patient Vs Service Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(doctorName)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
    # danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    IncentiveAmt = danpheEMR.find_element(By.XPATH, "//b[text()='Total :']/parent::td/following-sibling::td[1]").text
    print("IncentiveAmt", IncentiveAmt)
    TDSAmt = danpheEMR.find_element(By.XPATH, "//b[text()='Total :']/parent::td/following-sibling::td[2]").text
    print("TDSAmt", TDSAmt)
    NetPayable = danpheEMR.find_element(By.XPATH, "//b[text()='Total :']/parent::td/following-sibling::td[3]").text
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
    assert float(IncentiveAmt) == xIncentiveAmt + calcIncentive  # incentive %
    assert float(TDSAmt) == xTDSAmt + calcTDS  # TDS 15%
    print("xNetPayable", xNetPayable)
    print("NetPayable", NetPayable)
    print("TDSAmt", TDSAmt)
    assert float(NetPayable) == float(IncentiveAmt) - float(TDSAmt)
    assert float(NetPayable) == xNetPayable + float(calcIncentive) - float(calcTDS)  # incentive after deducting TDS

def transactionInvoice(danpheEMR, HospitalNo, ReferralName, Performer):
    print(">>START: TransactionInvoice")
    danpheEMR.find_element(By.LINK_TEXT, "Incentive").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Transactions").click()
    time.sleep(3)
    # danpheEMR.find_element(By.LINK_TEXT, "Invoice").click()
    # time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Load')]").click()
    time.sleep(4)
    danpheEMR.find_element(By.ID, 'srch_invoiceList').click()
    danpheEMR.find_element(By.ID, 'srch_invoiceList').send_keys(HospitalNo)
    danpheEMR.find_element(By.ID, 'srch_invoiceList').send_keys(Keys.ENTER)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(.,'Load')]").click()
    time.sleep(5)
    print("test1")
    # Source = danpheEMR.find_element(By.XPATH, "//i[@class = 'fa fa-eye']")
    # action = ActionChains(danpheEMR)
    # action.double_click(Source).perform()
    test = danpheEMR.find_element(By.XPATH, "//*[@class='fa fa-eye']")
    print(test.is_displayed())
    danpheEMR.find_element(By.XPATH, "//*[@class='fa fa-eye']").click()
    #time.sleep(5)
    print("test2")
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//*[@id='id_referral_chkbox_inctv']").click()
    print("test3")
    time.sleep(3)
    danpheEMR.find_element(By.ID, 'id_referral_employee_inctv').send.keys(ReferralName)
    time.sleep(3)
    danpheEMR.find_element(By.ID,'id_referral_percent_inctv').send.keys(10)
    time.sleep(3)
    danpheEMR.find_element(By.ID,'empIp_0').send.keys(Performer)
    time.sleep(3)
    danpheEMR.find_element(By.ID, 'percentip0').send.keys(20)
    time.sleep(3)
    danpheEMR.find_element(By.ID,'btn_SaveFraction').click()
    print(">>END: TransactionInvoice")

def ReferralSummaryReport(danpheEMR, doctorName):
    print(">>START Referral Summary Report")
    danpheEMR.find_element(By.XPATH, "//a[contains(.,' Reports ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Referral Summary Report").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(doctorName)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(Keys.ARROW_DOWN)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Show Report')]").click()


    print(">>END Referral Summary Report")





def wait_for_window(danpheEMR, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
