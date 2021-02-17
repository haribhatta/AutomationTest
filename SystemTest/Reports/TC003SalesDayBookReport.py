from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

vsdbr = A()

vsdbr.openBrowser()
vsdbr.login(foUserId, foUserPwd)
vsdbr.counteractivation()
vsdbr.getSalesDayBook()
vsdbr.patientquickentry(0, 'Cash')
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=500, cashreturn=0, credit=0, creditreturn=0)
vsdbr.returnBillingInvoice(returnmsg="this is bill return 1")
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=0, cashreturn=500, credit=0, creditreturn=0)

vsdbr.patientquickentry(0, 'CREDIT')
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=0, cashreturn=0, credit=500, creditreturn=0)
vsdbr.returnBillingInvoice(returnmsg="this is bill retur 2n")
vsdbr.preSystemSalesDayBook()
vsdbr.getSalesDayBook()
vsdbr.verifySalesDayBook(cash=0, cashreturn=0, credit=0, creditreturn=500)
vsdbr.logout()
vsdbr.closeBrowser()
