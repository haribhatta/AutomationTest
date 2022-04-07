import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.adminUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
# pharmacy user login
drug1Name = GSV.drug1BrandName
drug1Rate = GSV.drug1Rate
paymentMode = 'Cash'
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LD.verifyGenericNameOrItemNameInInvoice(danpheEMR=EMR, genericname=GSV.drug1GenericName, drugName=drug1Name, qty=1)