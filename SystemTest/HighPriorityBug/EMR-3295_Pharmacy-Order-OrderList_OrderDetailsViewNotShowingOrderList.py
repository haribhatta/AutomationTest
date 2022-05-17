'''
Objective:
To test EMR-3295:
'''

import Library.ApplicationConfiguration as AC
import Library.GlobalShareVariables as GSV
import Library.LibModuleDispensary as LD
import Library.LibModuleAppointment as LA
import Library.LibModulePharmacy as LP

########
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
drugSinex = GSV.drugSinexName
paymentMode = 'Cash'
supplierName = GSV.supplier
drugName = GSV.drug1BrandName
#############
#AC.login(foUserId, foUserPwd)
#LB.counteractivation()
#HospitalNo, InvoiceNo, discountPercentage = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae)
#AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activateDispensaryCounter(EMR, GSV.dispensaryName1)
LP.createPharmacyPurchaseOrder(EMR, supplierName, drugName)
LP.verifyCreatePharmacyPurchaseOrder(EMR, supplierName, drugName)
AC.logout()
AC.closeBrowser()
