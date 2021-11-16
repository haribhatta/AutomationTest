import Library.ApplicationConfiguration as AC

application = AC.appName

if application == "LPH":
      #defining Login Credentials for LPH
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'ashmita' #LPH user
      foUserPwD = 'pass123'
      #Lab user
      labUserID = 'karuna'
      labUserPwD = 'pass123'
      #ER Lab user
      ERlabUserID = 'erlab'
      ERlabUserPwD = 'pass123'
      #radiologist user
      radioUserID = 'radiology'
      radioUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'debika'
      pharmacyUserPwD = 'pass123'
      #nurse user
      nurseUserID = 'admin'
      nurseUserPwD = 'pass123'
      #store user
      storeUserID = 'shreeram'
      storeUserPwD = 'pass123'

      # Bill Items Name variables for LPH Hospital
      opdRate = 30
      CBC = "CBC"
      TFT = "TFT"
      TFTRate = 800
      LDH = "LDH"
      USG = "USG ABDOMEN/PELVIS"
      usgRate = 700
      admitRate = 30
      UrineRE = "URINE R/E"
      BTCT = "BT/CT"
      btctRate = 100
      erTest = "TC"
      LabType = "ER"

      #Drug name
      drug1BrandName = 'NIKO DROP 15ML BOTTLE'
      drug1GenericName = 'PARACETAMOL 150MG/ML ORAL DROP 15ML BOTTLE'
      drug1Rate = 25
      drug2BrandName = "MACLAR 500MG TAB"
      drug2GenericName = "CLARITHROMYCIN"
      drug2Rate = 563.5
      drug3BrandName = "Sinex tab"
      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49
      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86
      Testdrug = "testdrugreport"

      #Inventory Item name list
      Inventory1 = "General Inventory"
      SubStoreName1 = "ADMINISTRATION"
      Dispensary1 = "MainDispensary"
      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "DOTPEN"

      #Sub Store Name list
      SubStore1 = "General"
      SubStore2 = "PostOps"

      #Doctor/Department List
      doctorGyno = "Dr. doctor doctor"
      departmentGyno = "GYNAE & OBS"
      doctor2 = "Mr. admin admin"

      # User Name List
      UserBilling = 'Mr. Bhagawati Pandey'

      deposit = 100
###############################################################################
if application == "SNCH":

      #defining Login Credentials for SNCH
      #admin user
      adminUserID = 'admin'
      adminUserPwD = 'pass123'    # '28A7hi0jvH0='
      #billing user
      foUserID = 'sabitri'
      foUserPwD = 'pass123'
      #pharmacy user
      pharmacyUserID = 'shivraj'
      pharmacyUserPwD = 'pass123'
      #laboratory user
      labUserID = 'gayatri'
      labUserPwD = 'pass123'
      # Bill Items Name variables for SNCH
      opdRate = 500
      CBC = "CBC"
      TFT = "FREE TFT"   #TFT(FT3,FT4,TSH) CLLEA
      TFTRate = 1200
      LDH = "LDH"
      #UrineRE = "Urine RE/ME"
      UrineRE = "URINE R/E,M/E" # this gets changed on V1.49.3
      BTCT = "BT/CT"
      btctRate = 300
      USG = "USG ABDOMIN AND PELVIS"
      usgRate = 1000
      admitRate = 1500

      #Drug name for SNCH pharmacy billing
      drug1BrandName = "SINEX TAB"
      drug1GenericName = "quinapril"
      drug1Rate = 1.15

      drug2BrandName = 'ASTHALIN 2 MG TAB'
      drug2BrandRate = 1.14

      drug3BrandName = "Sinex tab"

      drug4BrandName = "10 ML DIS.SYRINGE"
      drug4BrandRate = 6.49

      drug5BrandName = 'MONOTRATE-20MG TAB'
      drug5BrandRate = 4.86

      drugSinexName = 'SINEX TAB'
      drugSinexRate = 3

      Testdrug = "Testdrugreport"

      #Inventory Item name list
      Inventory1 = "General Inventory"
      Dispensary1 = "General Inventory"

      A4Paper = 'Paper A4'
      PhotocopyPaper = 'PHOTOCOPY PAPER (CUTTING)'
      photocopypaperRate = 2300
      stationaryItem1 = "PENCIL"

      #Sub Store Name list
      SubStore1 = "General"
      SubStore2 = "PostOps"

      #Doctor/Department List
      doctorGyno = "Dr. Jyoti Rana"
      departmentGyno = "Gynecology"

      deposit = 200

   #def __str__(self):
    #  return