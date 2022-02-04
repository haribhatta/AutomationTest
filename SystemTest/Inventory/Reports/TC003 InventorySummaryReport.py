# Main objective: To verify inventory summary (value & qty) - 1.Opening 2.Closing, 3.Purchase, 4.Consumption, 5.StockManageIn, 6.StockManageOut

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

item = GSV.PhotocopyPaper
rate = GSV.photocopypaperRate
qty = 1
store1 = "Main Store"
store2 = "OT Store"
########
EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory="General Inventory")
LI.getInventorySummaryReport(danpheEMR=EMR)
LI.preInventorySummaryReport()
LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=item, rate=rate)
LI.getInventorySummaryReport(danpheEMR=EMR)
purchaseamount = rate*qty
print("purchaseamount", purchaseamount)
LI.verifyInventorySummaryReport(purchaseqty=qty, purchaseamount=purchaseamount, consumeqty=0, consumeamount=0, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)

# inventory rquisition from substore
# verification from verification module
# dispatch from inventory
# received by substore person
LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=item, qty=qty, store=store2)
#LSS.receivedStoreDispatch(store2)
LI.preInventorySummaryReport()
#LI.InventoryConsumption(item=item, qty=qty, store=store2)
consumptionamount = rate*qty
LI.getInventorySummaryReport(EMR)
LI.verifyInventorySummaryReport(purchaseqty=0, purchaseamount=0, consumeqty=qty, consumeamount=consumptionamount, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)
LI.preInventorySummaryReport()
LI.InventoryStockManage(danpheEMR=EMR, managetype='in')
manageinamount = rate*qty
LI.getInventorySummaryReport(EMR)
LI.verifyInventorySummaryReport(purchaseqty=0, purchaseamount=0, consumeqty=0, consumeamount=0, manageinqty=qty, manageinamount=manageinamount, manageoutqty=0, manageoutamount=0)
LI.preInventorySummaryReport()
LI.InventoryStockManage(danpheEMR=EMR, managetype='out')
manageoutamount = rate*qty
LI.getInventorySummaryReport(danpheEMR=EMR)
LI.verifyInventorySummaryReport(purchaseqty=0, purchaseamount=0, consumeqty=0, consumeamount=0, manageinqty=0,
                                 manageinamount=0, manageoutqty=qty, manageoutamount=manageoutamount)
AC.logout()
AC.closeBrowser()
