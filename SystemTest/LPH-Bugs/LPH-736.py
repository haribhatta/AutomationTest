# New patient cannot be added while doing  registration.

# Steps :
# Navigate through  Emergency ->New Patient ->
# click new registration -> fill the required form and click on Register.

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