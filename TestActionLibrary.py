from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
#from webdriver_manager.chrome import ChromeDriverManager
import random
import decimal
import string
import winsound
class A:
   drugqtyMS = 0
   drugqtySS = 0

   #defining global veriables for login users

   #admin user
   adminUserID = 'admin'
   adminUserPwD = 'pass123'

   #billing user
   foUserID = 'billing'
   foUserPwD = 'pass123'

   #Lab user
   labUserID = 'lab'
   labUserPwD = 'pass123'

   #radiologist user
   radioUserID = 'radio'
   radioUserPwD = 'pass123'

   #pharmacy user
   pharmacyUserID = 'pharmacy'
   pharmacyUserPwD = 'pass123'

   #nurse user
   nurseUserID = 'nurse'
   nurseUserPwD = 'pass123'

   #store user
   storeUserID = 'inventory'
   storeUserPwD = 'pass123'

   global appPort
   global appURL
   #appURL = "http://10.0.0.103:"
   appURL = "http://localhost:"

   @classmethod
   def applicationSelection(cls):
      global appURL
      global appPort
      appPort = input("Please enter application port."
            "81 for DanpheEMR Core"
            "82 for Danphe Lumbini")
      if appPort == "81":
         #appURL = "http://10.0.0.103:81/"
          appURL = "http://localhost:81/"
      if appPort == "82":
         #appURL = "http://10.0.0.103:82/"
          appURL = "http://localhost:82/"
      print("Starting", appURL)


   def openBrowser(self):

      global appURL
      global appPort

      global TFT
      global CBC
      global xrayChest
      global xrayLPH
      global labLPH
      global usgAbdomenPelvis
      global usgLPH
      global usgAbdomenPelvisRate
      global doctor1
      global doctor2
      TFT = "TFT(FT3,FT4,TSH) CLLEA"
      CBC = "CBC(HB,PCV,RBC,WBC,TC,DC,PLT,MCV)"
      labLPH = "TFT"
      xrayChest = "X-Ray Chest PA view"
      xrayLPH = "XRAY (300)"
      usgAbdomenPelvis = "USG (Abdomen / pelvis)"
      usgLPH = "USG ABDOMEN/PELVIS"
      usgAbdomenPelvisRate = 1050
      doctor1 = "Dr. Doctor Doctor"

      if appURL == "http://localhost:":
         appPort = input("Please enter application port."
                         "81 for DanpheEMR Core"
                         "82 for Danphe Lumbini")
         if appPort == "81":
            appURL = "http://localhost:81/"
         if appPort == "82":
            appURL = "http://localhost:82/"

      print(">>Open Browser: START")
      self.danpheEMR = webdriver.Chrome('D:/AutomationGIT/drivers/chromedriver.exe')
      #danpheEMR = webdriver.Chrome(ChromeDriverManager().install())
      self.danpheEMR.set_window_position(-2000, 0)
      self.danpheEMR.maximize_window()
      print("App url", appURL)
      print("Opening browser for", appURL)
      self.danpheEMR.get(appURL)
      #self.danpheEMR.find_element_by_xpath("//button[contains(text(),'Advanced')]").click()   --- This is to add SSL exceptional
      #time.sleep(2)
      #self.danpheEMR.find_element_by_xpath("//button[contains(text(),'Advanced')]").click()
      #time.sleep(2)
      #self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Proceed to demo.danphehealth.com (unsafe)')]").click()
      #time.sleep(3)
      print("Open Browser: END<<")
   def closeBrowser(self):
      print(">>Close Browser: START")
      self.danpheEMR.close()
      print("Close Browser: END<<")
   def login(self, userid, pwd):
      print(">>LogIn: START")
      self.danpheEMR.find_element_by_id("username_id").send_keys(userid)
      self.danpheEMR.find_element_by_id("password").send_keys(pwd)
      self.danpheEMR.find_element_by_id("login").submit()
      print("LogIn: END<<")
   def logout(self):
      print(">>LogOut: START")
      time.sleep(1)
      self.danpheEMR.find_element_by_css_selector(".dropdown-toggle:nth-child(1) > .fa").click()
      time.sleep(1)
      self.danpheEMR.find_element_by_link_text("Log Out").click()
      time.sleep(1)
      print("LogOut: END<<")

   # Module: Appointment --------------------
   def patientquickentry(self, discountpc, paymentmode):
      global InvoiceNo
      global contactno
      global HospitalNo
      global FullName
      #doctorname = "Dr. JAMAAL MORGAN"
      print(">>Create New Appointment: START")

      if appPort == "81":
         self.danpheEMR.find_element_by_link_text("Appointment").click()
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),' New Patient')]").click()
         self.danpheEMR.find_element_by_id("aptPatFirstName").send_keys("auto")
         self.danpheEMR.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
         sname = str(random.randint(1111, 9999))
         self.danpheEMR.find_element_by_css_selector(".col-md-3:nth-child(4) > .form-control").send_keys("pqe", sname)
         fname = "auto "
         mname = "test "
         z = "pqe"
         sname1 = z + sname
         print("Sir name", sname1)
         FullName = fname + mname + sname1
         print("Full name of patient:", FullName)
         age = random.randint(5, 99)
         self.danpheEMR.find_element_by_css_selector(".row > .form-control").send_keys(33)
         # gender.send_keys('Male')
         self.danpheEMR.find_element_by_css_selector(".rad-holder > .mt-radio:nth-child(1) > span").click()
         # self.danpheEMR.find_element_by_css_selector(".rad-holder > .mt-radio:nth-child(1) > span").click()
         # self.danpheEMR.find_element_by_css_selector(".col-md-3 > .ng-invalid").click()
         contactno = random.randint(9841111111, 9849999999)
         self.danpheEMR.find_element_by_css_selector(".form-group > .pr-0:nth-child(2) > .ng-untouched").send_keys(
            contactno)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").clear()
         # doctoroption = Select(self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]"))
         # time.sleep(2)
         # doctoroption.select_by_visible_text(doctorname)
         # time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").click()
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(doctor1)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
         # self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys("Dr. FERDINAND WARIS")
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
         subtotal = int(self.danpheEMR.find_element_by_xpath("//span/b").text)
         if subtotal == 0:
            self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").clear()
            self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(
               "Dr. FERDINAND WARIS")
            self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
         if discountpc > 0:
            self.danpheEMR.find_element_by_xpath("(//input[@type='number'])[3]").send_keys(discountpc)
            self.danpheEMR.find_element_by_xpath("//div[2]/div[2]/input").send_keys("This is auto discount check")
         if paymentmode == 'CREDIT':
            paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select[@id='pay_mode']"))
            paymentoptions.select_by_visible_text(paymentmode)
            self.danpheEMR.find_element_by_xpath("//div[2]/div[2]/input").send_keys("Credit in request of chairman")
         self.danpheEMR.find_element_by_css_selector(".btn-success").click()

      if appPort == "82":
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Registration").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("btnNewPatient").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("txtDepartment").send_keys("GYNAE & OBS")
         self.danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.TAB)
         self.danpheEMR.find_element_by_id("aptPatFirstName").send_keys("auto")
         self.danpheEMR.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("test")
         sname = str(random.randint(1111, 9999))
         self.danpheEMR.find_element_by_css_selector(".col-md-3:nth-child(4) > .form-control").send_keys("pqe", sname)
         fname = "auto "
         mname = "test "
         z = "pqe"
         sname1 = z + sname
         print("Sir name", sname1)
         FullName = fname + mname + sname1
         print("Full name of patient:", FullName)
         age = random.randint(5, 99)
         self.danpheEMR.find_element_by_css_selector(".row > .form-control").send_keys(33)
         self.danpheEMR.find_element_by_css_selector(".input-group > .ng-valid").click()#
         dropdown = self.danpheEMR.find_element_by_css_selector(".ng-dirty")#
         dropdown.find_element_by_xpath("//option[. = 'Years']").click()#
         self.danpheEMR.find_element_by_css_selector(".ng-dirty").click()#
         gender = Select(self.danpheEMR.find_element_by_xpath("//select[@formcontrolname='Gender']"))
         gender.select_by_visible_text("Male")
         if discountpc > 0:
            self.danpheEMR.find_element_by_css_selector(".comm-list").click()
            dropdown = self.danpheEMR.find_element_by_css_selector(".comm-list")
            time.sleep(3)
            dropdown.find_element_by_xpath("//option[. = 'SOCIAL SERVICE UNIT']").click()
            time.sleep(7)
            self.danpheEMR.find_element_by_css_selector(".comm-list").click()
            time.sleep(5)
            self.danpheEMR.find_element_by_css_selector(".membership-list").click()
            time.sleep(4)
            dropdown = self.danpheEMR.find_element_by_css_selector(".membership-list")
            time.sleep(5)
            dropdown.find_element_by_xpath("//option[. = ' Child Under Nutrition (50%)']").click()
            time.sleep(3)
            self.danpheEMR.find_element_by_css_selector(".membership-list").click()
         self.danpheEMR.find_element_by_css_selector(".btn-success").click()
         time.sleep(5)

      InvoiceNo = self.danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]/child::span").text
      print("InvoiceNoTemp", InvoiceNo)
      InvoiceNo = InvoiceNo.partition("BL")[2]
      print("InvoiceNo", InvoiceNo)
      HospitalNo = self.danpheEMR.find_element_by_xpath(
         "//strong[contains(text(), 'Hospital No:')]/parent::p/child::span/child::strong").text
      print("HospitalNo:", HospitalNo)
      print(" Verify OPD Invoice Details: END<<", "HospitalNo", HospitalNo, "InvoiceNo", InvoiceNo)
      print("Create New Appointment: END<<")

   def followUpAppointment(self):
      print("lets create appointment followup")
      if appPort == '81':
         self.danpheEMR.find_element_by_link_text("Appointment").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_link_text("Check In").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(
             "Dr. FERDINAND WARIS")
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[4]").send_keys(Keys.TAB)
         time.sleep(2)
         self.danpheEMR.find_element_by_css_selector(".btn-success").click()
         time.sleep(3)
      if appPort == '82':
          self.danpheEMR.find_element_by_link_text("Registration").click()
          time.sleep(5)
          self.danpheEMR.find_element_by_link_text("List Visits").click()
          time.sleep(2)
          self.danpheEMR.find_element_by_xpath("//span[contains(.,'Hospital No.')]").click()
          time.sleep(3)
          self.danpheEMR.find_element_by_xpath("followup").click()
          self.danpheEMR.find_element_by_xpath("//button[contains(.,'Add Followup Visit')]").click()
          self.danpheEMR.find_element_by_xpath("//i[contains(.,'X')]").click()
          time.sleep(3)



   # Module: Billing -----------------------
   def counteractivation(self):
      print(">>Activate Billing Counter: START")
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//a[contains(@href, '#/Billing/CounterActivate')])[2]").click()
      self.danpheEMR.find_element_by_css_selector(".col-md-2:nth-child(1) img").click()
      print("Activate Billing Counter: END<<")
   def verifyopdinvoice(self, deposit, billamt):
      print(">>Verify OPD Invoice Details: START")
      syscontactno = self.danpheEMR.find_element_by_xpath("//div[@id='printpage']/div/div[5]/div[5]/div/p").text
      syscontactno = syscontactno.partition("No: ")[2]
      print(syscontactno)
      print(contactno)
      assert int(contactno) == int(syscontactno)

      if deposit < billamt and deposit > 0:
         DepositDeductorReturn = self.danpheEMR.find_element_by_xpath("//div[@id='printpage']/div/div[5]/div[10]/span").text  #Deposit Deduct/Return:
         DepositDeductorReturn = DepositDeductorReturn.partition("n: ")[2]
         print("1: Deposit Deduct/Return: ", DepositDeductorReturn)
         assert int(DepositDeductorReturn) == deposit
         systender = self.danpheEMR.find_element_by_xpath("//div[@id='printpage']/div/div[5]/div[10]/span[2]").text  #Tender
         systender = systender.partition("r: ")[2]
         systender = systender.partition(".00")[0]
         Tender = int(billamt) - int(deposit)
         print("Expected Tender: ", Tender)
         print("Actual Tender:", systender)
         assert int(Tender) == int(systender)
         sysdepositbalance = self.danpheEMR.find_element_by_xpath("//div[@id='printpage']/div/div[5]/div[10]/span[3]").text  #Deposit Balance
         print("3:", sysdepositbalance)
         sysdepositbalance = sysdepositbalance.partition("e: ")[2]
         assert sysdepositbalance == "0"
   def returnBillingInvoice(self, returnmsg):
      print(">>START: Returning OPD Invoice.", InvoiceNo)
      global returnTotalAmount
      self.danpheEMR.find_element_by_link_text("Billing").click()
      self.danpheEMR.find_element_by_link_text("Return Bills").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_name("TransactionId").clear()
      self.danpheEMR.find_element_by_name("TransactionId").send_keys(InvoiceNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".fa-search").click()
      time.sleep(9)
      self.danpheEMR.find_element_by_id("txtRetQty_0").send_keys(1)
      self.danpheEMR.find_element_by_id("txtReturnRemarks").send_keys(returnmsg)
      self.danpheEMR.find_element_by_id("btnSubmit").click()
      time.sleep(3)
      returnremark = self.danpheEMR.find_element_by_xpath("//div[contains(text(), ' Remarks:')]").text
      returnTotalAmount = self.danpheEMR.find_element_by_xpath("//td[contains(text(),'Total Amount ')]/following-sibling::td").text
      #self.danpheEMR.find_element_by_id("btnPrintRecipt").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']").click() # This is to close print window.
      time.sleep(3)
      print("returnmsgTemp", returnremark)
      returnremark = returnremark.partition("Remarks: ")[2]
      print("returnremark", returnremark)
      print("returnmsg", returnmsg)
      assert returnremark == returnmsg
      print("returnTotalAmount", returnTotalAmount)
      print("<<END: Return OPD Invoice.")
   def creditPayment(self):
      print(">>START: Credit Payment")
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Settlements").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Show Details").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@value='Proceed']").click()
   def createlabxrayinvoice(self, labtest, imagingtest):
      print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")

      if appPort == "81":
         self.danpheEMR.find_element_by_link_text("Billing").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(contactno)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_link_text("Billing Request").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").click()
         self.danpheEMR.find_element_by_id("items-box0").send_keys(xrayChest)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
         time.sleep(2)
         price1 = self.danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
         time.sleep(1)
         self.danpheEMR.find_element_by_css_selector("a > .btn-success").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_id("items-box1").send_keys(TFT)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box1").send_keys(Keys.TAB)
         time.sleep(2)
         price2 = self.danpheEMR.find_element_by_xpath("(//input[@name='total'])[2]").get_attribute('value')
         totalprice = int(price1) + int(price2)
         print("Total Price:", totalprice)
         time.sleep(1)
         self.danpheEMR.find_element_by_id("items-box1").send_keys(Keys.TAB)
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[9]").clear()
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[9]").send_keys(doctor1)
         self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
         time.sleep(2)

      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Billing").click()
         self.danpheEMR.find_element_by_id("srch_PatientList").click()
         self.danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
         self.danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
         time.sleep(3)
         self.danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_id("items-box0").click()
         self.danpheEMR.find_element_by_id("items-box0").send_keys(xrayLPH)
         time.sleep(1)
         self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
         time.sleep(1)
         price1 = self.danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
         time.sleep(1)
         self.danpheEMR.find_element_by_css_selector("a > .btn-success").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_id("items-box1").send_keys(labLPH)
         time.sleep(1)
         self.danpheEMR.find_element_by_id("items-box1").send_keys(Keys.RETURN)
         time.sleep(2)
         price2 = self.danpheEMR.find_element_by_xpath("(//input[@name='total'])[2]").get_attribute('value')
         totalprice = int(price1) + int(price2)
         print("Total Price:", totalprice)
         time.sleep(1)
         self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
         time.sleep(2)

      print("Create OPD Invoice: 1 Lab + 1 Xray Items: END<<")
   def verifylabxrayinvoice(self):
      print(">>Verify OPD Invoice: 1 Lab + 1 Xray Items: START")
      #assert self.danpheEMR.find_element_by_css_selector(".bil-summ tr:nth-child(1) > td:nth-child(2)").text == "1,600.00"
      #vovcontact = self.danpheEMR.find_element_by_css_selector(".col-md-12:nth-child(5) > .left > .no-margin").text
      #self.contactno = str(contactno)
      #x = "Contact No: " + self.contactno
      #assert vovcontact == x
      time.sleep(3)
      invoiceNo = self.danpheEMR.find_element_by_css_selector(".no-margin:nth-child(1) > span").text
      hospitalNoT = self.danpheEMR.find_element_by_css_selector("span > strong").text
      assert HospitalNo == hospitalNoT
      print("Verify OPD Invoice: 1 Lab + 1 Xray Items: END<<", "HospitalNo", hospitalNoT, "InvoiceNo", invoiceNo)
   def createProvisionalBill(self, usgtest):
      print(">>START: Create USG Provisional bill")
      self.danpheEMR.find_element_by_link_text("Billing").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Request").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("items-box0").click()
      self.danpheEMR.find_element_by_id("items-box0").send_keys(usgAbdomenPelvis)
      time.sleep(3)
      #self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").click()
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(doctor1)
      time.sleep(3)
      #self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[3]").send_keys(Keys.ARROW_DOWN)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[3]").send_keys(Keys.TAB)
      time.sleep(2)
      self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Print Provisional Slip')]").click()
      #self.danpheEMR.find_element_by_css_selector(".creamyblue").click()
      time.sleep(5)
      print("<<END")
   def verifyDuplicateBill(self):
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Duplicate Prints ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Show Details").click()
   def createCopyItemInvoice(self, paymentmode):
      print(">>START: CreateCopyItemInvoice")
      global InvoiceNo
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Create Copy Of Items ')]").click()
      time.sleep(3)
      if paymentmode == 'CREDIT':
         self.danpheEMR.find_element_by_id("pay_mode").send_keys('CREDIT')
         self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("Credit in request of chairman")
         time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
      time.sleep(3)
      InvoiceNo = self.danpheEMR.find_element_by_xpath("//p[contains(text(), 'Invoice No:')]/child::span").text
      print("NewInvoiceNo", InvoiceNo)
      InvoiceNo = InvoiceNo.partition("BL")[2]
      print("NewInvoiceNo", InvoiceNo)
      CopyItemTotalAmount = self.danpheEMR.find_element_by_xpath("//td[contains(text(),'Total Amount ')]/following-sibling::td").text
      print("CopyItemTotalAmount:", CopyItemTotalAmount)
      print("returnTotalAmount", returnTotalAmount)
      assert CopyItemTotalAmount == returnTotalAmount #LPH-865 : LPH_V1.9.0
      print("<<END: CreateCopyItemInvoice")
   def getBillingDashboard(self):
      print(">>START: Get Billing Dashboard Information")
      global sysgrosstotal
      global syssubtotal
      global sysdiscountamount
      global sysreturnamount
      global systotalamount
      global sysnetcashcollection
      global sysprovisionalitems
      global sysunpaidcreditinvoices

      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing").click()
      self.danpheEMR.find_element_by_css_selector(".fa-home").click()
      time.sleep(3)

      repeat = 0
      loading = '0'

      while loading == '0' and repeat != 5:
         sysgrosstotal = self.danpheEMR.find_element_by_xpath("//div[@id='totalsales']/div").text
         print(sysgrosstotal)
         syssubtotal = sysgrosstotal.partition("\n")[0]
         syssubtotal = syssubtotal.partition("Rs. ")[2]
         print("System subTotal:", syssubtotal)
         loading = syssubtotal
         time.sleep(3)
         repeat+=1

      sysdiscountamount = sysgrosstotal.partition("ii.")[2]
      print(sysdiscountamount)
      sysdiscountamount = sysdiscountamount.partition("Rs. ")[2]
      print("System discountAmount:", sysdiscountamount)

      sysreturnamount = self.danpheEMR.find_element_by_css_selector("#totalsales > div:nth-child(4)").text
      print(sysreturnamount)
      sysreturnamount = sysreturnamount.partition("Rs. ")[2]
      print("System returnAmount:", sysreturnamount)

      systotalamount = self.danpheEMR.find_element_by_xpath("//div[@id='totalsales']/div[5]/b").text
      print(systotalamount)
      systotalamount = systotalamount.partition("Rs. ")[2]
      print("System totalAmount:", systotalamount)

      sysnetcashcollection = self.danpheEMR.find_element_by_css_selector(".blinkAmount").text
      sysnetcashcollection = sysnetcashcollection.partition("(")[2]
      sysnetcashcollection = sysnetcashcollection.partition(")")[0]
      print("System NetCashCollection:", sysnetcashcollection)

      sysprovisionalitems = self.danpheEMR.find_element_by_xpath("//div[2]/table/tbody/tr/td[2]").text
      sysprovisionalitems = sysprovisionalitems.partition("Rs. ")[2]
      print("System Provisional Item:", sysprovisionalitems)


      sysunpaidcreditinvoices = self.danpheEMR.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]").text
      sysunpaidcreditinvoices = sysunpaidcreditinvoices.partition("Rs. ")[2]
      print("System Unpaid Credit Invoice:", sysunpaidcreditinvoices)
   def preSystemDataBillingDashboard(self):
      print(">>START: Get Billing Dashboard Information")
      global presyssubtotal
      global presysdiscountamount
      global presysreturnamount
      global presystotalamount
      global presysnetcashcollection
      global presysprovisionalitems
      global presysunpaidcreditinvoices

      presyssubtotal = int(syssubtotal)
      print("presyssubtotal", presyssubtotal)
      presysdiscountamount = int(sysdiscountamount)
      print("presysdiscountamount", presysdiscountamount)
      presysreturnamount = int(sysreturnamount)
      print("presysreturnamount", presysreturnamount)
      presystotalamount = int(systotalamount)
      print("presystotalamount", presystotalamount)
      presysnetcashcollection = int(sysnetcashcollection)
      print("presysnetcashcollection", presysnetcashcollection)
      presysprovisionalitems = float(sysprovisionalitems)
      print("presysprovisionalitems", presysprovisionalitems)
      presysunpaidcreditinvoices = float(sysunpaidcreditinvoices)
      print("presysunpaidcreditinvoices", presysunpaidcreditinvoices)
      print("<<END:")
   def verifyBillingDashboard(self, cash, discountpc, cashReturn, credit, creditReturn, settlement, provisional, provisionalcancel):
      print(">>START: Verify Billing Dashboard new updated amounts")

      # 1. Cash Invoice (Check subTotal & totalAmount is increased in Total Sales area).
      if cash > 0 and cashReturn == 0 and discountpc == 0 and credit == 0 and creditReturn == 0:
         expectedsubtotal = presyssubtotal + cash
         time.sleep(3)
         assert int(syssubtotal) == expectedsubtotal
         assert int(systotalamount) == presystotalamount + cash
         assert int(sysnetcashcollection) == presysnetcashcollection + cash

      # 2. Return Cash Invoice (Check ReturnAmount is increased and TotalAmount is decreased on returning opd cash invoice).
      elif cash == 0 and cashReturn > 0 and discountpc == 0 and credit == 0 and creditReturn == 0:
         time.sleep(3)
         print("syssubtotal", syssubtotal)
         print("presyssubtotal", presyssubtotal)
         assert int(syssubtotal) == presyssubtotal #LPH-864: Prio-1 bug in LPH_V1.9.0
         tempresult = presysreturnamount + cashReturn
         print("tempresult", tempresult)
         print("sysreturnamount", sysreturnamount)
         print("presysreturnamount", presysreturnamount)
         assert int(sysreturnamount) == presysreturnamount + cashReturn
         assert int(systotalamount) == presystotalamount - cashReturn
         assert int(sysnetcashcollection) == presysnetcashcollection - cashReturn

      # 3. Cash Discount Invoice (Check Billing Dashboard for discount in OPD cash sale invoice).
      elif cash > 0 and cashReturn == 0 and discountpc > 0 and credit == 0 and creditReturn == 0:
         time.sleep(3)
         assert int(syssubtotal) == presyssubtotal + cash
         calctemp = presysdiscountamount + (discountpc*cash/100)
         print("calctemp", calctemp)
         print("sysdiscountamount", sysdiscountamount)
         assert int(sysdiscountamount) == calctemp
         assert int(sysreturnamount) == presysreturnamount
         assert int(systotalamount) == presystotalamount + cash - (discountpc*cash/100)
         assert int(sysnetcashcollection) == presysnetcashcollection + cash - (discountpc*cash/100)

      # 4. Return Cash Discount Invoice (Check Billing Dashboard for return of discounted OPD cash sale invoice).
      elif cash == 0 and cashReturn > 0 and discountpc > 0 and credit == 0 and creditReturn == 0:
         assert int(syssubtotal) == presyssubtotal
         assert int(sysdiscountamount) == presysdiscountamount
         print("sysreturnamount", sysreturnamount)
         print("presysreturnamount", presysreturnamount)
         print("cashReturn*discountpc", cashReturn*discountpc)
         assert int(sysreturnamount) == presysreturnamount + (cashReturn*(100-discountpc)/100)
         assert int(systotalamount) == presystotalamount - (cashReturn*(100-discountpc)/100)
         assert int(sysnetcashcollection) == presysnetcashcollection - (cashReturn*(100-discountpc)/100)

      # 5. Credit Invoice
      elif cash == 0 and cashReturn == 0 and discountpc == 0 and credit > 0 and creditReturn == 0:
         time.sleep(7)
         assert int(syssubtotal) == presyssubtotal + credit
         assert int(sysdiscountamount) == presysdiscountamount
         assert int(sysreturnamount) == presysreturnamount
         assert int(systotalamount) == presystotalamount + credit
         print("presysnetcashcollection", presysnetcashcollection)
         print("sysnetcashcollection", sysnetcashcollection)
         assert int(sysnetcashcollection) == presysnetcashcollection
         print("End of credit invoice check")

      # 6. Return Credit Invoice (Check ReturnAmount is increased and TotalAmount is decreased on returning opd cash invoice).
      elif cash == 0 and cashReturn == 0 and discountpc == 0 and credit == 0 and creditReturn > 0:
         time.sleep(3)
         print(syssubtotal)
         print(presyssubtotal)
         assert int(syssubtotal) == presyssubtotal
         print("sysreturnamount", sysreturnamount)
         print("presysreturnamount", presysreturnamount)
         print("creditReturn", creditReturn)
         assert int(sysreturnamount) == presysreturnamount + creditReturn
         assert int(systotalamount) == presystotalamount - creditReturn
         assert int(sysnetcashcollection) == presysnetcashcollection

      # 7. Credit Payment/Settlement
      elif credit > 0 and settlement == "CREDIT":
         assert int(sysnetcashcollection) == presysnetcashcollection + credit

      # 8. Provisional bill
      elif cash == 0 and credit == 0 and discountpc == 0 and cashReturn == 0 and provisional > 0:
         print("presysprovisionalitems:", presysprovisionalitems)
         print("provisional:", provisional)
         print(float(sysprovisionalitems))
         testvalu = presysprovisionalitems + provisional
         print(testvalu)
         #assert float(sysprovisionalitems) == presysprovisionalitems + provisional

      # 9. Cancel Provisional bill
      elif cash == 0 and credit == 0 and provisional == 0 and provisionalcancel > 0:
         print(presysprovisionalitems)

   #Module: OP Billing -----------------
   def opDeposit(self, amount):
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.ENTER)
         self.danpheEMR.find_element_by_link_text("Deposit").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//input[@name='amount']").send_keys(amount)
         self.danpheEMR.find_element_by_xpath("//input[@value='Add Deposit and Print']").click()
         time.sleep(3)
   def opDepositDbiling(self, deposit, testname):
         print("lets issue OPD invoice deducting amount from deposit.")
         self.danpheEMR.find_element_by_link_text("Billing").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Billing Request").click()
         self.danpheEMR.find_element_by_id("items-box0").click()
         self.danpheEMR.find_element_by_id("items-box0").send_keys(CBC)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
         itemAprice = self.danpheEMR.find_element_by_xpath("//input[@name='price']").get_attribute("value")
         SubTotal = itemAprice
         DepositBalance = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
         assert deposit == int(DepositBalance)
         BalanceAmount = self.danpheEMR.find_element_by_xpath("//td[2]/span").text
         assert deposit == int(BalanceAmount)
         TotalAmount = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]/input").get_attribute("value")
         print("TotalAmount", TotalAmount)
         assert TotalAmount == SubTotal
         Tender = self.danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
         print("Tender before deposit deduction: ", Tender)
         assert Tender == TotalAmount
         self.danpheEMR.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()  # Click on Deduct from Deposit
         Tender = self.danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
         print("Tender after deposit deduction: ", Tender)

         if int(DepositBalance) >= int(TotalAmount):
            assert Tender == "0"

         else:
            assert int(Tender) == int(TotalAmount) - int(DepositBalance)

         DepositDeduction = self.danpheEMR.find_element_by_xpath("//td/table/tbody/tr[2]/td[2]").text
         print("DepositDeduction:", DepositDeduction)

         if int(DepositBalance) < int(TotalAmount):
            assert DepositDeduction == DepositBalance

         else:
            assert DepositDeduction == TotalAmount

         NewDepositBalance = self.danpheEMR.find_element_by_xpath("//td/table/tbody/tr[3]/td[2]").text
         assert NewDepositBalance == str(int(DepositBalance) - int(DepositDeduction))
         print("NewDepositBalance:", NewDepositBalance)

         self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
         time.sleep(3)
   def opDepositDbilingTenderCashReturn(self, deposit, testname):
         global ChangeReturn
         print("lets issue OPD invoice deducting amount from deposit.")
         self.danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("quickFilterInput").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Billing Request").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").click()
         self.danpheEMR.find_element_by_id("items-box0").send_keys(testname)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
         itemAprice = self.danpheEMR.find_element_by_xpath("//input[@name='price']").get_attribute("value")
         SubTotal = itemAprice
         DepositBalance = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
         assert deposit == DepositBalance
         BalanceAmount = self.danpheEMR.find_element_by_xpath("//td[2]/span").text
         assert deposit == BalanceAmount
         TotalAmount = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]/input").get_attribute("value")
         print("TotalAmount", TotalAmount)
         assert TotalAmount == SubTotal
         print("subtotal", SubTotal)
         Tender = self.danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
         print("Tender before deposit deduction: ", Tender)
         assert Tender == TotalAmount

         self.danpheEMR.find_element_by_xpath("(//input[@type='checkbox'])[3]").click()  # Click on Deduct from Deposit

         Tender = self.danpheEMR.find_element_by_xpath("//input[@name='Tender']").get_attribute("value")
         print("Tender after deposit deduction: ", Tender)

         DepositDeduction = self.danpheEMR.find_element_by_xpath("//td/table/tbody/tr[2]/td[2]").text
         print("DepositDeduction", DepositDeduction)

         if int(DepositBalance) < int(TotalAmount):
            assert DepositDeduction == DepositBalance
            assert int(Tender) == int(TotalAmount) - int(DepositBalance)

         else:
            assert DepositDeduction == TotalAmount
            assert Tender == "0"

         NewDepositBalance = self.danpheEMR.find_element_by_xpath("//td/table/tbody/tr[3]/td[2]").text
         assert NewDepositBalance == str(int(DepositBalance) - int(DepositDeduction))
         print("NewDepositBalance", NewDepositBalance)

         if 300 < int(Tender) < 500:
            self.danpheEMR.find_element_by_xpath("//input[@name='Tender']").clear()
            self.danpheEMR.find_element_by_xpath("//input[@name='Tender']").send_keys(Tender)

         ChangeReturn = self.danpheEMR.find_element_by_xpath("//span/b").text
         ChangeReturn = int(ChangeReturn)
         assert ChangeReturn == int(Tender) + int(DepositBalance) - int(TotalAmount)

         self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
         time.sleep(7)
         # DepositDeductorReturn = self.danpheEMR.find_element_by_xpath("//div[10]/span").text
         DepositDeductorReturn = self.danpheEMR.find_element_by_xpath(
            "//span[contains(text(),'Deposit Deduct/Return:')]").text
         print("1:", DepositDeductorReturn)
         DepositDeductorReturn = DepositDeductorReturn.partition("n: ")[2]
         print("DepositDeductorReturn", DepositDeductorReturn)
         assert DepositDeductorReturn == DepositDeduction

         billTender = self.danpheEMR.find_element_by_xpath(
            "//div[@id='printpage']/div/div[5]/div[10]/span[2]").text  # Tender
         print("2:", billTender)
         billTender = billTender.partition("r: ")[2]
         billTender = billTender.partition(".")[0]
         Tender = int(TotalAmount) - int(DepositDeduction)
         assert int(Tender) == int(billTender)

         if ChangeReturn >= 1:
            eChangeReturn = self.danpheEMR.find_element_by_xpath(
               "//div[@id='printpage']/div/div[5]/div[10]/span[3]").text  # Change/Return
            print("3.1:", eChangeReturn)
            eChangeReturn = eChangeReturn.partition("n: ")[2]
            assert eChangeReturn == str(ChangeReturn)

            DepositBalance = self.danpheEMR.find_element_by_xpath(
               "//div[@id='printpage']/div/div[5]/div[10]/span[4]").text  # Deposit Balance
            print("3.2:", DepositBalance)
            DepositBalance = DepositBalance.partition("e: ")[2]
            assert DepositBalance == NewDepositBalance
   def createUSGinvoice(self, usgAbdomenPelvis):
      print(">>Create OPD Invoice: 1 Lab + 1 Xray Items: START")

      if appPort == "81":
         self.danpheEMR.find_element_by_link_text("Billing").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(contactno)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_link_text("Billing Request").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").click()
         self.danpheEMR.find_element_by_id("items-box0").send_keys(usgAbdomenPelvis)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
         time.sleep(2)
         price1 = self.danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
         totalprice = int(price1)
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Name' and @formcontrolname='ProviderId']").clear()
         self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Name' and @formcontrolname='ProviderId']").send_keys(doctor1)
         self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
         time.sleep(3)

      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Billing").click()
         self.danpheEMR.find_element_by_id("srch_PatientList").click()
         self.danpheEMR.find_element_by_id("srch_PatientList").send_keys(HospitalNo)
         self.danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.RETURN)
         time.sleep(3)
         self.danpheEMR.find_element_by_id("srch_PatientList").send_keys(Keys.TAB)
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[@id='btn_billRequest']").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").click()
         self.danpheEMR.find_element_by_id("items-box0").send_keys(usgLPH)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("items-box0").send_keys(Keys.TAB)
         time.sleep(2)
         price1 = self.danpheEMR.find_element_by_xpath("//input[@name='total']").get_attribute('value')
         totalprice = int(price1)
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//input[@value='Print INVOICE']").click()
         time.sleep(3)

      print("Create OPD Invoice: USG Items: END<<")

   #Module: IP Billing -----------------
   def createIPprovisionalBill(self, test):
      global testrate
      print(">>START: Cancel Admitted Provisional bill")
      self.danpheEMR.find_element_by_link_text("Billing").click()
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' New Item')]").click()
      self.danpheEMR.find_element_by_xpath("//input[@id='items-box0']").send_keys(test)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[5]").send_keys(doctor1)
      time.sleep(2)
      testrate = int(self.danpheEMR.find_element_by_xpath("//input[@name='price']").get_attribute("value"))
      print("testrate", testrate)
      self.danpheEMR.find_element_by_xpath("//input[@value='Request']").click()
      time.sleep(9)
      print("<<END")
   def cancelIPprovisionalBill(self, canceltest):
      print(">>START: Cancel IP Provisional bill")
      self.danpheEMR.find_element_by_link_text("Billing").click()
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(canceltest)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Edit").click()
      self.danpheEMR.find_element_by_xpath("//div/textarea").send_keys("Auto cancel of IP provisional bill items")
      time.sleep(9)
      self.danpheEMR.find_element_by_xpath("//div[3]/button[2]").click()
      time.sleep(3)
      assert self.danpheEMR.switch_to.alert.text == "This item will be cancelled. Are you sure you want to continue ?"
      time.sleep(3)
      self.danpheEMR.switch_to.alert.accept()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".fa-times").click()
   def getIPbillingDetails(self, paymentmode):
      global BillingTotal
      global NetTotal
      global ToBePaid
      global Tender
      Tender = 0
      global ChangeReturn
      ChangeReturn = 0
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(5)
      if paymentmode == "CREDIT":
         paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
         paymentoptions.select_by_visible_text("CREDIT")
      BillingTotal = self.danpheEMR.find_element_by_xpath("//td[contains(.,'Billing Total')]/following-sibling::td").text
      print("BillingTotal", BillingTotal)
      NetTotal = self.danpheEMR.find_element_by_xpath("//td[contains(.,'Net Total')]/following-sibling::td").text
      print("NetTotal", NetTotal)
      ToBePaid = self.danpheEMR.find_element_by_xpath("//td[contains(.,'To Be Paid')]/following-sibling::td").text
      print("ToBePaid", ToBePaid)
      if paymentmode != "CREDIT":
         Tender = self.danpheEMR.find_element_by_name("Tender").get_attribute("value")
         print("Tender1", Tender)
         ChangeReturn = self.danpheEMR.find_element_by_xpath("//td[contains(.,'Change/Return :')]/following-sibling::td").text
         print("ChangeReturn", ChangeReturn)
   def preIPbillingDetails(self):
      global xBillingTotal
      global xNetTotal
      global xToBePaid
      global xTender
      xTender = 0
      global xChangeReturn
      xChangeReturn = 0
      xBillingTotal = int(BillingTotal)
      xNetTotal = int(NetTotal)
      xToBePaid = int(ToBePaid)
      xTender = int(Tender)
      xChangeReturn = int(ChangeReturn)
   def verifyIPbillingDetails(self, testrate, canceltest, paymentmode):
      assert int(BillingTotal) == xBillingTotal + testrate - canceltest
      assert int(NetTotal) == xNetTotal + testrate - canceltest
      assert int(ToBePaid) == xToBePaid + testrate - canceltest
      if paymentmode != "CREDIT":
         assert int(Tender) == xTender + testrate - canceltest
         assert int(ChangeReturn) == xChangeReturn
   def modifyDischargeDate(self):
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//input[@name='day']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@name='day']").send_keys(Keys.ARROW_DOWN)
   def verifyConfirmDischarge(self, paymentmode):
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(3)
      if paymentmode == "CREDIT":
         paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
         paymentoptions.select_by_visible_text("CREDIT")
         self.danpheEMR.find_element_by_xpath("//textarea").send_keys("This is credit bill")
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
      time.sleep(3)
      if paymentmode == "CREDIT":
         assert self.danpheEMR.switch_to.alert.text == "Are you sure to discharge this patient on CREDIT?"
         time.sleep(3)
         self.danpheEMR.switch_to.alert.accept()
         time.sleep(3)
         self.danpheEMR.find_element_by_css_selector(".btn-danger").click()
         time.sleep(2)
      tobepaid = self.danpheEMR.find_element_by_xpath("(//td[text()='To Be Paid :']/following-sibling::td)[1]").text
      print("tobepaid", tobepaid)
      print("ToBePaid", ToBePaid)
      assert int(ToBePaid) == int(tobepaid)
      tender = self.danpheEMR.find_element_by_xpath("(//td[text()='Tender']/following-sibling::td)[1]").text
      assert int(Tender) == int(tender)
      change = self.danpheEMR.find_element_by_xpath("(//td[text()='Change']/following-sibling::td)[1]").text
      assert int(ChangeReturn) == int(change)
      self.danpheEMR.find_element_by_xpath("//textarea[@placeholder='Remarks']").send_keys("Patient discharge")
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[@type='button' and text()=' Discharge ']").click()
      time.sleep(7)
   def verifyDischargeInvoice(self, paymentmode):
      time.sleep(3)
      grosstotal = self.danpheEMR.find_element_by_xpath("//td/strong[text()='Gross Total']//parent::td//following-sibling::td").text
      grosstotal = grosstotal.partition(".")[0]
      grosstotal = grosstotal.replace(',', '')
      print("grosstotal", grosstotal)
      assert int(BillingTotal) == int(grosstotal)
      totalamount = self.danpheEMR.find_element_by_xpath("//td/strong[text()='Total Amount']//parent::td//following-sibling::td").text
      totalamount = totalamount.partition(".")[0]
      totalamount = totalamount.replace(',', '')
      print("totalamount", totalamount)
      assert int(NetTotal) == int(totalamount)
      depositedamount = self.danpheEMR.find_element_by_xpath("//td/strong[text()='Deposited Amount']//parent::td//following-sibling::td").text
      print("depositedamount", depositedamount)
      if paymentmode == "Cash":
         paidamount = self.danpheEMR.find_element_by_xpath("//td/strong[text()='Paid Amount ']//parent::td//following-sibling::td").text
         paidamount = paidamount.partition(".")[0]
         paidamount = paidamount.replace(',', '')
         print("paidamount", paidamount)
         assert int(ToBePaid) == int(paidamount)
         tender = self.danpheEMR.find_element_by_xpath("//td/strong[text()='Tender']//parent::td//following-sibling::td").text
         print("tender", tender)
         assert int(Tender) == int(tender)
      else:
         amounttobepaid = self.danpheEMR.find_element_by_xpath("//td/strong[text()='Amount to be Paid ']//parent::td//following-sibling::td").text
         amounttobepaid = amounttobepaid.partition(".")[0]
         amounttobepaid = amounttobepaid.replace(',', '')
         print("amounttobepaid", amounttobepaid)
         assert int(amounttobepaid) == int(ToBePaid)
      element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
      time.sleep(2)
      self.danpheEMR.execute_script("arguments[0].click();", element)
   def creditSettlements(self):
      self.danpheEMR.find_element_by_link_text("Billing").click()
      self.danpheEMR.find_element_by_link_text("Settlements").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Show Details')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@value='Proceed']").click()
   def generateDischargeInvoice(self, paymentmode):
      global InvoiceNo
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(7)
      if paymentmode == "CREDIT":
         paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select[@class='form-control ng-untouched ng-pristine ng-valid']"))
         paymentoptions.select_by_visible_text("CREDIT")
         self.danpheEMR.find_element_by_xpath("//textarea").send_keys("This is credit bill")
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
      if paymentmode == "CREDIT":
         time.sleep(4)
         assert self.danpheEMR.switch_to.alert.text == "Are you sure to discharge this patient on CREDIT?"
         time.sleep(3)
         self.danpheEMR.switch_to.alert.accept()
         time.sleep(2)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//textarea[@placeholder='Remarks']").send_keys("Patient discharge")
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[@type='button' and text()=' Discharge ']").click()
      time.sleep(7)
      InvoiceNo = self.danpheEMR.find_element_by_xpath("//td[contains(text(),' Invoice No:')]").text
      InvoiceNo = InvoiceNo.partition("- ")[2]
      print("InvoiceNo", InvoiceNo)
      time.sleep(2)
      element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
      time.sleep(2)
      self.danpheEMR.execute_script("arguments[0].click();", element)

   #Module: Pharmacy ------------------
   def activatePharmacyCounter(self):
      print(">>Pharmacy Counter Activate: START")
      time.sleep(7)

      if appPort == "81":
         self.danpheEMR.find_element_by_link_text("Pharmacy").click()
         time.sleep(3)
      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Dispensary").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//i[contains(text(),'MainDispensary')]").click()
         time.sleep(3)

      self.danpheEMR.find_element_by_link_text("Counter").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//h5").click()
      time.sleep(2)
      print("Pharmacy Counter Activate: END")
   def addPharmacyItem(self):  # incomplete
      print(">>START: Start add new drug")
      global DrugName
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Setting").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Item").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success']").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys("Pharmay Unit")
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.setSelectionRange(0, this.value.length)']").send_keys(Keys.TAB)
      drugMGtemp = random.randint(10, 1000)
      drugMG = str(drugMGtemp)
      DrugName = ('Autodrug' + drugMG)
      print(DrugName)
      self.danpheEMR.find_element_by_xpath("//input[@value='']").send_keys(DrugName)
      time.sleep(3)
      #self.danpheEMR.find_element_by_css_selector("//select").click()
      self.danpheEMR.find_element_by_xpath("//div[4]/div/div/div/input").send_keys("DEURALI JANTA")
      self.danpheEMR.find_element_by_xpath("//div[4]/div/div/div/input").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//div[5]/div/div/div/input").send_keys("ABGEL")#itemType
      self.danpheEMR.find_element_by_xpath("//div[5]/div/div/div/input").send_keys(Keys.TAB)#itemType
      #self.danpheEMR.find_element_by_css_selector(".ng-touched:nth-child(1)").send_keys("ABGEL")
      self.danpheEMR.find_element_by_xpath("//div[6]/div/div/div/input").send_keys("1 Tablet")#unit
      self.danpheEMR.find_element_by_xpath("//div[6]/div/div/div/input").send_keys(Keys.TAB)#unit
      self.danpheEMR.find_element_by_xpath("//div[7]/div/div/div/input").send_keys("ABGEL")#genericName
      self.danpheEMR.find_element_by_xpath("//div[7]/div/div/div/input").send_keys(Keys.TAB)#genericName
      time.sleep(3)
      self.danpheEMR.find_element_by_id("save").click()

      time.sleep(3)
   def verifyPharmacyItem(self):
       self.danpheEMR.find_element_by_link_text("Pharmacy").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_link_text("Setting").click()
       time.sleep(5)
       self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
       time.sleep(9)
       assert DrugName == self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div").text
   def getStoreDetail(self, drugname):
      global drugqtyMS
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Store").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
      time.sleep(3)
      drugnameMS = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
      print("drugnameMS:", drugnameMS)
      assert drugnameMS == drugname
      sysdrugqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQty'])[2]").text
      drugqtyMS = int(sysdrugqty)
      print("drugqtyMS:", drugqtyMS)
   def getStockDetail(self, drugname):
      global drugqtySS
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
      time.sleep(3)
      drugnameSS = self.danpheEMR.find_element_by_xpath("(//div[@col-id='ItemName'])[2]").text
      print("drugnameSS:", drugnameSS)
      sysdrugqty = self.danpheEMR.find_element_by_xpath("(//div[@col-id='AvailableQuantity'])[2]").text
      drugqtySS = int(sysdrugqty)
      print("drugqtySS:", drugqtySS)
   def verifyStoreDetail(self, drugname):
      self.danpheEMR.find_element_by_link_text("Store").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").clear()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
      time.sleep(2)
      sysdrugname = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[2]").text
      print("sysdrugname:", sysdrugname)
      assert drugname == sysdrugname
      sysdrugqty = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      print("sysdrugqty", sysdrugqty)
      print("newdrugqtyMS", drugqtyMScalc)
      assert int(drugqtyMScalc) == int(sysdrugqty)
   def verifyStockDetail(self, drugname):
      self.danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(drugname)
      time.sleep(2)
      sysdrugname = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div").text
      print("sysdrugname", sysdrugname)
      assert drugname == sysdrugname
      sysdrugqty = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      print("drugqtySS:", drugqtySS)
      print("sysdrugqty", sysdrugqty)
      assert int(drugqtySS) == int(sysdrugqty)
   def verifyStockDetailTC(self):
      self.danpheEMR.find_element_by_link_text("Stock").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(DrugName)
      time.sleep(2)
      sysdrugqty = self.danpheEMR.find_element_by_xpath(
         "//ag-grid-angular[@id='myGrid']/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      assert sysdrugqty == '0'
   def transferStore2Dispensary(self, drugname, tqty):
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
   def transferStore2DispensaryTC(self, tqty):
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
   def transferDispensary2Store(self, drugname, tqty):
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
      #self.danpheEMR.find_element_by_link_text("Store").click()
   def transferDispensary2StoreTC(self, tqty):
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
      if appPort == '81':
         self.danpheEMR.find_element_by_link_text("Pharmacy").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sale ')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("item-box0").click()
         self.danpheEMR.find_element_by_id("item-box0").clear()
         self.danpheEMR.find_element_by_id("item-box0").send_keys(drugname)
         self.danpheEMR.find_element_by_id("item-box0").send_keys(Keys.TAB)
         time.sleep(5)
         self.danpheEMR.find_element_by_id("qty-box0").click()
         self.danpheEMR.find_element_by_id("qty-box0").clear()
         self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
         time.sleep(3)
         if paymentmode == 'CREDIT':
            paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
            paymentoptions.select_by_visible_text("CREDIT")
            time.sleep(2)
            self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
         self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
         time.sleep(5)
         pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
         pInvoiceNo = pInvoiceNo.partition("PH")[2]
         self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
      if appPort == '82':
         self.danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sale ')]").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("patient-search").click()
         self.danpheEMR.find_element_by_id("patient-search").send_keys('test')
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

      if appPort == "81":
         self.danpheEMR.find_element_by_id("qty-box0").click()
         self.danpheEMR.find_element_by_id("qty-box0").clear()
         self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
         if paymentmode == 'Credit':
            paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
            paymentoptions.select_by_visible_text("CREDIT")
            time.sleep(2)
            self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
         self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()

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
      pInvoiceNo = pInvoiceNo.partition("PH")[2]
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
      if appPort == "81":
         self.danpheEMR.find_element_by_id("qty-box0").click()
         self.danpheEMR.find_element_by_id("qty-box0").clear()
         self.danpheEMR.find_element_by_id("qty-box0").send_keys(qty)
         if paymentmode == 'Credit':
            paymentoptions = Select(self.danpheEMR.find_element_by_xpath("//select"))
            paymentoptions.select_by_visible_text("CREDIT")
            time.sleep(2)
            self.danpheEMR.find_element_by_xpath("//input[@name='Remarks']").send_keys("This is credit bill")
         self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()

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
      #self.danpheEMR.find_element_by_css_selector(".page-content").click()
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
   def verifyPharmacyInvoice3(self,drugname, qty, rate):
      time.sleep(7)
      print(">>Verify Pharmacy Invoice: START")
      #assert drugname == self.danpheEMR.find_element_by_xpath("//tr[2]/td[2]").text
      #assert str(qty) == self.danpheEMR.find_element_by_xpath("//tr[2]/td[3]").text
      #tAmount = qty * rate
      #totalamount = self.danpheEMR.find_element_by_xpath("//div[2]/table/tbody/tr[2]/td[2]").text
      #totalamount = totalamount.partition("Rs. ")[2]
      #totalamount = totalamount.partition(".00")[0]
      #assert tAmount == int(totalamount)
      #print("Verify Pharmacy Invoice: END<<", "Pharmacy Invoice No: ", pInvoiceNo)
      #self.danpheEMR.find_element_by_xpath("//button[@class='btn green btn-success']").click()
      self.danpheEMR.find_element_by_xpath("//i[@class='fa fa-close']").click()
   def returnPharmacyInvoice(self, qty, returnremark):
      print(">>Return Pharmacy Invoice: START")
      if appPort == '81':
         self.danpheEMR.find_element_by_link_text("Pharmacy").click()
         self.danpheEMR.find_element_by_link_text("Sale").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Return From Customer").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("invoiceId").send_keys(pInvoiceNo)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.TAB)
         time.sleep(3)
         self.danpheEMR.find_element_by_id("invoiceId").send_keys(Keys.ENTER)
         time.sleep(2)
         # self.danpheEMR.find_element_by_xpath("//button[@value='Search Invoice']").click()
         # self.danpheEMR.find_element_by_xpath("//button[@value='Search Invoice']").click()
         time.sleep(3)
         # self.danpheEMR.find_element_by_xpath("//input[@type='checkbox']").click()
         self.danpheEMR.find_element_by_css_selector("th > input").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='ReturnedQty']").clear()
         self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='ReturnedQty']").send_keys(qty)
         self.danpheEMR.find_element_by_xpath("//textarea[@name='Remark']").send_keys(returnremark)
         self.danpheEMR.find_element_by_xpath("//input[@value='Return']").click()
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger']").click()
         time.sleep(5)
      if appPort == '82':
         self.danpheEMR.find_element_by_xpath("//span[contains(.,'Dispensary')]").click()
         time.sleep(3)
         #self.danpheEMR.find_element_by_xpath("//i[contains(.,'MainDispensary')]").click()
         #time.sleep(2)
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
         #self.danpheEMR.find_element_by_css_selector("th > input").click()
         #time.sleep(3)
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
      self.danpheEMR.find_element_by_link_text("Return Sale List").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Print").click()
      time.sleep(3)
      syspaymentmode = self.danpheEMR.find_element_by_xpath("//p[contains(text(),'Method of payment: ')]").text
      print("syspaymentmode:", syspaymentmode)
      syspaymentmode = syspaymentmode.partition("t: ")[2]
      #print("syspaymentmode1:", syspaymentmode)
      assert syspaymentmode == "Cash" # as per the comment on bug:EMR-2699 payment mode need to be cash on credit note.
      ReturnremarkTemp = self.danpheEMR.find_element_by_xpath("//div[@id='pharma-pat-info']/div[12]").text
      print("ReturnremarkTemp", ReturnremarkTemp)
      ReturnremarkTemp = ReturnremarkTemp.partition("s : ")[2]
      print("ReturnremarkTemp", ReturnremarkTemp)
      assert ReturnremarkTemp == returnRemark
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
      #self.danpheEMR.find_element_by_css_selector(".fa-close").click()
      print(">>Verify Return Pharmacy Invoice: END")
   def addPharmacyDeposit(self, deposit):
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
   def createPharmacyGoodsReceipt(self, qty):
      global goodsReceiptNo
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Order").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Goods Receipt").click()
      time.sleep(7)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys("Aayush surgichem")
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Select Supplier']").send_keys(Keys.TAB)
      gRNo = random.randint(1, 9999)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Invoice No']").send_keys(gRNo)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(DrugName)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.RETURN)
      self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(qty)
      self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
      self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.TAB)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
      self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
      self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
      self.danpheEMR.find_element_by_xpath("//input[@type='month']").send_keys(Keys.ARROW_UP)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@name='ReceivedQty']").clear()
      self.danpheEMR.find_element_by_xpath("//input[@name='ReceivedQty']").send_keys(100)
      self.danpheEMR.find_element_by_xpath("//input[@name='ReceivedQty']").send_keys(Keys.TAB)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@name='GRItemPrice']").clear()
      self.danpheEMR.find_element_by_xpath("//input[@name='GRItemPrice']").send_keys(270)
      self.danpheEMR.find_element_by_xpath("//input[@name='GRItemPrice']").send_keys(Keys.TAB)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@name='MRP']").clear()
      self.danpheEMR.find_element_by_xpath("//input[@name='MRP']").send_keys(285)
      self.danpheEMR.find_element_by_xpath("//input[@name='MRP']").send_keys(Keys.TAB)
      time.sleep(2)
      #self.danpheEMR.find_element_by_xpath("//select[contains(.,'Main Store')]").send_keys("Main Store") Temporary disable due to issue.
      self.danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
      time.sleep(3)
      goodsReceiptNo = self.danpheEMR.find_element_by_xpath("(//div[@col-id='GoodReceiptPrintId'])[2]").text
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
      global SubTotal
      global DiscountTotal
      global TotalAmount
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Order").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Goods Receipt List").click()
      time.sleep(2)
      SubTotal = self.danpheEMR.find_element_by_xpath(
      "//b[contains(text(),'Sub Total :')]/parent::td/following-sibling::td[1]").text
      print("SubTotal", SubTotal)
      DiscountTotal = self.danpheEMR.find_element_by_xpath(
         "//b[contains(text(),'Discount Total :')]/parent::td/following-sibling::td[1]").text
      print("DiscountTotal", DiscountTotal)
      TotalAmount = self.danpheEMR.find_element_by_xpath(
      "//b[contains(text(),'Total Amount :')]/parent::td/following-sibling::td").text
      print("TotalAmount", TotalAmount)
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
   def verifyPharmacyGoodsReceipt(self, qty):
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      self.danpheEMR.find_element_by_link_text("Order").click()
      self.danpheEMR.find_element_by_link_text("Goods Receipt List").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("View").click()
      time.sleep(3)
      sysdrugname = self.danpheEMR.find_element_by_xpath("//td[2]/b").text
      #print("hari", sysdrugname)
      assert sysdrugname == DrugName
      self.danpheEMR.find_element_by_css_selector(".fa-times").click()
   def closePopupApplication(self, saleinvoice):
      time.sleep(7)
      self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger history-del-btn']").click()
      time.sleep(3)

   #Pharmacy Reports: User Collection Report*********
   def getPharmacyDashboard(self):
      global TotalSale
      #global TotalReturn
      global CreditReturn
      global CashReturn
      global NetCashCollection
      global DepositAmount
      global DepositReturned
      global ProvisionalItems
      global UnpaidInvoices
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
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
      CreditReturn = self.danpheEMR.find_element_by_xpath("//h4[contains(text(),'Credit Return')]/following-sibling::b").text
      print("CreditReturn", CreditReturn)
      CreditReturn = CreditReturn.partition(": ")[2]
      CreditReturn = float(CreditReturn)
      print("CreditReturn", CreditReturn)
      NetCashCollection = self.danpheEMR.find_element_by_xpath("//h4[contains(text(),'Net Cash Collection')]/following-sibling::b").text
      print("NetCashCollection", NetCashCollection)
      NetCashCollection = NetCashCollection.partition(": ")[2]
      NetCashCollection = float(NetCashCollection)
      print("NetCashCollection", NetCashCollection)
      DepositAmount = self.danpheEMR.find_element_by_xpath("//h4[contains(text(),'Deposit Amount')]/following-sibling::b").text
      print("Deposit Amount", DepositAmount)
      DepositAmount = DepositAmount.partition(": ")[2]
      DepositAmount = float(DepositAmount)
      print("DepositAmount", DepositAmount)
      DepositReturned = self.danpheEMR.find_element_by_xpath("//h4[contains(text(),'Deposit Returned')]/following-sibling::b").text
      print("Deposit Returned", DepositReturned)
      DepositReturned = DepositReturned.partition(": ")[2]
      DepositReturned = float(DepositReturned)
      print("DepositReturned", DepositReturned)
      ProvisionalItems = self.danpheEMR.find_element_by_xpath("//td[contains(text(),'PROVISIONAL ITEMS')]/following-sibling::td").text
      print("PROVISIONAL ITEMS", ProvisionalItems)
      ProvisionalItems = ProvisionalItems.partition("Rs.")[2]
      ProvisionalItems = float(ProvisionalItems)
      print("ProvisionalItems", ProvisionalItems)
      UnpaidInvoices = self.danpheEMR.find_element_by_xpath("//td[contains(text(),'UNPAID INVOICES')]/following-sibling::td").text
      print("UNPAID INVOICES", UnpaidInvoices)
      UnpaidInvoices = UnpaidInvoices.partition("Rs.")[2]
      UnpaidInvoices = float(UnpaidInvoices)
      print("UnpaidInvoices", UnpaidInvoices)
   def preSystemPharmacyDashboard(self):
      global xTotalSale
      #global xTotalReturn
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
   def verifyPharmacyDashboard(self, cash, cashreturn, credit, creditreturn, deposit, depositreturn, provisional, provisionacancel):
      temp = round(xTotalSale + cash + credit)
      print("temp", temp)
      print("temp", float(temp))
      print("TotalSale", TotalSale)
      assert float(round(TotalSale)) == float(round(xTotalSale + cash + credit))
      print("TotalReturn-cash", CashReturn)
      print("xCashReturn", xCashReturn)
      #a = float(round(xTotalReturn + cashreturn + creditreturn))
      a = float(round(xCashReturn + cashreturn))
      b = float(round(xCreditReturn + creditreturn))
      assert CashReturn == a
      assert CreditReturn == b
      netcoltemp = float(round(xNetCashCollection + cash - cashreturn))
      print("netcollectiontemp", netcoltemp)
      print("xNetCollection", xNetCashCollection)
      assert float(round(NetCashCollection)) == float(round(xNetCashCollection + cash - cashreturn))
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
      self.danpheEMR.find_element_by_link_text("Pharmacy").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Report").click()
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
      time.sleep(2)
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
   def verifySystemPharmacyUserCollectionReport(self, cash, cashreturn, credit, creditreturn, creditsettlement, discount, deposit, depositreturn, provisional, provisionalcancel):
      print(">>START: verifySystemPharmacyUserCollectionReport")
      global sysPgrosstotalsales
      print("cash", cash)
      print("cashreturn", cashreturn)
      print("presysPnetcashcollection", presysPnetcashcollection)
      print("sysPnetcashcollection", sysPnetcashcollection)
      newCashCollection = presysPnetcashcollection + cash - cashreturn
      print("newCashCollection", newCashCollection)
      #assert round(float(sysPnetcashcollection)) == round(float(newCashCollection))
      assert int(sysPnetcashcollection) == int(round(newCashCollection))
      result = str(float(presysPgrosstotalsales) + cash + credit)
      print("result", result)
      print("sysPgrosstotalsales", sysPgrosstotalsales)
      print("presysPgrosstotalsales", presysPgrosstotalsales)
      #sysPgrosstotalsales = sysPgrosstotalsales.partition(".")[0]
      #result = result.partition(".")[0]
      #print("result", result)
      print("sysPgrosstotalsales", sysPgrosstotalsales)
      assert sysPgrosstotalsales == result
      assert float(sysPdiscount) == presysPdiscount + discount
      print("sysPreturnsubtotal", sysPreturnsubtotal)
      print("presysPreturnsubtotal", presysPreturnsubtotal)
      assert round(float(sysPreturnsubtotal)) == round(float(presysPreturnsubtotal + cashreturn + creditreturn))
      assert float(sysPreturndiscount) == presysPreturndiscount + discount
      assert round(float(sysPreturnamount)) == round(float(presysPreturnamount + cashreturn + creditreturn + discount))
      print("presysPnetsales", presysPnetsales)
      print("sysPnetsales", sysPnetsales)
      assert round(float(sysPnetsales)) == round(float(presysPnetsales + cash + credit - cashreturn - creditreturn - discount))
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
      assert float(sysPtotalcollection) == round(result2)

   # Module: Dispensary ------------------
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
      self.danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("(//a[contains(text(),'Sale') and @class='grid-action'])[2]").click()
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
      self.danpheEMR.find_element_by_xpath("//input[@value='Print Invoice']").click()
      time.sleep(5)
      pInvoiceNo = self.danpheEMR.find_element_by_xpath("//div[4]/div/div/p").text
      pInvoiceNo = pInvoiceNo.partition("PH")[2]
      print("END>> Create Pharmacy OPD Invoice.", pInvoiceNo)

