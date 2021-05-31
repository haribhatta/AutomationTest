from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

cgr = A()

itemname = GSV.Pencil
qty = 1

cgr.openBrowser()
cgr.login(storeUserId, storeUserPwd)
cgr.createInventoryGoodReceipt(qty=qty, item=itemname, rate=1)
cgr.editInventoryGoodsReceipt()
cgr.createInventoryDirectDispatch(itemname, qty=qty, store=1)
cgr.logout()
cgr.closeBrowser()

print("There is existing bug: EMR-2576")
