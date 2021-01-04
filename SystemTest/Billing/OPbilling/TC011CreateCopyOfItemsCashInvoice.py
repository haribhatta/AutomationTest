from TestActionLibrary import A

bil = A()
bil.openBrowser()
bil.login('billing1', 'pass123')
bil.counteractivation()
bil.patientquickentry(0, 'Cash')
bil.returnBillingInvoice("This is cash return 1.")
bil.createCopyItemInvoice('Cash')
bil.returnBillingInvoice("This is cash return 2.")
bil.createCopyItemInvoice('CREDIT')
bil.logout()
bil.closeBrowser()
