from TestActionLibrary import A

drugname = "SINEX TAB"
quantity = 2
rate = 3
paymentmode = "CREDIT"
returnremark = "This is auto return"

RPI = A()

RPI.openBrowser()
RPI.login("billing1", "pass123")
RPI.counteractivation()
RPI.patientquickentry(0, paymentmode)
RPI.verifyopdinvoice(deposit=0, billamt=500)
RPI.logout()

RPI.login("pharmacy1", "pass123")
RPI.activatePharmacyCounter()
RPI.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=paymentmode)
RPI.verifyPharmacyInvoice3(drugname, quantity, rate)
RPI.returnPharmacyInvoice(qty=quantity, returnremark=returnremark)
RPI.verifyReturnPharmacyInvoice(paymentmode, returnRemark=returnremark)
RPI.logout()
RPI.closeBrowser()
# This has open bug: EMR-2630
