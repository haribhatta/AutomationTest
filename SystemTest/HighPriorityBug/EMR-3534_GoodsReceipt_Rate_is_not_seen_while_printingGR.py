
#Objective:
#To test below check points:
#1. Create inventory goods receipt.
#2. Verify rate while printing goods receipt.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSettings as LS

# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD

itemname = GSV.stationaryItem1
print("itemName:", itemname)
qty = 1
rate = 10
storeName = GSV.subStoreName1
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(EMR)
LI.selectInventory(danpheEMR=EMR, inventory=inventory1)
grNo = LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=itemname, rate=rate, paymentMode='Credit', NepaliReceipt=NepaliReceipt)
#LI.editInventoryGoodsReceipt(danpheEMR=EMR, BillNo=grNo)
AC.logout()
AC.closeBrowser()
