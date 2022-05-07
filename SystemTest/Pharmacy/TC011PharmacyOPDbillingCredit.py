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
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType, case='+ve')
LB.verifyopdinvoice(danpheEMR=EMR, deposit=0, billamt=500)
AC.logout()

AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LD.createDispensarySale(EMR, HospitalNo=HospitalNo, drugName=drugname, qty=quantity, paymentmode=mode)
LD.verifyDispensarySaleInvoice(EMR, quantity)
AC.logout()
AC.closeBrowser()
