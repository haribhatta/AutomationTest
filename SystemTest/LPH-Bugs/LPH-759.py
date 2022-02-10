''''
Sub store : Inventory : Requisition | Create Requisition not working.

Create Requisition not working.

Navigation: Substore → Inventory → Inventory Requisition → Create Requisition
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleSubStore as LSS
import Library.LibModuleSubStore as LS
import Library.LibModulePatientPortal as LPP
import Library.LibModuleBilling as LB
import Library.LibModuleADT as LADT

# front desk user login
StoreUserId = GSV.storeUserID
StoreUserPwd = GSV.storeUserPwD

#Declaring store values
Store1 = GSV.SubStore1
Inventory1 = GSV.Inventory1
ItemName1 = GSV.stationaryItem1
Qty1 = 3

EMR = AC.openBrowser()
AC.login(StoreUserId, StoreUserPwd)
LSS.selectSubStore(substore=Store1)
LSS.createSubStoreRequisition(InventoryName=Inventory1, ItemName=ItemName1, Qty=Qty1)