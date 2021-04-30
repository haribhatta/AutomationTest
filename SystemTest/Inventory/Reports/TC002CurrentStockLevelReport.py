# Precondition>Settings:
# 1. AllowSubstoreDispatchWithoutVerification = 'true'
# 2. AllowSubstoreDispatchWithoutVerification = 'true

# The objective of this test case is to verify current stock level report for inventory.
# Scenarios to check:
# 1. Verify stock level for manage out case.
# 2. Verify stock level for manage in cas.
# 3. Verify stock level for dispatch out case.
# 4. Verify stock level for goods receipt case.

from TestActionLibrary import A

# front desk user login
adminUserId = A.adminUserID
adminUserPwd = A.adminUserPwD

cs = A()
item = "10 ML DIS.SYRINGE"
qty = 1
rate = 6.49
store1 = "Main Store"
store2 = "OT Store"

cs.openBrowser()
cs.login(adminUserId, adminUserPwd)
cs.getInventoryCurrentStockLevelReport(store=store1)
cs.preInventoryCurrentStockLevelReport()
cs.createInventoryDirectDispatch(itemname=item, qty=qty, store=store2)
cs.getInventoryCurrentStockLevelReport(store=store1)
print("Start: Stock Out proces")
cs.verifyInventoryCurrentStockLevelReport(type="out", qty=qty, unitprice=rate)
cs.getInventoryCurrentStockLevelReport(store=store2)
cs.preInventoryCurrentStockLevelReport()
cs.createInventoryDirectDispatch(itemname=item, qty=qty, store=store2)
# store need to received the items to increase in it's store
cs.receivedStoreDispatch()
cs.getInventoryCurrentStockLevelReport(store=store2)
print("Start: Store In process")
cs.verifyInventoryCurrentStockLevelReport(type="in", qty=qty, unitprice=rate)
