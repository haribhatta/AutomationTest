from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

ip = A()
test1 = GSV.USG
test1rate = GSV.usgRate
test2 = GSV.BTCT
test2rate = GSV.btctRate
paymode = "Cash"
doctor1 = GSV.doctor1
department1 = GSV.department1

ip.openBrowser()
ip.login(foUserId, foUserPwd)
ip.counteractivation()
ip.dischargeRandomPatient()  # This action is to free bed to admit new patient (Pre-condition to run test script).

ip.patientquickentry(discountpc=0, paymentmode="Cash")
ip.admitDisTrans(admit=1, discharge=0, trasfer=0, deposit=0,doctor=doctor1, department=department1)
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



