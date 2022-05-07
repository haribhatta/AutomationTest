import Library.GlobalShareVariables as GSV
import Library.ApplicationConfiguration as AC
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModuleBilling as LB
import Library.LibModulePharmacy as LP
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
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LP.addPharmacyCreditOrganization(EMR)
pInvoiceNo = LD.createDispensarySale(EMR, HospitalNo, qty=1, drugName=drug1Name, paymentmode="Credit")
LD.returnDispensaryInvoice(EMR, pInvoiceNo, qty=1, returnremark="Wrong entry")
AC.logout()
AC.closeBrowser()
