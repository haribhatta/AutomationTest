'''
Precondition:
1. EnableReceivedItemInSubstore = flag need to be 'True'.

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
itemname = GSV.stationaryItem1
subStoreAccount = GSV.subStoreAccount
GeneralInventory = GSV.Inventory1
qty = 2
#############
AC.login(storeUserid, storeUserPwd)
AC.verifyLogIn()
######## Inventory>Internal>Requisition: Direct Dispatch
RequisitionNo = LI.createInventoryDirectDispatch(EMR, itemname, qty=qty, store=subStoreAccount)
LI.verifyInventoryDirectDispatch(EMR, RequisitionNo, itemname, qty, subStoreAccount)
######## Inventory>Internal>Purchase: Purchase Request
PRNo = LI.createPurchaseRequest(EMR, itemname, qty)
print("Purchase Request No:", PRNo)
LI.verifyPurchaseRequest(EMR, PRNo, itemname, qty)
########SubStore>Inventory>Inventory Requisition: Create SubStore Requisition
#LSS.selectSubStore(substore=StoreName)
ssReqNo = LSS.createSubStoreRequisition(EMR, subStoreName=subStoreAccount, InventoryName=GeneralInventory, ItemName=itemname, Qty=qty)
print("Sub Store Requisition No:", ssReqNo)
LSS.verifySubStoreRequisition(EMR, ssReqNo, subStoreAccount, itemname, qty)
######## Dispatch Requisition
LI.dispatchRequisition(EMR, ssReqNo, GeneralInventory, itemname, qty)
LI.verifyDispatchRequisition(EMR, ssReqNo)
######## DispatchReceived
#Precondition: EnableReceivedItemInSubstore = flag need to be 'True'.
LSS.receiveInventoryDispatch(EMR, ssReqNo)
LSS.verifyReceivedInventoryDispatch(EMR, ssReqNo)
