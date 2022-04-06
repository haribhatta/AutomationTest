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
itemname = GSV.storeItem1Name
StoreName = GSV.SubStore1
inventoryName = GSV.inventoryName1
qty = 2
#############
AC.login(storeUserid, storeUserPwd)
AC.verifyLogIn(EMR)
######## Inventory>Internal>Requisition: Direct Dispatch
RequisitionNo = LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=itemname, qty=qty, inventory=inventoryName, store=StoreName)
LI.verifyInventoryDirectDispatch(danpheEMR=EMR, RequisitionNo=RequisitionNo, itemname=itemname, qty=qty, store=StoreName)
######## Inventory>Internal>Purchase: Purchase Request
PRNo = LI.createPurchaseRequest(danpheEMR=EMR, ItemName= itemname, qty=qty)
print("Purchase Request No:", PRNo)
LI.verifyPurchaseRequest(danpheEMR=EMR, PRNo=PRNo, ItemName=itemname, qty=qty)
########SubStore>Inventory>Inventory Requisition: Create SubStore Requisition
#LSS.selectSubStore(substore=StoreName)
ssReqNo = LSS.createSubStoreRequisition(danpheEMR=EMR, InventoryName=inventoryName, ItemName=itemname, Qty=qty)
print("Sub Store Requisition No:", ssReqNo)
LSS.verifySubStoreRequisition(danpheEMR=EMR, ssReqNo=ssReqNo, InventoryName=inventoryName, ItemName=itemname, Qty=qty)
######## Dispatch Requisition
LI.dispatchRequisition(danpheEMR=EMR, ssReqNo=ssReqNo, dispatchQuantity=qty)
LI.verifyDispatchRequisition(EMR, ssReqNo)
######## DispatchReceived
LSS.receiveInventoryDispatch(EMR, substore=StoreName, ssReqNo=ssReqNo)
LSS.verifyReceivedInventoryDispatch(EMR, ssReqNo)
