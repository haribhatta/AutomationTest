import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
#AC.applicationSelection()
EMR = AC.openBrowser()
#############
# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD
departmentGynae = GSV.departmentGyno
doctorGynae = GSV.doctorGyno
# pharmacy user login
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
drug1Name = GSV.drug1BrandName
drug1Rate = GSV.drug1Rate
paymentMode = 'Cash'
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType)
AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
pInvoiceNo = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drug1Name, paymentmode=paymentMode)
LD.returnDispensaryInvoice(EMR, pInvoiceNo, qty=1, returnremark="Wrong entry")
LD.verifyReturnDispensaryInvoice(danpheEMR=EMR, InvoiceNo=pInvoiceNo, paymentmode=paymentMode, returnRemark="Wrong entry")
AC.logout()
AC.closeBrowser()
