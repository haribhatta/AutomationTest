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
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drug = GSV.Testdrug
drugGenericName = GSV.drug1GenericName
drugPrice = GSV.drug1Rate

qty = 10

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LP.addPharmacyItem(EMR, drugGenericName)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, qty=qty, DrugName=drug, grPrice=drugPrice)
LP.getStoreDetail(danpheEMR=EMR, drugname=drug)
LP.manageStoreStock(danpheEMR=EMR, drugname=drug, type="In", qty=qty)
LP.verifyStoreDetail(danpheEMR=EMR, drugname=drug)
LP.getStoreDetail(danpheEMR=EMR, drugname=drug)
LP.manageStoreStock(danpheEMR=EMR, drugname=drug, type="Out", qty=qty)
LP.verifyStoreDetail(danpheEMR=EMR, drugname=drug)

AC.logout()
AC.closeBrowser()
