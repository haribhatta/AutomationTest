'''
Objective:
To test below check points:
1.
2.
'''
import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

itemname = GSV.stationaryItem1
print("itemName:", itemname)
qty = 1
rate = 1
storeName = GSV.subStoreName1
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory=inventory1)
billno = LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=itemname, rate=rate, paymentMode='Credit')
LI.verifyGoodReceiptNUmberInGridAndShow(danpheEMR=EMR, billno=billno)
AC.logout()
AC.closeBrowser()
