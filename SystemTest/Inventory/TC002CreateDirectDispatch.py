from TestActionLibrary import A

# front desk user login
adminUserId = A.adminUserID
adminUserPwd = A.adminUserPwD

cdd = A()
itemname = 'Paper A4'
qty = 2

cdd.openBrowser()
cdd.login(adminUserId, adminUserPwd)
cdd.createInventoryDirectDispatch(itemname, qty)
