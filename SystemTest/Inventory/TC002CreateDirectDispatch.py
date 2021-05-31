from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD

cdd = A()
itemname = GSV.A4Paper
qty = 2

cdd.openBrowser()
cdd.login(adminUserId, adminUserPwd)
cdd.createInventoryDirectDispatch(itemname, qty)
