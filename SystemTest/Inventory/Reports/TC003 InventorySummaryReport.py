# Main objective: To verify inventory summary (value & qty) - 1.Opening 2.Closing, 3.Purchase, 4.Consumption, 5.StockManageIn, 6.StockManageOut


from TestActionLibrary import A

# front desk user login
adminUserId = A.adminUserID
adminUserPwd = A.adminUserPwD

isr = A()
item = "PHOTOCOPY PAPER (CUTTING)"
rate = 430
qty = 1
store1 = "Main Store"
store2 = "OT Store"

isr.openBrowser()
isr.login(adminUserId, adminUserPwd)

isr.getInventorySummaryReport()
isr.preInventorySummaryReport()
isr.createInventoryGoodReceipt(qty=qty, item=item, rate=rate)
isr.getInventorySummaryReport()
purchaseamount = rate*qty
print("purchaseamount", purchaseamount)
isr.verifyInventorySummaryReport(purchaseqty=qty, purchaseamount=purchaseamount, consumeqty=0, consumeamount=0, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)

# inventory rquisition from substore
# verification from verification module
# dispatch from inventory
# received by substore person
isr.createInventoryDirectDispatch(itemname=item, qty=qty, store=store2)
isr.preInventorySummaryReport()
isr.InventoryConsumption(item=item, qty=qty)
consumptionamount = rate*qty
isr.getInventorySummaryReport()
isr.verifyInventorySummaryReport(purchaseqty=0, purchaseamount=0, consumeqty=qty, consumeamount=consumptionamount, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)

isr.preInventorySummaryReport()
isr.InventoryStockManage(managetype='in')
manageinamount = rate*qty
isr.getInventorySummaryReport()
isr.verifyInventorySummaryReport(purchaseqty=0, purchaseamount=0, consumeqty=0, consumeamount=0, manageinqty=qty, manageinamount=manageinamount, manageoutqty=0, manageoutamount=0)

isr.preInventorySummaryReport()
isr.InventoryStockManage(managetype='out')
manageoutamount = rate*qty
isr.getInventorySummaryReport()
isr.verifyInventorySummaryReport(purchaseqty=0, purchaseamount=0, consumeqty=0,consumeamount=0,manageinqty=0,
                                 manageinamount=0,manageoutqty=qty,manageoutamount=manageoutamount)
