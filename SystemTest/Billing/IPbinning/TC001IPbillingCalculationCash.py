from TestActionLibrary import A

ip = A()
test1 = "USG (Abdomen / pelvis)"
test1rate = 1050
test2 = "BT/CT"
test2rate = 200
paymode = "Cash"

ip.openBrowser()
ip.login("billing1", "pass123")
ip.counteractivation()
ip.dischargeRandomPatient()  # This action is to free bed to admit new patient (Pre-condition to run test script).

ip.patientquickentry(discountpc=0, paymentmode="Cash")
ip.admitDisTrans(admit=1, discharge=0, trasfer=0, deposit=0)
ip.getIPbillingDetails(paymentmode=paymode)
ip.preIPbillingDetails()
ip.createIPprovisionalBill(test=test1)
ip.getIPbillingDetails(paymentmode=paymode)
ip.verifyIPbillingDetails(testrate = test1rate, canceltest = 0, paymentmode=paymode)
ip.preIPbillingDetails()
ip.createIPprovisionalBill(test=test2)
ip.getIPbillingDetails(paymentmode=paymode)
ip.verifyIPbillingDetails(testrate = test2rate, canceltest = 0, paymentmode=paymode)
ip.preIPbillingDetails()
ip.cancelIPprovisionalBill(canceltest = test2)
ip.getIPbillingDetails(paymentmode=paymode)
ip.verifyIPbillingDetails(testrate = 0, canceltest = test2rate, paymentmode=paymode)
ip.preIPbillingDetails()
ip.modifyDischargeDate()
ip.getIPbillingDetails(paymentmode=paymode)
ip.verifyIPbillingDetails(testrate = 0, canceltest = 0, paymentmode=paymode)
ip.verifyConfirmDischarge(paymentmode=paymode)
ip.verifyDischargeInvoice(paymentmode=paymode)
ip.logout()
ip.closeBrowser()



