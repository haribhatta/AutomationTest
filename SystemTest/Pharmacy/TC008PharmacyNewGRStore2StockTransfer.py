'''
Objective:
To test below check points:
1. Check Store quantity.
2. Check Stock quantity.
3. Transfer from Store to Stock.
4. Verify Store quantity.
5. Verify Stock quantity.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP
import Library.LibModuleSettings as LS

# pharmacy desk user login
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
drugName = GSV.drug1BrandName
qty = 1

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
print(NepaliReceipt)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=GSV.pharmacySupplierName1, DrugName=drugName, grPrice=GSV.drug1Rate, qty=2, NepaliReceipt=NepaliReceipt)
LP.transferMainStore2MainDispensary(danpheEMR=EMR, drugname=GSV.drug1BrandName, qty=qty)
LD.verifyDispensaryStockDetail(danpheEMR=EMR, drugname=drugName)