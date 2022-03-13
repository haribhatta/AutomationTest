import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleSettings as LS
# front desk user login
adminuser = GSV.adminUserID
adminpswd = GSV.adminUserPwD

EMR = AC.openBrowser()
AC.login(adminuser, adminpswd)
LS.Setting_add_employee(EMR)
AC.logout()
