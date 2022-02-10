'''
Objective:
1. To Verify 'Previous Due Amt' + 'Collection Till Date' = 'Handover Till Date' + 'Due Amount'
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
LBR.getSummaryReport(EMR)
LBR.verify
#LBR.verifyTotalItemsBill(returnamt=opdAmt)
time.sleep(2)
AC.logout()
AC.closeBrowser()