#------------------- Module: Laboratory -------------------------
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
      assert  depositbalance == sysdepositamt + deposit - depositreturn
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
      ManageQuantity = self.danpheEMR.find_element_by_xpath("(//div[@col-id='Quantity'])[2]").text #There is open bug (EMR-2588) to list down latest manage record to top.
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

#Module: Laboratory****************************
   def collectLabSample(self, testname):
      global barcodeno
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)

      if appPort == "81":
         self.danpheEMR.find_element_by_link_text("Lab Requisition").click()
      if appPort == "82":
         self.danpheEMR.find_element_by_xpath("//a[contains(text(),' Sample Collection ')]").click()

      self.danpheEMR.find_element_by_id("quickFilterInput").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(9)
      sampleno = self.danpheEMR.find_element_by_name("Sample number").get_attribute("value")
      print(sampleno)
      samplecode = self.danpheEMR.find_element_by_name("Sample Code").get_attribute("value")
      print(samplecode)
      time.sleep(9)
      self.danpheEMR.find_element_by_css_selector(".btn").click()
      time.sleep(9)
      barcodeno = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(2) td:nth-child(3)").text
      print(barcodeno)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Close')]").click()

   def addLabResult(self):
      print("Starting>Adding Lab Report")

      if appPort == "81":
         self.danpheEMR.find_element_by_link_text("Laboratory").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_link_text("Add Results").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(barcodeno)
         time.sleep(2)
         # self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Add Result").click()
         time.sleep(7)
         # ---------------this is hardcoded for TFT test-----------
         self.danpheEMR.find_element_by_id("inputbox000").send_keys("2.23")
         self.danpheEMR.find_element_by_id("inputbox001").send_keys("15.0")
         self.danpheEMR.find_element_by_id("inputbox002").send_keys("4.05")
         time.sleep(7)
         self.danpheEMR.find_element_by_xpath("//div[3]/button").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Proceed')]").click()  # proceed for abnormal result

         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Update Signatories and Print ')]").click()
         self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Back To Grid ')]").click()

      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Laboratory").click()
         time.sleep(1)
         self.danpheEMR.find_element_by_link_text("Add Results").click()
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(barcodeno)
         time.sleep(2)
         # self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(Keys.RETURN)
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("Add Result").click()
         time.sleep(7)
         # ---------------this is hardcoded for TFT test-----------
         self.danpheEMR.find_element_by_id("inputbox000").send_keys("2.23")
         self.danpheEMR.find_element_by_id("inputbox001").send_keys("15.0")
         self.danpheEMR.find_element_by_id("inputbox002").send_keys("4.05")
         time.sleep(7)
         self.danpheEMR.find_element_by_xpath("//div[3]/button").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Proceed')]").click()  # proced for abnormal result

         time.sleep(3)
         self.danpheEMR.find_element_by_css_selector(".c-btn > .fa").click()
         self.danpheEMR.find_element_by_css_selector(".pure-checkbox:nth-child(2) > label").click()
         self.danpheEMR.find_element_by_css_selector(".ng-untouched .row:nth-child(1)").click()
         self.danpheEMR.find_element_by_css_selector(".margin-7-hr").click()

         time.sleep(2)
         #self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Edit Signatories')]/preceding-sibling::button").click()
         #self.danpheEMR.find_element_by_xpath("//button[contains(text(),' Back To Grid ')]").click()
         # self.danpheEMR.find_element_by_id("close print window").click()   # failed with bug ID:
         # self.danpheEMR.find_element_by_xpath("//div[3]/div/div/button").click()
         # self.danpheEMR.close()
         # self.danpheEMR.find_element_by_xpath("//button[contains(.,' Back To Grid')]").click()

   def verifyLabReport(self):
      self.danpheEMR.find_element_by_link_text("PendingReports").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Verify ')]").click()

   def printLabReport(self, t3, t4, tsh):
      self.danpheEMR.find_element_by_link_text("Laboratory").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Final Reports").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(7)
      #isprinted = self.danpheEMR.find_element_by_css_selector("span > b").text
      #print(isprinted)
      #assert isprinted == "NO"
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(2)
      assert t3 == self.danpheEMR.find_element_by_xpath("//td[2]/span").text
      print(t3)
      assert t4 == self.danpheEMR.find_element_by_xpath("//tr[3]/td[2]/span").text
      print(t4)
      assert tsh == self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]/span").text
      print(tsh)

