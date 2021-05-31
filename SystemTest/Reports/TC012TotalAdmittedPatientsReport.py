from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

tapr = A()

tapr.openBrowser()
tapr.login(foUserId, foUserPwd)
tapr.counteractivation()
tapr.patientquickentry(0, 'Cash')
tapr.admitDisTrans(1, 0, 0, 0)
tapr.verifyTotalAdmittedPatients()
tapr.logout()
tapr.closeBrowser()
