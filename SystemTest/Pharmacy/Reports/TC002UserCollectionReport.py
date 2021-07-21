from TestActionLibrary import A
from GlobalShareVariables import GSV

# pharmacy desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

# front desk user login
billingId = GSV.foUserID
billingPwd = GSV.foUserPwD

ucc = A()
drugname = GSV.drug1BrandName
qty = 1
paymode = 'Cash'
rate = GSV.drug1Rate
amount = qty*rate
totalamount = amount
remark = "This is test return."

ucc.openBrowser()
# To get random patient information
ucc.login(userid=billingId, pwd=billingPwd)
ucc.getRandomPatient()
ucc.logout()
# Start of User collection report
ucc.login(pharmacyUserId, pharmacyUserPwd)
ucc.activatePharmacyCounter()
ucc.createPharmacyInvoiceAnonymous(drugname=drugname, qty=qty, paymentmode=paymode)
ucc.getPharmacyUserCollectionReport(pharmacyUserId)
ucc.getStockDetail(drugname=drugname)
ucc.createPharmacyInvoiceTC(qty=qty, drugname=drugname, paymentmode='Cash')
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(pharmacyUserId)
ucc.verifySystemPharmacyUserCollectionReport(cash=totalamount, cashreturn=0, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.returnPharmacyInvoice(qty=qty, returnremark=remark)
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(pharmacyUserId)
ucc.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=totalamount, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.createPharmacyInvoiceTC(drugname=drugname, qty=qty, paymentmode='Credit')
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(pharmacyUserId)
ucc.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=amount, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.returnPharmacyInvoice(qty=qty, returnremark=remark)
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(pharmacyUserId)
ucc.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=amount, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.logout()
ucc.closeBrowser()

# Test script is failling with bug: EMR-2764.