#Module: Patient Registration -----------------
   def patientRegistration(self):
      global contactno
      global HospitalNo
      global FullName
      self.danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Register Patient").click()
      time.sleep(2)

      #fname = "auto "
      #z = "preg"
      #sname1 = z+sname
      #print("Sir name", sname1)
      #FullName = fname + sname1
      #print("Full name of patient:", FullName)

      age = random.randint(1, 99)
      self.danpheEMR.find_element_by_xpath("//input[@type='number']").send_keys(age)
      contactno = random.randint(9811111111, 9899999999)
      self.danpheEMR.find_element_by_xpath("//input[@type='tel']").send_keys(contactno)
      print(contactno)

      if appPort == "81":
         self.danpheEMR.find_element_by_css_selector(".col-md-6:nth-child(2) > .form-group:nth-child(1) .mt-checkbox:nth-child(1) > span").click()
      if appPort == "82":
         self.danpheEMR.find_element_by_link_text("Register Patient").click()
         self.danpheEMR.find_element_by_id("regPatFirstName").send_keys("auto")
         sname = str(random.randint(1111, 9999))
         self.danpheEMR.find_element_by_xpath("(//input[@value=''])[3]").send_keys("preg", sname)
         gender = Select(self.danpheEMR.find_element_by_xpath("//select[@formcontrolname='Gender']"))
         gender.select_by_visible_text("Female")

      self.danpheEMR.find_element_by_xpath("//input[@value='Register Patient']").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(contactno)
      time.sleep(2)
      assert str(contactno) == self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                                    "/div/div/div/div[3]/div[2]/div/div/div/div[5]").text
      global HospitalNo
      HospitalNo = self.danpheEMR.find_element_by_xpath("//ag-grid-angular[@id='myGrid']"
                                                        "/div/div/div/div[3]/div[2]/div/div/div/div").text
      print(HospitalNo)
   def getRandomPatient(self):
      self.danpheEMR.find_element_by_link_text("Patient").click()
      time.sleep(5)
      global HospitalNo
      HospitalNo = self.danpheEMR.find_element_by_xpath("(//div[@col-id='PatientCode'])[2]").text

