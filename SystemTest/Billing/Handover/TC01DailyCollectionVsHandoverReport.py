'''
Objective:
1. To Verify 'Total Collection' amount in 'Daily Collection Vs Handover Report' is equal to 'User Collection Report'.
'''

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LP
import Library.LibModuleADT as LADT
import time

# front desk user login
itUserId = GSV.itUserID
itUserPwd = GSV.itUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
EMR = AC.openBrowser()
AC.login(itUserId, itUserPwd)
LB.counteractivation(EMR)
LBR.verifyUserCollectionVsHandOverReport(EMR)
#Current Issue: EMR-4827
time.sleep(2)
AC.logout()
AC.closeBrowser()
