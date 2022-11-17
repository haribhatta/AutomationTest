import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSettings as LS
# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD
vendorname = "LUMBINI TRADE STORE"

itemname = GSV.stationaryItem1
print("itemName:", itemname)
qty = 100.0
rate = 1.0
totalAmount = qty*rate
storeName = GSV.subStoreName1
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(EMR)
LI.selectInventory(danpheEMR=EMR, inventory=inventory1)
grNo = LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=itemname, rate=rate, paymentMode='Credit',
                                     NepaliReceipt=NepaliReceipt)
LI.verifyGoodReceiptNumberInGridAndShow(danpheEMR=EMR, billno=grNo, totalAmount=totalAmount, NepaliReceipt=NepaliReceipt)
LI.RetunToVendor(danpheEMR=EMR, vendorName=vendorname, billNo=grNo, GRno=grNo, purchaseQuantity=qty, returnqty=5,
                 purchaseRate=rate, returnRate=1, item=itemname)
AC.logout()
AC.closeBrowser()