#Module: ADT -----------------------------
   def admitDisTrans(self, admit, discharge, trasfer, deposit):
      if admit == 1:
         time.sleep(5)
         self.danpheEMR.find_element_by_link_text("ADT").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Admit").click()
         time.sleep(3)
         self.danpheEMR.find_element_by_id("RequestingDeptId").send_keys("GENERAL MEDICINE")
         self.danpheEMR.find_element_by_id("RequestingDeptId").send_keys(Keys.RETURN)
         #self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys("Dr. Dr Dr")
         self.danpheEMR.find_element_by_xpath("(//input[@onclick='this.select();'])[2]").send_keys(Keys.TAB)
         time.sleep(3)
         #self.danpheEMR.find_element_by_css_selector(".col-md-6:nth-child(2) > .ng-dirty").click()
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_xpath("//select").send_keys(Keys.RETURN)
         time.sleep(3)
         #self.danpheEMR.find_element_by_xpath("//div[3]/div/select").send_keys(Keys.RETURN)
         #self.danpheEMR.find_element_by_xpath("//div[3]/div/select").send_keys(Keys.ARROW_DOWN)
         #self.danpheEMR.find_element_by_xpath("//div[3]/div/select").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.RETURN)
         time.sleep(1)
         self.danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.ARROW_DOWN)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("BedFeatureId").send_keys(Keys.RETURN)
         time.sleep(2)
         self.danpheEMR.find_element_by_id("BedId").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_id("BedId").send_keys(Keys.ARROW_DOWN)
         self.danpheEMR.find_element_by_id("BedId").send_keys(Keys.RETURN)
         self.danpheEMR.find_element_by_xpath("//input[@name='amount']").send_keys(deposit)
         time.sleep(3)
         caseDropdownValue = self.danpheEMR.find_element_by_id("admissionCase")
         caseDropdownValue.find_element_by_xpath("//option[. = 'General']").click()
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Save Admission')]").click()
         print("Patient successfully admitted.")
         time.sleep(5)
         self.danpheEMR.find_element_by_xpath("(//a[@class='btn btn-danger history-del-btn'])[1]").click()
         #self.danpheEMR.find_element_by_css_selector(".col-md-6 > .modelbox-div > .btn").click()
         time.sleep(2)
      elif discharge == 1:
         time.sleep(3)
         self.danpheEMR.find_element_by_link_text("Billing").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("IPBilling").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_link_text("View Details").click()
         time.sleep(2)
         self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
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
         self.danpheEMR.find_element_by_xpath("//textarea[@name='Remarks']").send_keys("Transfer to ICU ward")
         self.danpheEMR.find_element_by_xpath("//input[@name='name']").click()

   def billingIP(self, deposit):
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      time.sleep(1)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(9)
      billingTotalExp = "500"
      billingTotalAct = self.danpheEMR.find_element_by_xpath("//td[2]/label").text
      print(billingTotalAct)
      totalDiscountExp = "0"
      totalDiscountAct = self.danpheEMR.find_element_by_xpath("//input[@type='number']").get_attribute("value")
      print(totalDiscountAct)
      assert totalDiscountExp == totalDiscountAct
      netTotalExp = int(billingTotalExp) - int(totalDiscountExp)
      netTotalAct = self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]/label").text
      print(netTotalAct)
      depositBalanceExp = int(deposit)
      depositBalanceAct = self.danpheEMR.find_element_by_xpath("//tr[6]/td[2]/label").text
      print(depositBalanceAct)
      print(depositBalanceExp)
      assert depositBalanceExp == int(depositBalanceAct)
      if depositBalanceExp > netTotalExp:
         toBeRefundExp = depositBalanceExp - netTotalExp
         toBeRefundAct = self.danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
         print("To be refund:", toBeRefundAct)
      elif depositBalanceExp < netTotalExp:
         toBePaidExp = netTotalExp - depositBalanceExp
         toBePaidAct = self.danpheEMR.find_element_by_css_selector("tr:nth-child(7) label").text
         print("To be paid:", toBePaidAct)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
      self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
      time.sleep(10)
      element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
      time.sleep(2)
      self.danpheEMR.execute_script("arguments[0].click();", element)
      time.sleep(5)

   def cancelDischarge(self):
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
      self.danpheEMR.find_element_by_link_text("Billing").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("IPBilling").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("View Details").click()
      time.sleep(9)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Confirm Discharge')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//div[3]/textarea").send_keys("Patient discharging")
      self.danpheEMR.find_element_by_xpath("(//button[@type='button'])[5]").click()
      time.sleep(10)
      element = self.danpheEMR.find_element_by_xpath("//a[@class='btn btn-danger del-btn']")
      time.sleep(2)
      self.danpheEMR.execute_script("arguments[0].click();", element)
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


