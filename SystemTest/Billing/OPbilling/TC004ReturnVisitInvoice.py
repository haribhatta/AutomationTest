from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD

OPD = A.opdRate

rvi = A()

rvi.openBrowser()
rvi.login(foUserId, foUserPwd)
rvi.counteractivation()
rvi.patientquickentry(0, 'Cash')
#rvi.verifyopdinvoice(deposit=0, billamt=500)
rvi.getBillingDashboard()
rvi.returnBillingInvoice("This is cash return.")
rvi.preSystemDataBillingDashboard()
rvi.getBillingDashboard()
rvi.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=OPD, credit=0, creditReturn=0, settlement=0, provisional=0
                           , provisionalcancel=0)
rvi.logout()
rvi.closeBrowser()
