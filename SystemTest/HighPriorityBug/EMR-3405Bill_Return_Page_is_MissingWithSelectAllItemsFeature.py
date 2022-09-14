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
phuserid = GSV.pharmacyUserID
phuserpwd = GSV.pharmacyUserPwD
drug1Name = GSV.drug1BrandName
drug2Name = GSV.drug2BrandName
drug1Rate = GSV.drug1Rate
drug2Rate = GSV.drug1Rate
paymentMode = 'Cash'
creditOrganization = GSV.creditOrganization
########
priceCategoryType = "Normal"
discountScheme = GSV.discountSchemeName
#############
AC.login(foUserId, foUserPwd)
LB.counteractivation(EMR)
HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(EMR, discountScheme=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae, priceCategoryType=priceCategoryType, case='+ve')
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
invoiceNo = LD.createDispensarySaleMultipleItems(danpheEMR=EMR, HospitalNo=HospitalNo, drugname=drug1Name, drugname1=drug2Name, qty1=2, qty2=2, creditOrganization=creditOrganization,paymentmode=paymentMode)
LD.returnallInvoice(danpheEMR=EMR, pInvoiceNo=invoiceNo)
AC.logout()
AC.closeBrowser()
