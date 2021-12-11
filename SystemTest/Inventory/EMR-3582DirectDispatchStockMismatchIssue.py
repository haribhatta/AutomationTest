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

foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
itemname = 'A4 PAPER'
qty = 1
store = 'Emergency Sto'
StoreName = 'Emergency Sto'
ItemName = 'A4 PA'

EMR = AC.openBrowser()
AC.login(foUserId, foUserPwd)
LI.activateInventory(inventory='General Inventory')
itemstock = LI.countStock(itemname=itemname)
preitemstock = LI.preCountStock(itemstock)
requisitionNo = LI.createInventoryDirectDispatch(itemname=itemname, qty=qty, store=store)
itemstock = LI.countStock(itemname=itemname)
LI.verifyStock(qty, preitemstock, itemstock)
LS.selectSubStore(substore="Emergency Store")
stock = LS.countStockSub(itemname)
preStock = LS.prestockcountSub(stock)
LS.receiveInventoryDispatch(ssReqNo=requisitionNo)
stock = LS.countStockSub(itemname)
LS.verifyStockSub(qty, preStock, stock)

# LI.verifyInventoryDirectDispatch(RequisitionNo=requisitionNo, itemname=ItemName, qty=qty, store=StoreName)
