'''
Objective:
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
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)
drug = GSV.drug1BrandName
rate = GSV.drug1Rate
qty = 2
amount = rate*qty
print("Amount", amount)
AC.logout()
AC.login(phUserId, phUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LPR.getPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, drugname=drug)
LPR.preSystemPharmacyOpeningEndingStockSummaryReport()
pInvoiceNo = LP.createPharmacyInvoice(danpheEMR=EMR, HospitalNo=HospitalNo, qty=qty, paymentmode='Cash')
LPR.getPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, drugname=drug)
LPR.verifyPharmacyOpeningEndingStockSummaryReport(danpheEMR=EMR, qty=qty)
AC.logout()
AC.closeBrowser()