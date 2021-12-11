'''
Sanity_TC007
"Verify :
1. inventory Purchase Request (PR) & Direct Dispatch (DD) entry,
2. Inventory requisition, inventory dispatch and inventory received."
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS

EMR = AC.openBrowser()
#############
# Inventory user login
storeUserid = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD
drugSinex = GSV.drugSinexName
paymentMode = 'Cash'
itemname = GSV.File
StoreName = GSV.SubStore1
GeneralInventory = GSV.GeneralInventory
qty = 2
#############
AC.login(storeUserid, storeUserPwd)
AC.verifyLogIn()
######## Inventory>Internal>Requisition: Direct Dispatch
RequisitionNo = LI.createInventoryDirectDispatch(itemname, qty=qty, store=StoreName)
LI.verifyInventoryDirectDispatch(RequisitionNo, itemname, qty, StoreName)
######## Inventory>Internal>Purchase: Purchase Request
PRNo = LI.createPurchaseRequest(itemname, qty)
print("Purchase Request No:", PRNo)
LI.verifyPurchaseRequest(PRNo, itemname, qty)
########SubStore>Inventory>Inventory Requisition: Create SubStore Requisition
#LSS.selectSubStore(substore=StoreName)
ssReqNo = LSS.createSubStoreRequisition(InventoryName=GeneralInventory, ItemName=itemname, Qty=qty)
print("Sub Store Requisition No:", ssReqNo)
LSS.verifySubStoreRequisition(ssReqNo, StoreName, itemname, qty)
######## Dispatch Requisition
LI.dispatchRequisition(ssReqNo, GeneralInventory, itemname, qty)
LI.verifyDispatchRequisition(ssReqNo)
######## DispatchReceived
LSS.receiveInventoryDispatch(ssReqNo)
LSS.verifyReceivedInventoryDispatch(ssReqNo)
