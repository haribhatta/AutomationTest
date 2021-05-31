from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

pr = A()

pr.openBrowser()
pr.login(foUserId, foUserPwd)
pr.counteractivation()
pr.patientRegistration()
#pr.logout()
#pr.closeBrowser()
print("Status:Passed -> TC001 PatientRegistrationPrintHealthCard")

