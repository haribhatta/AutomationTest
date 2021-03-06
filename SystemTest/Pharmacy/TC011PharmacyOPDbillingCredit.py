from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD
# pharmacy desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

drugname = "SINEX TAB"
quantity = 1
mode = "Credit"
rate = 3

phaoB = A()

phaoB.openBrowser()
phaoB.login(foUserId, foUserPwd)
phaoB.counteractivation()
phaoB.patientquickentry(0, "Cash")
phaoB.verifyopdinvoice(deposit=0, billamt=500)
phaoB.logout()

phaoB.login(pharmacyUserId, pharmacyUserPwd)
phaoB.activatePharmacyCounter()
phaoB.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=mode)
phaoB.verifyPharmacyInvoice3(drugname, quantity, rate)
phaoB.logout()
phaoB.closeBrowser()
