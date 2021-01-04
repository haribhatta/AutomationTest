from TestActionLibrary import A

tibr = A()

tibr.openBrowser()
tibr.login('billing1', 'pass123')
tibr.counteractivation()
tibr.patientquickentry(0, 'Cash')
tibr.getTotalItemsBill()
tibr.returnBillingInvoice("This is cash return.")
tibr.preSystemTotalItemsBill()
tibr.getTotalItemsBill()
tibr.verifyTotalItemsBill(returnamt=500, discountamt=0)
tibr.logout()
tibr.closeBrowser()
