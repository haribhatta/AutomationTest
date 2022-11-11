import Library.GlobalShareVariables as GSV
import Library.LibModulePatientPortal as LP
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LP.patientRegistration(EMR)
AC.logout()
AC.closeBrowser()
