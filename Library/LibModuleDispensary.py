from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)


# Module:Dispensary ------------------
def createDispensarySale(self, qty, paymentmode):
    print(">>Create Dispensary Sale to Hospital Patient: START")
    global pInvoiceNo
    self.danpheEMR.find_element_by_link_text("Dispensary").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Sale").click()
    self.danpheEMR.find_element_by_id("patient-search").click()
    self.danpheEMR.find_element_by_id("patient-search").send_keys(HospitalNo)
    time.sleep(3)
    self.danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
    self.danpheEMR.find_element_by_id("patient-search").send_keys(Keys.RETURN)
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").click()
    self.danpheEMR.find_element_by_id("item-box0").clear()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").send_keys()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    drugavlqty = self.danpheEMR.find_element_by_xpath("(//input[@value=''])[6]").get_attribute("Value")
    print("Drug Available qty:", drugavlqty)
    drugavlqty = self.danpheEMR.find_element_by_css_selector("td:nth-child(8) > .form-control").text
    print("Drug Available qty:", drugavlqty)
    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").click()
    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").clear()
    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").send_keys(qty)
    drugremainingqty = int(drugqtySS) - qty
    print("Remaining qty:", drugremainingqty)
    newdrugqtySS = drugremainingqty
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text("CREDIT")
        time.sleep(2)
        self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")

    self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
    time.sleep(5)
    pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]

    print("Create Pharmacy OPD Invoice: END<<")


def createDispensarySaleRandomPatient(self, drugname, qty, paymentmode):
    print("<<START: Create Dispensary sales to random customer.")
    global pInvoiceNo
    self.danpheEMR.find_element_by_link_text("Dispensary").click()
    time.sleep(2)
    # self.danpheEMR.find_element_by_link_text("Patient").click()
    # time.sleep(5)
    # self.danpheEMR.find_element_by_xpath("(//a[contains(text(),'Sale') and @class='grid-action'])[2]").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").click()
    self.danpheEMR.find_element_by_id("item-box0").clear()
    self.danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").click()
    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").clear()
    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname= 'Quantity']").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'CREDIT':
        paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text("CREDIT")
        time.sleep(2)
        self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    # self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
    self.danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
    time.sleep(5)
    pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("END>> Create Pharmacy OPD Invoice.", pInvoiceNo)
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

