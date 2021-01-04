from TestActionLibrary import A

qt = A()

qt.openBrowser()
qt.login("frontdesk1", "frontdesk12")
usgtest = "USG ABDOMEN & PELVIS"
usgprice = 1000
admision = 3210

#qt.getBillingDashboard()
qt.counteractivation()
qt.patientRegistration()
qt.getBillingDashboard()
qt.admitDisTrans(1, 0, 0, 0)
qt.preSystemDataBillingDashboard()
qt.getBillingDashboard()
qt.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=admision, provisionalcancel=0)
qt.createIPprovisionalBill(usgtest)
qt.preSystemDataBillingDashboard()
qt.getBillingDashboard()
qt.verifyBillingDashboard(cash=0, discountpc=0, cashReturn=0, credit=0, creditReturn=0,
                          settlement=0, provisional=usgprice, provisionalcancel=0)