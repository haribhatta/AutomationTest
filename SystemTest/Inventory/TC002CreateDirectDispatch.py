import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleInventory as LI

AC.applicationSelection()
AC.openBrowser()
#############
# Inventory user login
storeUserid = GSV.storeUserID
storeUserPwd = GSV.storeUserPwD
drugSinex = GSV.drugSinexName
paymentMode = 'Cash'
itemname = GSV.A4Paper
StoreName = GSV.SubStore1
qty = 2
#############
AC.login(storeUserid, storeUserPwd)
LI.createInventoryDirectDispatch(itemname, qty=qty, store=StoreName)
