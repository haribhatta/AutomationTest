from TestActionLibrary import A
from TestActionLibrary import GSV

# front desk user login
foUserId = GSV.foUserID
foUserPwd = GSV.foUserPwD

#-------- Billing Items ---------
labitem = GSV.TFT
imagingitem = GSV.USG

oblx = A()
oblx.openBrowser()
oblx.login(foUserId, foUserPwd)
oblx.counteractivation()
oblx.patientquickentry(0, 'Cash')
#oblx.verifyopdinvoice(deposit=0, billamt=500)
oblx.createlabxrayinvoice(labitem, imagingitem)
#oblx.verifylabxrayinvoice()
oblx.logout()
oblx.closeBrowser()
print("Status:Passed -> TC002OPDbillingLabXray.py")
