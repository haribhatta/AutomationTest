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
import Library.LibModulePharmacyReports as LPR
import Library.LibModuleAppointment as LA
#import Library.LibModuleBilling as LB

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
drugName = GSV.drug1BrandName
qty = 50

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LP.addPharmacyItem(EMR, GSV.drug1GenericName)
LP.verifyPharmacyItem(EMR)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, supplier=GSV.supplier, DrugName=drugName, grPrice=GSV.drug1Rate, qty=2)
LP.transferMainStore2MainDispensary(danpheEMR=EMR, drugname=GSV.drug1BrandName, qty=qty)
LD.verifyDispensaryStockDetail(danpheEMR=EMR, drugname=drugName)