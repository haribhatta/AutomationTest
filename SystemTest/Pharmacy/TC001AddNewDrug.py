from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

AND = A()

drugname = GSV.Testdrug

AND.openBrowser()
AND.login(pharmacyUserId, pharmacyUserPwd)
AND.activatePharmacyCounter()
AND.addPharmacyItem()
AND.verifyPharmacyItem()
AND.logout()
AND.closeBrowser()

print("This tc is incomplete")
