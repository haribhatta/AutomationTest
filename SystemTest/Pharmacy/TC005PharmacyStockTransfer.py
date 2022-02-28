'''
Objective:
To test below check points:
1. Count pharmacy stock.
2. Transfer pharmacy stock.
3. Verify pharmacy stock.
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
###
drug = GSV.drug1BrandName
transferqty = 1
transferStore2Dispensary = 'Yes'
dispensaryName = GSV.dispensaryName1
###
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activatePharmacyCounter(EMR,dispensaryName=dispensaryName)
#LP.getStoreDetail(drugname=drug, danpheEMR=EMR)
#LP.getStockDetail(danpheEMR=EMR, drugname=drug)
LP.transferMainStore2MainDispensary(danpheEMR=EMR, drugname=drug, qty=transferqty)
#LP.verifyStockDetail(danpheEMR=EMR, drugname=drug)
#LP.verifyStoreDetail(danpheEMR=EMR, drugname=drug)
LD.transferMainDispensary2MainStore(danpheEMR=EMR, drugname=drug, qty=transferqty)
#LP.verifyStoreDetail(danpheEMR=EMR, drugname=drug)
#LP.verifyStockDetail(danpheEMR=EMR, drugname=drug)

AC.logout()
AC.closeBrowser()
