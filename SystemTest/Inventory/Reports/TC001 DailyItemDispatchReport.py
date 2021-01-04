from TestActionLibrary import A

didr = A()

itemname = 'Paper A4'
qty = 1

didr.openBrowser()
didr.login('admin', 'pass123')
didr.createInventoryDirectDispatch(itemname, qty)
didr.verifyInventoryDailyItemDispatchReport(itemname, qty)
