'''
Objective:
To test Pharmacy> Stock Manage Detail Summary Report with below check points:
1. Get Stock Details Report
2. Manage Stock Quantity
3. Verify Stock Details Report
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePatientPortal as LPP
import Library.LibModulePharmacy as LP

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drug = GSV.Testdrug
setupqty = 5
testqty = 7

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName)
LP.getDispensaryStockDetail(danpheEMR=EMR, drugname=drug)
LP.manageStoreStock(danpheEMR=EMR, drugname=drug, type='In', qty=setupqty)
LPR.getPharmacyStockManageDetailReport(danpheEMR=EMR, drugname=drug)
LPR.preSystemPharmacyStockManageDetailReport()
LP.manageStoreStock(danpheEMR=EMR, drugname=drug, type='In', qty=testqty)
LPR.getPharmacyStockManageDetailReport(danpheEMR=EMR, drugname=drug)
LPR.verifyPharmacyStockManageDetailReport(In=testqty, Out=0)
#Blocked by EMR-2588