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
print("itemName:", itemname)
qty = 1
inventory1 = GSV.Inventory1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory=inventory1)
grNo = LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=itemname, rate=1)
LI.editInventoryGoodsReceipt(danpheEMR=EMR, BillNo=grNo)
print("There is existing bug: EMR-4850")
LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=itemname, qty=qty, store=1, inventory=inventory1)
AC.logout()
AC.closeBrowser()
print("There is existing bug: EMR-4850")
