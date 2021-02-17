from TestActionLibrary import A

# front desk user login
adminUserId = A.adminUserID
adminUserPwd = A.adminUserPwD

didr = A()

itemname = 'Paper A4'
qty = 1

didr.openBrowser()
didr.login(adminUserId, adminUserPwd)
didr.createInventoryDirectDispatch(itemname, qty)
didr.verifyInventoryDailyItemDispatchReport(itemname, qty)
