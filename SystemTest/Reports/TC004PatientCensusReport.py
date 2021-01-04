from TestActionLibrary import A

pcr = A()
pcr.openBrowser()
pcr.login('billing1', 'pass123')
pcr.getPatientCensus()
pcr.counteractivation()
pcr.patientquickentry(0, 'Cash')
pcr.preSystemPatientCensus()
pcr.getPatientCensus()
pcr.verifyPatientCensus(cash=500, cashreturn=0, credit=0, creditreturn=0, provisional=0)
pcr.logout()
pcr.closeBrowser()