#Module: Radiology ***************************
   def doRadioScan(self):
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Radiology").click()
      self.danpheEMR.find_element_by_link_text("List Requests").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Scan Done").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Done')]").click()

   def generateUSGReport(self, testname):
      print(">>START: Generate Radiology Report")
      time.sleep(3)
      #self.vars = {}
      self.danpheEMR.find_element_by_link_text("Radiology").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Add Report')]").click()
      time.sleep(2)
      #self.danpheEMR.find_element_by_xpath("//button[contains(text(),'Collect Sample')]").click()
      time.sleep(2)


   def getTotalItemsBill(self):
      print(">>START: getTotalItemsBill")
      global sysreturnQty
      global sysreturnSubtotal
      global sysreturnQtyDiscount
      global sysreturnTotalamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Total Items Bill')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysreturnQty = self.danpheEMR.find_element_by_xpath('//tr[4]/td[2]').text
      print(sysreturnQty)
      sysreturnSubtotal = self.danpheEMR.find_element_by_xpath('//tr[4]/td[3]').text
      print(sysreturnSubtotal)
      sysreturnQtyDiscount = self.danpheEMR.find_element_by_xpath('//tr[4]/td[4]').text
      print(sysreturnQtyDiscount)
      sysreturnTotalamount = self.danpheEMR.find_element_by_xpath('//tr[4]/td[5]').text
      print(sysreturnTotalamount)
      print("<<END: getTotalItemsBill")

   def preSystemTotalItemsBill(self):
      print(">>START: preSystemTotalItemsBill")
      global presysreturnQty
      global presysreturnSubtotal
      global presysreturnQtyDiscount
      global presysreturnTotalamount
      presysreturnQty = int(sysreturnQty)
      print(presysreturnQty)
      presysreturnSubtotal = int(sysreturnSubtotal)
      print(presysreturnSubtotal)
      presysreturnQtyDiscount = int(sysreturnQtyDiscount)
      print(presysreturnQtyDiscount)
      presysreturnTotalamount = int(sysreturnTotalamount)
      print(presysreturnTotalamount)
      print("<<END: preSystemTotalItemsBill")

   def verifyTotalItemsBill(self, returnamt, discountamt):
      print(">>START: verifyTotalItemsBill")
      if returnamt > 0:
         assert int(sysreturnQty) == (presysreturnQty + 1)
         assert int(sysreturnSubtotal) == (presysreturnSubtotal + returnamt)
         assert  int(sysreturnQtyDiscount) == (presysreturnQtyDiscount + discountamt)
         assert  int(sysreturnTotalamount) == (presysreturnTotalamount + returnamt)

