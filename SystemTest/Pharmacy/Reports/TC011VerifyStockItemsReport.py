from TestActionLibrary import A

si = A()

drug = 'SINEX TAB'

si.openBrowser()
si.login("pharmacy1", "pass123")
si.getStockDetail(drugname=drug)
si.getStoreDetail(drugname=drug)
si.verifyStockItemsReport(drugname=drug)

# Test script is failed with bug: EMR-2767
