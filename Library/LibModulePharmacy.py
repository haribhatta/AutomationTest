from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)


# Module:Pharmacy ------------------
def activatePharmacyCounter(self):
    print(">>Start: Pharmacy Counter Activate: START")
    time.sleep(7)
    # if appPort == "81":
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(3)
    if appPort == "82":
        self.danpheEMR.find_element_by_link_text("Dispensary").click()
        time.sleep(7)
        self.danpheEMR.find_element_by_xpath("//i[contains(text(),'MainDispensary')]").click()
        time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Counter").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//h5").click()
    time.sleep(2)
    print("Pharmacy Counter Activate: END")
    print("End>> generateDischargeInvoice")


def addPharmacyItem(self, genericName):  # incomplete
    print(">>START: addPharmacyItem")
    global DrugName
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Setting").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Item").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success']").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_xpath("//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(
        "Pharmay Unit")
    self.danpheEMR.find_element_by_xpath("//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(
        Keys.RETURN)
    drugMGtemp = random.randint(10, 1000)
    drugMG = str(drugMGtemp)
    DrugName = ('Autodrug' + drugMG)
    print(DrugName)
    self.danpheEMR.find_element_by_xpath("//input[@value='']").send_keys(DrugName)
    self.danpheEMR.find_element_by_xpath("//input[@value='']").send_keys(Keys.RETURN)
    time.sleep(3)
    # self.danpheEMR.find_element_by_css_selector("//select").click()
    self.danpheEMR.find_element_by_xpath("//div[4]/div/div/div/input").send_keys("HIMALAYAN")  # Company
    self.danpheEMR.find_element_by_xpath("//div[4]/div/div/div/input").send_keys(Keys.RETURN)
    self.danpheEMR.find_element_by_xpath("//div[5]/div/div/div/input").send_keys(genericName)  # itemType
    self.danpheEMR.find_element_by_xpath("//div[5]/div/div/div/input").send_keys(Keys.RETURN)  # itemType
    # self.danpheEMR.find_element_by_css_selector(".ng-touched:nth-child(1)").send_keys("ABGEL")
    self.danpheEMR.find_element_by_xpath("//div[6]/div/div/div/input").send_keys("Tablet")  # unit
    self.danpheEMR.find_element_by_xpath("//div[6]/div/div/div/input").send_keys(Keys.RETURN)  # unit
    self.danpheEMR.find_element_by_xpath("//div[7]/div/div/div/input").send_keys(genericName)  # genericName
    self.danpheEMR.find_element_by_xpath("//div[7]/div/div/div/input").send_keys(Keys.RETURN)  # genericName
    time.sleep(3)
    self.danpheEMR.find_element_by_id("save").click()
    time.sleep(9)
    print("End>>addPharmacyItem")


def verifyPharmacyItem(self):
    print(">>Start:verifyPharmacyItem")
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Setting").click()
    time.sleep(5)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(9)
    assert DrugName == self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
    print("End>>verifyPharmacyItem")


def getStoreDetail(self, drugname):
    print(">>Start: getStoreDetail")
    global drugqtyMS
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Store").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    #    time.sleep(5)
    #    drugnameMS = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
    #    print("drugnameMS:", drugnameMS)
    #    print("drugname:", drugname)
    #    assert drugnameMS == drugname
    #    sysdrugqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQty'])[2]").text
    #    drugqtyMS = int(sysdrugqty)
    #    print("drugqtyMS:", drugqtyMS)
    if appPort == '82':
        self.danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Store").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
        time.sleep(5)
        drugnameMS = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
        print("drugnameMS:", drugnameMS)
        print("drugname:", drugname)
        assert drugnameMS == drugname
        sysdrugqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
        drugqtyMS = int(sysdrugqty)
        print("drugqtyMS:", drugqtyMS)
    print("End>>getStoreDetail")


def getStockDetail(self, drugname):
    print(">>Start: getStockDetail")
    global drugqtySS
    # if appPort == '81':
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(5)
    #    self.danpheEMR.find_element_by_link_text("Stock").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    #    time.sleep(3)
    #    drugnameSS = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
    #    print("drugnameSS:", drugnameSS)
    #    sysdrugqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
    #    drugqtySS = int(sysdrugqty)
    #    print("drugqtySS:", drugqtySS)
    if appPort == '82':
        time.sleep(3)
        self.danpheEMR.find_element_by_link_text("Dispensary").click()
        time.sleep(5)
        self.danpheEMR.find_element_by_link_text("Stock").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
        time.sleep(3)
        drugnameSS = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
        print("drugnameSS:", drugnameSS)
        sysdrugqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
        drugqtySS = int(sysdrugqty)
        print("drugqtySS:", drugqtySS)
    print("End>>getStockDetail")


def verifyStoreDetail(self, drugname):
    print(">>Start:verifyStoreDetail")
    self.danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").clear()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(2)
    sysdrugname = self.danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[2]").text
    print("sysdrugname:", sysdrugname)
    assert drugname == sysdrugname
    sysdrugqty = self.danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    print("sysdrugqty", sysdrugqty)
    print("newdrugqtyMS", drugqtyMScalc)
    assert int(drugqtyMScalc) == int(sysdrugqty)
    print("End>>verifyStoreDetail")


def verifyStockDetail(self, drugname):
    print(">>Start: verifyStockDetail")
    self.danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(5)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(2)
    sysdrugname = self.danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div").text
    print("sysdrugname", sysdrugname)
    assert drugname == sysdrugname
    sysdrugqty = self.danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    print("drugqtySS:", drugqtySS)
    print("sysdrugqty", sysdrugqty)
    assert int(drugqtySS) == int(sysdrugqty)
    print("End>>: verifyStockDetail")


def verifyStockDetailTC(self):
    print(">>Start: verifyStockDetailTC")
    self.danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(5)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(2)
    sysdrugqty = self.danpheEMR.find_element_by_xpath(
        "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
    assert sysdrugqty == '0'
    print("End>>verifyStockDetailTC")


def transferStore2Dispensary(self, drugname, tqty):
    print(">>Start:transferStore2Dispensary")
    global drugqtyMS
    global drugqtySS
    self.danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").clear()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Transfer Item").click()
    self.danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(tqty)
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys("MainDispensary")
    time.sleep(1)
    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    drugqtyMS = drugqtyMS - tqty
    print("drugqtyMS", drugqtyMS)
    drugqtySS = drugqtySS + tqty
    print("drugqtySS", drugqtySS)
    print("End>>transferStore2Dispensary")


def transferStore2DispensaryTC(self, tqty, DrugName):
    print(">>Start:transferStore2DispensaryTC")
    self.danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").clear()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Transfer Item").click()
    self.danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(tqty)
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys("MainDispensary")
    time.sleep(1)
    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    print("End>>transferStore2DispensaryTC")


