'''
Objective:
To test Pharmacy Stock Items Reports with below scenarios:
1. Get Pharmacy Stock Items Report.
2. Dispatch Pharmacy Stock Item.
3. Verify Pharmacy Stock Items Report.
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacyReports as LPR
import Library.LibModulePharmacy as LP
import Library.LibModuleDispensary as LD

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
Dispensary1 = GSV.Dispensary1

drug = GSV.drug1BrandName

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.selectDispensary(dispensary=Dispensary1)
LP.getStockDetail(danpheEMR=EMR, drugname=drug)
LP.getStoreDetail(danpheEMR=EMR, drugname=drug)
LPR.verifyStockItemsReport(danpheEMR=EMR, drugname=drug)

# Test script is failed with bug: EMR-2767
