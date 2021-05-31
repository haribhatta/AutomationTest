from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

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