def transferDispensary2Store(self, drugname, tqty):
    print(">>Start: transferDispensary2Store")
    global drugqtySS
    global drugqtyMS
    self.danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Store Transfer").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_id("transfertoStoreQty").send_keys(tqty)
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    drugqtySS = int(drugqtySS) - tqty
    print("drugqtySS", drugqtySS)
    drugqtyMS = int(drugqtyMS) + tqty
    print("drugqtyMS", drugqtyMS)
    # self.danpheEMR.find_element_by_link_text("Store").click()
    print("End>>transferDispensary2Store")


def transferDispensary2StoreTC(self, tqty):
    print(">>Start: transferDispensary2StoreTC")
    self.danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Store Transfer").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_id("transfertoStoreQty").send_keys(tqty)
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Transfer')]").click()
    time.sleep(2)
    print("End>>transferDispensary2StoreTC")


def manageStoreStock(self, drugname, type, qty):
    print(">>START: Manage Store Stock")
    global drugqtyMScalc
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Store").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Manage Item").click()
    time.sleep(2)
    if type == "In":
        self.danpheEMR.find_element_by_css_selector(".mt-checkbox:nth-child(1) > span").click()
        drugqtyMScalc = int(drugqtyMS) + qty
    elif type == "Out":
        self.danpheEMR.find_element_by_css_selector(".mt-checkbox:nth-child(2) > span").click()
        drugqtyMScalc = int(drugqtyMS) - qty
    self.danpheEMR.find_element_by_xpath("//input[@name='UpdatedQty']").send_keys(qty)
    self.danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys("Stock adjusted")
    self.danpheEMR.find_element_by_xpath("//input[@value='Update Stock']").click()
    time.sleep(2)


def createPharmacyInvoice(self, qty, paymentmode):
    print(">>Create Pharmacy OPD Invoice: START")
    global pInvoiceNo
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
    self.danpheEMR.find_element_by_id("qty-box0").click()
    self.danpheEMR.find_element_by_id("qty-box0").clear()
    self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
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


def createPharmacyInvoiceRandomPatient(self, drugname, qty, paymentmode):
    print("<<START: Create Pharmacy OPD Invoice.")
    global pInvoiceNo
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(5)
    #    self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sale ')]").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("patient-search").click()
    #    self.danpheEMR.find_element_by_id("patient-search").send_keys('test')
    #    time.sleep(4)
    #    self.danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("item-box0").click()
    #    self.danpheEMR.find_element_by_id("item-box0").clear()
    #    self.danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    #    self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    #    time.sleep(5)
    #    self.danpheEMR.find_element_by_id("qty-box0").click()
    #    self.danpheEMR.find_element_by_id("qty-box0").clear()
    #    self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
    #    time.sleep(3)
    #    if paymentmode == 'CREDIT':
    #       paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
    #       paymentoptions.select_by_visible_text("CREDIT")
    #       time.sleep(2)
    #       self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    #    self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
    #    time.sleep(5)
    #    pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    #    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    #    self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    if appPort == '82':
        self.danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sale ')]").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_id("patient-search").click()
        self.danpheEMR.find_element_by_id("patient-search").send_keys('Auto Test')
        time.sleep(5)
        self.danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
        time.sleep(2)
        self.danpheEMR.find_element_by_id("item-box0").click()
        self.danpheEMR.find_element_by_id("item-box0").clear()
        self.danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
        self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
        time.sleep(5)
        self.danpheEMR.find_element_by_id("qty0").click()
        self.danpheEMR.find_element_by_id("qty0").clear()
        self.danpheEMR.find_element_by_id("qty0").send_keys(qty)
        time.sleep(3)
        if paymentmode == 'CREDIT':
            paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
            paymentoptions.select_by_visible_text("CREDIT")
            time.sleep(2)
            self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
        self.danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()
        time.sleep(5)
        pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
        pInvoiceNo = pInvoiceNo.partition("PH")[2]
        self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()

    time.sleep(3)
    print("END>> Create Pharmacy OPD Invoice.", pInvoiceNo)


def createPharmacyInvoiceTC(self, drugname, qty, paymentmode):
    print(">>Create Pharmacy OPD Invoice: START")
    global pInvoiceNo
    self.danpheEMR.find_element_by_link_text("Sale").click()
    self.danpheEMR.find_element_by_id("patient-search").click()
    self.danpheEMR.find_element_by_id("patient-search").send_keys(HospitalNo)
    time.sleep(3)
    self.danpheEMR.find_element_by_id("patient-search").send_keys(Keys.TAB)
    self.danpheEMR.find_element_by_id("patient-search").send_keys(Keys.RETURN)
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").click()
    self.danpheEMR.find_element_by_id("item-box0").clear()
    self.danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)

    # if appPort == "81":
    #    self.danpheEMR.find_element_by_id("qty-box0").click()
    #    self.danpheEMR.find_element_by_id("qty-box0").clear()
    #    self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
    #    if paymentmode == 'Credit':
    #       paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
    #       paymentoptions.select_by_visible_text("CREDIT")
    #       time.sleep(2)
    #       self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    #    self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()

    if appPort == "82":
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").send_keys(qty)
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").send_keys(Keys.RETURN)
        time.sleep(3)
        self.danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()

    time.sleep(5)
    pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    print("pInvoiceNo", pInvoiceNo)
    self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    epInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("Create Pharmacy OPD Invoice: END<<")


def createPharmacyInvoiceAnonymous(self, drugname, qty, paymentmode):
    print(">>Create Pharmacy OPD Invoice: START")
    global pInvoiceNo
    self.danpheEMR.find_element_by_link_text("Sale").click()
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Anonymous Patient')]").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").click()
    self.danpheEMR.find_element_by_id("item-box0").clear()
    self.danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
    self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    # if appPort == "81":
    #    self.danpheEMR.find_element_by_id("qty-box0").click()
    #    self.danpheEMR.find_element_by_id("qty-box0").clear()
    #    self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
    #    if paymentmode == 'Credit':
    #       paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
    #       paymentoptions.select_by_visible_text("CREDIT")
    #       time.sleep(2)
    #       self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    #    self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()

    if appPort == "82":
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").click()
        self.danpheEMR.find_element_by_xpath("// input[ @ formcontrolname = 'Quantity']").send_keys(qty)
        self.danpheEMR.find_element_by_xpath("//button[@title='ALT + P']").click()

    time.sleep(5)
    pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    print("pInvoiceNo", pInvoiceNo)
    self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("END>>: Create Pharmacy OPD Invoice.", pInvoiceNo)


