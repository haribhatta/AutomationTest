'''
Objective:
To test below check points:
1. Create pharmacy OPD invoice.
2. Verify pharmacy OPD invoice.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

#Drug name for billing
drugname = GSV.drug1BrandName
genericname = GSV.drug1GenericName
rate = GSV.drug1Rate
quantity = 1
mode = "Cash"
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(danpheEMR=EMR, discountScheme=0, paymentmode="Cash", department=GSV.departmentGyno, doctor=GSV.doctorGyno, priceCategoryType=priceCategoryType)
AC.logout()

AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, dispensaryName=GSV.dispensaryName1)

#  Create PO
#phaoB.createPharmacyPurchaseOrder()
#phaoB.verifyPharmacyPurchaseOrder()

# Received GR from above PO
#phaoB.addPharmacyGRfromPO()

LD.createDispensarySale(danpheEMR=EMR, HospitalNo=HospitalNo, drugName=drugname, qty=quantity, paymentmode=mode)
AC.logout()
AC.closeBrowser()
