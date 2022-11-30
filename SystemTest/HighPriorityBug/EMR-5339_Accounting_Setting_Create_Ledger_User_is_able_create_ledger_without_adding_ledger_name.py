import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleAccounting as LA


# admin user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
###############

#AC.login(adminUserId, adminUserPwd)
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
#############

LA.createLedger(danpheEMR=EMR)
