from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

cs = A()
paymode = "CREDIT"
itemrate = 500

cs.openBrowser()
cs.login(foUserId, foUserPwd)
cs.counteractivation()
cs.patientquickentry(discountpc=0, paymentmode=paymode)
cs.getBillingDashboard()
cs.preSystemDataBillingDashboard()
cs.creditSettlements()
cs.getBillingDashboard()
cs.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=itemrate, provisional=0, provisionalcancel=0)

