#[key][1] means dictionary
#[key][0] means 's' or 'd'
def AddingIntoDB( DictForSymptomsAndDiseases , db):

	for key in DictForSymptomsAndDiseases:
		if len(DictForSymptomsAndDiseases[key]) > 1 :
			
			TempDict = {}
			TempDict["_id"] = key
			TempDict["value"] = DictForSymptomsAndDiseases[key]
			if DictForSymptomsAndDiseases[key][0] == 's':
				print "Adding Symptom" + key,
				db['symptomCollection'].insert_one(TempDict)
				
				#print DictForSymptomsAndDiseases[key][1]
				#print DictForSymptomsAndDiseases[key][1]
				if 'Causes' in DictForSymptomsAndDiseases[key][1]:
					TempList = DictForSymptomsAndDiseases[key][1]['Causes'][1]
					for l in TempList:
						TempDictForSTD = {}
						
						if  DictForSymptomsAndDiseases[l][0] == 'd' :
							
							TempDictForSTD['disease'] = l
							TempDictForSTD['symptom'] = key
							db['symptomsToDisease'].insert_one(TempDictForSTD)
							print "Added"
			else:
				print "Adding Disease" + key,
				db['diseaseCollection'].insert_one(TempDict)
				#print key
					
				# 	DictForSymptomsAndDiseases[key][1]['Symptoms'][1] contains refrence list
				# DictForSymptomsAndDiseases[key][1]['Symptoms'][0] contains data 

				if 'Symptoms' in DictForSymptomsAndDiseases[key][1]:
					
					TempList = DictForSymptomsAndDiseases[key][1]['Symptoms'][1]
				
					for l in TempList:
						TempDictForSTD = {}
						
						if  DictForSymptomsAndDiseases[l][0] == 's' :
							
							TempDictForSTD['symptom'] = l
							TempDictForSTD['disease'] = key
							db['symptomsToDisease'].insert_one(TempDictForSTD)
							print "Added"
