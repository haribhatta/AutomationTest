'''
Objective:
To test Pharmacy Dashboard with below scenarios:
1. Cash Sale
2. Cash Sale Return
3. Credit Sale
4. Credit Settlement
5. Credit Sale Return
6. Deposit
7. Deposit Return
8. Estimation bill (i.e. Provisional).
9. Cancel estimation bill.
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD

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
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)
drug = GSV.drug1BrandName
rate = GSV.drug1Rate
qty = 2
amount = rate*qty
print("Amount", amount)
AC.logout()
AC.login(phUserId, phUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LPR.getPharmacyDashboard(EMR)
LPR.preSystemPharmacyDashboard()
InvoiceNo = LP.createPharmacyInvoiceAnonymous(danpheEMR=EMR, drugname=drug, qty=qty, paymentmode='cash')
#LPR.createDispensarySaleRandomPatient(drugname=drug, qty=qty, paymentmode='Cash')
LPR.getPharmacyDashboard(EMR)
LPR.verifyPharmacyDashboard(cash=amount, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
LPR.preSystemPharmacyDashboard()
LD.returnPharmacyInvoice(danpheEMR=EMR, pInvoiceNo=InvoiceNo, qty=qty, returnremark="This is cash bill return")
LPR.getPharmacyDashboard(EMR)
LPR.verifyPharmacyDashboard(cash=0, cashreturn=amount, credit=0, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
LPR.preSystemPharmacyDashboard()
InvoiceNo1= LD.createDispensarySale(danpheEMR=EMR,HospitalNo=HospitalNo, drugName=drug, qty=qty, paymentmode='credit')
LPR.getPharmacyDashboard(EMR)
LPR.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=amount, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
LPR.preSystemPharmacyDashboard()
LD.returnPharmacyInvoice(danpheEMR=EMR, pInvoiceNo=InvoiceNo1, qty=qty, returnremark="This is credit bill return")
LPR.getPharmacyDashboard(EMR)
LPR.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=amount, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
AC.logout()
AC.closeBrowser()


