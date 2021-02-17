from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

bil = A()
bil.openBrowser()
bil.login(foUserId, foUserPwd)
bil.counteractivation()
bil.patientquickentry(0, 'CREDIT')
bil.returnBillingInvoice("This is credit bill return")
bil.createCopyItemInvoice('CREDIT')
bil.returnBillingInvoice("This is copy bill return")
bil.createCopyItemInvoice('Cash')
bil.logout()
bil.closeBrowser()
