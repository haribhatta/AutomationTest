import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI

# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
itemName = 'PLANE SCISSOR 6"'
qty = 1
inventoryName = 'General Inventory'
storeName = 'OPD'
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=itemName, qty=qty, inventory=inventoryName, store=storeName)
LI.verifyInventoryDailyItemDispatchReport(danpheEMR=EMR, itemname=itemName, qty=qty, storeName=storeName)
