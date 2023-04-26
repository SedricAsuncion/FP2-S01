#-----------------------------
#External_Files.py
#Sedric Asuncion
#-----------------------------

## ----- Import ----- ##

## ----- Functions ----- ##
def inputs():
    #Prompts user to enter name of file and basic Character information
    Player = input("Create Character Name: ")
    Race = input('Create Character Race: ')
    Job = input('Create Character Job: ')
    Level = 0

    #Returns Character Name, Race, Job, and Level
    return Player, Race, Job, Level

def file_create():
    #Calls the inputs function to get the values of the prompts 
    #What we only need read is the Player value
    Player, Race, Job, Level = inputs()

    #Creates the file and writes the placeholders for the values
    with open(f"{Player}_Data.txt", 'w') as crt:
        crt.write('User: ')
        crt.write('\nRace: ')
        crt.write('\nJob: ')
        crt.write('\nLevel: ')
    #Returns the values, we need those in next functions
    return Player, Race, Job, Level

def file_append():
    #Calls the inputs function to get the values of the prompts
    #I don't recall inputs function, because it'll prompt again
    Player, Race, Job, Level = file_create()

    #Appends the values to the file on their rightful placeholders
    with open(f"{Player}_Data.txt", 'r+') as app:
        lines = app.readlines()
        lines[0] = lines[0].strip() + f' {Player}\n'
        lines[1] = lines[1].strip() + f' {Race}\n'
        lines[2] = lines[2].strip() + f' {Job}\n'
        lines[3] = lines[3].strip() + f' {Level}\n'
        app.seek(0)
        app.writelines(lines)

    #Returns the file_name value
    x = Player
    return x

def file_read():
    Player = file_append()

    #Reads and prints file and values
    with open(f"{Player}_Data.txt", 'r') as rd:
        print(rd.read())
        

## ----- Main Code ----- ##
file_read()