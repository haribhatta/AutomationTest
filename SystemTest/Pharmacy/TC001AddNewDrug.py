from TestActionLibrary import A

AND = A()

drugname = "Auto Test Drug"

AND.openBrowser()
AND.login("pharmacy1", "pass123")
AND.activatePharmacyCounter()
AND.addPharmacyItem()
AND.verifyPharmacyItem()
AND.logout()
AND.closeBrowser()

print("This tc is incomplete")
