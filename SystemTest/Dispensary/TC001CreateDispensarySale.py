from TestActionLibrary import A
from GlobalShareVariables import GSV

mode = 'Cash'
drug = GSV.Sinex

phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD

ds = A()
#ds.applicationSelection()
ds.openBrowser()
ds.login(phuserid, phuserpwd)
ds.activatePharmacyCounter()
ds.createDispensarySaleRandomPatient(qty=1, drugname=drug, paymentmode=mode)
ds.logout()
ds.closeBrowser()
