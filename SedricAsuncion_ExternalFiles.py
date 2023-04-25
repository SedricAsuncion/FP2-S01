#-----------------------------
#External_Files.py
#Sedric Asuncion
#-----------------------------

## ----- Import ----- ##
import os

## ----- Functions ----- ##
def file_create():
    Player = input("Create Character Name: ")
    Race = input('Create Character Race: ')
    Job = input('Create Character Job: ')
    Level = 0
    with open(f"{Player}_Data.txt", 'w') as created:
        created.write(f'User {Player}')
        created.write(f'\nRace: {Race}')
        created.write(f'\nJob: {Job}')
        created.write(f'\nLevel: {Level}')

def main():
    file_create()

main()