from TestActionLibrary import A

# front desk user login
storeUserId = A.storeUserID
storeUserPwd = A.storeUserPwD

cgr = A()

itemname = "PENCIL"
qty = 1

cgr.openBrowser()
cgr.login(storeUserId, storeUserPwd)
cgr.createInventoryGoodReceipt(qty=qty, item=itemname, rate=1)
cgr.createInventoryDirectDispatch(itemname, qty=qty, store=1)
cgr.logout()
cgr.closeBrowser()

print("There is existing bug: EMR-2576")
