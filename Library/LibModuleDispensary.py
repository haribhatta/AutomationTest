import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
AppName = AC.appName
# Module:Dispensary ------------------
def activatePharmacyCounter():
    print(">>Start: Pharmacy Counter Activate: START")
    time.sleep(7)
    if AppName == "SNCH":
        danpheEMR.find_element_by_link_text("Dispensary").click()
        time.sleep(7)
        danpheEMR.find_element_by_xpath("//i[contains(text(),'MainDispensary')]").click()
        time.sleep(3)
    danpheEMR.find_element_by_link_text("Counter").click()
    time.sleep(2)
    danpheEMR.find_element_by_xpath("//h5").click()
    time.sleep(2)
    print("Pharmacy Counter Activate: END")
def createDispensarySale(HospitalNo, qty, drugName, paymentmode):
    print(">>Create Dispensary Sale to Hospital Patient: START")
    global pInvoiceNo
    danpheEMR.find_element_by_link_text("Dispensary").click()
    time.sleep(3)
    danpheEMR.find_element_by_link_text("Sale").click()
    danpheEMR.find_element_by_id("patient-search").click()
    danpheEMR.find_element_by_id("patient-search").send_keys(HospitalNo)
    time.sleep(3)
    danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
    danpheEMR.find_element_by_id("patient-search").send_keys(Keys.RETURN)
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").click()
    danpheEMR.find_element_by_id("item-box0").clear()
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").send_keys(drugName)
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    #drugavlqty = danpheEMR.find_element_by_xpath("(//input[@value=''])[6]").get_attribute("Value")
    #print("Drug Available qty:", drugavlqty)
    danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").click()
    danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").clear()
    danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text("credit")
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    danpheEMR.find_element_by_id("btnPrintPhrmInvoice").send_keys(Keys.ESCAPE)
    print("Create Pharmacy OPD Invoice: END<<")
def createDispensarySaleRandomPatient(drugname, qty, paymentmode):
    print("<<START: Create Dispensary sales to random customer.")
    global pInvoiceNo
    danpheEMR.find_element_by_link_text("Dispensary").click()
    time.sleep(2)
    time.sleep(3)
    danpheEMR.find_element_by_id("item-box0").click()
    danpheEMR.find_element_by_id("item-box0").clear()
    danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").click()
    danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").clear()
    danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'CREDIT':
        paymentoptions = Select(danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text("CREDIT")
        time.sleep(2)
        danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    danpheEMR.find_element_by_id("btnPrintPhrmInvoice").send_keys(Keys.ESCAPE)
    print("END>> Create Pharmacy OPD Invoice.", pInvoiceNo)
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