#Module: Report: SalesDayBook******************
   def getSalesDayBook(self):
      print(">>START: getSalesDayBook")
      global syssales
      #global returnamount
      global sysgrosssales
      global syscreditsalestotal
      #global creditcancel
      global sysnetsalesamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Sales DayBook')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      syssales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td").text
      print(syssales)
      sysgrosssales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td[7]").text
      print(sysgrosssales)
      syscreditsalestotal = self.danpheEMR.find_element_by_xpath("//tr[2]/td[3]").text
      print(syscreditsalestotal)
      sysnetsalesamount = self.danpheEMR.find_element_by_xpath("//tr[2]/td[7]").text
      print(sysnetsalesamount)
      print("<<END: getSalesDayBook")

   def preSystemSalesDayBook(self):
      print(">>START: preSystemSalesDayBook")
      global presyssales
      #global returnamount
      global presysgrosssales
      global presyscreditsalestotal
      #global presyscreditcancel
      global presysnetsalesamount
      presyssales = int(syssales)
      presysgrosssales = int(sysgrosssales)
      presyscreditsalestotal = int(syscreditsalestotal)
      presysnetsalesamount = int(sysnetsalesamount)
      print("<<END: preSystemSalesDayBook")

   def verifySalesDayBook(self, cash, credit, cashreturn, creditreturn):
      print(">>START: verifySalesDayBook")
      assert int(syssales) == presyssales + cash + credit - cashreturn - creditreturn
      #assert int(sysgrosssales) == presysgrosssales + cash + credit
      assert int(syscreditsalestotal) == presyscreditsalestotal + credit - creditreturn
      #assert int(sysnetsalesamount) == presysnetsalesamount + cash + credit - cashreturn - creditreturn
      print("<<END: verifySalesDayBook")

#Module: Report: PatientCensus***************
   def getPatientCensus(self):
      print(">>START: getPatientCensus")
      global sysnoofcount
      global sysamount
      global sysunconfirmedcount
      global sysunconfirmedamount
      global sysconfirmedcount
      global sysconfirmedamount
      global systotalcount
      global systotalamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Patient Census')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysnoofcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[1]").text
      print("sysnoofcount", sysnoofcount)
      sysamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[2]").text
      print("sysamount", sysamount)
      sysunconfirmedcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[3]").text
      print("sysunconfirmedcount", sysunconfirmedcount)
      sysunconfirmedamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[4]").text
      print("sysunconfirmedamount", sysunconfirmedamount)
      sysconfirmedcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[5]").text
      print("sysconfirmedcount", sysconfirmedcount)
      sysconfirmedamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[6]").text
      print("sysconfirmedamount", sysconfirmedamount)
      systotalcount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[7]").text
      print("systotalcount", systotalcount)
      systotalamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'SUMMARY:')]/following-sibling::td[8]").text
      print("systotalamount", systotalamount)
      print("<<END: getPatientCensus")

   def preSystemPatientCensus(self):
      print(">>START: preSystemPatientCensus")
      global presysnoofcount
      global presysamount
      global presysunconfirmedcount
      global presysunconfirmedamount
      global presysconfirmedcount
      global presysconfirmedamount
      global presystotalcount
      global presystotalamount
      presysnoofcount = int(sysnoofcount)
      presysamount = int(sysamount)
      presysunconfirmedcount = int(sysunconfirmedcount)
      presysunconfirmedamount = int(sysunconfirmedamount)
      presysconfirmedcount = int(sysconfirmedcount)
      presysconfirmedamount = int(sysconfirmedamount)
      presystotalcount = int(systotalcount)
      presystotalamount = int(systotalamount)
      print("<<END: preSystemPatientCensus")

   def verifyPatientCensus(self, cash, cashreturn, credit, creditreturn, provisional):
      print(">>START: verifyPatientCensus")
      assert int(sysnoofcount) == presysnoofcount + cash/cash
      print("presysamount", presysamount)
      print("sysamount", sysamount)
      print("cash", cash)
      assert int(sysamount) == int(int(presysamount) + int(cash))
      assert int(sysunconfirmedcount) == presysunconfirmedcount + provisional
      assert int(sysunconfirmedamount) == presysunconfirmedamount + provisional
      assert int(sysconfirmedcount) == presysconfirmedcount + credit
      assert int(sysconfirmedamount) == presysconfirmedamount + credit
      assert int(systotalcount) == presystotalcount + cash/cash + credit
      assert int(systotalamount) == presystotalamount + cash + credit
      print("<<END: verifyPatientCensus")

