from TestActionLibrary import A

ip = A()
paymode = "CREDIT"
itemprice = 1500

ip.openBrowser()
ip.login("billing1", "pass123")
ip.counteractivation()
ip.patientRegistration()
ip.getBillingDashboard()
ip.preSystemDataBillingDashboard()
ip.admitDisTrans(admit=1, discharge=0, trasfer=0, deposit=0)
ip.getBillingDashboard()
ip.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=0, provisional=itemprice, provisionalcancel=0)
ip.preSystemDataBillingDashboard()
ip.generateDischargeInvoice(paymentmode = paymode)
ip.getBillingDashboard()
ip.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=itemprice, creditReturn=0, settlement=0, provisional=0, provisionalcancel=itemprice)
ip.preSystemDataBillingDashboard()
ip.creditSettlements()
ip.getBillingDashboard()
ip.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0, settlement=itemprice, provisional=0, provisionalcancel=0)
ip.logout()
ip.closeBrowser()
