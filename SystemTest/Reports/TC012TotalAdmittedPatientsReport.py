from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

tapr = A()

tapr.openBrowser()
tapr.login(foUserId, foUserPwd)
tapr.counteractivation()
tapr.patientquickentry(0, 'Cash')
tapr.admitDisTrans(1, 0, 0, 0)
tapr.verifyTotalAdmittedPatients()
tapr.logout()
tapr.closeBrowser()
