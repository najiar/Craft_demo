#Craft.py / Main file

#Install the following libraries:
1. pip install prettytable / To show JSON output in a table format
2. pip install requests / To handle the get, post, put requests
3. pip install pysqlite3 / For the sqlite3 database 
4. python craft.py / To run the python file

NOTE!: Only trial accounts are used in this program, the tokens are hardcoded


#Adding a new contact to FreshDesk contacts list, using a Github's user information
When you run the file, insert any Github's username, if its a valid GitHub username it will show u information about the user desired
After that you will be asked to enter Freshdesk domain:
FRESHDESK DOMAIN = najear
If the domain is correct it will show you information about the new contact added.

#Updating a contact from FreshDesk contacts list
You may comment the the functions getGitUser, addFreshContact and uncomment the function updateFreshContact
Fields that can be updated:
 * name
 * address
 * description 
 If you choose to update only one or two from the Fields, the third field will remain empty and it will be loaded with the old contact's information
 Example: 
 Already contact = Martin, sofia, a web developer
 Update function = updateFreshContact(John, '', Back-end developer)
 Modified contact = John, sofia, Back-end developer / address is still the same
 



