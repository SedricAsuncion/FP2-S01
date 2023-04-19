#-----------------------------
#External_Files.py
#Sedric Asuncion
#-----------------------------

## ----- Import ----- ##

## ----- Functions ----- ##
def file_create():
    with open('Player_Data.txt', 'w') as created:
        created.write('Created')

file_create()