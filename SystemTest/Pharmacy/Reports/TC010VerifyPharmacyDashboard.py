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
AC.login(phUserId, phUserPwd)
LD.activatePharmacyCounter()
LPR.getPharmacyDashboard()
LPR.preSystemPharmacyDashboard()
LP.createPharmacyInvoiceAnonymous(drugname=drug, qty=qty, paymentmode='Cash')
#LPR.createDispensarySaleRandomPatient(drugname=drug, qty=qty, paymentmode='Cash')
LPR.getPharmacyDashboard()
LPR.verifyPharmacyDashboard(cash=amount, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
LPR.preSystemPharmacyDashboard()
LD.returnPharmacyInvoice(qty=qty, returnremark="This is cash bill return")
LPR.getPharmacyDashboard()
LPR.verifyPharmacyDashboard(cash=0, cashreturn=amount, credit=0, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
LPR.preSystemPharmacyDashboard()
LD.createDispensarySaleRandomPatient(drugname=drug, qty=qty, paymentmode='CREDIT')
LPR.getPharmacyDashboard()
LPR.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=amount, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
LPR.preSystemPharmacyDashboard()
LD.returnPharmacyInvoice(qty=qty, returnremark="This is credit bill return")
LPR.getPharmacyDashboard()
LPR.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=amount, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
AC.logout()
AC.closeBrowser()