def createPharmacyPurchaseOrder(self):
    print(">>Start: Create purchase order in pharmacy")
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    self.danpheEMR.find_element_by_link_text("Order").click()
    self.danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderItems')]").click()
    self.danpheEMR.find_element_by_css_selector(".col-md-9 > .form-control").click()
    time.sleep(9)
    dropdown = self.danpheEMR.find_element_by_css_selector(".col-md-9 > .form-control")
    time.sleep(3)
    dropdown.find_element_by_xpath("//option[. = 'AARATI MEDITCHA PVT']").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .form-control").send_keys(
        "ABEN SUSPENSION 10ML")
    self.danpheEMR.find_element_by_name("quantity").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_name("quantity").send_keys("100")
    self.danpheEMR.find_element_by_name("price").click()
    self.danpheEMR.find_element_by_name("price").send_keys("1")
    # self.danpheEMR.find_element_by_css_selector(".page-content").click()
    self.danpheEMR.find_element_by_css_selector(".text-right > .btn-success").click()
    time.sleep(5)


def verifyPharmacyPurchaseOrder(self):
    print(">>Start: Verify purchase order in pharmacy")
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Order").click()
    self.danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderList')]").click()
    # Jira ticket EMR-3297 need to deploy to search the purchase order with PO number.


def addPharmacyGRfromPO(self):
    print(">>Start: Create GR from purchase order in pharmacy")
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    self.danpheEMR.find_element_by_link_text("Order").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Order/PurchaseOrderList')]").click()
    self.danpheEMR.find_element_by_link_text("Add Goods Receipt").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()


def verifyPharmacyInvoice(self, qty):
    print(">>Verify Pharmacy Invoice: START")
    assert str(qty) == self.danpheEMR.find_element_by_xpath("//tr[2]/td[3]").text
    totalamount = self.danpheEMR.find_element_by_xpath("//table[@id='pharma-bill-sum']/tbody/tr[3]/td[2]").text
    totalamount = totalamount.partition("Rs. ")[2]
    totalamount = totalamount.partition(".00")[0]
    print("Verify Pharmacy Invoice: END<<", "Pharmacy Invoice No: ", pInvoiceNo)


def verifyPharmacyInvoice3(self, drugname, qty, rate):
    time.sleep(7)
    print(">>Verify Pharmacy Invoice: START")
    # assert drugname == self.danpheEMR.find_element_by_xpath("//tr[2]/td[2]").text
    # assert str(qty) == self.danpheEMR.find_element_by_xpath("//tr[2]/td[3]").text
    # tAmount = qty * rate
    # totalamount = self.danpheEMR.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]").text
    # totalamount = totalamount.partition("Rs. ")[2]
    # totalamount = totalamount.partition(".00")[0]
    # assert tAmount == int(totalamount)
    # print("Verify Pharmacy Invoice: END<<", "Pharmacy Invoice No: ", pInvoiceNo)
    # self.danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success']").click()
    self.danpheEMR.find_element_by_xpath("//i[@class='fa fa-close']").click()


def returnPharmacyInvoice(self, qty, returnremark):
    print(">>Return Pharmacy Invoice: START")
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    self.danpheEMR.find_element_by_link_text("Sale").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Return From Customer").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("invoiceId").send_keys(pInvoiceNo)
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.TAB)
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.ENTER)
    #    time.sleep(2)
    #    # self.danpheEMR.find_element_by_xpath("//button[@value='Search Invoice']").click()
    #    # self.danpheEMR.find_element_by_xpath("//button[@value='Search Invoice']").click()
    #    time.sleep(3)
    #    # self.danpheEMR.find_element_by_xpath("//input[@type='checkbox']").click()
    #    self.danpheEMR.find_element_by_css_selector("th > input").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='ReturnedQty']").clear()
    #    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='ReturnedQty']").send_keys(qty)
    #    self.danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys(returnremark)
    #    self.danpheEMR.find_element_by_xpath("//input[@value='Return']").click()
    #    time.sleep(5)
    #    self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger']").click()
    #    time.sleep(5)
    if appPort == '82':
        self.danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
        time.sleep(3)
        # self.danpheEMR.find_element_by_xpath("//i[contains(.,'MainDispensary')]").click()
        # time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Return From Customer").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_id("invoiceId").send_keys(pInvoiceNo)
        print("pInvoiceNo is getting returned", pInvoiceNo)
        time.sleep(2)
        self.danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.TAB)
        time.sleep(3)
        self.danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.ENTER)
        time.sleep(2)
        # self.danpheEMR.find_element_by_xpath("//button[@value='Search Invoice']").click()
        # self.danpheEMR.find_element_by_xpath("//button[@value='Search Invoice']").click()
        time.sleep(3)
        # self.danpheEMR.find_element_by_xpath("//input[@type='checkbox']").click()
        # self.danpheEMR.find_element_by_css_selector("th > input").click()
        # time.sleep(3)
        self.danpheEMR.find_element_by_id("ReturnedQty0").clear()
        self.danpheEMR.find_element_by_id("ReturnedQty0").send_keys(qty)
        self.danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys(returnremark)
        self.danpheEMR.find_element_by_id("return").click()
        time.sleep(5)
        self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger']").click()
        time.sleep(5)

    print("<<Return Pharmacy Invoice: END")


def verifyReturnPharmacyInvoice(self, paymentmode, returnRemark):
    print("<<Verify Return Pharmacy Invoice: START")
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Return Sale List").click()
    #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_link_text("Print").click()
    #    time.sleep(3)
    #    syspaymentmode = self.danpheEMR.find_element_by_xpath("//strong[contains(text(),'Method of payment:')]/parent::p/child::span").text
    #    print("syspaymentmode:", syspaymentmode)
    #    syspaymentmode = syspaymentmode.partition("t: ")[2]
    #    #print("syspaymentmode1:", syspaymentmode)
    #    assert syspaymentmode == "Cash" # as per the comment on bug:EMR-2699 payment mode need to be cash on credit note.
    #    ReturnremarkTemp = self.danpheEMR.find_element_by_xpath("//div[@id='pharma-pat-info']/div[12]").text
    #    print("ReturnremarkTemp", ReturnremarkTemp)
    #    ReturnremarkTemp = ReturnremarkTemp.partition("s : ")[2]
    #    print("ReturnremarkTemp", ReturnremarkTemp)
    #    assert ReturnremarkTemp == returnRemark
    #    time.sleep(5)
    #    self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    #    #self.danpheEMR.find_element_by_css_selector(".fa-close").click()
    if appPort == '82':
        self.danpheEMR.find_element_by_link_text("Return Sale List").click()
        self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        self.danpheEMR.find_element_by_link_text("Print").click()
        time.sleep(3)
        syspaymentmode = self.danpheEMR.find_element_by_xpath("//p[contains(text(),'Method of payment: ')]").text
        print("syspaymentmode:", syspaymentmode)
        syspaymentmode = syspaymentmode.partition("t: ")[2]
        # print("syspaymentmode1:", syspaymentmode)
        assert syspaymentmode == "Cash"  # as per the comment on bug:EMR-2699 payment mode need to be cash on credit note.
        ReturnremarkTemp = self.danpheEMR.find_element_by_xpath("//div[@id='pharma-pat-info']/div[12]").text
        print("ReturnremarkTemp", ReturnremarkTemp)
        ReturnremarkTemp = ReturnremarkTemp.partition("s : ")[2]
        print("ReturnremarkTemp", ReturnremarkTemp)
        assert ReturnremarkTemp == returnRemark
        time.sleep(5)
        self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
        # self.danpheEMR.find_element_by_css_selector(".fa-close").click()

    print(">>Verify Return Pharmacy Invoice: END")


