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

qty = 50

EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LP.addPharmacyItem(EMR, GSV.drug1GenericName)
LP.verifyPharmacyItem(EMR)
LP.createPharmacyGoodsReceipt(danpheEMR=EMR, DrugName=GSV.drug1BrandName, grPrice=GSV.drug1Rate, qty=2)
LP.transferMain2Dispensary(qty)
LP.verifyDispensaryStock(EMR, qty)
