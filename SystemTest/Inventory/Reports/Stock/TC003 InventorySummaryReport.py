# Main objective: To verify inventory summary (value & qty) - 1.Opening 2.Closing, 3.Purchase, 4.Consumption, 5.StockManageIn, 6.StockManageOut

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS

# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.adminUserPwD

item = "Pencil"
rate = 5
qty = 1
costAmount = rate * qty

subStore1 = GSV.SubStore1
subStore2 = GSV.SubStore2
########
EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory="General Inventory")
LI.getInventorySummaryReport(EMR)
LI.preInventorySummaryReport()
LI.createInventoryGoodReceipt(EMR, qty, item, rate)
LI.receiveGoodReceipt(EMR)
RequsitionNo = LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=item, qty=qty, inventory="General Inventory", store=subStore1)
print(RequsitionNo)
LSS.receiveInventoryDispatch(EMR, substore=subStore1, ssReqNo=RequsitionNo)
LSS.createNewConsumption(danpheEMR=EMR, substore=subStore1, itemName=item)
LI.getInventorySummaryReport(EMR)
LI.verifyInventorySummaryReport(purchaseqty=1, purchaseamount=costAmount, consumeqty=1, consumeamount=costAmount, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)
AC.logout()
AC.closeBrowser()
