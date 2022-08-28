#craft.py / Main file

#Install the following libraries:
1. pip install prettytable / To show JSON output in a table format
2. pip install requests / To handle the get, post, put requests
3. pip install pysqlite3 / For the sqlite3 database 
4. python craft.py / To run the python file

NOTE!: Only trial accounts are used in this program, the tokens are hardcoded


#Adding a new contact to FreshDesk contacts list, using a Github's user information:

When you run the file, insert any Github's username, if its a valid GitHub username it will show you information about the user desired.

After that you will be asked to enter Freshdesk domain:

FRESHDESK DOMAIN = najear

If the domain is correct it will show you information about the new contact added.

#Updating a contact from FreshDesk contacts list using their ID:

You may comment the the functions getGitUser, addFreshContact and what is also related to them, uncomment the function updateFreshContact from the main function

Fields that can be updated:
 * name
 * address
 * description 
 
 If you choose to update only one or two from the Fields, the third field will remain empty and it will be loaded with the old contact's information
 
 Example: 
 
 Already contact = Martin, sofia, a web developer
 
 Update function = updateFreshContact(John, '', Back-end developer)
 
 Modified contact = John, sofia, Back-end developer / address is still the same
 
 #test_craft.py / unit tests
 
 Functions tested using mock:
 * getGitUser() - when returns true and false
 * addFreshContact() - when returns true and false
 * updateFreshContact - when returns true and false
 
 
#SQLITE database
The files included in project are: sqlite3.dll and sqlite3.def

The database file: craft.db

Note!: This files are for windows 64x if you are using any other os check https://www.sqlite.org/download.html and replace the files with the proper ones.

To access the sqlite database using cmd:
cd/project_file
sqlite3 craft.db 

Commands:
.tables = To show tables / you should see users table

Select * from users; / To show the users your looked for from github

If any of the users Fields are = None it means the user didnt specify the information that we are looking for 





