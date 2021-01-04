from TestActionLibrary import A

cdd = A()
itemname = 'Paper A4'
qty = 2

cdd.openBrowser()
cdd.login('admin', 'pass123')
cdd.createInventoryDirectDispatch(itemname, qty)
