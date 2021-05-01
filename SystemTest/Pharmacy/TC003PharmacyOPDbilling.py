from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD
# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

drugname = "ASTHALIN 2 MG TAB"
genericname = "SALBUTAMOL 2 MG TAB"
quantity = 1
mode = "Cash"
rate = 1.14

phaoB = A()

phaoB.openBrowser()
phaoB.login(foUserId, foUserPwd)
phaoB.counteractivation()
phaoB.patientquickentry(0, "Cash")
phaoB.logout()

phaoB.login(pharmacyUserId, pharmacyUserPwd)
phaoB.activatePharmacyCounter()

#  Create PO
#phaoB.createPharmacyPurchaseOrder()
#phaoB.verifyPharmacyPurchaseOrder()

# Received GR from above PO
#phaoB.addPharmacyGRfromPO()

phaoB.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=mode)
phaoB.logout()
phaoB.closeBrowser()
