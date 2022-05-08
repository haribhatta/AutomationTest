'''
Scripted by: Hari P. Bhatta
Headline:
Store>Report>Stock>Stock summary report: Opening value and closing value mismatch.
Description:
1. Login to the application.2. Navigate to the Store>Report>Stock>Stock summary report.3. Then go to select store and select MainDispensary and click on show report.

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

########
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
#############
# pharmacy desk user login
phUserId = GSV.pharmacyUserID
phUserPwd = GSV.pharmacyUserPwD
#############
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
LPR.getPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, drugname=drug)
LPR.preSystemPharmacyOpeningEndingStockSummaryReport()
pInvoiceNo = LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty, drugName=drug, paymentmode='Cash')
LPR.getPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, drugname=drug)
LPR.verifyPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, qty=qty)
AC.logout()
AC.closeBrowser()