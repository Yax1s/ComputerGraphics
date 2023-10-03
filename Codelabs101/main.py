import openpyxl
from functions import *

path = r'C:\Users\kioko\Documents\VS Code Projects\ComputerGraphics\Codelabs101\Test Files.xlsx'

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook(path)
 
# Define variable to read sheet
dataframe1 = dataframe.active

emails = create_emails(dataframe1)
unique_email(emails)
male_students = list_male(dataframe1)
female_students = list_female(dataframe1)
save_tsv(emails)
