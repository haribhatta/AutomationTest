from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

#Drug name for billing
drugname = GSV.drug1BrandName
genericname = GSV.drug1GenericName
rate = GSV.drug1Rate
quantity = 1
mode = "Cash"


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
