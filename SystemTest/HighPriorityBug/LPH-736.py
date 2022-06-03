# New patient cannot be added while doing  registration.

# Steps :
# Navigate through  Emergency ->New Patient ->
# click new registration -> fill the required form and click on Register.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleEmergency as LE


# front desk user login
EmergencyId = GSV.adminUserID
EmergencyPwd = GSV.adminUserPwD

EMR = AC.openBrowser()
AC.login(EmergencyId, EmergencyPwd)
LE.EmergencyRegistration(EMR)
AC.logout()
AC.closeBrowser()
print("The Emergency Patient Registered.")