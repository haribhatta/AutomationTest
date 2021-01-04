from TestActionLibrary import A

ir = A()
paymode = "Cash"
itemprice = 500

# incentive % = 60%

ir.openBrowser()
ir.login("admin", "pass123")
ir.counteractivation()
ir.synchBilingIncentive()
ir.patientquickentry(discountpc=0, paymentmode=paymode)
ir.getIncentiveTransactionReport()
ir.preIncentiveTransactionReport()
ir.synchBilingIncentive()
ir.getIncentiveTransactionReport()
ir.verifyIncentiveTransactionReport(cash=itemprice, credit=0)
ir.logout()
ir.closeBrowser()
