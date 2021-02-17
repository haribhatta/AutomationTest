from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

pcr = A()
pcr.openBrowser()
pcr.login(foUserId, foUserPwd)
pcr.getPatientCensus()
pcr.counteractivation()
pcr.patientquickentry(0, 'Cash')
pcr.preSystemPatientCensus()
pcr.getPatientCensus()
pcr.verifyPatientCensus(cash=500, cashreturn=0, credit=0, creditreturn=0, provisional=0)
pcr.logout()
pcr.closeBrowser()
