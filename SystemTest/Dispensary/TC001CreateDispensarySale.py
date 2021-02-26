from TestActionLibrary import A

mode = 'Cash'
drug = 'Sinex tab'

phuserid = A.pharmacyUserID
phuserpwd = A.pharmacyUserPwD

ds = A()
ds.applicationSelection()
ds.openBrowser()
ds.login(phuserid, phuserpwd)
ds.activatePharmacyCounter()
ds.createDispensarySaleRandomPatient(qty=1, drugname=drug, paymentmode=mode)
ds.logout()
ds.closeBrowser()
