from TestActionLibrary import A

paymentmode = "Cash"
qty = 50

phaoB = A()
exec(open("TC008PharmacyNewGRStore2StockTransfer.py").read())
phaoB.createPharmacyOPDBilling(qty, paymentmode)
phaoB.logout()
phaoB.closeBrowser()
