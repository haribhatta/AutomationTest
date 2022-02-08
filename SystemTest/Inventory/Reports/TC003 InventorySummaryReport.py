# Main objective: To verify inventory summary (value & qty) - 1.Opening 2.Closing, 3.Purchase, 4.Consumption, 5.StockManageIn, 6.StockManageOut

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

item = "Pencil"
rate = 5
qty = 1
store1 = "Main Store"
store2 = "Accounting Store"
########
EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory="General Inventory")
LI.getInventorySummaryReport(EMR)
LI.preInventorySummaryReport()
LI.createInventoryGoodReceipt(EMR, qty, item, rate)
LI.receiveGoodReceipt(EMR)
RequsitionNo = LI.createInventoryDirectDispatch(EMR, item, qty, "General Inventory", store2)
print(RequsitionNo)
LSS.receiveInventoryDispatch(EMR, substore=store2, ssReqNo=RequsitionNo)
LSS.createNewConsumption(danpheEMR=EMR, substore=store2, itemName=item)
LI.getInventorySummaryReport(EMR)
LI.verifyInventorySummaryReport(purchaseqty=1, purchaseamount=5, consumeqty=1, consumeamount=8, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)
AC.logout()
AC.closeBrowser()
