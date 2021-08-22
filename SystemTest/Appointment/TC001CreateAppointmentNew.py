from AutomationTest.TestActionLibrary import A
from AutomationTest.GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

a = A()

a.openBrowser()
a.login(foUserId, foUserPwd)
a.counteractivation()
a.patientquickentry(discountpc=0, paymentmode='Cash')
#can.verifyopdinvoice(deposit=0, billamt=500)
a.logout()
a.closeBrowser()
print("Status:Passed - > TC001 CreateAppointmentNew")

a.openBrowser()
a.login(foUserId, foUserPwd)
a.counteractivation()
a.patientRegistration()
a.logout()
