from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
opdRate = GSV.opdRate
dr = A()

dr.openBrowser()
dr.login(foUserId, foUserPwd)
dr.counteractivation()
dr.patientquickentry(50, 'Cash')
dr.verifyDiscountReport(cash=opdRate, discountpc=50)
dr.logout()
dr.closeBrowser()
