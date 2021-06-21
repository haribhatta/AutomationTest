from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD

si = A()

drug = GSV.drug1BrandName

si.openBrowser()
si.login(pharmacyUserId, pharmacyUserPwd)
si.getStockDetail(drugname=drug)
si.getStoreDetail(drugname=drug)
si.verifyStockItemsReport(drugname=drug)

# Test script is failed with bug: EMR-2767
