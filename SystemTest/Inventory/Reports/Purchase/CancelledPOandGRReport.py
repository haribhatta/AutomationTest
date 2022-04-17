import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleProcurement as LP
import Library.LibModuleSettings as LS

# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD

item = "Pencil"
item2 = "WEIGHT MATCHINE"
rate = 5
qty = 1
store1 = "Main Store"
store2 = "Accounting Store"
########
EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(EMR)
LI.activateInventory(EMR, 'General Inventory')
BillNo = LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=item, rate=rate, paymentMode="Credit", NepaliReceipt=NepaliReceipt)
print("Bill Number of Given Good Receipt is :", BillNo)
LP.cancelInventoryGoodsReceipt(EMR, BillNo=BillNo)
pono = LP.createPurchaseOrder(EMR, itemName1=item, qty=qty, rate=rate, itemName2=item2)
print("Purchase Order Number is :", pono)
LP.cancelPurchaseOrder(EMR, pono)
LI.getCancelPoReport(EMR, pono)
LI.getCancelGRReport(EMR, BillNo)
AC.logout()
AC.closeBrowser()