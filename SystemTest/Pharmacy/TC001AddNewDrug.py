from TestActionLibrary import A

# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

AND = A()

drugname = "Auto Test Drug"

AND.openBrowser()
AND.login(pharmacyUserId, pharmacyUserPwd)
AND.activatePharmacyCounter()
AND.addPharmacyItem()
AND.verifyPharmacyItem()
AND.logout()
AND.closeBrowser()

print("This tc is incomplete")
