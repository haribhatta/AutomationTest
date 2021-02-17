from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

tibr = A()

tibr.openBrowser()
tibr.login(foUserId, foUserPwd)
tibr.counteractivation()
tibr.patientquickentry(0, 'Cash')
tibr.getTotalItemsBill()
tibr.returnBillingInvoice("This is cash return.")
tibr.preSystemTotalItemsBill()
tibr.getTotalItemsBill()
tibr.verifyTotalItemsBill(returnamt=500, discountamt=0)
tibr.logout()
tibr.closeBrowser()
