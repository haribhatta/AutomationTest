import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleProcurement as PO
import Library.LibModuleSubStore as LS
import Library.LibModulePatientPortal as LP

# front desk user login
storeUserId = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD

itemname1 = GSV.stationaryItem1
# itemname2 = GSV.stationaryItem2
print("itemName:", itemname1)
qty = 1
rate = 1
storeName = GSV.subStoreName1
inventory1 = GSV.inventoryName1

EMR = AC.openBrowser()
AC.login(storeUserId, storeUserPwd)
hospitalNo = LP.patientRegistration(danpheEMR=EMR)
PO.enablePatientConsumptionApplicable(danpheEMR=EMR, itemname="FACEMASK")
LS.countStockSub(danpheEMR=EMR, substore="Accounting", itemname="FACEMASK")
LS.prestockcountSub()
LS.createPatientConsumption(danpheEMR=EMR, substore="Accounting", hospitalNumber=hospitalNo, itemName="FACEMASK")
LS.countStockSub(danpheEMR=EMR, substore="Accounting", itemname="FACEMASK")
LS.verifyStockSub(qty=1)
AC.logout()
AC.closeBrowser()