# Main objective: To verify inventory summary (value & qty) - 1.Opening 2.Closing, 3.Purchase, 4.Consumption, 5.StockManageIn, 6.StockManageOut

import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LSS
import Library.LibModuleSettings as LS

# front desk user login
storeUserId = GSV.adminUserID
storeUserPwd = GSV.adminUserPwD

item = "Pencil"
rate = 5
qty = 1
costAmount = rate * qty

subStore1 = GSV.subStoreName1
subStore2 = GSV.subStoreName2
########
EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
flagReceivedItemInSubstore = LS.EnableReceivedItemInSubstore(EMR)
print("flagReceivedItemInSubstore:", flagReceivedItemInSubstore)
NepaliReceipt = LS.CheckNepaliReceiptValue(EMR)
LI.selectInventory(danpheEMR=EMR, inventory="General Inventory")
LI.getInventorySummaryReport(danpheEMR=EMR)
LI.preInventorySummaryReport()
### Create GR Credit entry
LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=item, rate=rate, paymentMode='Credit', NepaliReceipt=NepaliReceipt)
LI.receiveGoodReceipt(danpheEMR=EMR)
### Create Inventory DD
RequsitionNo = LI.createInventoryDirectDispatch(danpheEMR=EMR, itemname=item, qty=qty, inventory="General Inventory", store=subStore1)
### Receive Inventory dispatch
if flagReceivedItemInSubstore == "true":
    LSS.receiveInventoryDispatch(danpheEMR=EMR, substore=subStore1, ssReqNo=RequsitionNo)
###TestAction: Create SubStore Consumption
LSS.createNewConsumption(danpheEMR=EMR, substore=subStore1, itemName=item)
LI.getInventorySummaryReport(danpheEMR=EMR)
LI.verifyInventorySummaryReport(purchaseqty=1, purchaseamount=costAmount, consumeqty=1, consumeamount=costAmount, manageinqty=0, manageinamount=0, manageoutqty=0, manageoutamount=0)
AC.logout()
AC.closeBrowser()
