from prettytable import PrettyTable #Show data in a table format
import requests #To handle the get, post, put requests
import sqlite3 #for the sqlite db

#connect to database
conn = sqlite3.connect('craft.db')
conn.execute("PRAGMA foreign_keys = 1")

# Adding cursor of the database
c = conn.cursor()

# Creating tables users in craft db
try:
    c.execute('''
            CREATE TABLE IF NOT EXISTS users
            ([id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, [username] TEXT, [name] TEXT, [email] TEXT, [address] TEXT, [description] TEXT, [created_at] TEXT)
            ''')
except:
    pass


FRESHDESK_TOKEN = 'kRFDaV6VTj7G3SdcYae3'
GITHUB_TOKEN = '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'


class Craft:
    def __init__(self):
        print()

    def getGitUser(self, username):
        api_url = f"https://api.github.com/users/{username}" #url of the desired user
        try:

            feedback = requests.get(api_url, auth=('najear', GITHUB_TOKEN)) #get request and auth info are specified

        except requests.exceptions.RequestException as error_req: #in case of an error
            print ("Error: ", error_req)

        return feedback #return the response
    
    def addFreshContact(self, domain, token, name, email, address, description):
    
        json_data = { #data we want the new contact to have
            'name': name,
            'address': address,
            'description': description,
            'phone': '+359000000000', #in case the github user's email is private or none
            'email': email,
        }

        headers = { #set the content type 
            'Content-Type': 'application/json',
        }
        try:
            #post request so we can add the contact to freshdesk / Domain and token are given
            feedback = requests.post('https://'+ domain +'.freshdesk.com/api/v2/contacts', headers=headers, json=json_data, auth=(token, 'X'))
            
        except requests.exceptions.RequestException as error_req: 
            print ("Error: ", error_req)
        return feedback #return the response

    def updateFreshContact(self, domain, token, id, name, address, description):

        headers = {
            'Content-Type': 'application/json',
        }
        try:
            #First we need to have the contacts old information, in case we dont want to update other fields for ex: name only or name and address but not description
            #we do it using get request / Domain and token are given
            feedback = requests.get('https://'+domain+'.freshdesk.com/api/v2/contacts/'+id, headers=headers, auth=(token, 'X')).json()

        except requests.exceptions.RequestException as error_req:
            print ("Error: ", error_req)

        #if any of the fields are empty load it with the old data of the contact
        try:
            if len(name) == 0:
                name = feedback["name"]
            if len(address) == 0:
                address = feedback["address"]
            if len(description) == 0:
                description = feedback["description"]
        except Exception as ex:
            print(ex)

        json_data = {
            'name': name,
            'address': address,
            'description': description, 
        }
        try:

            #put request is used to update and conact desired
            feedback = requests.put('https://'+domain+'.freshdesk.com/api/v2/contacts/'+id, headers=headers, json=json_data, auth=(token, 'X'))

        except requests.exceptions.RequestException as error_req:
            print ("Error: ", error_req)

        return feedback #return the response


if __name__ == "__main__":

    craft = Craft() #Create an object of type craft

    #For pretty JSON output
    gitUserInfo = PrettyTable()
    gitUserInfo.field_names = ["Key", "Value"]
    freshDeskInfo = PrettyTable() 
    freshDeskInfo.field_names = ["Key", "Value"]


    print("Please enter a GitHub Username: ")
    gitUser = input() 

    #Call the function getGitUser to get the desired user's info
    gitData =  craft.getGitUser(gitUser).json()

    for key, value in gitData.items():
        if len(key) < 10: #add keys with length smaller than 10
            gitUserInfo.add_row([key, value]) #Add it to the prettyTable

    print(gitUserInfo) #Print the table

    #Insert into the table users the found github user information
    try:
        c.execute("INSERT INTO USERS VALUES (?, ?, ?, ?, ?, ?, ?)", (None, gitData['login'], gitData['name'], gitData['email'], gitData['location'], gitData['bio'], gitData['created_at']))
        conn.commit()
        conn.close()
    except:
        pass

    print("Please enter Freshdesk Domain: ")
    freshDomain = input()

    #Using the information that we got from the github user we can create a new contact in freshdesk
    #Using the fuction addFreshContact

    freshData = craft.addFreshContact(freshDomain, FRESHDESK_TOKEN, gitData['name'], gitData['email'], gitData['location'], gitData['bio']).json()

    #Using the fucntion updateFreshContact we can update an already existing contact / note !!: Use id to specify the user 

    #freshData = craft.updateFreshContact(freshDomain, FRESHDESK_TOKEN, '103008026157', 'Martin', '', 'Mathematics Professor').json()
    for key, value in freshData.items():
        freshDeskInfo.add_row([key, value]) #Add it to the prettyTable

    print(freshDeskInfo)