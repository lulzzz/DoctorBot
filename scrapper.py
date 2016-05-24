import requests
import pymongo 
import sys
import re
import urlparse
from bs4 import BeautifulSoup
reload(sys)


# url = "http://umm.edu/health/medical/ency/symptoms?c=B"

def ExtractSymptomsOrDiseasesList( url , DictForSymptomsAndDiseases , ch ):

	
	leftUrl =url;
	for i in range(26):
		print "extracting ",chr(65+i) , ch
		url = leftUrl + chr(65+i)
		req = requests.get(url)
		if req.status_code == 200:
			soup = BeautifulSoup(req.content,"lxml")
			categories = soup.find_all("ul", {"class": "letter"})
			for category in categories:
				links = category.find_all("a")
				for link in links:
					DictForSymptomsAndDiseases[link.text] = [ch]



def CrawlData( url , DictForSymptomsAndDiseases ):

	
	leftUrl =url;
	for i in range(26):
		print "Crawling ",chr(65+i)
		url = leftUrl + chr(65+i) + ".htm"
		req = requests.get(url)
		if req.status_code == 200:
			soup = BeautifulSoup(req.content,"lxml")
			categories = soup.find_all("ul", {"id": "index"})
			for category in categories:
				links = category.find_all("a")
				for link in links:

					if link.text in DictForSymptomsAndDiseases.keys():
						print link.text
						data  = {}
						newUrl = urlparse.urljoin(req.url, link.get("href"))
						ExtractData( newUrl, data ,DictForSymptomsAndDiseases )
						DictForSymptomsAndDiseases[link.text].append(data)
						

def ExtractData( url , data , DictForSymptomsAndDiseases ):

	
	req = requests.get(url)
	if req.status_code == 200:
		soup = BeautifulSoup(req.content,"lxml")
		content = soup.find("div", {"id": "d-article"})
		description = content.find("div",{"id":"ency_summary"})
		sections = content.find_all("div",{"class":"section"})
		for section in sections:
			sectionHeader = section.find("div",{"class":"section-header"}).text.strip('\t\r\n ')
			sectionBody = section.find("div",{"class":"section-body"})
			
			#sectionBody = sectionBody.findAll()
			#print sectionBody
			
			InSection = sectionBody.find_all( recursive=False)

			#print secti
			textBetweenTags = ""
			referenceList = sectionBody.find_all("a")
			references = []
			count=0
			for reference in referenceList:
				if reference.text in DictForSymptomsAndDiseases:
					count+=1
					references.append(reference.text)
			print "\tSection Header", sectionHeader,"references count",count
			for eachElement in  InSection:
				
				if str(eachElement).find("<p>") >= 0 :
					textBetweenTags += eachElement.text + "\n"
				elif str(eachElement).find("<ul>") >= 0 :
					listItems = eachElement.find_all("li")
					for item in listItems:
						if item.text in DictForSymptomsAndDiseases:
							references.append(item.text) 
						textBetweenTags += item.text + "\n"
					

			data[ sectionHeader ] = textBetweenTags,references

	else:
		print url		

			
			

		






	

			


				
		



# url = "https://www.nlm.nih.gov/medlineplus/ency/encyclopedia_"
#def Spider(	url ):

	

	
