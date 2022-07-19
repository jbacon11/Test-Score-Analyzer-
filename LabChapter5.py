#Test Score Analyzer 
#Jeremy Bargy
#March 4, 2020


#Display welcome page and developer name
def welcome():

    beginSequence= 'y'       #str
    
    print('\n\t\t\t\tHello Students!\n\t\t\t\t---------------')
    print('Thank you for taking the time to use this program.')
    print('The program was made by Jeremy Bargy.')
    print('Last update March 2020')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to help students identify the average score they achieved from the test taken.')
    print('A student with this information can identify the actions needed to improve their overall academic status.\n\n\n\n')
    print('Here is a list of how to use this program:\n')

    print('1) The program will ask users for their first name.\n')                                                            #step 1
    print('\ta: Be sure to enter letters for your name and not leave an empty box.\n')

    print('2) The program will ask users to enter their test score in a numeric value.\n')                                    #step 2
    print('\ta: Be sure to enter in a positive number and not to exceed 100.\n')

    print('3) The program will then return the letter grade associated with your score and a feedback message.\n')            #step 3

    print('4) The program will ask users if this is another test score to enter. \n')                                         #step 4
    print('\ta: You will enter a "y" or "Y" for Yes and the program will continue to ask for your test scores.\n')
    print('\tb: You will enter a "n" or "N" for No and the program will enter the next sequence.\n')

    print('5) The program will return the average for the test scores entered and number of test entered.\n')                 #step 5

    print('6) The program will ask if the user would like to restart this program for another user.\n')                       #step 6
    print('\ta: You will enter a "y" or "Y" for Yes and the program will restart.\n')
    print('\tb: You will enter a "n" or "N" for No and the program will end.\n')

    print('Take a minute to ready through the instructions before you begin.\n\n\n')

    print('Have you read the instructions and are ready to begin?')
    print('Enter "Y" for yes. Please use capital letters.')
    print('Or enter "N" for no. Please use capital letters.')
    #loop until user had read instructions
    beginSequence = input('Begin program?\n ')
    while not(beginSequence == 'Y' or beginSequence == 'y') or beginSequence=='' or beginSequence== ' ':
        print('Error: please read the instructions and enter "Y" for yes to begin: \n')
        beginSequence= input('Begin program? \n')


def main():
    #execute GetInput, DisplayScore functions
    startProgram='Y'
    
    #calls welcome function
    welcome()

    #loop continues as long as user enters Y or y
    while startProgram == 'Y' or startProgram =='y':
        GetInput()
        
        #repeat program if more groups need to enter data.
        print('\n\nWould you like to restart this program?\n')
        startProgram = input('Please enter "Y" to restart program. \n Or "N" to end the program: \n')
        while not(startProgram == 'Y' or startProgram=='y' or startProgram=='N' or startProgram=='n') or startProgram=='' or startProgram== ' ':
            print('\nError: please "Y" for yes to restart:')
            print('Or enter "N" to end the program: ')
            startProgram= input('Restart program? \n')

def GetInput():
    #calls GetName, GetScores, DisplayScores functions and calculates the average grade for tests entered
    TotalTests = 0
    TotalGrade = 0
    
    userName = GetName()
    contGetTest = 'Y'
    while contGetTest == 'Y' or contGetTest =='y':
        testscore =GetScores()
        DisplayScores(userName, testscore)
        TotalGrade += testscore
        TotalTests += 1
        
        #repeat program if another student needs to enter data.
        contGetTest = input('\nPlease enter "Y" to enter more student test data. \n Or "N" to move to the next sequence: \n')
        while not(contGetTest == 'Y' or contGetTest=='y' or contGetTest=='N' or contGetTest=='n') or contGetTest=='' or contGetTest== ' ':
            print('\nError: please "Y" for yes to restart: ')
            print('Or enter "N" to move on:')
            contGetTest= input('Restart program? \n')

    #calculate averages for tests entered
    testAverages = (TotalGrade / TotalTests)
    print('\n\n_______________________________________')
    print('\nFor',TotalTests, 'tests, you averaged', testAverages,'%!')
    print('_______________________________________\n\n')
    
def GetName():
    #ask for user name
    userName= input('\nPlease enter your first name: \n')
    while not(userName.isalpha()) or userName == ' ' or userName == '' :
        print('Error: incorrect input:')
        userName =input('Please your first name: \n')
        
    return userName

def GetScores():
    # retrieves user test score - value returning function
    # Get student user to enter test score
    testScores = (input('\nPlease enter the test score you have earned. Please use a numeric value that is positive and does not exceed 100: \n'))
    testScores = validate(testScores)
    return testScores

def validate(testScore):
    #validate input is a number and within accepted range
    while not( testScore.isdigit()) or int( testScore) >= 101 or int( testScore) < 0 or int( testScore) == ' ' or int( testScore)=='':
            print('Error: incorrect input: \n')
            testScore = (input('Please enter the test score you have earned. Please use a numeric value that is positive and does not exceed 100: \n'))
    testScore = int(testScore)

    return testScore

def DisplayScores(userName,testscore):
    #calculate letter grade and feedback message
    letterGrade = ''
    message = ''
    
    if testscore >= 90:
        letterGrade = 'A'
        message = 'Excellent Work!'
    elif testscore >= 80:
        letterGrade = 'B'
        message = 'Nice Job!'
    elif testscore >= 70:
        letterGrade = 'C'
        message = 'Not Bad!'
    elif testscore >= 60:
        letterGrade = 'D'
        message = 'Room for Improvement!'
    else:
        letterGrade = 'F'
        message = 'Go Back & Review!'

    #Display Student name, letterGrade, message
    print('\n\n_______________________________________')
    print(userName, 'has scored the letter grade:', letterGrade)
    print(message)
    print('_______________________________________\n\n')
       
main()  
#display farewell message
print('\n')
print('Thanks for using our program!')
print('Goodbye!')
