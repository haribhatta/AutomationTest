from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

drugname = GSV.Asthalin2MG
quantity = 2
rate = GSV.asthalin2mgRate
paymentmode = "CREDIT"
returnremark = "This is auto return"

RPI = A()

RPI.openBrowser()
RPI.login(foUserId, foUserPwd)
RPI.counteractivation()
RPI.patientquickentry(0, paymentmode)
RPI.logout()

RPI.login(pharmacyUserId, pharmacyUserPwd)
RPI.activatePharmacyCounter()
RPI.createPharmacyInvoiceTC(drugname=drugname, qty=quantity, paymentmode=paymentmode)
#RPI.verifyPharmacyInvoice3(drugname, quantity, rate)
RPI.returnPharmacyInvoice(qty=quantity, returnremark=returnremark)
RPI.verifyReturnPharmacyInvoice(paymentmode, returnRemark=returnremark)
RPI.logout()
RPI.closeBrowser()
# This has open bug: EMR-2630
