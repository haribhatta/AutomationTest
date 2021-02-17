from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD
# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

drugname = "SINEX TAB"
quantity = 2
rate = 3
paymentmode = "CREDIT"
returnremark = "This is auto return"

RPI = A()

RPI.openBrowser()
RPI.login(foUserId, foUserPwd)
RPI.counteractivation()
RPI.patientquickentry(0, paymentmode)
RPI.verifyopdinvoice(deposit=0, billamt=500)
RPI.logout()

RPI.login(pharmacyUserId, pharmacyUserPwd)
RPI.activatePharmacyCounter()
RPI.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=paymentmode)
RPI.verifyPharmacyInvoice3(drugname, quantity, rate)
RPI.returnPharmacyInvoice(qty=quantity, returnremark=returnremark)
RPI.verifyReturnPharmacyInvoice(paymentmode, returnRemark=returnremark)
RPI.logout()
RPI.closeBrowser()
# This has open bug: EMR-2630
