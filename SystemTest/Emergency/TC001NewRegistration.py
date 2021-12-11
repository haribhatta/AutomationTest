import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleEmergency as LE

# front desk user login
EmergencyId = GSV.adminUserID
EmergencyPwd = GSV.adminUserPwD

EMR = AC.openBrowser()
AC.login(EmergencyId, EmergencyPwd)
LE.EmergencyRegistration()
print("The Emergency Patient Registered.")