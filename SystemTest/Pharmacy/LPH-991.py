'''
Objective:
To test EMR-991: Pharmacy | Good Receipt | Failed to add Good receipt.
Steps:
1. Navigate to Pharmacy → Order → Good Receipt.
2. Add all the mandatory value and Print Receipt.
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
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
Qty1 = 1
Drug1 = GSV.drug1BrandName
Drug1Price = GSV.drug1Rate

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName)
print("Test script failling with LPH-1095")
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, qty=Qty1, DrugName=Drug1, grPrice=Drug1Price)