def addPharmacyDeposit(self, deposit):
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Patient')]").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_link_text("Deposit").click()
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='DepositAmount']").send_keys(deposit)
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_xpath("//input[@value='Add Deposit']").click()
    #    time.sleep(3)
    if appPort == '82':
        self.danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Patient')]").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
        time.sleep(3)
        self.danpheEMR.find_element_by_link_text("Deposit").click()
        time.sleep(3)
        self.danpheEMR.find_element_by_xpath("//input[@name='DepositAmount']").send_keys(deposit)
        time.sleep(2)
        self.danpheEMR.find_element_by_xpath("//input[@value='Add Deposit']").click()
        time.sleep(3)


def returnPharmacyDeposit(self, depositreturn):
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Patient')]").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Deposit").click()
    time.sleep(5)
    deposittype = Select(self.danpheEMR.find_element_by_xpath("//select"))
    deposittype.select_by_visible_text("Return Deposit")
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//input[@name='DepositAmount']").send_keys(depositreturn)
    self.danpheEMR.find_element_by_xpath("//input[@value='Return Deposit']").click()
    time.sleep(3)


def createPharmacyGoodsReceipt(self, qty, DrugName, grPrice):
    global goodsReceiptNo
    if appPort == '82':
        self.danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Order").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Goods Receipt").click()
        time.sleep(7)
        self.danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys("Aayush surgichem")
        self.danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
        gRNo = random.randint(100, 9999)
        print("GR No:", gRNo)
        self.danpheEMR.find_element_by_xpath("//input[@placeholder='Invoice No']").send_keys(gRNo)
        self.danpheEMR.find_element_by_id("btn_AddNew").click()
        time.sleep(7)
        self.danpheEMR.find_element_by_id("txt_ItemName").send_keys(DrugName)
        self.danpheEMR.find_element_by_id("txt_ItemName").send_keys(Keys.TAB)
        time.sleep(3)
        self.danpheEMR.find_element_by_id("txt_BatchNo").send_keys(gRNo)
        self.danpheEMR.find_element_by_id("ItemQTy").send_keys(qty)
        print("grPrice", grPrice)
        grPrice = int(grPrice)
        self.danpheEMR.find_element_by_id("GRItemPrice").send_keys(grPrice)
        self.danpheEMR.find_element_by_id("Margin").send_keys(14)
        self.danpheEMR.find_element_by_id("btn_Save").click()
        # self.danpheEMR.find_element_by_xpath("//select[contains(.,'Main Store')]").send_keys("Main Store") Temporary disable due to issue.
        self.danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success tooltip']").click()
        time.sleep(14)
        goodsReceiptNo = self.danpheEMR.find_element_by_xpath("(//div[@col-id='GoodReceiptPrintId'])[2]").text
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Order").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Goods Receipt").click()
    #    time.sleep(7)
    #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys("Aayush surgichem")
    #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
    #    gRNo = random.randint(1, 9999)
    #    self.danpheEMR.find_element_by_xpath("//input[@placeholder='Invoice No']").send_keys(gRNo)
    #
    #    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(DrugName)
    #    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.ARROW_DOWN)
    #    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.RETURN)
    #    self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
    #    self.danpheEMR.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(qty)
    #    self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
    #    self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.TAB)
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
    #    self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
    #    self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
    #    self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
    #    time.sleep(3)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='ReceivedQty']").clear()
    #    self.danpheEMR.find_element_by_xpath("//input[@name='ReceivedQty']").send_keys(100)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='ReceivedQty']").send_keys(Keys.TAB)
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='GRItemPrice']").clear()
    #    self.danpheEMR.find_element_by_xpath("//input[@name='GRItemPrice']").send_keys(270)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='GRItemPrice']").send_keys(Keys.TAB)
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='MRP']").clear()
    #    self.danpheEMR.find_element_by_xpath("//input[@name='MRP']").send_keys(285)
    #    self.danpheEMR.find_element_by_xpath("//input[@name='MRP']").send_keys(Keys.TAB)
    #    time.sleep(2)
    #    #self.danpheEMR.find_element_by_xpath("//select[contains(.,'Main Store')]").send_keys("Main Store") Temporary disable due to issue.
    #    self.danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
    #    time.sleep(3)
    #    goodsReceiptNo = self.danpheEMR.find_element_by_xpath("(//div[@col-id='GoodReceiptPrintId'])[2]").text

    print("goodsReceiptNo:", goodsReceiptNo)


def cancelPharmacyGoodsReceipt(self):
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Order").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Goods Receipt List").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("(//a[contains(text(), 'View')])[1]").click()
    time.sleep(3)
    sysGRno = self.danpheEMR.find_element_by_xpath("//p[contains(text(), 'Goods Receipt No.:')]").text
    print("sysGRno", sysGRno)
    self.danpheEMR.find_element_by_xpath("//button[@title='Cancel Goods Receipt']").click()
    time.sleep(2)
    assert self.danpheEMR.switch_to.alert.text == "NOTE !!! Do you want to cancel Good Receipt?"
    time.sleep(3)
    self.danpheEMR.switch_to.alert.accept()
    time.sleep(7)


def getPharmacyGoodsReceiptListAmount(self):
    print(">>Start:getPharmacyGoodsReceiptListAmount")
    global SubTotal
    global DiscountTotal
    global TotalAmount
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Order").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Goods Receipt List").click()
    #    time.sleep(2)
    #    SubTotal = self.danpheEMR.find_element_by_xpath(
    #    "//b[contains(text(),'Sub Total :')]/parent::td/following-sibling::td[1]").text
    #    print("SubTotal", SubTotal)
    #    DiscountTotal = self.danpheEMR.find_element_by_xpath(
    #       "//b[contains(text(),'Discount Total :')]/parent::td/following-sibling::td[1]").text
    #    print("DiscountTotal", DiscountTotal)
    #    TotalAmount = self.danpheEMR.find_element_by_xpath(
    #    "//b[contains(text(),'Total Amount :')]/parent::td/following-sibling::td").text
    #    print("TotalAmount", TotalAmount)

    if appPort == '82':
        self.danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Order").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Goods Receipt List").click()
        time.sleep(2)
        SubTotal = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Sub Total')]//parent::span//parent::td//following-sibling::td)[1]").text
        print("SubTotal", SubTotal)
        DiscountTotal = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Discount Total')]//parent::span//parent::td//following-sibling::td)[1]").text
        print("DiscountTotal", DiscountTotal)
        TotalAmount = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),' Total Amount ')]//parent::span//parent::td//following-sibling::td)[1]").text
        print("TotalAmount", TotalAmount)
        print(">>Start:getPharmacyGoodsReceiptListAmount")


