from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

bil = A()
bil.openBrowser()
bil.login(foUserId, foUserPwd)
bil.counteractivation()
bil.patientquickentry(0, 'Cash')
bil.returnBillingInvoice("This is cash return 1.")
bil.createCopyItemInvoice('Cash')
bil.returnBillingInvoice("This is cash return 2.")
bil.createCopyItemInvoice('CREDIT')
bil.logout()
bil.closeBrowser()
