from TestActionLibrary import A

dr = A()

dr.openBrowser()
dr.login('billing1', 'pass123')
dr.counteractivation()
dr.patientquickentry(50, 'Cash')
dr.verifyDiscountReport(cash=500, discountpc=50)
dr.logout()
dr.closeBrowser()
