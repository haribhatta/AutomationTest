# Precondition>Settings:
# 1. AllowSubstoreDispatchWithoutVerification = 'true'
# 2. AllowSubstoreDispatchWithoutVerification = 'true

from TestActionLibrary import A

cs = A()
item = "10 ML DIS.SYRINGE"
qty = 1
rate = 6.49
store1 = "Main Store"
store2 = "OT Store"

cs.openBrowser()
cs.login('admin', 'pass123')
cs.getInventoryCurrentStockLevelReport(store=store1)
cs.preInventoryCurrentStockLevelReport()
cs.createInventoryDirectDispatch(itemname=item, qty=qty, store=store2)
cs.getInventoryCurrentStockLevelReport(store=store1)
cs.verifyInventoryCurrentStockLevelReport(type="out", qty=qty, unitprice=rate)
cs.getInventoryCurrentStockLevelReport(store=store2)
cs.preInventoryCurrentStockLevelReport()
cs.createInventoryDirectDispatch(itemname=item, qty=qty, store=store2)
cs.getInventoryCurrentStockLevelReport(store=store2)
cs.verifyInventoryCurrentStockLevelReport(type="in", qty=qty, unitprice=rate)
