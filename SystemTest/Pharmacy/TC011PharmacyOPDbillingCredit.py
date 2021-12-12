'''
Objective:
To test below check points:
1. Create pharmacy OPD credit invoice.
2. Cancel pharmacy OPD credit invoice.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drugname = "SINEX TAB"
quantity = 1
mode = "Credit"
rate = 3

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
LB.verifyopdinvoice(danpheEMR=EMR, deposit=0, billamt=500)
AC.logout()

AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LP.createPharmacyInvoiceTC(EMR, HospitalNo=HospitalNo, drugname=drugname, qty=quantity, paymentmode=mode)
LP.verifyPharmacyInvoice3(EMR, drugname, quantity, rate)
AC.logout()
AC.closeBrowser()
