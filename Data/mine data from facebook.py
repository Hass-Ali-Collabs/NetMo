# Program to mine data from your own facebook account
#!usr/bin/env python
# Program to get a page information

import json
import facebook

def main():
	token = "{Your Token}"
	graph = facebook.GraphAPI(token)
	page_name = raw_input("Enter a page name: ")
	
	# list of required fields
	fields = ['id','name','about','likes','link','band_members']
	
	fields = ','.join(fields)
	
	page = graph.get_object(page_name, fields=fields)
		
	print(json.dumps(page,indent=4))

if __name__ == '__main__':
	main()