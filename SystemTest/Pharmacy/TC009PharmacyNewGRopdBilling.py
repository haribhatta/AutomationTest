from TestActionLibrary import A
from GlobalShareVariables import GSV

paymentmode = "Cash"
qty = 50

phaoB = A()
exec(open("TC008PharmacyNewGRStore2StockTransfer.py").read())
phaoB.createPharmacyOPDBilling(qty, paymentmode)
phaoB.logout()
phaoB.closeBrowser()
