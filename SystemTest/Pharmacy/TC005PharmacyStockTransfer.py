'''
Objective:
Happy Path Testing
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
# pharmacy desk user login as transfer is not access to user so change to admin user
pharmacyUserId = GSV.adminUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
###
drug = GSV.drug1BrandName
transferqty = 1
transferStore2Dispensary = 'Yes'
dispensaryName = GSV.dispensaryName1
###
EMR = AC.openBrowser()
AC.login(pharmacyUserId, pharmacyUserPwd)
LD.activateDispensaryCounter(EMR,dispensaryName=dispensaryName)
LP.transferMainStore2MainDispensary(danpheEMR=EMR, drugname=drug, qty=transferqty)
LD.transferMainDispensary2MainStore(danpheEMR=EMR, drugname=drug, qty=transferqty)
AC.logout()
AC.closeBrowser()
