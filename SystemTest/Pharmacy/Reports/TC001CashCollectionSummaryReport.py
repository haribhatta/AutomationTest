from TestActionLibrary import A

user = 'pharmacy1'

drugname = 'MONOTRATE-20MG TAB'
qty = 1
rate = 4.86
amount = qty*rate
totalamount = round(amount)
remark = "This is test return."

ccsr = A()
ccsr.openBrowser()
ccsr.login(user, 'pass123')
ccsr.activatePharmacyCounter()
ccsr.getPharmacyCashCollectionSummary(user)
ccsr.getStockDetail(drugname=drugname)
ccsr.getRandomPatient()
ccsr.createPharmacyInvoiceTC(qty=qty, drugname=drugname, paymentmode='Cash')
ccsr.preSystemPharmacyCashCollectionSummary()
ccsr.getPharmacyCashCollectionSummary(user)
ccsr.verifyPharmacyCashCollectionSummary(cash=totalamount, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=0, discount=0)
ccsr.returnPharmacyInvoice(qty=qty, returnremark=remark)
ccsr.preSystemPharmacyCashCollectionSummary()
ccsr.getPharmacyCashCollectionSummary(user)
ccsr.verifyPharmacyCashCollectionSummary(cash=0, cashreturn=amount, credit=0, creditreturn=0, deposit=0, depositreturn=0, discount=0)
ccsr.logout()
ccsr.closeBrowser()