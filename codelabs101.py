import openpyxl

path = r'D:\Bachelor of Science in Informatics and Computer Science\Year 3\Semester 2\Computer Graphics\Code\Repository\ComputerGraphics\Test Files.xlsx'

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook(path)
 
# Define variable to read sheet
dataframe1 = dataframe.active
 
# Iterate the loop to read the cell values
# for row in range(0, 64):
#    for col in dataframe1.iter_cols(0, 6):
#       print(col[row].value)

#Extract first letter from name
for row in range(1, 64):
    for col in dataframe1.iter_cols(3, 3):
        name = col[row].value
        string_name = str(name)
        print(string_name[0])

#Extract last name from name
reversed_string = reversed(string_name)
last_name = ""
for char in reversed_string:
    if char.isspace():
        true_name = reversed(last_name)
    else:
        last_name = last_name + str(char)

print(true_name)