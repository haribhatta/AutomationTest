from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)

# Module:Inventory---------------------------------------------------------
   def createInventoryGoodReceipt(self, qty, item, rate):
      print(">>START: createGoodReceipt")
      global BillNo
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Inventory").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("Procurement").click()
      #    time.sleep(3)
      #    #self.danpheEMR.find_element_by_xpath("//i[contains(.,'General Inventory')]").click()
      #    #time.sleep(5)
      #    #self.danpheEMR.find_element_by_link_text("Goods Arrival Notification").click()
      #    time.sleep(5)
      #    self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Create Good Receipt')]").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .form-control").send_keys(Keys.RETURN)
      #    BillNo = random.randint(100, 99999)
      #    print("Bill No", BillNo)
      #    self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='BillNo']").send_keys(BillNo) # LPH-934, LPH_V1.9.3
      #    self.danpheEMR.find_element_by_id("itemName0").send_keys(item)
      #    self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
      #    self.danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_id("rateip0").clear()
      #    self.danpheEMR.find_element_by_id("rateip0").send_keys(rate)
      #    self.danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
      #    time.sleep(3)
      if appPort == '82':
         #self.danpheEMR.find_element_by_link_text("Inventory").click()
         #time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Procurement").click()
         #time.sleep(3)
         #self.danpheEMR.find_element_by_xpath("//i[contains(.,'General Inventory')]").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_link_text("Goods Arrival Notification").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("//a[contains(.,' Create Goods Receipt')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .form-control").send_keys(Keys.RETURN)
         BillNo = random.randint(100, 99999)
         print("Bill No", BillNo)
         self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='BillNo']").send_keys(BillNo) # LPH-934, LPH_V1.9.3
         self.danpheEMR.find_element_by_id("itemName0").send_keys(item)
         self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
         self.danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("rateip0").clear()
         self.danpheEMR.find_element_by_id("rateip0").send_keys(rate)
         self.danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[contains(text(),'Back to Goods Receipt List')]").click()
      print("<<END: createGoodReceipt")
   def editInventoryGoodsReceipt(self):
      print(">>START: edit GoodReceipt")
      time.sleep(2)
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Procurement").click()
      #    time.sleep(3)
      #    #self.danpheEMR.find_element_by_xpath("//i[contains(.,'General Inventory')]").click()
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(BillNo)
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Edit Receipt ')]").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_id("qtyip0").clear() #Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
      #    self.danpheEMR.find_element_by_id("qtyip0").send_keys(2)
      #    self.danpheEMR.find_element_by_id("SaveGoodsReceiptbtn").click()
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Procurement").click()
         time.sleep(2)
         #self.danpheEMR.find_element_by_xpath("//i[contains(.,'General Inventory')]").click()
         #time.sleep(5)
         self.danpheEMR.find_element_by_link_text("Goods Arrival Notification").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(BillNo)
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Edit Receipt ')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("qtyip0").clear() #Bugs:LPH-867, .. .Issue on: LPH_V1.9.0
         self.danpheEMR.find_element_by_id("qtyip0").send_keys(2)
         self.danpheEMR.find_element_by_id("SaveGoodsReceiptbtn").click()
   def InventoryConsumption(self, item, qty, store):
      time.sleep(5)
      # if appPort == '81':
      #    #self.danpheEMR.find_element_by_link_text("SubStore").click()
      #    time.sleep(5)
      #    a = "//i[contains(text(),'"
      #    b = store
      #    c = "')]"
      #    d = a + b + c
      #    print("test:", d)
      #
      #    #self.danpheEMR.find_element_by_xpath(d).click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("Consumption").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("New Consumption").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_id("itemName0").clear()
      #    self.danpheEMR.find_element_by_id("itemName0").send_keys(item)
      #    self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
      #    self.danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").clear()
      #    self.danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").send_keys(qty)
      #    self.danpheEMR.find_element_by_css_selector(".btn-success").click()
      #    time.sleep(2)
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("SubStore").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//i[contains(text(),'Billing Store')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Consumption").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("New Consumption").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("itemName0").clear()
         self.danpheEMR.find_element_by_id("itemName0").send_keys(item)
         self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
         self.danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").clear()
         self.danpheEMR.find_element_by_xpath("//input[@id='qtyip0']").send_keys(qty)
         self.danpheEMR.find_element_by_css_selector(".btn-success").click()
         time.sleep(2)
   def createInventoryDirectDispatch(self, itemname, qty, store):
       print(">>START: directDispatch")
       # if appPort == '81':
       #    time.sleep(3)
       #    self.danpheEMR.find_element_by_link_text("Inventory").click()
       #    time.sleep(5)
       #    self.danpheEMR.find_element_by_link_text("Internal").click()
       #    time.sleep(5)
       #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Direct Dispatch  ')]").click()
       #    time.sleep(2)
       #    self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(store)
       #    self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(Keys.TAB)
       #    time.sleep(1)
       #    self.danpheEMR.find_element_by_id("itemName0").send_keys(itemname)
       #    time.sleep(1)
       #    self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.ENTER)
       #    time.sleep(1)
       #    self.danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
       #    time.sleep(5)
       #    #self.danpheEMR.find_element_by_id("qtyip0").send_keys(Keys.ENTER)
       #    self.danpheEMR.find_element_by_xpath("//textarea[@name='Remarks']").send_keys("Direct dispatch test")
       #    time.sleep(1)
       #    self.danpheEMR.find_element_by_xpath("//input[@value='Direct Dispatch']").click()
       if appPort == '82':
          time.sleep(3)
          self.danpheEMR.find_element_by_link_text("Inventory").click()
          time.sleep(5)
          self.danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
          time.sleep(3)
          self.danpheEMR.find_element_by_link_text("Internal").click()
          time.sleep(5)
          self.danpheEMR.find_element_by_xpath("//button[contains(.,'Direct Dispatch  ')]").click()
          time.sleep(2)
          self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(store)
          self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(Keys.TAB)
          time.sleep(1)
          self.danpheEMR.find_element_by_id("itemName0").send_keys(itemname)
          time.sleep(1)
          self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.ENTER)
          time.sleep(1)
          self.danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
          time.sleep(5)
          #self.danpheEMR.find_element_by_id("qtyip0").send_keys(Keys.ENTER)
          self.danpheEMR.find_element_by_id("remarks").send_keys("Direct dispatch test")
          time.sleep(1)
          self.danpheEMR.find_element_by_xpath("//input[@value='Direct Dispatch']").click()
       print("<<END: directDispatch")
   def InventoryStockManage(self, managetype):
      print(">>START: InventoryStockManage")
      self.danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys("PHOTOCOPY PAPER (CUTTING)")
      time.sleep(2)
      availableQty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
      availableQty = int(availableQty)
      print("case1", availableQty)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'View')]").click()
      grNo = self.danpheEMR.find_element_by_xpath("(//div[@col-id='GoodsReceiptNo'])[2]").text
      print("Goods Receipt No", grNo)
      global UnitPrice
      UnitPrice = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemRate'])[2]").text
      print("Unit Price", UnitPrice)
      self.danpheEMR.find_element_by_xpath("//i[@class='fa fa-backward']").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys("PHOTOCOPY PAPER (CUTTING)")
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Manage Stock')]").click()
      time.sleep(3)
      grNoTemp = self.danpheEMR.find_element_by_xpath("//td[contains(text(),'GR No.')]/parent::tr/parent::thead/following-sibling::tbody/child::tr/child::td").text
      assert grNo == grNoTemp
      currentQty = self.danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").get_attribute("value")
      print("currentQty", currentQty)
      currentQty = float(currentQty)
      modifyin = int(currentQty + 1)
      modifyOut = int(currentQty - 1)
      print("modifyOut", modifyOut)
      print("modifyin", modifyin)
      self.danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").clear()
      if managetype == "in":
         self.danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").send_keys(modifyin)
         print("Manage In done")
      if managetype == "out":
         self.danpheEMR.find_element_by_xpath("//input[@name='ModQuantity']").send_keys(modifyOut)
         print("Manage Out done")
         time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@value='Update Stock']").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys("PHOTOCOPY PAPER (CUTTING)")
      time.sleep(2)
      newavailableQty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailQuantity']/child::span/child::div)[1]").text
      print("newavailableQty", newavailableQty)         #
      print("availableQty", availableQty)               #
      if managetype == "in":
         assert int(newavailableQty) == int(availableQty + 1)
      if managetype == "out":
         assert int(newavailableQty) == availableQty - 1
   def verifyInventoryDailyItemDispatchReport(self, itemname, qty):
       self.danpheEMR.find_element_by_link_text("Inventory").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//i[contains(.,'Daily Item Dispatch')]").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_id("quickFilterInput").send_keys("nursing store")
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//span[contains(.,'Requisition ID')]").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//span[contains(.,'Requisition ID')]").click()
       time.sleep(2)
       element1 = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
       assert element1 == itemname
       element2 = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
       print(element2)
       print(qty)
       assert element2 == str(qty)
   def getInventoryCurrentStockLevelReport(self, store):
      global TotalStockQuantity
      global TotalStockValue
      self.danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Current Stock Level')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".fa-remove").click()
      self.danpheEMR.find_element_by_xpath("//span[contains(.,'---Select Item---')]").click()
      self.danpheEMR.find_element_by_xpath("//input[@type='text']").send_keys(store)
      if store == "Main Store":
         self.danpheEMR.find_element_by_xpath("//label[contains(.,'Main Store')]").click()
      if store == "OT Store":
         self.danpheEMR.find_element_by_xpath("//label[contains(.,'OT Store')]").click()
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Load')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("(//a[contains(text(),'View')])[1]").click()
      time.sleep(3)
      sysStoreName = self.danpheEMR.find_element_by_xpath(
         "(//th[contains(text(),' Store Name ')]/parent::tr/following-sibling::tr/child::td)[1]").text
      print("sysStoreName", sysStoreName)
      assert store == sysStoreName
      self.danpheEMR.find_element_by_xpath("//a[@title='Cancel']").click()
      time.sleep(7)
      TotalStockQuantity = self.danpheEMR.find_element_by_xpath(
         "//b[contains(text(),' Total Stock Quantity ')]/parent::span/parent::td/following-sibling::td[1]").text
      print("TotalStockQuantity-:", TotalStockQuantity)
      TotalStockValue = self.danpheEMR.find_element_by_xpath(
         "//b[contains(text(),' Total Stock Value ')]/parent::span/parent::td/following-sibling::td[1]").text
      TotalStockValue = TotalStockValue.replace(',', '')
      print("TotalStockValue:", TotalStockValue)
   def preInventoryCurrentStockLevelReport(self):
      global preTotalStockQuantity
      global preTotalStockValue
      preTotalStockQuantity = float(TotalStockQuantity)
      preTotalStockValue = float(TotalStockValue)
   def verifyInventoryCurrentStockLevelReport(self, type, qty, unitprice):
      global calcTotalStockQuantity
      global calcTotalStockValue
      print("preTotalStockQuantity", preTotalStockQuantity)
      print("TotalStockQuantity", TotalStockQuantity)
      print("qty", qty)
      calcQtyValue = float(qty * unitprice)
      if type == "out":
         calcTotalStockQuantity = format(preTotalStockQuantity - qty)
         calcTotalStockValue = float(preTotalStockValue - calcQtyValue)
      if type == "in":
         calcTotalStockQuantity = float(preTotalStockQuantity + qty)
         calcTotalStockValue = float(preTotalStockValue + calcQtyValue)
      print("calcTotalStockQuantity", calcTotalStockQuantity)
      calcTotalStockQuantityf = calcTotalStockQuantity.partition(".")[0]
      TotalStockQuantityf = TotalStockQuantity.partition(".")[0]
      print("calcTotalStockQuantityf", calcTotalStockQuantityf)
      print("TotalStockQuantityf", TotalStockQuantityf)
      assert TotalStockQuantityf == calcTotalStockQuantityf
      print("calcQtyValue", calcQtyValue)
      print("calcTotalStockValue", calcTotalStockValue)
      print("TotalStockValue", TotalStockValue)
      calcTotalStockValue = float(calcTotalStockValue)
      TotalStockValuec = float(TotalStockValue)
      assert round(float(TotalStockValuec)) == round(float(calcTotalStockValue))
   def selectInventory(self, inventory):
      time.sleep(5)
      # if appPort == '81':
      #    print("This is test")
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Inventory").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
         time.sleep(3)
   def selectDispensary(self, dispensary):
      time.sleep(5)
      # if appPort == '81':
      #    print("This is test")
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Dispensary").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("//i[contains(text(),'MainDispensary')]").click()
         time.sleep(3)
   def getInventorySummaryReport(self):
      global OpeningValue
      global OpeningQty
      global PurchaseValue
      global PurchaseQty
      global StockManageInValue
      global StockManageInQty
      global StockManageOutValue
      global StockManageOutQty
      global ConsumptionValue
      global ConsumptionQty
      global ClosingValue
      global ClosingQty
      time.sleep(3)
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("ssInventory").click()
      #    time.sleep(5)
      #    self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//i[contains(.,'Inventory Summary')]").click()
      #    time.sleep(3)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,' Load')]").click()
      #    time.sleep(7)
      #    OpeningValue = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),' Opening Value ')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    OpeningValue = float(OpeningValue.replace(',', ''))
      #    print("OpeningValue", OpeningValue)
      #    OpeningQty = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'Opening Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    print("OpeningQty", OpeningQty)
      #    PurchaseValue = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),' Purchase Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    PurchaseValue = float(PurchaseValue.replace(',', ''))
      #    print("PurchaseValue", PurchaseValue)
      #    PurchaseQty = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'Purchase Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    print("PurchaseQty", PurchaseQty)
      #    StockManageInValue = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'StockManage In-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    StockManageInValue = float(StockManageInValue.replace(',', ''))
      #    print("StockManageInValue", StockManageInValue)
      #    StockManageInQty = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'StockManage In-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    print("StockManageInQty", StockManageInQty)
      #    StockManageOutValue = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'StockManage OUT-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    StockManageOutValue = float(StockManageOutValue.replace(',', ''))
      #    print("StockManageOutValue", StockManageOutValue)
      #    StockManageOutQty = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'StockManage OUT-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    print("StockManageOutQty", StockManageOutQty)
      #    ConsumptionValue = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'Consumption Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    ConsumptionValue = float(ConsumptionValue.replace(',', ''))
      #    print("ConsumptionValue", ConsumptionValue)
      #    ConsumptionQty = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'Consumption Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    print("ConsumptionQty", ConsumptionQty)
      #    ClosingValue = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'Closing Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    ClosingValue = float(ClosingValue.replace(',', ''))
      #    print("ClosingValue", ClosingValue)
      #    ClosingQty = self.danpheEMR.find_element_by_xpath(
      #       "(//b[contains(text(),'Closing Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
      #    print("ClosingQty", ClosingQty)

      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Inventory").click()
         time.sleep(5)
         #self.danpheEMR.find_element_by_xpath("//i[contains(text(),'General Inventory')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//i[contains(.,'Inventory Summary')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,' Load')]").click()
         time.sleep(7)
         OpeningValue = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),' Opening Value ')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         OpeningValue = float(OpeningValue.replace(',', ''))
         print("OpeningValue", OpeningValue)
         OpeningQty = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Opening Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("OpeningQty", OpeningQty)
         PurchaseValue = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),' Purchase Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         PurchaseValue = float(PurchaseValue.replace(',', ''))
         print("PurchaseValue", PurchaseValue)
         PurchaseQty = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Purchase Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("PurchaseQty", PurchaseQty)
         StockManageInValue = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage In-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         StockManageInValue = float(StockManageInValue.replace(',', ''))
         print("StockManageInValue", StockManageInValue)
         StockManageInQty = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage In-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("StockManageInQty", StockManageInQty)
         StockManageOutValue = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage OUT-Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         StockManageOutValue = float(StockManageOutValue.replace(',', ''))
         print("StockManageOutValue", StockManageOutValue)
         StockManageOutQty = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'StockManage OUT-Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("StockManageOutQty", StockManageOutQty)
         ConsumptionValue = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Consumption Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         ConsumptionValue = float(ConsumptionValue.replace(',', ''))
         print("ConsumptionValue", ConsumptionValue)
         ConsumptionQty = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Consumption Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("ConsumptionQty", ConsumptionQty)
         ClosingValue = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Closing Value')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         ClosingValue = float(ClosingValue.replace(',', ''))
         print("ClosingValue", ClosingValue)
         ClosingQty = self.danpheEMR.find_element_by_xpath(
            "(//b[contains(text(),'Closing Quantity')]/parent::span/parent::td/following-sibling::td/child::span)[1]").text
         print("ClosingQty", ClosingQty)
   def preInventorySummaryReport(self):
      global preOpeningValue
      global preOpeningQty
      global prePurchaseValue
      global prePurchaseQty
      global preStockManageInValue
      global preStockManageInQty
      global preStockManageOutValue
      global preStockManageOutQty
      global preConsumptionValue
      global preConsumptionQty
      global preClosingValue
      global preClosingQty
      preOpeningValue = OpeningValue
      preOpeningQty = OpeningQty
      prePurchaseValue = PurchaseValue
      prePurchaseQty = PurchaseQty
      preStockManageInValue = StockManageInValue
      preStockManageInQty = StockManageInQty
      preStockManageOutValue = StockManageOutValue
      preStockManageOutQty = StockManageOutQty
      preConsumptionValue = ConsumptionValue
      preConsumptionQty = ConsumptionQty
      preClosingValue = ClosingValue
      preClosingQty = ClosingQty
   def verifyInventorySummaryReport(self, purchaseqty, purchaseamount, consumeqty, consumeamount, manageinqty, manageinamount, manageoutqty, manageoutamount):
      print("preOpeningValue", preOpeningValue)
      print("OpeningValue", OpeningValue)
      time.sleep(3)
      assert OpeningValue == preOpeningValue
      assert OpeningQty == preOpeningQty
      x = PurchaseValue
      print("x", x)
      y = prePurchaseValue + purchaseamount
      print("y", y)
      assert x == y
      assert int(PurchaseQty) == int(prePurchaseQty) + purchaseqty
      calcNewStockManageInValue = preStockManageInValue + manageinamount   #
      print("calcNewStockManageInValue", calcNewStockManageInValue)        #
      print("StockManageInValue", StockManageInValue)
      print("preStockManageInValue", preStockManageInValue)
      print("manageinamount", manageinamount)
      assert StockManageInValue == preStockManageInValue + manageinamount #script failing with bug: EMR-2832
      assert int(StockManageInQty) == int(preStockManageInQty) + manageinqty
      assert StockManageOutValue == preStockManageOutValue + manageoutamount
      assert int(StockManageOutQty) == int(preStockManageOutQty) + manageoutqty
      print("ConsumptionValue", ConsumptionValue)
      print("preConsumptionValue", preConsumptionValue)
      print("consumeamount", consumeamount)
      tempSum = float(preConsumptionValue) + float(consumeamount)
      print("TempSum", tempSum)
      assert int(ConsumptionValue) == int(tempSum)
      assert int(ConsumptionQty) == int(preConsumptionQty) + consumeqty
      print("ClosingValue", ClosingValue)
      print("preClosingValue", preClosingValue)
      print("purchaseamount", purchaseamount)
      print("consumeamount", consumeamount)
      print("manageinamount", manageinamount)
      tempclosing = float(preClosingValue) + float(purchaseamount) + float(manageinamount) - float(consumeamount) - float(manageoutamount)
      print("tempclosing", tempclosing)
      assert float(ClosingValue) == tempclosing
      print("ClosingQty", ClosingQty)
      print("preClosingQty", preClosingQty)
      print("purchaseqty", purchaseqty)
      print("consumeqty", consumeqty)
      print("manageinqty", manageinqty)
      tempclosingqty = float(preClosingQty) + purchaseqty +manageinqty - consumeqty -manageoutqty
      print("tempclosingqty", tempclosingqty)
      print("ClosingQty", ClosingQty)
      assert float(ClosingQty) == float(tempclosingqty)


def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

