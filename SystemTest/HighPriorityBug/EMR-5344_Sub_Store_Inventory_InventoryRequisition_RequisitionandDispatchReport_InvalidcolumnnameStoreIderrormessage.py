''''
Scripted by: Alina Shrestha
'''
########
import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleBilling as LB
import Library.LibModuleAppointment as LA
import Library.LibModuleInventory as LI
import Library.LibModuleVerification as LV
import Library.LibModuleSubStore as LSS

#############
# admin user login
admUserId = GSV.adminUserID
admUserPwd = GSV.adminUserPwD
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
########
InventoryName = GSV.inventoryName1
ItemName = GSV.storeItem1Name
substore = GSV.subStoreName2
#discountScheme = GSV.discountSchemeName
#############
EMR = AC.openBrowser()
AC.login(admUserId, admUserPwd)
ssReqNo = LSS.createSubStoreRequisition(EMR,InventoryName=InventoryName, ItemName=ItemName, Qty=1)
LSS.verifySubStoreRequisition(EMR, ssReqNo=ssReqNo, InventoryName=InventoryName, ItemName=ItemName, Qty=1)
LV.substoreRequisitionVerification(EMR, reqno=ssReqNo, itemname=ItemName, qty=1)
LI.dispatchRequisition(EMR, ssReqNo=ssReqNo, dispatchQuantity=1)
LSS.receiveInventoryDispatch(EMR, substore=substore,ssReqNo=ssReqNo)
LSS.verifyReceivedInventoryDispatch(EMR, ssReqNo=ssReqNo)
LSS.RequisitionandDispatchReport(EMR, ItemName,qty=1)
AC.logout()
AC.closeBrowser()