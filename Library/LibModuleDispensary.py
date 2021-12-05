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
    if AppName == "SNCH" or AppName == "MPH" or AppName == "LPH":
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
    return pInvoiceNo
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
def returnPharmacyInvoice(pInvoiceNo, qty, returnremark):
    print(">>Return Pharmacy Invoice: START")
    if AppName == 'SNCH' or AppName == "MPH" or AppName == "LPH":
        danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        # danpheEMR.find_element_by_xpath("//i[contains(.,'MainDispensary')]").click()
        # time.sleep(2)
        danpheEMR.find_element_by_link_text("Return From Customer").click()
        time.sleep(3)
        danpheEMR.find_element_by_id("invoiceId").send_keys(pInvoiceNo)
        print("pInvoiceNo is getting returned", pInvoiceNo)
        time.sleep(2)
        danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.TAB)
        time.sleep(3)
        danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.ENTER)
        time.sleep(5)
        danpheEMR.find_element_by_id("ReturnedQty0").clear()
        danpheEMR.find_element_by_id("ReturnedQty0").send_keys(qty)
        danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys(returnremark)
        danpheEMR.find_element_by_id("return").click()
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger']").click()
        time.sleep(5)
    print("<<Return Pharmacy Invoice: END")
def verifyReturnPharmacyInvoice(HospitalNo, paymentmode, returnRemark):
    print("<<Verify Return Pharmacy Invoice: START")
    if AppName == 'SNCH':
        danpheEMR.find_element_by_link_text("Return Sale List").click()
        danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        danpheEMR.find_element_by_link_text("Print").click()
        time.sleep(3)
        syspaymentmode = danpheEMR.find_element_by_xpath("//p[contains(text(),'Method of payment: ')]").text
        print("syspaymentmode:", syspaymentmode)
        syspaymentmode = syspaymentmode.partition("t: ")[2]
        # print("syspaymentmode1:", syspaymentmode)
        assert syspaymentmode == "Cash"  # as per the comment on bug:EMR-2699 payment mode need to be cash on credit note.
        ReturnremarkTemp = danpheEMR.find_element_by_xpath("//div[@id='pharma-pat-info']/div[12]").text
        print("ReturnremarkTemp", ReturnremarkTemp)
        ReturnremarkTemp = ReturnremarkTemp.partition("s : ")[2]
        print("ReturnremarkTemp", ReturnremarkTemp)
        assert ReturnremarkTemp == returnRemark
        time.sleep(5)
        danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
        # danpheEMR.find_element_by_css_selector(".fa-close").click()

    print(">>Verify Return Pharmacy Invoice: END")

def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__():
      return

