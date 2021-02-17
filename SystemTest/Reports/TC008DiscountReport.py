from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

dr = A()

dr.openBrowser()
dr.login(foUserId, foUserPwd)
dr.counteractivation()
dr.patientquickentry(50, 'Cash')
dr.verifyDiscountReport(cash=500, discountpc=50)
dr.logout()
dr.closeBrowser()
