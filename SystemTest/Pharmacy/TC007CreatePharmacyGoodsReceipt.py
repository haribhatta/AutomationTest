from TestActionLibrary import A

# pharmacy desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

cpgr = A()
qty = 50

cpgr.openBrowser()
cpgr.login(pharmacyUserId, pharmacyUserPwd)
cpgr.activatePharmacyCounter()
cpgr.addPharmacyItem()
cpgr.verifyPharmacyItem()
cpgr.createPharmacyGoodsReceipt(qty)
cpgr.verifyPharmacyGoodsReceipt(qty)
cpgr.logout()
cpgr.closeBrowser()
#Blocked by bug EMR-2591
#Failed with bug EMR-3177