from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD
# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

drugname = "ABEN SUSPENSION 10ML"
quantity = 1
mode = "Cash"
rate = 3

phaoB = A()

#phaoB.applicationSelection()
phaoB.openBrowser()
#phaoB.login(foUserId, foUserPwd)
#phaoB.counteractivation()
#phaoB.patientquickentry(0, "Cash")
#phaoB.verifyopdinvoice(deposit=0, billamt=500)
#phaoB.logout()

phaoB.login(pharmacyUserId, pharmacyUserPwd)
phaoB.activatePharmacyCounter()

#  Create PO
phaoB.createPharmacyPurchaseOrder()
phaoB.verifyPharmacyPurchaseOrder()

# Received GR from above PO
phaoB.addPharmacyGRfromPO()
#

#phaoB.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=mode)
#phaoB.closePopupApplication(saleinvoice=1)
#phaoB.verifyPharmacyInvoice3(drugname, quantity, rate)
#phaoB.logout()
#phaoB.closeBrowser()
