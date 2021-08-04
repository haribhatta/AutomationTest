from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
EmergencyId = GSV.adminUserID
EmergencyPwd = GSV.adminUserPwD
EPR = A()

EPR.openBrowser()
EPR.login(EmergencyId, EmergencyPwd)
EPR.EmergencyRegistration()
print("The Emergency Patient Registered.")