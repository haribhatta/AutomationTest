from selenium import webdriver
import time
import AutomationTest.Library.ApplicationConfiguration as AC

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)

#Module:ADT -----------------------------
   def admitDisTrans(self, admit, discharge, trasfer, deposit, doctor, department):
      if admit == 1:
         if appPort == "82":
            time.sleep(5)
            self.danpheEMR.find_element_by_link_text("ADT").click()
            time.sleep(3)
            self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
            time.sleep(5)
            self.danpheEMR.find_element_by_link_text("Admit").click()
            time.sleep(3)
            self.danpheEMR.find_element_by_id("admissionCase").click()
            dropdown = self.danpheEMR.find_element_by_id("admissionCase")
            dropdown.find_element_by_xpath("//option[. = 'General']").click()
            self.danpheEMR.find_element_by_id("admissionCase").click()
            self.danpheEMR.find_element_by_id("RequestingDeptId").send_keys("GENERAL MEDICINE")
            self.danpheEMR.find_element_by_id("RequestingDeptId").send_keys(Keys.RETURN)
            self.danpheEMR.find_element_by_id("RequestingDeptId").click()
            dropdown = self.danpheEMR.find_element_by_id("WardId")
            dropdown.find_element_by_xpath("//option[. = 'Medical Ward']").click()
            self.danpheEMR.find_element_by_id("WardId").click()
            self.danpheEMR.find_element_by_id("BedFeatureId").click()
            self.danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)
            self.danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.DOWN)
            self.danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)

            #dropdown = self.danpheEMR.find_element_by_id("BedFeatureId")
            #dropdown.find_element_by_xpath("//option[. = 'General Bed']").click()
            self.danpheEMR.find_element_by_id("BedFeatureId").click()
            self.danpheEMR.find_element_by_id("BedId").click()
            self.danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
            self.danpheEMR.find_element_by_id("BedId").send_keys(Keys.DOWN)
            self.danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
            #dropdown = self.danpheEMR.find_element_by_id("BedId")
            #dropdown.find_element_by_xpath("//option[. = 'M-2']").click()
            self.danpheEMR.find_element_by_id("BedId").click()
            time.sleep(5)
            self.danpheEMR.find_element_by_id("SaveAdmission").click()
            time.sleep(7)
            self.danpheEMR.find_element_by_id("btnAdtSticker").send_keys(Keys.ESCAPE)

            print("Patient successfully admitted.")
            time.sleep(5)
            #self.danpheEMR.find_element_by_xpath("(//a[@class='btn btn-danger history-del-btn'])[1]").click()
            #self.danpheEMR.find_element_by_css_selector(".col-md-6 > .modelbox-div > .btn").click()
            time.sleep(2)
      elif discharge == 1:
         time.sleep(5)
         self.danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(5)
         #self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//pat-ip-bill-summary/div/div[2]/div/div/div/div/a").click()
         self.danpheEMR.close()
      elif trasfer == 1:
         self.danpheEMR.find_element_by_link_text("ADT").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Admitted Patients").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Transfer").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.RETURN)
         #self.danpheEMR.find_element_by_xpath("//textarea[@name='Remarks']").send_keys("Transfer to ICU ward")
         self.danpheEMR.find_element_by_id("Remarks").send_keys("Transfer to ICU ward")
         self.danpheEMR.find_element_by_xpath("//input[@name='name']").click()
   def billingIP(self, admitCharge, deposit):
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Billing").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("IPBilling").click()
      #    time.sleep(1)
      #    self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("View Details").click()
      #    time.sleep(9)
      #    billingTotalExp = admitCharge
      #    billingTotalAct = self.danpheEMR.find_element_by_xpath("//td[2]/label").text
      #    print(billingTotalAct)
      #    totalDiscountExp = "0"
      #    totalDiscountAct = self.danpheEMR.find_element_by_xpath("//input[@type='number']").get_attribute("value")
      #    print(totalDiscountAct)
      #    assert totalDiscountExp == totalDiscountAct
      #    netTotalExp = int(billingTotalExp) - int(totalDiscountExp)
      #    netTotalAct = self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]/label").text
      #    print(netTotalAct)
      #    depositBalanceExp = deposit
      #    depositBalanceAct = self.danpheEMR.find_element_by_xpath("//tr[6]/td[2]/label").text
      #    print("depositBalanceAct", depositBalanceAct)
      #    depositBalanceAct = depositBalanceAct.replace(',', '')
      #    print("depositBalanceAct", depositBalanceAct)
      #    print("depositBalanceExp", depositBalanceExp)
      #    assert depositBalanceExp == int(depositBalanceAct)
      #    if depositBalanceExp > netTotalExp:
      #       toBeRefundExp = depositBalanceExp - netTotalExp
      #       toBeRefundAct = self.danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
      #       print("To be refund:", toBeRefundAct)
      #    elif depositBalanceExp < netTotalExp:
      #       toBePaidExp = netTotalExp - depositBalanceExp
      #       toBePaidAct = self.danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
      #       print("To be paid:", toBePaidAct)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
      #    self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
      #    time.sleep(10)
      #    element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
      #    time.sleep(2)
      #    self.danpheEMR.execute_script("arguments[0].click();", element)
      #    time.sleep(5)

      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         if deposit >= 1:
            self.danpheEMR.find_element_by_xpath("//button[contains(.,' Add Deposit ')]").click()
            self.danpheEMR.find_element_by_id("txtAmount").send_keys(deposit)
            self.danpheEMR.find_element_by_id("btnAddDeposit").click()
            time.sleep(2)
            self.danpheEMR.find_element_by_id("btn_PrintReceipt").send_keys(Keys.ESCAPE)
         time.sleep(2)
         billingTotalExp = admitCharge
         billingTotalAct = self.danpheEMR.find_element_by_xpath("//td[2]/label").text
         print(billingTotalAct)
         totalDiscountExp = 0 # discount is zero
         #totalDiscountAct = self.danpheEMR.find_element_by_xpath("//td[contains(text(),' Discount Amt.')]/following-sibling::td").get_attribute("value")
         totalDiscountAct = self.danpheEMR.find_element_by_xpath("//td[contains(text(),' Discount Amt.')]/following-sibling::td").text
         print("totalDiscountAct", totalDiscountAct)
         print("totalDiscountExp", totalDiscountExp)
         #assert totalDiscountExp == totalDiscountAct
         netTotalExp = int(billingTotalExp) - int(totalDiscountExp)
         netTotalAct = self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]/label").text
         print(netTotalAct)
         depositBalanceExp = int(deposit)
         depositBalanceAct = self.danpheEMR.find_element_by_xpath("//tr[6]/td[2]/label").text
         print("depositBalanceAct", depositBalanceAct)
         depositBalanceAct = depositBalanceAct.replace(',', '')
         print("depositBalanceAct", depositBalanceAct)
         print("depositBalanceExp", depositBalanceExp)
         assert depositBalanceExp == int(depositBalanceAct)
         if depositBalanceExp > netTotalExp:
            toBeRefundExp = depositBalanceExp - netTotalExp
            toBeRefundAct = self.danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
            print("To be refund:", toBeRefundAct)
         elif depositBalanceExp < netTotalExp:
            toBePaidExp = netTotalExp - depositBalanceExp
            toBePaidAct = self.danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
            print("To be paid:", toBePaidAct)
         time.sleep(4)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(10)
         element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
         time.sleep(2)
         self.danpheEMR.execute_script("arguments[0].click();", element)
         time.sleep(5)
   def cancelDischarge(self):
      # To cancel discharge user need to return discharge invoice
      print("Start: cancel discharge")
      self.danpheEMR.find_element_by_link_text("ADT").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Discharged Patients").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Cancel Discharge')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("DischargeCancelNote").send_keys("Cancel Discharge")
      time.sleep(2)
      self.danpheEMR.find_element_by_id("Approve").click()
      time.sleep(5)
      print("End: cancel discharge")
   def dischargeRandomPatient(self):
      time.sleep(2)
      # if appPort == '81':
      #    self.danpheEMR.find_element_by_link_text("Billing").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("IPBilling").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_link_text("View Details").click()
      #    time.sleep(9)
      #    self.danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
      #    time.sleep(2)
      #    self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
      #    self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
      #    time.sleep(10)
      #    element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
      #    time.sleep(2)
      #    self.danpheEMR.execute_script("arguments[0].click();", element)
      if appPort == '82':
         self.danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)
         time.sleep(14)

      time.sleep(5)
   def checkAutoAddItems(self):
      self.danpheEMR.find_element_by_link_text("Settings").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),' ADT ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Manage Auto Add Billing Items").click()
      time.sleep(2)
      #self.danpheEMR.find_element_by_xpath("//h4[text()='Auto Add Bill Item: ']").click()
      autoaddbillitemvalue = self.danpheEMR.find_element_by_xpath("//b[contains(.,'  False')]").text
      autoaddBeditemvalue = self.danpheEMR.find_element_by_xpath("//b[contains(.,'  True')]").text
      print("autoaddbillitemvalue", autoaddbillitemvalue)
      print("autoaddBeditemvalue", autoaddBeditemvalue)
      #assert autoaddbillitemvalue == "autoaddbillitemvalue   False"      rework needed
      #assert autoaddBeditemvalue == "autoaddBeditemvalue   True"        rework needed
def wait_for_window(timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = danpheEMR.window_handles
      wh_then = vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

def __str__(self):
      return