def XgetPharmacyGoodsReceiptListAmount(self):
    global xSubTotal
    global xDiscountTotal
    global xTotalAmount
    xSubTotal = SubTotal
    xDiscountTotal = DiscountTotal
    xTotalAmount = TotalAmount


def verifygetPharmacyGoodsReceiptListAmount(self, amount, discount):
    x = float(xSubTotal) + amount
    print("x", x)
    print("amount", amount)
    print("xSubTotal", xSubTotal)
    print("SubTotal", SubTotal)
    assert float(SubTotal) == float(x)
    assert float(DiscountTotal) == float(xDiscountTotal) + discount
    assert float(TotalAmount) == float(xTotalAmount) + amount - discount


def verifyDispensaryStock(self, qty):
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Stock").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
    time.sleep(5)
    drugnameTemp = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
    assert drugnameTemp == DrugName
    drugqtyTemp = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
    assert drugqtyTemp == str(qty)


def createPharmacyOPDBilling(self, qty, paymentmode):
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Sale").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Anonymous Patient')]").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("item-box0").click()
    self.danpheEMR.find_element_by_id("item-box0").clear()
    self.danpheEMR.find_element_by_id("item-box0").send_keys(DrugName)
    self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
    time.sleep(5)
    self.danpheEMR.find_element_by_id("qty-box0").click()
    self.danpheEMR.find_element_by_id("qty-box0").clear()
    self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
    time.sleep(3)
    if paymentmode == 'Credit':
        paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
        paymentoptions.select_by_visible_text(paymentmode)
        time.sleep(2)
        self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
    self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
    time.sleep(5)
    pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
    pInvoiceNo = pInvoiceNo.partition("PH")[2]
    print("Create Pharmacy OPD Invoice: END<<")


def verifyPharmacyGoodsReceipt(self, qty, DrugName):
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    self.danpheEMR.find_element_by_link_text("Order").click()
    self.danpheEMR.find_element_by_link_text("Goods Receipt List").click()
    time.sleep(7)
    self.danpheEMR.find_element_by_link_text("View").click()
    time.sleep(3)
    sysdrugname = self.danpheEMR.find_element_by_xpath("//td[2]/b").text
    print("sysdrugname:", sysdrugname)
    assert sysdrugname == DrugName
    self.danpheEMR.find_element_by_css_selector(".fa-times").click()


def closePopupApplication(self, saleinvoice):
    time.sleep(7)
    self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
    time.sleep(3)


# Module:Pharmacy_Reports: User Collection Report*********
def getPharmacyDashboard(self):
    global TotalSale
    # global TotalReturn
    global CreditReturn
    global CashReturn
    global NetCashCollection
    global DepositAmount
    global DepositReturned
    global ProvisionalItems
    global UnpaidInvoices
    time.sleep(5)
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(9)
    self.danpheEMR.find_element_by_xpath("//a[contains(@href, '#/Pharmacy/Dashboard')]").click()
    time.sleep(3)
    TotalSale = self.danpheEMR.find_element_by_xpath("//h4[contains(text(),'Total Sale')]/following-sibling::b").text
    print("Total Sale", TotalSale)
    TotalSale = TotalSale.partition(": ")[2]
    TotalSale = float(TotalSale)
    print("Total Sale", TotalSale)
    CashReturn = self.danpheEMR.find_element_by_xpath("//h4[contains(text(),'Cash Return')]/following-sibling::b").text
    print("CashReturn", CashReturn)
    CashReturn = CashReturn.partition(": ")[2]
    CashReturn = float(CashReturn)
    print("CashReturn", CashReturn)
    CreditReturn = self.danpheEMR.find_element_by_xpath(
        "//h4[contains(text(),'Credit Return')]/following-sibling::b").text
    print("CreditReturn", CreditReturn)
    CreditReturn = CreditReturn.partition(": ")[2]
    CreditReturn = float(CreditReturn)
    print("CreditReturn", CreditReturn)
    NetCashCollection = self.danpheEMR.find_element_by_xpath(
        "//h4[contains(text(),'Net Cash Collection')]/following-sibling::b").text
    print("NetCashCollection", NetCashCollection)
    NetCashCollection = NetCashCollection.partition(": ")[2]
    NetCashCollection = float(NetCashCollection)
    print("NetCashCollection", NetCashCollection)
    DepositAmount = self.danpheEMR.find_element_by_xpath(
        "//h4[contains(text(),'Deposit Amount')]/following-sibling::b").text
    print("Deposit Amount", DepositAmount)
    DepositAmount = DepositAmount.partition(": ")[2]
    DepositAmount = float(DepositAmount)
    print("DepositAmount", DepositAmount)
    DepositReturned = self.danpheEMR.find_element_by_xpath(
        "//h4[contains(text(),'Deposit Returned')]/following-sibling::b").text
    print("Deposit Returned", DepositReturned)
    DepositReturned = DepositReturned.partition(": ")[2]
    DepositReturned = float(DepositReturned)
    print("DepositReturned", DepositReturned)
    ProvisionalItems = self.danpheEMR.find_element_by_xpath(
        "//td[contains(text(),'PROVISIONAL ITEMS')]/following-sibling::td").text
    print("PROVISIONAL ITEMS", ProvisionalItems)
    ProvisionalItems = ProvisionalItems.partition("Rs.")[2]
    ProvisionalItems = float(ProvisionalItems)
    print("ProvisionalItems", ProvisionalItems)
    UnpaidInvoices = self.danpheEMR.find_element_by_xpath(
        "//td[contains(text(),'UNPAID INVOICES')]/following-sibling::td").text
    print("UNPAID INVOICES", UnpaidInvoices)
    UnpaidInvoices = UnpaidInvoices.partition("Rs.")[2]
    UnpaidInvoices = float(UnpaidInvoices)
    print("UnpaidInvoices", UnpaidInvoices)


