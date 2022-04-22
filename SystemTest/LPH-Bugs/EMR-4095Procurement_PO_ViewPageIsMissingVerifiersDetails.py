import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleVerification as LV
import Library.LibModuleSettings as LS
import Library.LibModuleProcurement as LP
import Library.LibModuleInventory as LI
# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD

itemname1 = GSV.stationaryItem1
itemname2 = GSV.stationaryItem2
print("itemName:", itemname1)
qty = 1
rate = 1
storeName = GSV.subStoreName1
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(EMR)
LI.selectInventory(danpheEMR=EMR, inventory=inventory1)
purchaseNumber = LP.createPurchaseOrder(danpheEMR=EMR, itemName1=itemname1, rate=rate, itemName2=itemname2, NepaliReceipt=NepaliReceipt)
LV.verifyInventoryPurchaseOrder(danpheEMR=EMR, NepaliReceipt=NepaliReceipt, purchaseOrderNo=purchaseNumber, itemname=itemname1, quantity=qty)
LP.verifyPOVerifyer(danpheEMR=EMR, pono=purchaseNumber, NepaliReceipt=NepaliReceipt)
AC.logout()
AC.closeBrowser()