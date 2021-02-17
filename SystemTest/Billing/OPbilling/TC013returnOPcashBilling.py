from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

rb = A()
paymode = "Cash"
itemrate = 500

rb.openBrowser()
rb.login(foUserId, foUserPwd)
rb.counteractivation()
rb.patientquickentry(discountpc=0, paymentmode=paymode)
rb.getBillingDashboard()
rb.preSystemDataBillingDashboard()
rb.returnBillingInvoice(returnmsg="This is test return")
rb.getBillingDashboard()
rb.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=itemrate, credit=0, creditReturn=0, settlement=0, provisional=0, provisionalcancel=0)
