from TestActionLibrary import A

rb = A()
paymode = "Cash"
paymode1 = "CREDIT"

rb.openBrowser()
rb.login("billing1", "pass123")
rb.counteractivation()
rb.patientRegistration()
rb.admitDisTrans(admit=1, discharge=0, trasfer=0, deposit=0)
rb.generateDischargeInvoice(paymentmode=paymode)
rb.getBillingDashboard()
rb.preSystemDataBillingDashboard()
rb.cancelDischarge()
rb.returnBillingInvoice(returnmsg="This is bill return")
rb.getBillingDashboard()
rb.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=1500, credit=0, creditReturn=0, settlement=0, provisional=0, provisionalcancel=0)

rb.generateDischargeInvoice(paymentmode=paymode1)
rb.getBillingDashboard()
rb.preSystemDataBillingDashboard()
rb.cancelDischarge()
rb.returnBillingInvoice(returnmsg="This is bill return")
rb.getBillingDashboard()
rb.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=1500, settlement=0, provisional=0, provisionalcancel=0)


# Test script is failing due to bug: EMR-2769

