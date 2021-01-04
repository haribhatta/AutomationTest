from TestActionLibrary import A

drugname = "SINEX TAB"
quantity = 1
mode = "Cash"
rate = 3

phaoB = A()

phaoB.openBrowser()
phaoB.login("billing1", "pass123")
phaoB.counteractivation()
phaoB.patientquickentry(0, "Cash")
phaoB.verifyopdinvoice(deposit=0, billamt=500)
phaoB.logout()

phaoB.login("pharmacy1", "pass123")
phaoB.activatePharmacyCounter()
phaoB.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=mode)
phaoB.verifyPharmacyInvoice3(drugname, quantity, rate)
phaoB.logout()
phaoB.closeBrowser()
