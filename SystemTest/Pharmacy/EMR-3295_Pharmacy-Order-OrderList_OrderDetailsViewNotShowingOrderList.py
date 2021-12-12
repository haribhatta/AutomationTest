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
supplierName = GSV.supplierShremad
drugName = GSV.drugAasma
#############
#AC.login(foUserId, foUserPwd)
#LB.counteractivation()
#HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=departmentGynae, doctor=doctorGynae)
#AC.logout()
#############
AC.login(phuserid, phuserpwd)
LD.activatePharmacyCounter(EMR, GSV.dispensaryName)
LP.createPharmacyPurchaseOrder(EMR, supplierName, drugName)
LP.verifyCreatePharmacyPurchaseOrder(EMR, supplierName, drugName)
AC.logout()
AC.closeBrowser()
