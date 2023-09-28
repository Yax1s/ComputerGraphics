import openpyxl
from functions import *

path = r'D:\Bachelor of Science in Informatics and Computer Science\Year 3\Semester 2\Computer Graphics\Code\Repository\ComputerGraphics\Codelabs101\Test Files.xlsx'

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook(path)
 
# Define variable to read sheet
dataframe1 = dataframe.active

emails = create_emails(dataframe1)
unique_email(emails)
male_students = list_male(dataframe1)
female_students = list_female(dataframe1)
save_tsv(emails)
