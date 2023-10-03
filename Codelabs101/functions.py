import re
import logging
import csv

#Create a file for logging
logging.basicConfig(filename = "C:\Users\kioko\Documents\VS Code Projects\ComputerGraphics\Codelabs101\logfile.log", format = '%(asctime)s %(message)s', filemode = 'w')

#Create logger object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


#Function to reverse a string
def reverse_string(x):
    logging.info("Successfully reversed a string.")
    return x[::-1]

#Function to create email from name
def create_emails(spreadsheet):
    emails = [] #Variable to hold all the emails
    email = "" #Variable to temporarily hold an email
    #Loop through all data, focusing on the name column
    for row in range(1, spreadsheet.max_row):
        for col in spreadsheet.iter_cols(3, 3):
            name = col[row].value
            string_name = str(name)
            email = email + string_name[0] #Add the first letter of the name to the email
            reversed_string = reverse_string(string_name)
            last_name = ""
            #Loop through each reversed name until a space is reached then extract that substring
            for char in reversed_string:
                if char.isspace():
                    true_name = reverse_string(last_name)
                    email = email + true_name #Append the extracted name to the email
                    email = email + '@email.com'
                    #Remove special characters
                    alphaEmail = re.sub("['_!#$%^&*()<>?/\|}{~:]","",email)
                    emails.append(alphaEmail)
                    email = ""
                    alphaEmail = ""
                    break
                else:
                    last_name = last_name + str(char) #Append the character to the last_name variable
    logging.info("Created a list of emails successfully.")
    return emails

#Function to check if the email addresses are unique
def unique_email(emails):
    unique = True
    for i in range(len(emails)):
        for j in range(len(emails)):
            if i != j:
                if emails[i] == emails[j]:
                    unique = False
                    print(emails[i])
    if unique:
        print("The email addresses are unique.")
    else:
        print("The above email address is repeated.")
    logging.info("Unique emails function executed successfully.")

#Function to return a list of all male students
def list_male(spreadsheet):
    males = []
    for row in range(1, spreadsheet.max_row):
        if (spreadsheet.cell(row, column = 6).value == 'M'):
            males.append(spreadsheet.cell(row, column = 3).value)
    logging.info("Generated list of males successfully.")
    return males

#Function to return a list of all female students
def list_female(spreadsheet):
    females = []
    for row in range(1, spreadsheet.max_row):
        if (spreadsheet.cell(row, column = 6).value == 'M'):
            females.append(spreadsheet.cell(row, column = 3).value)
    logging.info("Generated list of females successfully.")
    return females

#Function to save a list to a TSV file
def save_tsv(emails):
    tsv_filename = "C:\Users\kioko\Documents\VS Code Projects\ComputerGraphics\Codelabs101\emails.tsv"
    with open(tsv_filename, 'w', newline = '') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter = '\t')
        for row in emails:
            tsv_writer.writerow(row)
    print("The emails have been saved to emails.tsv")