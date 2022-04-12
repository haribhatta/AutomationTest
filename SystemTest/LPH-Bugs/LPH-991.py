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
import Library.LibModuleSettings as LS
# front desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
Qty1 = 1
Drug1 = GSV.drug1BrandName
Drug1Price = GSV.drug1Rate

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(danpheEMR=EMR, dispensaryName=GSV.dispensaryName1)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
print("Test script failling with LPH-1095")
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=GSV.pharmacySupplierName1, qty=Qty1, DrugName=Drug1, grPrice=Drug1Price, NepaliReceipt=NepaliReceipt)