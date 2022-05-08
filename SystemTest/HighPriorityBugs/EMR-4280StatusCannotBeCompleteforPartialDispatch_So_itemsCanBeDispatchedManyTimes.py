'''
Sanity_TC007
"Verify :
Steps to Reproduce :

 1.Navigate to Sub-store > Inventory > Inventory Requisition and create Requisition. Then

2.Navigate to Inventory >Internal > Requisition and see that requisition and click on Dispatch.

3. Dispatch partial quantity only (if 10 Request  dispatch 5 only)

4.Go back to requisition list and do again dispatch for remaining items . again go back to requisition list

5. check the status (status must be complete) if not try dispatch again.
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS
import Library.LibModuleVerification as LV

EMR = AC.openBrowser()
#############
# Inventory user login
storeUserid = GSV.adminUserID
storeUserPwd = GSV.storeUserPwD
drugSinex = GSV.drugSinexName
paymentMode = 'Cash'
itemname = GSV.storeItem1Name
StoreName = GSV.subStoreName1
inventoryName = GSV.inventoryName1
qty = 2
#############
AC.login(storeUserid, storeUserPwd)
requisitionNumber = LSS.createSubStoreRequisition(danpheEMR=EMR, InventoryName=inventoryName, ItemName=itemname, Qty=qty)
LV.substoreRequisitionVerification(danpheEMR=EMR, reqno=requisitionNumber, itemname=itemname, qty=qty)
LI.selectInventory(danpheEMR=EMR, inventory=inventoryName)
LI.dispatchRequisition(danpheEMR=EMR, ssReqNo=requisitionNumber, dispatchQuantity=1)
LI.verifyInventorypartialStatusofPartialDispatch(danpheEMR=EMR, ssReqNo=requisitionNumber, status="partial")
LI.dispatchRequisition(danpheEMR=EMR, ssReqNo=requisitionNumber, dispatchQuantity=1)
LI.verifyDispatchRequisition(EMR, requisitionNumber)
AC.logout()
AC.closeBrowser()