#Module: Report: Income Segregation Report*****************
   def getIncomeSegregation(self):
      print(">>START: getIncomeSegregation")
      global sysunit
      global syscashgrosssales
      global syscashdiscount
      global syscreditgrosssales
      global syscreditdiscount
      global sysreturnqty
      global sysreturnamount
      global sysreturndiscount
      global systotalgrosssales
      global systotaldiscount
      global systotalnetsales
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Income Segregation')]").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(15)
      sysunit = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[1]").text
      print("sysunit", sysunit)
      syscashgrosssales = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[2]").text
      print("syscashgrosssales", syscashgrosssales)
      syscashdiscount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[3]").text
      print("syscashdiscount", syscashdiscount)
      syscreditgrosssales = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[4]").text
      print("syscreditgrosssales", syscreditgrosssales)
      syscreditdiscount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[5]").text
      print("syscreditdiscount", syscreditdiscount)
      sysreturnqty = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[6]").text
      print("sysreturnqty", sysreturnqty)
      sysreturnamount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[7]").text
      print("sysreturnamount", sysreturnamount)
      sysreturndiscount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[8]").text
      print("sysreturndiscount", sysreturndiscount)
      systotalgrosssales = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[9]").text
      print("systotalgrosssales", systotalgrosssales)
      systotaldiscount = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[10]").text
      print("systotaldiscount", systotaldiscount)
      systotalnetsales = self.danpheEMR.find_element_by_xpath(
         "//td[contains(text(), 'Unit')]/parent::tr/following-sibling::tr[3]/td[11]").text
      print("systotalnetsales", systotalnetsales)
      print("<<END getIncomeSegregation")

   def preSystemIncomeSegregation(self):
      print(">>START: preSystemIncomeSegregation")
      global presysunit
      global presyscashgrosssales
      global presyscashdiscount
      global presyscreditgrosssales
      global presyscreditdiscount
      global presysreturnqty
      global presysreturnamount
      global presysreturndiscount
      global presystotalgrosssales
      global presystotaldiscount
      global presystotalnetsales
      presysunit = float(sysunit)
      print("presysunit", presysunit)
      presyscashgrosssales = int(syscashgrosssales)
      print("presyscashgrosssales", presyscashgrosssales)
      presyscashdiscount = int(syscashdiscount)
      print("presyscashdiscount", presyscashdiscount)
      presyscreditgrosssales = int(syscreditgrosssales)
      print("presyscreditgrosssales", presyscreditgrosssales)
      presyscreditdiscount = int(syscreditdiscount)
      print("presyscreditdiscount", presyscreditdiscount)
      presysreturnqty = int(sysreturnqty)
      print("presysreturnqty", presysreturnqty)
      presysreturnamount = int(sysreturnamount)
      print("presysreturnamount", presysreturnamount)
      presysreturndiscount = int(sysreturndiscount)
      print("presysreturndiscount", presysreturndiscount)
      presystotalgrosssales = int(systotalgrosssales)
      print("presystotalgrosssales", presystotalgrosssales)
      presystotaldiscount = int(systotaldiscount)
      print("presystotaldiscount", presystotaldiscount)
      presystotalnetsales = int(systotalnetsales)
      print("presystotalnetsales", presystotalnetsales)
      print("<<END preSystemIncomeSegregation")

   def verifyIncomeSegregation(self, cash, cashreturn, credit, creditreturn, provision):
      print(">>START: verifyIncomeSegregation")
      unit = 0
      returnqty = 0
      if cash > 0 or credit > 0:
         returnqty = 0
         unit = 1
      elif cashreturn > 0 or creditreturn > 0:
         returnqty = 1
         unit = 0
      calcUnit = presysunit + unit
      print("calcUnit", calcUnit)
      assert float(sysunit) == int(calcUnit)
      print("syscashgrosssales", syscashgrosssales)
      calcCashGrossSales = int(presyscashgrosssales + cash)
      print("calcCashGrossSales", calcCashGrossSales)
      assert int(syscashgrosssales) == int(presyscashgrosssales + cash) #Issues: LPH-866,...  .Issue on: V1.9.0,.....
      assert int(syscashdiscount) == presyscashdiscount + 0
      assert int(syscreditgrosssales) == presyscreditgrosssales + credit
      assert int(syscreditdiscount) == presyscreditdiscount + 0
      assert int(sysreturnqty) == presysreturnqty + returnqty
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
      assert int(sysreturndiscount) == presysreturndiscount + 0
      assert int(systotalgrosssales) == presystotalgrosssales + cash - cashreturn + credit - creditreturn
      assert int(systotaldiscount) == presystotaldiscount + 0
      assert int(systotalnetsales) == presystotalnetsales + cash - cashreturn + credit - creditreturn
      print("<<END verifyIncomeSegregation")

   def getPatientCreditSummary(self):
      print(">>START: getPatientCreditSummary")
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Patient Credit Summary')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      print("<<END: getPatientCreditSummary")

   def preSystemPatientCreditSummary(self):
      print(">>START: preSystemPatientCreditSummary")
      print("<<END: preSystemPatientCreditSummary")

   def verifyPatientCreditSummary(self):
      print(">>START: verifyPatientCreditSummary")
      print("<<END: verifyPatientCreditSummary")

   def getDoctorSummary(self, doctor):
      print(">>START: getDoctorSummary")
      global sysgrosstotal
      global sysdiscountamount
      global sysreturnamount
      global sysnetsales
      global sysprovisionalamount
      global syscancelamount
      global syscreditamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Doctor Summary')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysgrosstotal = self.danpheEMR.find_element_by_css_selector(".table tr:nth-child(1) > td:nth-child(2)").text
      print("sysgrosstotal", sysgrosstotal)
      sysdiscountamount = self.danpheEMR.find_element_by_css_selector(".table tr:nth-child(1) > td:nth-child(4)").text
      print("sysdiscountamount", sysdiscountamount)
      sysreturnamount = self.danpheEMR.find_element_by_css_selector(".table tr:nth-child(1) > td:nth-child(6)").text
      print("sysreturnamount", sysreturnamount)
      sysnetsales = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) td:nth-child(8)").text
      print("sysnetsales", sysnetsales)
      sysprovisionalamount = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)").text
      print("sysprovisionalamount", sysprovisionalamount)
      syscancelamount = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(4)").text
      print("cancel amount", syscancelamount)
      syscreditamount = self.danpheEMR.find_element_by_css_selector("tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(6)").text
      print("syscreditamount", syscreditamount)
      print("<<END: getDoctorSummary")

   def preSystemDoctorSummary(self):
      print(">>START: preSystemDoctorSummary")
      global presysgrosstotal
      global presysdiscountamount
      global presysreturnamount
      global presysnetsales
      global presysprovisionalamount
      global presyscancelamount
      global presyscreditamount
      presysgrosstotal = int(sysgrosstotal)
      presysdiscountamount = int(sysdiscountamount)
      presysreturnamount = int(sysreturnamount)
      presysnetsales = int(sysnetsales)
      presysprovisionalamount = int(sysprovisionalamount)
      presyscancelamount = int(syscancelamount)
      presyscreditamount = int(syscreditamount)
      print("<<END: preSystemDoctorSummary")

   def verifyDoctorSummary(self, cash, cashreturn, credit, creditreturn, discount, provisional, provisionalcancel):
      print(">>START: verifyDoctorSummary")
      assert int(sysgrosstotal) == presysgrosstotal + cash + credit
      assert int(sysdiscountamount) == presysdiscountamount + discount
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
      assert int(sysnetsales) == presysnetsales + cash + credit - discount - cashreturn - creditreturn
      assert int(sysprovisionalamount) == presysprovisionalamount + provisional
      assert int(syscancelamount) == presyscancelamount + provisionalcancel
      assert int(syscreditamount) == presyscreditamount + credit - creditreturn
      print("<<END: verifyDoctorSummary")

# Module: Inventory---------------------------------------------------------
   def createInventoryGoodReceipt(self, qty, item, rate):
      print(">>START: createGoodReceipt")
      global BillNo
      self.danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Procurement").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'General Inventory')]").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_link_text("Goods Arrival Notification").click()
      time.sleep(5)
      self.danpheEMR.find_element_by_xpath("//a[contains(.,' Create Goods Receipt')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_css_selector(".danphe-auto-complete-wrapper > .form-control").send_keys(Keys.RETURN)
      BillNo = random.randint(100, 99999)
      self.danpheEMR.find_element_by_xpath("//input[@formcontrolname='BillNo']").send_keys(BillNo)
      self.danpheEMR.find_element_by_id("itemName0").send_keys(item)
      self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
      time.sleep(2)
      self.danpheEMR.find_element_by_id("rateip0").clear()
      self.danpheEMR.find_element_by_id("rateip0").send_keys(rate)
      self.danpheEMR.find_element_by_xpath("//input[@value='Receipt']").click()
      time.sleep(3)
      print("<<END: createGoodReceipt")

   def editInventoryGoodsReceipt(self):
      print(">>START: edit GoodReceipt")
      time.sleep(2)
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


   def InventoryConsumption(self, item, qty):
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
       self.danpheEMR.find_element_by_link_text("Inventory").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_link_text("Internal").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//button[contains(.,'Direct Dispatch  ')]").click()
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(store)
       self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select();']").send_keys(Keys.TAB)
       time.sleep(1)
       self.danpheEMR.find_element_by_id("itemName0").send_keys(itemname)
       time.sleep(1)
       self.danpheEMR.find_element_by_id("itemName0").send_keys(Keys.TAB)
       time.sleep(1)
       self.danpheEMR.find_element_by_id("qtyip0").send_keys(qty)
       time.sleep(1)
       self.danpheEMR.find_element_by_id("qtyip0").send_keys(Keys.TAB)
       self.danpheEMR.find_element_by_xpath("//textarea[@name='Remarks']").send_keys("Direct dispatch test")
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
      calcTotalStockQuantityf = float(calcTotalStockQuantity)
      TotalStockQuantityf = float(TotalStockQuantity)
      print("calcTotalStockQuantityf", calcTotalStockQuantityf)
      print("TotalStockQuantityf", TotalStockQuantityf)
      assert round(float(TotalStockQuantityf)) == round(float(calcTotalStockQuantityf))
      print("calcQtyValue", calcQtyValue)
      print("calcTotalStockValue", calcTotalStockValue)
      print("TotalStockValue", TotalStockValue)
      calcTotalStockValue = float(calcTotalStockValue)
      TotalStockValuec = float(TotalStockValue)
      assert round(float(TotalStockValuec)) == round(float(calcTotalStockValue))

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
      self.danpheEMR.find_element_by_link_text("Inventory").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      time.sleep(2)
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
      assert PurchaseValue == prePurchaseValue + purchaseamount
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
      assert float(ConsumptionValue) == tempSum
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

#Module: Billing report: Discount Report**********************
   def verifyDiscountReport(self, cash, discountpc):
      print(">>START: verifyDiscountReport")
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'DiscountReport')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      date = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div/span").text
      print(date)
      receiptno = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      print(receiptno)
      hospitalno = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      print(hospitalno)
      assert HospitalNo == hospitalno
      subtotal = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
      print(subtotal)
      assert cash == int(subtotal)
      discount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text
      print(discount)
      assert int(discount) == (discountpc*cash/100)
      tax = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[7]").text
      print(tax)
      totalamount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[8]/span").text
      print(totalamount)
      assert int(totalamount) == int(subtotal) - int(discount)
      user = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[9]").text
      print(user)
      print("<<END: verifyDiscountReport")

#Module: Billing report: Deposit Report*********************
   def verifyDepositBalanceReport(self, deposit):
      print(">>START: verifyDepositBalanceReport")
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Deposit Balance')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(3)
      hospitalno = self.danpheEMR.find_element_by_xpath("//div[3]/div[2]/div/div/div/div[2]").text
      #assert HospitalNo == hospitalno
      depositamt = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
      print(depositamt)
      print(deposit)
      assert int(depositamt) == deposit
      print("<<END: verifyDepositBalanceReport")

#Module: Billing report: Department Summary Report**********
   def getDepartmentSummary(self):
      global sysgrosstotal
      global sysdiscountamount
      global sysreturnamount
      global sysnetsales
      global sysprovisionalamount
      global syscancelamount
      global syscreditamount
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Billing Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'Department Summary')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").clear()
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys("OPD")
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(
         Keys.ARROW_DOWN)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(Keys.TAB)
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Enter Service Department Name']").send_keys(
         Keys.RETURN)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(9)
      sysgrosstotal = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td").text
      print(sysgrosstotal)
      sysdiscountamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[2]").text
      print(sysdiscountamount)
      sysreturnamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[3]").text
      print(sysreturnamount)
      sysnetsales = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr/td[4]").text
      print(sysnetsales)
      sysprovisionalamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td").text
      print(sysprovisionalamount)
      syscancelamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td[2]").text
      print(syscancelamount)
      syscreditamount = self.danpheEMR.find_element_by_xpath("//table[2]/tbody/tr[2]/td[3]").text
      print(syscreditamount)

   def preSystemDepartmentSummary(self):
      global presysgrosstotal
      global presysdiscountamount
      global presysreturnamount
      global presysnetsales
      global presysprovisionalamount
      global presyscancelamount
      global presyscreditamount
      presysgrosstotal = int(sysgrosstotal)
      presysdiscountamount = int(sysdiscountamount)
      presysreturnamount = int(sysreturnamount)
      presysnetsales = int(sysnetsales)
      presysprovisionalamount = int(sysprovisionalamount)
      presyscancelamount = int(syscancelamount)
      presyscreditamount = int(syscreditamount)

   def verifyDepartmentSummary(self, cash, cashreturn, credit, creditreturn, discount, provisional, provisionalcancel):
      assert int(sysgrosstotal) == presysgrosstotal + cash + credit
      assert int(sysdiscountamount) == presysdiscountamount + discount
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn
      assert int(sysnetsales) == presysnetsales - discount - cashreturn - creditreturn + cash + credit
      assert int(sysprovisionalamount) == presysprovisionalamount + provisional
      assert int(syscancelamount) == presyscancelamount + provisionalcancel
      assert int(syscreditamount) == presyscreditamount + credit - creditreturn

