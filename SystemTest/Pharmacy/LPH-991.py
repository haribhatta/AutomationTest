# Pharmacy | Good Receipt | Failed to add Good receipt.

''''
Steps:

Navigate to Pharmacy → Order → Good Receipt.

Add all the mandatory value and Print Receipt.
'''

from TestActionLibrary import A
from GlobalShareVariables import GSV

# front desk user login
pharmacyUserId = GSV.pharmacyUserID
pharmacyUserPwd = GSV.pharmacyUserPwD
Qty1 = 1
Drug1 = GSV.drug1BrandName
Drug1Price = GSV.drug1Rate

TA = A()

TA.openBrowser()
TA.login(pharmacyUserId, pharmacyUserPwd)
TA.activatePharmacyCounter()
TA.createPharmacyGoodsReceipt(qty=Qty1, DrugName=Drug1, grPrice=Drug1Price)