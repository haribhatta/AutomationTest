from TestActionLibrary import A

cgr = A()

itemname = "BALL PEN"
qty = 1

cgr.openBrowser()
cgr.login('inventory', 'pass123')
cgr.createInventoryGoodReceipt(qty=qty, item=itemname, rate=1)
cgr.createInventoryDirectDispatch(itemname, qty=qty, store=1)
cgr.logout()
cgr.closeBrowser()

print("There is existing bug: EMR-2576")
