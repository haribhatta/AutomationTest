import time
import random
from selenium.webdriver.common.keys import Keys
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

########
AppName = GSV.appName


########
# Module:Incentive ******************
def verifyAcMasterMapping():
    print(" ##Start of ACC_MST_Hospital table mapping with AccPrimaryHospitalShortName core cfg parameter value ##")


def createManualVoucher(danpheEMR, ledger1, ledger2):
    danpheEMR.find_element(By.LINK_TEXT, "Accounting").click()
    time.sleep(7)
    danpheEMR.find_element(By.LINK_TEXT, "Transaction").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "Ledger_1").send_keys(ledger1)
    danpheEMR.find_element(By.ID, "Ledger_1").send_keys(Keys.RETURN)
    time.sleep(3)
    amount = random.randint(1111, 9999)
    danpheEMR.find_element(By.ID, "Amount_1").clear()
    danpheEMR.find_element(By.ID, "Amount_1").send_keys(amount)
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[@class='fa fa-plus btn btn-success']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "Ledger_2").send_keys(ledger2)
    danpheEMR.find_element(By.ID, "Ledger_2").send_keys(Keys.RETURN)
    time.sleep(2)
    #danpheEMR.find_element(By.ID, "Amount_2").clear()
    #danpheEMR.find_element(By.ID, "Amount_2").send_keys(10000)
    danpheEMR.find_element(By.ID, "DrCr_2").send_keys("Cr")
    danpheEMR.find_element(By.ID, "narration").send_keys("Salary Paid")
    #danpheEMR.find_element(By.XPATH, "//button[@title='Alt+S, Enter']").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[@class='btn blue']").click()
    time.sleep(3)
    assert danpheEMR.switch_to.alert.text == "Are you sure you want to save?"
    danpheEMR.switch_to.alert.accept()
    time.sleep(3)
    voucherNo = danpheEMR.find_element(By.XPATH, "//td[contains(text(),'JV')]").text
    print("voucher No:", voucherNo)
    voucherNo = voucherNo.partition('No: ')[2]
    print("voucher No:", voucherNo)
    danpheEMR.find_element(By.XPATH, "//a[@title='Cancel' and contains(text(),'X')]").click()
    return voucherNo

def verifyVoucherReport(danpheEMR, voucherNo):
    danpheEMR.find_element(By.LINK_TEXT, "Accounting").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "(//a[@href='#/Accounting/Reports'])[2]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//i[contains(text(),'Voucher Report')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),' Load ')]").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(voucherNo)
    sysVoucherNo = danpheEMR.find_element(By.XPATH, "(//div[@col-id='VoucherNumber'])[2]").text
    print("sysVoucherNo:", sysVoucherNo)
    assert sysVoucherNo == voucherNo


def createLedgerGroup(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Accounting").click()
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Transaction").click()
    danpheEMR.find_element(By.LINK_TEXT, "Voucher Entry").click()
    dropdown = danpheEMR.find_element(By.ID, "voucher")
    dropdown.find_element(By.XPATH, "//option[. = 'Purchase Voucher']").click()
    assert danpheEMR.switch_to.alert.text == "Are you sure you want to change the Voucher Type?"
    danpheEMR.switch_to.alert.accept()
    danpheEMR.find_element(By.CSS_SELECTOR, ".fa-question").click()
    assert danpheEMR.switch_to.alert.text == "Do you want to create new Ledger?"
    danpheEMR.switch_to.alert.accept()
    time.sleep(4)
    danpheEMR.find_element(By.ID, "primarygroup").click()
    time.sleep(3)
    dropdown = danpheEMR.find_element(By.ID, "primarygroup")
    time.sleep(4)
    #dropdown.find_element(By.XPATH, "//option[. = 'Assets']").click()
    primaryGroup = Select(danpheEMR.find_element(By.XPATH, "//select[@formcontrolname='PrimaryGroup']"))
    primaryGroup.select_by_visible_text("Assets")
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//input[@placeholder='Ledger GroupName']").send_keys("Inventory")
    time.sleep(2)
    ledgerNumber = str(random.randint(15, 60))
    generatedLedgerName = "LedgerName" + ledgerNumber
    print("generatedLedgerName:", generatedLedgerName)
    danpheEMR.find_element(By.XPATH, "//input[@formcontrolname='LedgerName']").send_keys(generatedLedgerName)
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//input[@value='Add Ledger']").click()
    time.sleep(3)
    sysLedgerName = danpheEMR.find_element(By.XPATH, "//input[@placeholder='Ledger Name']").send_keys(Keys.RETURN)
    time.sleep(3)
    sysLedgerName = danpheEMR.find_element(By.XPATH, "//input[@placeholder='Ledger Name']").get_attribute("value")
    print("sysLedgerName:", sysLedgerName)
    assert sysLedgerName == generatedLedgerName


def PosttoAccounting(danpheEMR):
    danpheEMR.find_element(By.LINK_TEXT, "Accounting").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Post to Accounting").click()
    time.sleep(5)
    Module = Select(danpheEMR.find_element(By.ID, "sectionid"))
    time.sleep(5)
    Module.select_by_visible_text("Billing")
    time.sleep(5)
    Voucher = Select(danpheEMR.find_element(By.ID, "voucherhead"))
    time.sleep(5)
    Voucher.select_by_visible_text("life")
    time.sleep(5)
    danpheEMR.find_element(By.XPATH, "//button[@title='Load records of selected date']").click()
    time.sleep(3)
    danpheEMR.find_element(By.XPATH, "//button[@title='save selected to accounting'][1]").click()


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return
