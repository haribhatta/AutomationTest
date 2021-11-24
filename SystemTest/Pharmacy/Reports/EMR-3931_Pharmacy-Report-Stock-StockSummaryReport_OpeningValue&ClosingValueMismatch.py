import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD

AC.applicationSelection()
AC.openBrowser()
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
LB.counteractivation()
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)
drug = GSV.drug1BrandName
rate = GSV.drug1Rate
qty = 2
amount = rate*qty
print("Amount", amount)
AC.logout()
AC.login(phUserId, phUserPwd)
LD.activatePharmacyCounter()
LPR.getPharmacyOpeningEndingStockSummaryReport(drugname=drug)
LPR.preSystemPharmacyOpeningEndingStockSummaryReport()
pInvoiceNo = LP.createPharmacyInvoice(HospitalNo, qty, paymentmode='Cash')
LPR.getPharmacyOpeningEndingStockSummaryReport(drugname=drug)
LPR.verifyPharmacyOpeningEndingStockSummaryReport(qty)
AC.logout()
AC.closeBrowser()