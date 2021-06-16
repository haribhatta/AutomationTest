from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

pd = A()
drug = GSV.drug1BrandName
rate = GSV.drug1Rate
qty = 2
amount = rate*qty
print("Amount", amount)

pd.openBrowser()
pd.login(pharmacyUserId, pharmacyUserPwd)
pd.getPharmacyDashboard()
pd.preSystemPharmacyDashboard()
pd.activatePharmacyCounter()
pd.createPharmacyInvoiceAnonymous(drugname=drug, qty=qty, paymentmode='Cash')
#pd.createDispensarySaleRandomPatient(drugname=drug, qty=qty, paymentmode='Cash')
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=amount, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
pd.preSystemPharmacyDashboard()
pd.returnPharmacyInvoice(qty=qty, returnremark="This is cash bill return")
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=0, cashreturn=amount, credit=0, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
pd.preSystemPharmacyDashboard()
pd.createPharmacyInvoiceRandomPatient(drugname=drug, qty=qty, paymentmode='CREDIT')
pd.getPharmacyDashboard()
#pd.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=amount, creditreturn=0, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
pd.preSystemPharmacyDashboard()
pd.returnPharmacyInvoice(qty=qty, returnremark="This is credit bill return")
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=amount, deposit=0, depositreturn=0, provisional=0, provisionacancel=0)
pd.logout()
pd.closeBrowser()