#Module: Billing report: User Collection Report***********
   def getUserCollectionReport(self, user):
       global sysnetcashcollection
       global sysgrosstotalsales
       global sysdiscount
       global sysreturnsubtotal
       global sysreturndiscount
       global sysreturnamount
       global sysnetsales
       global syslesscreditamount
       global sysadddepositreceived
       global syslessdepositrefund
       global sysaddcollectionfromreceivables
       global syslesscashdiscount
       global systotalcollection
       self.danpheEMR.find_element_by_link_text("Reports").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_link_text("Billing Reports").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//i[contains(.,'User Collection')]").click()
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(user)
       time.sleep(3)
       self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(Keys.TAB)
       time.sleep(2)
       self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
       time.sleep(9)
       sysnetcashcollection = self.danpheEMR.find_element_by_css_selector(".blinkAmount").text
       print(sysnetcashcollection)
       sysnetcashcollection = sysnetcashcollection.partition("( ")[2]
       sysnetcashcollection = sysnetcashcollection.partition(")")[0]
       print(sysnetcashcollection)
       sysgrosstotalsales = self.danpheEMR.find_element_by_xpath("//div/div/table/tbody/tr/td[2]").text
       print(sysgrosstotalsales)
       sysdiscount = self.danpheEMR.find_element_by_xpath("//tr[2]/td[2]").text
       print(sysdiscount)
       sysreturnsubtotal = self.danpheEMR.find_element_by_xpath("//tr[3]/td[2]").text
       print(sysreturnsubtotal)
       sysreturndiscount = self.danpheEMR.find_element_by_xpath("//tr[4]/td[2]").text
       print(sysreturndiscount)
       sysreturnamount = self.danpheEMR.find_element_by_xpath("//tr[5]/td[2]").text
       print(sysreturnamount)
       sysnetsales = self.danpheEMR.find_element_by_xpath("//tr[6]/td[2]").text
       print(sysnetsales)
       syslesscreditamount = self.danpheEMR.find_element_by_xpath("//tr[7]/td[2]").text
       print(syslesscreditamount)
       sysadddepositreceived = self.danpheEMR.find_element_by_xpath("//tr[8]/td[2]").text
       print(sysadddepositreceived)
       syslessdepositrefund = self.danpheEMR.find_element_by_xpath("//tr[9]/td[2]").text
       print(syslessdepositrefund)
       sysaddcollectionfromreceivables = self.danpheEMR.find_element_by_xpath("//tr[10]/td[2]").text
       print(sysaddcollectionfromreceivables)
       syslesscashdiscount = self.danpheEMR.find_element_by_xpath("//tr[11]/td[2]").text
       print(syslesscashdiscount)
       systotalcollection = self.danpheEMR.find_element_by_xpath("//tr[12]/td[2]").text
       print(systotalcollection)

   def preSystemUserCollectionReport(self):
      global presysnetcashcollection
      global presysgrosstotalsales
      global presysdiscount
      global presysreturnsubtotal
      global presysreturndiscount
      global presysreturnamount
      global presysnetsales
      global presyslesscreditamount
      global presysadddepositreceived
      global presyslessdepositrefund
      global presysaddcollectionfromreceivables
      global presyslesscashdiscount
      global presystotalcollection
      presysnetcashcollection = int(sysnetcashcollection)
      presysgrosstotalsales = int(sysgrosstotalsales)
      presysdiscount = int(sysdiscount)
      presysreturnsubtotal = int(sysreturnsubtotal)
      presysreturndiscount = int(sysreturndiscount)
      presysreturnamount = int(sysreturnamount)
      presysnetsales = int(sysnetsales)
      presyslesscreditamount = int(syslesscreditamount)
      presysadddepositreceived = int(sysadddepositreceived)
      presyslessdepositrefund = int(syslessdepositrefund)
      presysaddcollectionfromreceivables = int(sysaddcollectionfromreceivables)
      presyslesscashdiscount = int(syslesscashdiscount)
      presystotalcollection = int(systotalcollection)
   def verifyUserCollectionReport(self, cash, cashreturn, credit, creditreturn, discount, deposit, depositreturn, creditsettlement, provisional, provisionalcancel):
      assert int(sysnetcashcollection) == presysnetcashcollection + cash - cashreturn + deposit - depositreturn - creditsettlement
      assert int(sysgrosstotalsales) == presysgrosstotalsales + cash + credit
      assert int(sysdiscount) == presysdiscount + discount
      assert int(sysreturnsubtotal) == presysreturnsubtotal + cashreturn + creditreturn
      assert int(sysreturndiscount) == presysreturndiscount + discount
      assert int(sysreturnamount) == presysreturnamount + cashreturn + creditreturn - discount
      assert int(sysnetsales) == presysnetsales + cash - cashreturn + credit - creditreturn
      assert int(syslesscreditamount) == presyslesscreditamount + credit - creditreturn
      assert int(sysadddepositreceived) == presysadddepositreceived + deposit
      assert int(syslessdepositrefund) == presyslessdepositrefund + depositreturn
      assert int(sysaddcollectionfromreceivables) == presysaddcollectionfromreceivables + creditsettlement
      assert int(syslesscashdiscount) == presyslesscashdiscount + discount
      assert int(systotalcollection) == presystotalcollection + cash - cashreturn + deposit - depositreturn - creditsettlement

#Module: Admission report: Total Admitted Patients Report**********************
   def verifyTotalAdmittedPatients(self):
      self.danpheEMR.find_element_by_link_text("Reports").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Admission").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Admitted Patient").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(HospitalNo)
      time.sleep(5)
      hospitalno = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      assert hospitalno == HospitalNo

#Module: Incentive ******************
   def synchBilingIncentive(self):
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Bill Sync").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Sync Billing to Incentives')]").click()
      time.sleep(5)

   def getIncentiveTransactionReport(self):
      global quantity
      global incentiveAmt
      global tdsAmount
      global netPayable
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'Reports')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[text()='Transaction Report']").click()
      time.sleep(1)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(doctor1)
      time.sleep(1)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      quantity = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[3]").text
      print("quantity", quantity)
      incentiveAmt = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[4]").text
      print("incentiveAmt", incentiveAmt)
      tdsAmount = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[5]").text
      print("tdsAmount", tdsAmount)
      netPayable = self.danpheEMR.find_element_by_xpath("//div[@id='itmSummaryPrintPage']/table/tbody/tr[2]/td[6]").text
      print("netPayable", netPayable)

   def preIncentiveTransactionReport(self):
      global xquantity
      global xincentiveAmt
      global xtdsAmount
      global xnetPayable
      xquantity = int(quantity)
      xincentiveAmt = float(incentiveAmt)
      xtdsAmount = float(tdsAmount)
      xnetPayable = float(netPayable)

   def verifyIncentiveTransactionReport(self, cash, credit):
      assert int(quantity) == int(xquantity) + 1
      incentiveAmtCalc = cash*0.6 + credit
      print("incentiveAmtCalc", int(incentiveAmtCalc))
      assert int(incentiveAmt) == int(incentiveAmtCalc) + int(xincentiveAmt)
      tdsAmtCalc = incentiveAmtCalc*0.15
      print("tdsAmtCalc", int(tdsAmtCalc))
      assert float(tdsAmount) == float(xtdsAmount) + tdsAmtCalc
      netPayableCalc = incentiveAmtCalc - tdsAmtCalc
      print("netPayableCalc", netPayableCalc)
      assert float(netPayable) == float(xnetPayable) + netPayableCalc

   def IncentivePayment(self):
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Payment").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//button[contains(text(), ' Search ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Ledger Name']").send_keys("Nisha & Dharam")
      self.danpheEMR.find_element_by_xpath("//textarea").send_keys("This is test payment")
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Make Payment')]").click()
      time.sleep(5)

   def createLedgerIncentivePayment(self):
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Payment").click()
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.ARROW_DOWN)
      self.danpheEMR.find_element_by_xpath("//input[@onclick='this.select()']").send_keys(Keys.TAB)
      self.danpheEMR.find_element_by_xpath("//strong[contains(.,'Create ledger for selected doctor')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Create New Ledger").click()

   def getIncentivePaymentReport(self):
      global TotalIncome
      global TDSAmt
      global NetIncome
      global AdjustedAmount
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(.,' Reports ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Payment Report").click()
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(doctor1)
      time.sleep(5)
      TotalIncome = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[3]").text
      TDSAmt = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[4]").text
      NetIncome = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[5]").text
      AdjustedAmount = self.danpheEMR.find_element_by_xpath("//div[2]/div/div/div/div[6]").text

   def preIncentivePaymentReport(self):
      global xTotalIncome
      global xTDSAmt
      global xNetIncome
      global xAdjustedAmount
      xTotalIncome = TotalIncome
      xTDSAmt = TDSAmt
      xNetIncome = NetIncome
      xAdjustedAmount = AdjustedAmount

   def verifyIncentivePaymentReport(self):
      assert TotalIncome == xTotalIncome # + totalIncomeCalc
      assert TDSAmt == xTDSAmt # + tdsAmtCalc
      assert NetIncome == xNetIncome # + netIncomeCalc
      assert AdjustedAmount == xAdjustedAmount # + adjustAmtCalc

   def getIncentivePatientVsServiceReport(self):
      global IncentiveAmt
      global TDSAmt
      global NetPayable
      self.danpheEMR.find_element_by_link_text("Incentive").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_xpath("//a[contains(.,' Reports ')]").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Patient Vs Service Report").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(Keys.TAB)
      #self.danpheEMR.find_element_by_xpath("//input[@placeholder='Search Doctor Name']").send_keys(doctor1)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Show Report')]").click()
      time.sleep(3)
      IncentiveAmt = self.danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[1]").text
      print("IncentiveAmt", IncentiveAmt)
      TDSAmt = self.danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[2]").text
      print("TDSAmt", TDSAmt)
      NetPayable = self.danpheEMR.find_element_by_xpath("//b[text()='Total :']/parent::td/following-sibling::td[3]").text
      print("NetPayable", NetPayable)
      time.sleep(5)

   def preIncentivePatientVsServiceReport(self):
      global xIncentiveAmt
      global xTDSAmt
      global xNetPayable
      xIncentiveAmt = float(IncentiveAmt)
      xTDSAmt = float(TDSAmt)
      xNetPayable = float(NetPayable)

   def verifyIncentivePatientVsServiceReport(self, amount):
       calcIncentive = amount * .60
       calcTDS = calcIncentive * .15
       print("IncentiveAmt", IncentiveAmt)
       print("xIncentiveAmt", xIncentiveAmt)
       print("calcIncentive", calcIncentive)
       assert float(IncentiveAmt) == xIncentiveAmt + calcIncentive   # incentive %
       assert float(TDSAmt) == xTDSAmt + calcTDS         # TDS 15%
       print("xNetPayable", xNetPayable)
       print("NetPayable", NetPayable)
       print("TDSAmt", TDSAmt)
       assert  float(NetPayable) == float(IncentiveAmt) - float(TDSAmt)
       assert float(NetPayable) == xNetPayable + float(calcIncentive) - float(calcTDS) # incentive after deducting TDS

   def insurancePatientRegistration(self):
      global NSHI
      print("Start >> Insurance Patient Registration")
      self.danpheEMR.find_element_by_link_text("GovInsurance").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Patient List").click()
      self.danpheEMR.find_element_by_id("btnNewInsurancePat").click()
      fname = str(random.randint(1111, 9999))
      self.danpheEMR.find_element_by_id("aptPatFirstName").send_keys("insu", fname)
      #self.danpheEMR.find_element_by_id("middleName").send_keys("Patient")
      self.danpheEMR.find_element_by_id("lastName").send_keys("registration")
      dropdown = self.danpheEMR.find_element_by_id("selGender")
      dropdown.find_element_by_xpath("//option[. = 'Male']").click()
      self.danpheEMR.find_element_by_id("selGender").click()
      self.danpheEMR.find_element_by_id("age").send_keys(5)
      NSHI = str(random.randint(11111, 99999))
      self.danpheEMR.find_element_by_id("Ins_NshiNumber").send_keys(NSHI)
      self.danpheEMR.find_element_by_id("Ins_InsuranceBalance").send_keys(50000)
      dropdown = self.danpheEMR.find_element_by_id("firstServicePoint")
      dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
      self.danpheEMR.find_element_by_id("firstServicePoint").click()
      time.sleep(3)
      dropdown = self.danpheEMR.find_element_by_id("IsFamilyHead")
      dropdown.find_element_by_xpath("//option[. = 'Yes']").click()
      self.danpheEMR.find_element_by_id("IsFamilyHead").click()
      self.danpheEMR.find_element_by_id("register").click()

   def insuranceNewVisit(self):
      global NSHI
      print(">> Start: Create insurance patient new visit")
      self.danpheEMR.find_element_by_link_text("GovInsurance").click()
      time.sleep(3)
      self.danpheEMR.find_element_by_link_text("Patient List").click()
      self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(NSHI)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//a[contains(text(),'New Visit')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_id("txtDepartment").send_keys("GYNAE & OBS")
      time.sleep(3)
      self.danpheEMR.find_element_by_id("txtDepartment").send_keys(Keys.RETURN)
      time.sleep(2)
      self.danpheEMR.find_element_by_id("btnPrintInvoice").click()

   def receivedStoreDispatch(self):
      self.danpheEMR.find_element_by_link_text("SubStore").click()
      time.sleep(8)
      self.danpheEMR.find_element_by_xpath("//i[contains(.,'OT Store')]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_link_text("Inventory Requisition").click()
      #ReqNo = 750
      #self.danpheEMR.find_element_by_id("quickFilterInput").send_keys(ReqNo)
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("(//a[contains(.,'Receive Items')])[1]").click()
      time.sleep(2)
      self.danpheEMR.find_element_by_xpath("//button[contains(.,'Receive')]").click()
      self.danpheEMR.find_element_by_xpath("//button[contains(.,' Back to Requisition List')]").click()








   #def insuranceBilling(self, itemName):







   def wait_for_window(self, timeout=2):
      time.sleep(round(timeout / 1000))
      wh_now = self.danpheEMR.window_handles
      wh_then = self.vars["window_handles"]
      if len(wh_now) > len(wh_then):
         return set(wh_now).difference(set(wh_then)).pop()

   def __str__(self):
      return

