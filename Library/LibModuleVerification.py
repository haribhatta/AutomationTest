import time
import Library.GlobalShareVariables as GSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


AppName = GSV.appName
# This item name and quantity is to verify that the correct name and items along with grno to verify


def substoreRequisitionVerification(danpheEMR, reqno, itemname, qty):
    danpheEMR.find_element(By.LINK_TEXT, "Verification").click()
    # danpheEMR.find_element(By.LINK_TEXT, "Requisition").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(reqno)
    time.sleep(4)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'View')]").click()
    time.sleep(2)
    item = danpheEMR.find_element(By.XPATH, "//*[@id='itemRow']/td[3]").text
    print("Item Name is :", item)
    print("Requested item name is :", itemname)
    assert item == itemname
    time.sleep(4)
    quantity = danpheEMR.find_element(By.XPATH, "//*[@id='itemRow']/td[8]").text
    quantity = int(quantity)
    print("Quantity in the system is ", quantity)
    time.sleep(2)
    print("Requisition Quantity is ", qty)
    qty = int(qty)
    assert quantity == qty
    danpheEMR.find_element(By.NAME, "VerificationRemarks").send_keys("This requisition is Verified please proceed further process")
    danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Approve')]").click()


def verifyInventoryPurchaseOrder(danpheEMR,  NepaliReceipt, purchaseOrderNo, itemname, quantity):
    print("START: Verifying Purchase Order")
    if NepaliReceipt == 'true' or 'false':
        danpheEMR.find_element(By.LINK_TEXT, "Verification").click()
        time.sleep(2)
        danpheEMR.find_element(By.LINK_TEXT, "Purchase Order").click()
        time.sleep(1)
        danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(purchaseOrderNo)
        danpheEMR.find_element(By.XPATH, "//a[@class = 'grid-action'= 'verify']").click()
        time.sleep(1)
        name = danpheEMR.find_element(By.XPATH, "//*[@id='itemRow']/td[4]").text
        print("Itemname of Given item is :", name)
        orderQuantity = danpheEMR.find_element(By.XPATH, "//*[@id='itemRow']/td[5]").text
        print("Order Quantity is :", orderQuantity)
        orderQuantity = int(orderQuantity)
        assert itemname == name
        assert quantity == orderQuantity
        danpheEMR.find_element(By.NAME, "VerificationRemarks").send_keys(
            "This Purchase Ordeer is Verified so, please proceed ")
        danpheEMR.find_element(By.XPATH, "//button[contains(text(), 'Approve')]").click()
    print("END: Verifying purchase Order")


