from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
opdRate = GSV.opdRate

pcr = A()
pcr.openBrowser()
pcr.login(foUserId, foUserPwd)
pcr.getPatientCensus()
pcr.counteractivation()
pcr.patientquickentry(0, 'Cash')
pcr.preSystemPatientCensus()
pcr.getPatientCensus()
pcr.verifyPatientCensus(cash=opdRate, cashreturn=0, credit=0, creditreturn=0, provisional=0)
pcr.logout()
pcr.closeBrowser()