def preSystemPharmacyDashboard(self):
    global xTotalSale
    # global xTotalReturn
    global xCashReturn
    global xCreditReturn
    global xNetCashCollection
    global xDepositAmount
    global xDepositReturned
    global xProvisionalItems
    global xUnpaidInvoices
    xTotalSale = TotalSale
    xCashReturn = CashReturn
    xCreditReturn = CreditReturn
    xNetCashCollection = NetCashCollection
    xDepositAmount = DepositAmount
    xDepositReturned = DepositReturned
    xProvisionalItems = ProvisionalItems
    xUnpaidInvoices = UnpaidInvoices


def verifyPharmacyDashboard(self, cash, cashreturn, credit, creditreturn, deposit, depositreturn, provisional,
                            provisionacancel):
    # if appPort == '81':
    #    temp = round(xTotalSale + cash + credit)
    #    print("temp", temp)
    #    print("temp", float(temp))
    #    print("TotalSale", TotalSale)
    #    assert float(round(TotalSale)) == float(round(xTotalSale + cash + credit))
    #    print("TotalReturn-cash", CashReturn)
    #    print("xCashReturn", xCashReturn)
    #    #a = float(round(xTotalReturn + cashreturn + creditreturn))
    #    a = float(round(xCashReturn + cashreturn))
    #    b = float(round(xCreditReturn + creditreturn))
    #    assert CashReturn == a
    #    assert CreditReturn == b
    #    netcoltemp = float(round(xNetCashCollection + cash - cashreturn))
    #    print("netcollectiontemp", netcoltemp)
    #    print("xNetCollection", xNetCashCollection)
    #    assert float(round(NetCashCollection)) == float(round(xNetCashCollection + cash - cashreturn))
    #    assert DepositAmount == xDepositAmount + deposit
    #    assert DepositReturned == xDepositReturned + depositreturn
    #    assert ProvisionalItems == xProvisionalItems + provisional - provisionacancel
    #    c = float(round(xUnpaidInvoices + credit - creditreturn))
    #    print("c", c)
    #    print("UnpaidInvoices", UnpaidInvoices)
    #    assert float(round(UnpaidInvoices)) == c
    if appPort == '82':
        temp = round(xTotalSale + cash + credit)
        print("temp", temp)
        print("temp", float(temp))
        print("TotalSale", TotalSale)
        assert float(round(TotalSale)) == float(round(xTotalSale + cash + credit))
        print("CashReturn", CashReturn)
        print("xCashReturn", xCashReturn)
        # a = float(round(xTotalReturn + cashreturn + creditreturn))
        a = float(round(xCashReturn + cashreturn))
        print("a", a)
        print("CashReturn", CashReturn)
        b = float(round(xCreditReturn + creditreturn))
        print("b", b)
        print("CreditReturn", CreditReturn)
        assert CashReturn == a
        assert CreditReturn == b

        print("xNetCollection", xNetCashCollection)
        x = int(xNetCashCollection + cash - cashreturn)
        print("x:", x)
        y = int(NetCashCollection)
        print("Y", y)
        assert y == x
        assert DepositAmount == xDepositAmount + deposit
        assert DepositReturned == xDepositReturned + depositreturn
        assert ProvisionalItems == xProvisionalItems + provisional - provisionacancel
        c = float(round(xUnpaidInvoices + credit - creditreturn))
        print("c", c)
        print("UnpaidInvoices", UnpaidInvoices)
        assert float(round(UnpaidInvoices)) == c


def getPharmacyCashCollectionSummary(self, user):
    global sysinvoiceamount
    global sysinvoicereturned
    global sysdeposit
    global sysdepositreturn
    global sysnetamount
    global sysdiscountamount
    # if appPort == '81':
    #    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_link_text("Report").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Cash Collection Summary')]").click()
    #    time.sleep(2)
    #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
    #    time.sleep(9)
    #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(user)
    #    time.sleep(2)
    #    username = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
    #    sysinvoiceamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
    #    print(sysinvoiceamount)
    #    sysinvoicereturned = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
    #    print(sysinvoicereturned)
    #    sysdeposit = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
    #    print(sysdeposit)
    #    sysdepositreturn = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
    #    print(sysdepositreturn)
    #    sysnetamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
    #    print(sysnetamount)
    #    sysdiscountamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
    #    print(sysdiscountamount)
    if appPort == '82':
        self.danpheEMR.find_element_by_link_text("Pharmacy").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Report").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_link_text("Sales").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_xpath("//i[contains(.,'Cash Collection Summary')]").click()
        time.sleep(2)
        self.danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
        time.sleep(9)
        self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(user)
        time.sleep(2)
        username = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
        sysinvoiceamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
        print(sysinvoiceamount)
        sysinvoicereturned = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
        print(sysinvoicereturned)
        sysdeposit = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
        print(sysdeposit)
        sysdepositreturn = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
        print(sysdepositreturn)
        sysnetamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
        print(sysnetamount)
        sysdiscountamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
        print(sysdiscountamount)


def preSystemPharmacyCashCollectionSummary(self):
    global presysinvoiceamount
    global presysinvoicereturned
    global presysdeposit
    global presysdepositreturn
    global presysnetamount
    global presysdiscountamount
    presysinvoiceamount = int(sysinvoiceamount)
    presysinvoicereturned = float(sysinvoicereturned)
    presysdeposit = int(sysdeposit)
    presysdepositreturn = int(sysdepositreturn)
    presysnetamount = float(sysnetamount)
    presysdiscountamount = int(sysdiscountamount)


def verifyPharmacyCashCollectionSummary(self, cash, cashreturn, credit, creditreturn, deposit, depositreturn, discount):
    print("presysinvoiceamount:", presysinvoiceamount)
    print("sysinvoiceamount:", sysinvoiceamount)
    print("cash:", cash)
    print("credit:", credit)
    print("presysinvoicereturned:", presysinvoicereturned)
    print("sysinvoicereturned:", sysinvoicereturned)
    print("cashreturn:", cashreturn)
    print("creditreturn:", creditreturn)
    assert int(sysinvoiceamount) == presysinvoiceamount + cash + credit
    assert float(sysinvoicereturned) == float(presysinvoicereturned + cashreturn + creditreturn)
    assert int(sysdeposit) == presysdeposit + deposit
    assert int(sysdepositreturn) == presysdepositreturn + depositreturn
    result = float(sysinvoiceamount) - float(sysinvoicereturned) - float(sysdeposit) - float(sysdepositreturn)
    print("result:", result)
    netamount = float(result)
    print("netamount", netamount)
    assert float(sysnetamount) == float(netamount)
    assert int(sysdiscountamount) == presysdiscountamount + discount


