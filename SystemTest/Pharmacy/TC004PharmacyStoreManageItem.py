# Happy Path

'''
Objective:
To test below check points:
1. Check pharmacy store quantity.
2. Manage-In pharmacy store quantity.
3. Verify pharmacy store quantity.
4. Manage-Out pharmacy store quantity.
5. Verify pharmacy store quantity.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacy as LP

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drug = GSV.drug1BrandName
drugGenericName = GSV.drug1GenericName
drugPrice = GSV.drug1Rate
supplierName = GSV.pharmacySupplierName1
dispensaryName = GSV.dispensaryName1

qty = 10

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, dispensaryName)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=supplierName, qty=qty, DrugName=drug, grPrice=drugPrice)
LD.getDispensaryStockDetail(danpheEMR=EMR, drugname=drug)
LP.manageStoreStock(danpheEMR=EMR, drugname=drug, type="In", qty=qty)
LD.verifyDispensaryStockDetail(danpheEMR=EMR, drugname=drug)
LD.getDispensaryStockDetail(danpheEMR=EMR, drugname=drug)
LP.manageStoreStock(danpheEMR=EMR, drugname=drug, type="Out", qty=qty)
LD.verifyDispensaryStockDetail(danpheEMR=EMR, drugname=drug)

AC.logout()
AC.closeBrowser()
