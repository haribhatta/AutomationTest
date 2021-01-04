from TestActionLibrary import A

ucc = A()
drugname = 'MONOTRATE-20MG TAB'
qty = 1
paymode = 'Cash'
rate = 4.86
amount = qty*rate
totalamount = amount
user = 'pharmacy1'
remark = "This is test return."

ucc.openBrowser()
ucc.login(user, 'pass123')
ucc.activatePharmacyCounter()
ucc.createPharmacyInvoiceAnonymous(drugname=drugname, qty=qty, paymentmode=paymode)
ucc.getPharmacyUserCollectionReport(user)
ucc.getStockDetail(drugname=drugname)
ucc.getRandomPatient()
ucc.createPharmacyInvoiceTC(qty=qty, drugname=drugname, paymentmode='Cash')
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(user)
ucc.verifySystemPharmacyUserCollectionReport(cash=totalamount, cashreturn=0, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.returnPharmacyInvoice(qty=qty, returnremark=remark)
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(user)
ucc.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=totalamount, credit=0, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.createPharmacyInvoiceTC(drugname=drugname, qty=qty, paymentmode='Credit')
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(user)
ucc.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=amount, creditreturn=0, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.returnPharmacyInvoice(qty=qty, returnremark=remark)
ucc.preSystemPharmacyUserCollectionReport()
ucc.getPharmacyUserCollectionReport(user)
ucc.verifySystemPharmacyUserCollectionReport(cash=0, cashreturn=0, credit=0, creditreturn=amount, creditsettlement=0,
                                             discount=0, deposit=0, depositreturn=0, provisional=0, provisionalcancel=0)
ucc.logout()
ucc.closeBrowser()

# Test script is failling with bug: EMR-2764.