def getPharmacyUserCollectionReport(self, user):
    global sysPnetcashcollection
    global sysPgrosstotalsales
    global sysPdiscount
    global sysPreturnsubtotal
    global sysPreturndiscount
    global sysPreturnamount
    global sysPnetsales
    global sysPlesscreditamount
    global sysPadddepositreceived
    global sysPdepositdeducted
    global sysPlessdepositrefund
    global sysPaddcollectionfromreceivables
    global sysPlesscashdiscount
    global sysPtotalcollection
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Report").click()
    time.sleep(4)
    self.danpheEMR.find_element_by_link_text("Sales").click()
    time.sleep(4)
    self.danpheEMR.find_element_by_xpath("//i[contains(.,'User Collection')]").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(user)
    time.sleep(9)
    sysPnetcashcollection = self.danpheEMR.find_element_by_css_selector(".blinkAmount").text
    print(sysPnetcashcollection)
    sysPnetcashcollection = sysPnetcashcollection.partition("( ")[2]
    sysPnetcashcollection = sysPnetcashcollection.partition(")")[0]
    sysPgrosstotalsales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td[2]").text
    print(sysPgrosstotalsales)
    sysPdiscount = self.danpheEMR.find_element_by_xpath("//tr[2]/td[2]").text
    print(sysPdiscount)
    sysPreturnsubtotal = self.danpheEMR.find_element_by_xpath("//tr[3]/td[2]").text
    print(sysPreturnsubtotal)
    sysPreturndiscount = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
    print(sysPreturndiscount)
    sysPreturnamount = self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]").text
    print(sysPreturnamount)
    sysPnetsales = self.danpheEMR.find_element_by_xpath("//tr[6]/td[2]").text
    print(sysPnetsales)
    sysPlesscreditamount = self.danpheEMR.find_element_by_xpath("//tr[7]/td[2]").text
    print(sysPlesscreditamount)
    sysPadddepositreceived = self.danpheEMR.find_element_by_xpath("//tr[8]/td[2]").text
    print(sysPadddepositreceived)
    sysPdepositdeducted = self.danpheEMR.find_element_by_xpath("//tr[9]/td[2]").text
    print(sysPdepositdeducted)
    sysPlessdepositrefund = self.danpheEMR.find_element_by_xpath("//tr[10]/td[2]").text
    print(sysPlessdepositrefund)
    sysPaddcollectionfromreceivables = self.danpheEMR.find_element_by_xpath("//tr[11]/td[2]").text
    print(sysPaddcollectionfromreceivables)
    sysPlesscashdiscount = self.danpheEMR.find_element_by_xpath("//tr[12]/td[2]").text
    print(sysPlesscashdiscount)
    sysPtotalcollection = self.danpheEMR.find_element_by_xpath("//tr[13]/td[2]").text
    print(sysPtotalcollection)


def preSystemPharmacyUserCollectionReport(self):
    global presysPnetcashcollection
    global presysPgrosstotalsales
    global presysPdiscount
    global presysPreturnsubtotal
    global presysPreturndiscount
    global presysPreturnamount
    global presysPnetsales
    global presysPlesscreditamount
    global presysPadddepositreceived
    global presysPdepositdeducted
    global presysPlessdepositrefund
    global presysPaddcollectionfromreceivables
    global presysPlesscashdiscount
    global presysPtotalcollection
    presysPnetcashcollection = float(sysPnetcashcollection)
    presysPgrosstotalsales = float(sysPgrosstotalsales)
    presysPdiscount = float(sysPdiscount)
    presysPreturnsubtotal = float(sysPreturnsubtotal)
    presysPreturndiscount = float(sysPreturndiscount)
    presysPreturnamount = float(sysPreturnamount)
    presysPnetsales = float(sysPnetsales)
    presysPlesscreditamount = float(sysPlesscreditamount)
    presysPadddepositreceived = float(sysPadddepositreceived)
    presysPdepositdeducted = float(sysPdepositdeducted)
    presysPlessdepositrefund = float(sysPlessdepositrefund)
    presysPaddcollectionfromreceivables = float(sysPaddcollectionfromreceivables)
    presysPlesscashdiscount = float(sysPlesscashdiscount)
    presysPtotalcollection = float(sysPtotalcollection)


def verifySystemPharmacyUserCollectionReport(self, cash, cashreturn, credit, creditreturn, creditsettlement, discount,
                                             deposit, depositreturn, provisional, provisionalcancel):
    global sysPgrosstotalsales
    # if appPort == '81':
    #    print(">>START: verifySystemPharmacyUserCollectionReport")
    #    print("cash", cash)
    #    print("cashreturn", cashreturn)
    #    print("presysPnetcashcollection", presysPnetcashcollection)
    #    print("sysPnetcashcollection", sysPnetcashcollection)
    #    newCashCollection = presysPnetcashcollection + cash - cashreturn
    #    print("newCashCollection", newCashCollection)
    #    #assert round(float(sysPnetcashcollection)) == round(float(newCashCollection))
    #    assert int(sysPnetcashcollection) == int(round(newCashCollection))
    #    result = str(float(presysPgrosstotalsales) + cash + credit)
    #    print("result", result)
    #    print("sysPgrosstotalsales", sysPgrosstotalsales)
    #    print("presysPgrosstotalsales", presysPgrosstotalsales)
    #    #sysPgrosstotalsales = sysPgrosstotalsales.partition(".")[0]
    #    #result = result.partition(".")[0]
    #    #print("result", result)
    #    print("sysPgrosstotalsales", sysPgrosstotalsales)
    #    assert sysPgrosstotalsales == result
    #    assert float(sysPdiscount) == presysPdiscount + discount
    #    print("sysPreturnsubtotal", sysPreturnsubtotal)
    #    print("presysPreturnsubtotal", presysPreturnsubtotal)
    #    assert round(float(sysPreturnsubtotal)) == round(float(presysPreturnsubtotal + cashreturn + creditreturn))
    #    assert float(sysPreturndiscount) == presysPreturndiscount + discount
    #    assert round(float(sysPreturnamount)) == round(float(presysPreturnamount + cashreturn + creditreturn + discount))
    #    print("presysPnetsales", presysPnetsales)
    #    print("sysPnetsales", sysPnetsales)
    #    assert round(float(sysPnetsales)) == round(float(presysPnetsales + cash + credit - cashreturn - creditreturn - discount))
    #    print("sysPlesscreditamount", sysPlesscreditamount)
    #    print("presysPlesscreditamount", presysPlesscreditamount)
    #    print("Credit", credit)
    #    assert round(float(sysPlesscreditamount)) == round(presysPlesscreditamount + credit)
    #    assert float(sysPadddepositreceived) == presysPadddepositreceived + deposit
    #    assert float(sysPdepositdeducted) == presysPdepositdeducted
    #    assert float(sysPlessdepositrefund) == presysPlessdepositrefund - depositreturn
    #    assert float(sysPaddcollectionfromreceivables) == presysPaddcollectionfromreceivables + creditsettlement
    #    assert float(sysPlesscashdiscount) == presysPlesscashdiscount + discount
    #    print("sysPtotalcollection", sysPtotalcollection)
    #    result2 = presysPtotalcollection + cash - cashreturn + deposit - depositreturn + creditsettlement
    #    print("result2", result2)
    #    assert float(sysPtotalcollection) == round(result2)
    if appPort == '82':
        print(">>START: verifySystemPharmacyUserCollectionReport")
        print("cash", cash)
        print("cashreturn", cashreturn)
        print("presysPnetcashcollection", presysPnetcashcollection)
        print("sysPnetcashcollection", sysPnetcashcollection)
        newCashCollection = presysPnetcashcollection + cash - cashreturn
        print("newCashCollection", newCashCollection)
        assert round(float(sysPnetcashcollection)) == round(float(newCashCollection))
        result = str(float(presysPgrosstotalsales) + cash + credit)
        print("result", result)
        print("sysPgrosstotalsales", sysPgrosstotalsales)
        print("presysPgrosstotalsales", presysPgrosstotalsales)
        # sysPgrosstotalsales = sysPgrosstotalsales.partition(".")[0]
        # result = result.partition(".")[0]
        # print("result", result)
        print("sysPgrosstotalsales", sysPgrosstotalsales)
        assert sysPgrosstotalsales == result
        assert float(sysPdiscount) == presysPdiscount + discount
        print("sysPreturnsubtotal", sysPreturnsubtotal)
        print("presysPreturnsubtotal", presysPreturnsubtotal)
        assert round(float(sysPreturnsubtotal)) == round(float(presysPreturnsubtotal + cashreturn + creditreturn))
        assert float(sysPreturndiscount) == presysPreturndiscount + discount
        assert round(float(sysPreturnamount)) == round(
            float(presysPreturnamount + cashreturn + creditreturn + discount))
        print("presysPnetsales", presysPnetsales)
        print("sysPnetsales", sysPnetsales)
        assert round(float(sysPnetsales)) == round(
            float(presysPnetsales + cash + credit - cashreturn - creditreturn - discount))
        print("sysPlesscreditamount", sysPlesscreditamount)
        print("presysPlesscreditamount", presysPlesscreditamount)
        print("Credit", credit)
        assert round(float(sysPlesscreditamount)) == round(presysPlesscreditamount + credit)
        assert float(sysPadddepositreceived) == presysPadddepositreceived + deposit
        assert float(sysPdepositdeducted) == presysPdepositdeducted
        assert float(sysPlessdepositrefund) == presysPlessdepositrefund - depositreturn
        assert float(sysPaddcollectionfromreceivables) == presysPaddcollectionfromreceivables + creditsettlement
        assert float(sysPlesscashdiscount) == presysPlesscashdiscount + discount
        print("sysPtotalcollection", sysPtotalcollection)
        result2 = presysPtotalcollection + cash - cashreturn + deposit - depositreturn + creditsettlement
        print("result2", result2)
        x = str(sysPtotalcollection)
        x = x.replace(" ", "")
        print("X", x)
        y = str(result2)
        y = y.replace(" ", "")
        print("Y", x)
        assert x == y


