from TestActionLibrary import A

# front desk user login
pharmacyUserId = A.pharmacyUserID
pharmacyUserPwd = A.pharmacyUserPwD

si = A()

drug = 'SINEX TAB'

si.openBrowser()
si.login(pharmacyUserId, pharmacyUserPwd)
si.getStockDetail(drugname=drug)
si.getStoreDetail(drugname=drug)
si.verifyStockItemsReport(drugname=drug)

# Test script is failed with bug: EMR-2767
