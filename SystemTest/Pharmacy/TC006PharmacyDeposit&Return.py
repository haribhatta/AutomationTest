from TestActionLibrary import A

# front desk user login
foUserId = A.foUserID
foUserPwd = A.foUserPwD
# pharmacy desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

pd = A()

pd.openBrowser()
pd.login(foUserId, foUserPwd)
pd.patientRegistration()
pd.logout()
pd.login(pharmacyUserId, pharmacyUserPwd)
pd.activatePharmacyCounter()
pd.getPharmacyDashboard()
pd.preSystemPharmacyDashboard()
pd.addPharmacyDeposit(deposit=1000)
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=0, deposit=1000, depositreturn=0, provisional=0, provisionacancel=0)
pd.returnPharmacyDeposit(depositreturn=1000)
pd.preSystemPharmacyDashboard()
pd.getPharmacyDashboard()
pd.verifyPharmacyDashboard(cash=0, cashreturn=0, credit=0, creditreturn=0, deposit=0, depositreturn=1000, provisional=0, provisionacancel=0)
pd.logout()
pd.closeBrowser()