def getPharmacyDepositBalanceReport(self):
    global sysdepositamt
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Report").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//i[contains(text(),'Deposit Balance Report ')]").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(9)
    assert HospitalNo == self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
    sysdepositamt = int(self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text)


def verifyPharmacyDepositBalanceReport(self, deposit, depositreturn):
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(3)
    self.danpheEMR.find_element_by_link_text("Report").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//i[contains(text(),'Deposit Balance Report ')]").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
    time.sleep(9)
    assert HospitalNo == self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
    depositbalance = int(self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text)
    assert depositbalance == sysdepositamt + deposit - depositreturn


def getPharmacyOpeningEndingStockSummaryReport(self, drugname):
    global sysdrugname
    global sysopeningstock
    global sysendingstock
    self.danpheEMR.find_element_by_link_text('Pharmacy').click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text('Report').click()
    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Opening and Ending Stock Summary')]").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(3)
    sysdrugname = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
    print("sysdrugname", sysdrugname)
    assert sysdrugname == drugname
    sysopeningstock = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
    print("sysopeningstock", sysopeningstock)
    sysendingstock = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
    print("sysendingstock", sysendingstock)


def preSystemPharmacyOpeningEndingStockSummaryReport(self):
    global presysdrugname
    global presysdrugbatch
    global presysdrugexpiry
    global presysopeningstock
    global presysendingstock
    presysopeningstock = sysopeningstock
    presysendingstock = sysendingstock
    presysdrugname = sysdrugname
    presysdrugbatch = sysdrugbatch
    presysdrugexpiry = sysdrugexpiry


def verifyPharmacyOpeningEndingStockSummaryReport(self, qty):
    self.danpheEMR.find_element_by_link_text('Pharmacy').click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text('Report').click()
    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Opening and Ending Stock Summary')]").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
    time.sleep(9)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(presysdrugname, ' ', presysdrugbatch)
    time.sleep(7)
    assert presysdrugname == self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
    assert presysdrugbatch == self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
    assert presysdrugexpiry == self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]/span").text
    assert presysopeningstock == self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
    sysendingstock = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]").text
    assert int(sysendingstock) == int(presysendingstock) - qty


def getPharmacyStockManageDetailReport(self, drugname):
    global ManageQuantity
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Report").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Stock Manage Detail Report')]").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Show Report')]").click()
    time.sleep(9)
    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
    time.sleep(5)
    ManageQuantity = self.danpheEMR.find_element_by_xpath(
        "(//div[@col-id='Quantity'])[2]").text  # There is open bug (EMR-2588) to list down latest manage record to top.
    print("Manage Quantity", ManageQuantity)


def preSystemPharmacyStockManageDetailReport(self):
    global xManageQuantity
    xManageQuantity = ManageQuantity


def verifyPharmacyStockManageDetailReport(self, In, Out):
    assert int(ManageQuantity) == int(xManageQuantity) + In - Out


def verifyStockItemsReport(self, drugname):
    self.danpheEMR.find_element_by_link_text("Pharmacy").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_link_text("Report").click()
    time.sleep(2)
    self.danpheEMR.find_element_by_xpath("//i[contains(text(),'Stock Items')]").click()
    time.sleep(5)
    self.danpheEMR.find_element_by_xpath("//input[@placeholder='--Select Item--']").send_keys(drugname)
    time.sleep(1)
    self.danpheEMR.find_element_by_xpath("//input[@placeholder='--Select Item--']").send_keys(Keys.ARROW_DOWN)
    self.danpheEMR.find_element_by_xpath("//input[@placeholder='--Select Item--']").send_keys(Keys.TAB)
    self.danpheEMR.find_element_by_xpath("//select").send_keys("Dispensary")
    self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
    time.sleep(3)
    sysqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
    print("sysqty", sysqty)
    print("drugqtySS", drugqtySS)
    assert int(drugqtySS) == int(sysqty)


def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

