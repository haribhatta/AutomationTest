from selenium import webdriver
import time
import Library.ApplicationConfiguration as AC
from selenium.webdriver.common.keys import Keys

danpheEMR = AC.danpheEMR
print("DanpheEMR", danpheEMR)
AppName = AC.appName

#Module:ADT -----------------------------
def admitDisTrans(admit, discharge, trasfer, deposit, doctor, department):
      if admit == 1:
         if AppName == "SNCH":
            time.sleep(5)
            danpheEMR.find_element_by_link_text("ADT").click()
            time.sleep(3)
            danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
            time.sleep(5)
            danpheEMR.find_element_by_link_text("Admit").click()
            time.sleep(3)
            danpheEMR.find_element_by_id("admissionCase").click()
            dropdown = danpheEMR.find_element_by_id("admissionCase")
            dropdown.find_element_by_xpath("//option[. = 'General']").click()
            danpheEMR.find_element_by_id("admissionCase").click()
            danpheEMR.find_element_by_id("RequestingDeptId").send_keys("GENERAL MEDICINE")
            danpheEMR.find_element_by_id("RequestingDeptId").send_keys(Keys.RETURN)
            danpheEMR.find_element_by_id("RequestingDeptId").click()
            dropdown = danpheEMR.find_element_by_id("WardId")
            dropdown.find_element_by_xpath("//option[. = 'Medical Ward']").click()
            danpheEMR.find_element_by_id("WardId").click()
            danpheEMR.find_element_by_id("BedFeatureId").click()
            danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.DOWN)
            danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedFeatureId").click()
            danpheEMR.find_element_by_id("BedId").click()
            danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedId").send_keys(Keys.DOWN)
            danpheEMR.find_element_by_id("BedId").send_keys(Keys.ENTER)
            danpheEMR.find_element_by_id("BedId").click()
            time.sleep(5)
            danpheEMR.find_element_by_id("SaveAdmission").click()
            time.sleep(7)
            danpheEMR.find_element_by_id("btnAdtSticker").send_keys(Keys.ESCAPE)
            print("Patient successfully admitted.")
            time.sleep(5)
            time.sleep(2)
      elif discharge == 1:
         time.sleep(5)
         danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(5)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(3)
         danpheEMR.find_element_by_xpath("//pat-ip-bill-summary/div/div[2]/div/div/div/div/a").click()
         danpheEMR.close()
      elif trasfer == 1:
         danpheEMR.find_element_by_link_text("ADT").click()
         time.sleep(3)
         danpheEMR.find_element_by_link_text("Admitted Patients").click()
         time.sleep(3)
         danpheEMR.find_element_by_link_text("Transfer").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_xpath("//tr[5]/td[2]/select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.ARROW_DOWN)
         danpheEMR.find_element_by_xpath("//tr[7]/td[2]/select").send_keys(Keys.RETURN)
         danpheEMR.find_element_by_id("Remarks").send_keys("Transfer to ICU ward")
         danpheEMR.find_element_by_xpath("//input[@name='name']").click()
def billingIP(admitCharge, deposit):
      if AppName == 'SNCH':
         danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(1)
         danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(2)
         danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         if deposit >= 1:
            danpheEMR.find_element_by_xpath("//button[contains(.,' Add Deposit ')]").click()
            danpheEMR.find_element_by_id("txtAmount").send_keys(deposit)
            danpheEMR.find_element_by_id("btnAddDeposit").click()
            time.sleep(2)
            danpheEMR.find_element_by_id("btn_PrintReceipt").send_keys(Keys.ESCAPE)
         time.sleep(2)
         billingTotalExp = admitCharge
         billingTotalAct = danpheEMR.find_element_by_xpath("//td[2]/label").text
         print(billingTotalAct)
         totalDiscountExp = 0 # discount is zero
         totalDiscountAct = danpheEMR.find_element_by_xpath("//td[contains(text(),' Discount Amt.')]/following-sibling::td").text
         print("totalDiscountAct", totalDiscountAct)
         print("totalDiscountExp", totalDiscountExp)
         netTotalExp = int(billingTotalExp) - int(totalDiscountExp)
         netTotalAct = danpheEMR.find_element_by_xpath("//tr[5]/td[2]/label").text
         print(netTotalAct)
         depositBalanceExp = int(deposit)
         depositBalanceAct = danpheEMR.find_element_by_xpath("//tr[6]/td[2]/label").text
         print("depositBalanceAct", depositBalanceAct)
         depositBalanceAct = depositBalanceAct.replace(',', '')
         print("depositBalanceAct", depositBalanceAct)
         print("depositBalanceExp", depositBalanceExp)
         assert depositBalanceExp == int(depositBalanceAct)
         if depositBalanceExp > netTotalExp:
            toBeRefundExp = depositBalanceExp - netTotalExp
            toBeRefundAct = danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
            print("To be refund:", toBeRefundAct)
         elif depositBalanceExp < netTotalExp:
            toBePaidExp = netTotalExp - depositBalanceExp
            toBePaidAct = danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
            print("To be paid:", toBePaidAct)
         time.sleep(4)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(10)
         element = danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
         time.sleep(2)
         danpheEMR.execute_script("arguments[0].click();", element)
         time.sleep(5)
def cancelDischarge():
      # To cancel discharge user need to return discharge invoice
      print("Start: cancel discharge")
      danpheEMR.find_element_by_link_text("ADT").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Discharged Patients").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      danpheEMR.find_element_by_xpath("//a[contains(text(),'Cancel Discharge')]").click()
      time.sleep(2)
      danpheEMR.find_element_by_id("DischargeCancelNote").send_keys("Cancel Discharge")
      time.sleep(2)
      danpheEMR.find_element_by_id("Approve").click()
      time.sleep(5)
      print("End: cancel discharge")
def dischargeRandomPatient():
      time.sleep(2)
      if AppName == "SNCH":
         danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(9)
         danpheEMR.find_element_by_xpath("//button[contains(.,'Discharge')]").click()
         time.sleep(2)
         danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
         time.sleep(3)
         danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
         time.sleep(3)
         danpheEMR.find_element_by_id("btnPrintDischargeInvoice").send_keys(Keys.ESCAPE)
         time.sleep(14)
      time.sleep(5)
def checkAutoAddItems():
      danpheEMR.find_element_by_link_text("Settings").click()
      time.sleep(2)
      danpheEMR.find_element_by_xpath("//a[contains(text(),' ADT ')]").click()
      time.sleep(3)
      danpheEMR.find_element_by_link_text("Manage Auto Add Billing Items").click()
      time.sleep(2)
      #danpheEMR.find_element_by_xpath("//h4[text()='Auto Add Bill Item: ']").click()
      autoaddbillitemvalue = danpheEMR.find_element_by_xpath("//b[contains(.,'  False')]").text
      autoaddBeditemvalue = danpheEMR.find_element_by_xpath("//b[contains(.,'  True')]").text
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

def __str__():
      return

