# Precondition>Settings:
# 1. AllowSubstoreDispatchWithoutVerification = 'true'
# 2. AllowSubstoreDispatchWithoutVerification = 'true

# The objective of this test case is to verify current stock level report for inventory.
# Scenarios to check:
# 1. Verify stock level for manage out case.
# 2. Verify stock level for manage in cas.
# 3. Verify stock level for dispatch out case. #dispatch requisition case
# 4. Verify stock level for goods receipt case. #consumption case

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS


# front desk user login
adminUserId = GSV.adminUserID
adminUserPwd = GSV.adminUserPwD
opdAmt = GSV.opdRate
user = GSV.foUserID
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
########
item = GSV.storeItem1Name
print("Item:", item)
qty = 1
rate = GSV.storeItem1Rate
print("Rate:", rate)
store1 = GSV.store1
Inventory1 = GSV.Inventory1
########
EMR = AC.openBrowser()
AC.login(adminUserId, adminUserPwd)
LI.selectInventory(danpheEMR=EMR, inventory=Inventory1)
LI.getInventoryStoreCurrentStockLevelReport(danpheEMR=EMR, inventory=Inventory1, store=store1)
LI.preInventoryStoreCurrentStockLevelReport()
#dispatch requisition or direct dispatch: This need to deduct qty/amount from main store and increase in substore
dispatchNo = LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=item, qty=qty, inventory=Inventory1, store=store1)
'''
# For CoreCFG parameter setting-'Receive not needed': store need to received the items to increase in it's store
'''
LSS.receiveInventoryDispatch(danpheEMR=EMR, substore=store1, ssReqNo=dispatchNo)

LI.getInventoryStoreCurrentStockLevelReport(danpheEMR=EMR, inventory=Inventory1, store=store1)
LI.verifyInventoryStoreCurrentStockLevelReport(type="DirectDispatch", qty=qty, unitprice=rate)
#consumption case: This need to deduct qty/amount from subStore and no change in main store
LI.preInventoryStoreCurrentStockLevelReport()
LI.consumptionStore(danpheEMR=EMR, itemName=item, qty=qty, store=store1)
LI.getInventoryStoreCurrentStockLevelReport(danpheEMR=EMR, inventory=Inventory1, store=store1)
LI.verifyInventoryStoreCurrentStockLevelReport(type="SubStoreConsumption", qty=qty, unitprice=rate)
'''
############# Manage Stock is disable for all hospitals hence Manage Stock scenario is kept OnHold ########

#Manage Stock case: ManageIn must increase qty/amount and ManageOut must decrease qty/amount.
## Action: ManageIn
LI.preInventoryStoreCurrentStockLevelReport()
LI.InventoryStockManage(danpheEMR=EMR, managetype='in')
LI.getInventoryStoreCurrentStockLevelReport(danpheEMR=EMR, inventory=Inventory1, store=store1)
LI.verifyInventoryStoreCurrentStockLevelReport(type="SubStoreConsumption", qty=qty, unitprice=rate)
## Action: ManageOut
LI.preInventoryStoreCurrentStockLevelReport()
LI.InventoryStockManage(danpheEMR=EMR, managetype='out')
LI.getInventoryStoreCurrentStockLevelReport(danpheEMR=EMR, inventory=Inventory1, store=store1)
LI.verifyInventoryStoreCurrentStockLevelReport(type="SubStoreConsumption", qty=qty, unitprice=rate)
'''
AC.logout()
AC.closeBrowser()
