from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD

didr = A()

itemname = GSV.A4Paper
qty = 1

didr.openBrowser()
didr.login(adminUserId, adminUserPwd)
didr.createInventoryDirectDispatch(itemname, qty)
didr.verifyInventoryDailyItemDispatchReport(itemname, qty)
