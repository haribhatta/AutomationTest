import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleProcurement as PO
import Library.LibModuleSettings as LS

# front desk user login
storeUserId = GSV.storeUserID
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
PO.activateInventory(danpheEMR=EMR, inventory='General Inventory' or 'Medical Inventory')
PO.CreateGoodsArrivalNotification(danpheEMR=EMR, rate=1, itemName1=GSV.stationaryItem1, itemName2=GSV.stationaryItem2)
