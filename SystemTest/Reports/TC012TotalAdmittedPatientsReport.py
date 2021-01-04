from TestActionLibrary import A

tapr = A()

tapr.openBrowser()
tapr.login('billing1', 'pass123')
tapr.counteractivation()
tapr.patientquickentry(0, 'Cash')
tapr.admitDisTrans(1, 0, 0, 0)
tapr.verifyTotalAdmittedPatients()
tapr.logout()
tapr.closeBrowser()
