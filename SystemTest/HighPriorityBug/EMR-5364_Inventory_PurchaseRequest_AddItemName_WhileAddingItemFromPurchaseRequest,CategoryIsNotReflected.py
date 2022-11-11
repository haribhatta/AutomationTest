'''
Objective:
To test below check points:
1.
2.
'''
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSettings as LS
# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD
qty = 25
rate = 1
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory=inventory1)
LI.createPurchaseRequestByAddingNewItem(danpheEMR=EMR,qty=25)
AC.logout()
AC.closeBrowser()

