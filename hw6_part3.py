# File:    hw6_part3.py
# Author:  Matthew Grant
# Date:    10/21/15
# Section: 03 
# Email:   mgr1@umbc.edu
# Description: 
#             This program tells the word count of a file and gives the average word length.


def main():

    print("Word Counter \nCoded by Matthew Grant")

    print("This program accepts only .dat or .txt files.")

    # Initialize file type variable 

    fileType = 'invalid'

    # Ensure that the file type is valid

    while fileType == 'invalid':

       # Get file name

        fileName = input("Please enter a file name ending in .dat or .txt: ")

        # Check that file type is .txt or .dat

        if fileName[:-4:-1] == 'txt':

            fileType = 'text'

        elif fileName[:-4:-1] == 'tad':

            fileType = 'data'   

        else:
   
            fileType = 'invalid'


    # Open file object once a valid name is provided

    fileToRead = open(fileName, "r")

    # Read in file and split so it can be iterated

    fileObject = fileToRead.read()

    fileObject = fileObject.split()

    # Initialize word count variable at zero
    
    wordCount = 0        

    # Add to the word count variable

    for w in range(len(fileObject)):

        wordCount += 1

    # Give the word count


    print("The word count of", fileName, "is: ", wordCount)     
 
    # Initialize sum of word lengths, so it can be averaged

    sumWordLengths = 0   

    # Find average word lengths

    for obj in fileObject:

        sumWordLengths += len(obj)


    avgWordLength = sumWordLengths / wordCount

    # Give the average word length

    print("On average, each word is", avgWordLength, "characters long")


    # Close file

    fileToRead.close()


main()
