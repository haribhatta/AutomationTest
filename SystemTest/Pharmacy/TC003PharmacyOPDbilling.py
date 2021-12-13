'''
Objective:
To test below check points:
1. Create pharmacy OPD invoice.
2. Verify pharmacy OPD invoice.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

#Drug name for billing
drugname = GSV.drugSinexName
genericname = GSV.drug1GenericName
rate = GSV.drug1Rate
quantity = 1
mode = "Cash"

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo = LA.patientquickentry(danpheEMR=EMR, discountpc=0, paymentmode="Cash", department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
AC.logout()

AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)

#  Create PO
#phaoB.createPharmacyPurchaseOrder()
#phaoB.verifyPharmacyPurchaseOrder()

# Received GR from above PO
#phaoB.addPharmacyGRfromPO()

LP.createPharmacyInvoiceTC(danpheEMR=EMR,HospitalNo=HospitalNo, drugname=drugname, qty=quantity, paymentmode=mode)
AC.logout()
AC.closeBrowser()
