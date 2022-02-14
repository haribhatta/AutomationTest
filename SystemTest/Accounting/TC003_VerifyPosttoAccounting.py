# Objective: Verify Post to Accounting.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleAccounting as LA


#AC.applicationSelection()
AC.openBrowser()

danpheEMR = AC.danpheEMR
#AppName = AC.appName

# admin user login
foUserId = GSV.adminUserID
foUserPwd = GSV.adminUserPwD
AC.login(foUserId, foUserPwd)
LA.PosttoAccounting()
AC.logout()
AC.closeBrowser()