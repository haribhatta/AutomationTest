from TestActionLibrary import A

bil = A()
bil.openBrowser()
bil.login('billing1', 'pass123')
bil.counteractivation()
bil.patientquickentry(0, 'CREDIT')
bil.returnBillingInvoice("This is credit bill return")
bil.createCopyItemInvoice('CREDIT')
bil.returnBillingInvoice("This is copy bill return")
bil.createCopyItemInvoice('Cash')
bil.logout()
bil.closeBrowser()
