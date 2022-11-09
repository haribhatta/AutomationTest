import time
import Library.GlobalShareVariables as gSV
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

AppName = gSV.appName

# Since System Use the default value 1 the Quantity is Removed


def activateInventory(danpheEMR, inventory='General Inventory' or 'Medical Inventory'):
    print("Inventory Selection Start")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    time.sleep(5)
    if inventory == 'General Inventory':
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'General Inventory')]").click()
    else:
        danpheEMR.find_element(By.XPATH,  "//i[contains(text(),'Medical Inventory')]").click()
    print("Inventory Selection End")

def createPurchaseOrder(danpheEMR, itemName1, rate, itemName2, NepaliReceipt):
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    time.sleep(2)
    danpheEMR.find_element(By.XPATH, "//a[@href = '#/ProcurementMain/PurchaseOrder']").click()
    danpheEMR.find_element(By.XPATH, "//input[@value = 'Create Purchase Order']").click()
    danpheEMR.find_element(By.ID, "VendorName").click()
    danpheEMR.find_element(By.ID, "VendorName").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "poItemName0").send_keys(itemName1)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "poItemName0").send_keys(Keys.ENTER)
    # danpheEMR.find_element(By.ID, "ipqty0").send_keys(Keys.CLEAR)
    # danpheEMR.find_element(By.ID, "ipqty0").send_keys(qty)
    danpheEMR.find_element(By.ID, "ipstdrate0").send_keys(rate)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Add New Row')]").click()
    danpheEMR.find_element(By.ID, "poItemName1").send_keys(itemName2)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "poItemName1").send_keys(Keys.ENTER)
    # danpheEMR.find_element(By.ID, "ipqty1").send_keys(Keys.CLEAR)
    # danpheEMR.find_element(By.ID, "ipqty1").send_keys(qty)
    danpheEMR.find_element(By.ID, "ipstdrate1").send_keys(rate)
    danpheEMR.find_element(By.ID, "PurchaseOrderbtn").click()
    time.sleep(3)
    if NepaliReceipt == 'false':
        pono = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/table[2]/tbody/tr[1]/td[2]").text
        pono = int(str(pono.replace("PO No.:", "")))
    else:
        pono = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/div/div[1]/div[2]/div[3]/div[1]").text
        pono = int(str(pono.replace("खरिद आदेश नं : ", "")))
    print("Purchase Order Number is :", pono)
    return pono


def verifyPOVerifyer(danpheEMR, pono, NepaliReceipt):
    print("START:Verifying the Purchase Verifyer  ")
    time.sleep(3)
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    danpheEMR.find_element(By.XPATH, "//a[@href = '#/ProcurementMain/PurchaseOrder']").click()
    time.sleep(3)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(pono)
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//a[@class ='grid-action' = 'view']").click()
    time.sleep(1)
    if NepaliReceipt == 'false':
        time.sleep(2)
        verifyer = "Mr. admin admin"
        verifiedby = danpheEMR.find_element(By.XPATH, "//*[@id='printpage']/table[4]/tbody/tr[3]/td[2]/div/div[1]").text
        print(verifiedby)
        assert verifyer == verifiedby


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

def CreateGoodsArrivalNotification(danpheEMR, itemName1, rate, itemName2):
    print("START>> Create new goods arrival notification")
    danpheEMR.find_element(By.LINK_TEXT, "Procurement").click()
    danpheEMR.find_element(By.LINK_TEXT, "Goods Arrival Notification").click()
    time.sleep(5)
    danpheEMR.find_element(By.LINK_TEXT, "Create Goods Receipt").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "VendorName").click()
    time.sleep(5)
    danpheEMR.find_element(By.ID, "VendorName").send_keys(Keys.ENTER)
    danpheEMR.find_element(By.ID, "poItemName0").send_keys(itemName1)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "poItemName0").send_keys(Keys.ENTER)
    # danpheEMR.find_element(By.ID, "ipqty0").send_keys(Keys.CLEAR)
    # danpheEMR.find_element(By.ID, "ipqty0").send_keys(qty)
    danpheEMR.find_element(By.ID, "ipstdrate0").send_keys(rate)
    danpheEMR.find_element(By.XPATH, "//button[contains(text(),'Add New Row')]").click()
    danpheEMR.find_element(By.ID, "poItemName1").send_keys(itemName2)
    time.sleep(1)
    danpheEMR.find_element(By.ID, "poItemName1").send_keys(Keys.ENTER)


def enablePatientConsumptionApplicable(danpheEMR, itemname):
    print("START: enabling item for patient consumption")
    time.sleep(1)
    source = danpheEMR.find_element(By.LINK_TEXT, "Procurement")
    action = ActionChains(danpheEMR)
    action.double_click(source).perform()
    time.sleep(5)
    danpheEMR.find_element(By.CSS_SELECTOR, ".page-breadcrumb > li:nth-child(5) > a").click()
    time.sleep(2)
    danpheEMR.find_element(By.ID, "quickFilterInput").send_keys(itemname)
    time.sleep(1)
    danpheEMR.find_element(By.XPATH, "//a[contains(text(), 'Edit')]").click()
    checkbox = danpheEMR.find_element(By.ID, "IsPatConsumptionApplicable")
    print(checkbox.is_selected())
    time.sleep(2)
    if checkbox.is_selected == "False":
        danpheEMR.find_element(By.CSS_SELECTOR, ".col-md-5 .ng-tns-c12-0:nth-child(2)").click()
        danpheEMR.find_element(By.ID, "AddItem").click()
    else:
        danpheEMR.find_element(By.ID, "AddItem").click()
    print("END: Items Enabled for Patient consumption")


def wait_for_window(danpheEMR, timeout=2):
    time.sleep(round(timeout / 1000))
    wh_now = danpheEMR.window_handles
    wh_then = vars("window_handles")
    if len(wh_now) > len(wh_then):
        return set(wh_now).difference(set(wh_then)).pop()


def __str__():
    return

