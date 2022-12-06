import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSettings as LS


# Front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
NepaliReceipt = LS.CheckNepaliReceiptValue(danpheEMR=EMR)
LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=10, item='A4 PAPER', rate=20, paymentMode='cash', NepaliReceipt=NepaliReceipt)
LI.getpurchaseitemreport(danpheEMR=EMR)
AC.logout()
AC.closeBrowser()

