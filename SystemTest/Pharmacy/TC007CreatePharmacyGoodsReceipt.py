'''
Objective:
To test below check points:
1. Create Pharmacy goods receipt.
2. Verify Pharmacy goods receipt.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
genericName = GSV.drug1GenericName
drugName = GSV.drug1BrandName
drugRate = GSV.drug1Rate

qty = 50

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LP.addPharmacyItem(EMR, GSV.drug1GenericName)
LP.verifyPharmacyItem(EMR)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, qty=qty, DrugName=drugName, grPrice=drugRate)
LP.verifyPharmacyGoodsReceipt(danpheEMR=EMR, qty=qty, DrugName=drugName)
AC.logout()
AC.closeBrowser()
#Blocked by bug EMR-2591
#Failed with bug EMR-3177