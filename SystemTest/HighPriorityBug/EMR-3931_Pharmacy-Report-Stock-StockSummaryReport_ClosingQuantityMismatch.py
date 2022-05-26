'''
Scripted by: Hari P. Bhatta
Headline:
Store>Report>Stock>Stock summary report: Opening value and closing value mismatch.
Description:
1. Login to the application.
2. Navigate to the Store>Report>Stock>Stock summary report.
3. Then go to select store and select MainDispensary and click on show report.

Issue:

Opening value and closing value mismatch on MainDispensary.

Pharmacy Stock Summary Report (Closing Quantity) is not matching with Dispensary quantity.
To test jira story EMR-3931
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

########
EMR = AC.openBrowser()

#############
# front desk user login
AppName = GSV.appName
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
# pharmacy desk user login
phUserId = GSV.pharmacyUserID
phUserPwd = GSV.pharmacyUserPwD
#############
# 1. Login to the application.

AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType="Normal", case='+ve')
#can.verifyopdinvoice(deposit=0, billamt=500)
drug = GSV.drug1BrandName
rate = GSV.drug1Rate
qty = 2
amount = rate*qty
print("Amount", amount)
AC.logout()
AC.login(phUserId, phUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
# 2. Get Dispensary quantity.
print("START >>> Verifying Narcotic Stock Report>>")
danpheEMR = EMR
if AppName == "LPH":
    print("Ï am inside test drive.")
    danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
    danpheEMR.find_element(By.LINK_TEXT, "Stock").click()
    danpheEMR.find_element(By.LINK_TEXT, "Stock Details List").click()


else:
    danpheEMR.find_element(By.LINK_TEXT, "Pharmacy").click()
time.sleep(9)
danpheEMR.find_element(By.ID, "quickFilterInput").send_keys("THYROXINE 75 MCG")
time.sleep(3)
availableQty = danpheEMR.find_element(By.XPATH, "(//div[@col-id='AvailableQuantity'])[2]").text
print("available quantity:", availableQty)

# 3. Then go to select store and select MainDispensary and click on show report.
danpheEMR.find_element(By.LINK_TEXT, "Dispensary").click()
time.sleep(3)
danpheEMR.find_element(By.LINK_TEXT, "Sale").click()
time.sleep(3)
danpheEMR.find_element(By.ID, "item-box0").send_keys("THYRONORM 75MCG(120TAB/BOT)")
time.sleep(3)
danpheEMR.find_element(By.ID, "item-box0").send_keys(Keys.ENTER)
time.sleep(3)
saleQty = danpheEMR.find_element(By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine'])[2]").get_attribute("value")
print("Sale Avai Qty", saleQty)
assert saleQty == availableQty
AC.logout()
AC.closeBrowser()