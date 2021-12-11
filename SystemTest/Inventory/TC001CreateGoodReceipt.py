'''
Objective:
To test below check points:
1.
2.
'''
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LS

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

itemname = GSV.stationaryItem1
qty = 1
inventory1 = GSV.Inventory1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(inventory=inventory1)
LI.createInventoryGoodReceipt(qty=qty, item=itemname, rate=1)
LI.editInventoryGoodsReceipt()
LI.createInventoryDirectDispatch(itemname, qty=qty, store=1)
AC.logout()
AC.closeBrowser()

print("There is existing bug: EMR-2576")
