### Test Case Senario ###
'''
1. To verify patient balance is not negative.
'''
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleBillingReports as LBR
import Library.LibModuleAppointment as LA
import Library.LibModulePatientPortal as LPP
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD


EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LBR.verifydepositbalancereportall(danpheEMR=EMR)
AC.logout()
AC.closeBrowser()

### testcase is failed due to negative amt in balance ###