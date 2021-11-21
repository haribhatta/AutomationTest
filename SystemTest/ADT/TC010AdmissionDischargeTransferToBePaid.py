#-------------Objective of this script----------
# To verify admission, transfer and discharge of newly registered patient. Patient has to get refund money from deposit left.

from Library import ApplicationConfiguration as AC
from Library import LibModuleBilling as LB
from Library import LibModuleADT as ADT
from Library import LibModuleAppointment as LA
from Library import GlobalShareVariables as GSV

# front desk user login

#------------Local Veriables-------------------
labitem = GSV.UrineRE
imagingitem = GSV.USG
admitcharge = GSV.admitRate
deposit = 1000

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

AC.applicationSelection()
AC.openBrowser()
#############

AC.login(foUserId, foUserPwd)
LB.counteractivation()
HospitalNo = LA.patientquickentry(discountpc=0, paymentmode='Cash', department=GSV.departmentGyno, doctor=GSV.doctorGyno).HospitalNo
#can.verifyopdinvoice(deposit=0, billamt=500)

LB.createlabxrayinvoice(HospitalNo=HospitalNo, labtest=labitem, imagingtest = imagingitem)
ADT.admitDisTrans(admit=1, discharge=0, trasfer=0, deposit=deposit,hospitalNO=HospitalNo , department=GSV.doctorGyno)
AC.logout()
AC.closeBrowser()