
from scrapper import *

from dbController import *
import pickle
import requests
import pymongo 
import sys
import re
import urlparse
from bs4 import BeautifulSoup
from pymongo import MongoClient
reload(sys)


client = pymongo.MongoClient('mongodb://localhost:27017/')



db = client.DoctorBotDB


symptoms_url =  "http://umm.edu/health/medical/ency/symptoms?c="

disease_url = "http://umm.edu/health/medical/ency/diseases?c="

#ExtractSymptomsOrDiseasesList(symptoms_url);

DictForSymptomsAndDiseases = {}

print "extracting Disease List"
ExtractSymptomsOrDiseasesList(disease_url , DictForSymptomsAndDiseases , 'd')

print "extracting Symptoms List"
ExtractSymptomsOrDiseasesList(symptoms_url , DictForSymptomsAndDiseases , 's')



ContentUrl = "https://www.nlm.nih.gov/medlineplus/ency/encyclopedia_"

print "Crawling data"

CrawlData( ContentUrl , DictForSymptomsAndDiseases )

print "Adding into Database"

f = open("dict",'w')

pickle.dump(DictForSymptomsAndDiseases, f, pickle.HIGHEST_PROTOCOL)



AddingIntoDB( DictForSymptomsAndDiseases , db )







#print DiseaseNamesList


