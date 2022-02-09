import time
import Library.GlobalShareVariables as gSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

AppName = gSV.appName


def createPurchaseOrder(danpheEMR, itemName1, qty, rate, itemName2):
    time.sleep(2)
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    danpheEMR.find_element(By.XPATH, "//a[@href = '#/ProcurementMain/PurchaseOrder']").click()
    danpheEMR.find_element(By.XPATH, "//input[@value = 'Create Purchase Order']").click()
    danpheEMR.find_element(By.ID, "VendorName").click()
    danpheEMR.find_element(By.ID, "VendorName").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "poItemName0").send_keys(itemName1)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "poItemName0").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "ipqty0").send_keys(qty)
    danpheEMR.find_element(By.ID, "ipstdrate0").send_keys(rate)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Add New Row')]").click()
    danpheEMR.find_element(By.ID, "poItemName1").send_keys(itemName2)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "poItemName1").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "ipqty1").send_keys(qty)
    danpheEMR.find_element(By.ID, "ipstdrate1").send_keys(rate)
    danpheEMR.find_element(By.ID, "PurchaseOrderbtn").click()
    time.sleep(3)
    pono = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/table[2]/tbody/tr[1]/td[3]").text
    pono = int(str(pono.replace("PO No.:", "")))
    print("Purchase Order Number is :", pono)
    return pono


def cancelPurchaseOrder(danpheEMR, pono):
    danpheEMR.implicitly_wait(10)
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    danpheEMR.find_element(By.XPATH, "//a[@href = '#/ProcurementMain/PurchaseOrder']").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(pono)
    danpheEMR.find_element(By.XPATH, "//*[@id='myGrid']/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div[9]/span/a[1]").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Withdraw')]").click()
    danpheEMR.find_element(By.NAME, "cancelRemarks").send_keys("Cancelled due to some reason")
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Yes')]").click()
    time.sleep(1)

def cancelInventoryGoodsReceipt(danpheEMR, BillNo):
    print("START>> Canceling Inventory Good Receipt")
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(BillNo)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(),'View')]").click()
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Cancel GR')]").click()
    time.sleep(2)
    danpheEMR.find_element(By.NAME, "cancelRemarks").send_keys("Cancel good receipt due to breakage")
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Yes')]").click()
    time.sleep(2)


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return

