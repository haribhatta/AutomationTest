# Inventory | Direct Dispatch Stock Mismatch Issue

# 1: Proceed Direct Dispatch from Inventory(Any ie Medical or General) to Sub Store(any);
#     a: Check the Availability in Inventory Stock.
#
# 2: Navigate to SubStore and Go inside that dispatched SubStore;
#   a: Receive the Item.
#   b: After receiving, Stock in that SubStore must Increase AND Stock in Dispatch-From Inventory must Decrease.

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI
import Library.LibModuleSubStore as LS
import Library.LibModuleSettings as LSS

foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
itemname = 'A4 PAPER'
qty = 1
store = 'Emergency Store'
StoreName = 'Emergency Store'
ItemName = 'A4 PA'
rate = 10

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
NepaliReceipt = LSS.CheckNepaliReceiptValue(EMR)
LI.activateInventory(EMR, inventory='General Inventory')
BillNo = LI.createInventoryGoodReceipt(danpheEMR=EMR, qty=qty, item=itemname, rate=rate, paymentMode="Credit", NepaliReceipt=NepaliReceipt)
LI.receiveGoodReceipt(EMR)
itemstock = LI.countStock(EMR, itemname=itemname)
preitemstock = LI.preCountStock(itemstock)
requisitionNo = LI.createInventoryDirectDispatch(EMR, itemname=itemname, qty=qty, inventory='General Inventory', store=store)
itemstock = LI.countStock(EMR, itemname=itemname)
LI.verifyStock(qty, preitemstock, itemstock)
LS.selectSubStore(EMR, substore="Emergency Store")
LS.receiveInventoryDispatch(EMR, substore=store, ssReqNo=requisitionNo)
stock = LS.countStockSub(EMR, itemname)
preStock = LS.prestockcountSub(stock)
LS.receiveInventoryDispatch(EMR, substore=store, ssReqNo=requisitionNo)
stock = LS.countStockSub(EMR, itemname)
LS.verifyStockSub(qty, preStock, stock)

# LI.verifyInventoryDirectDispatch(RequisitionNo=requisitionNo, itemname=ItemName, qty=qty, store=StoreName)
