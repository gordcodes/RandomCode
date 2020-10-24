#find a set of letters in a word with the most vowels



word='asoijrteinc'
characters=4

numVowels=0
finalString=''

wordPos=0

while wordPos<(len(word)-characters+1):
    finalChar=wordPos+characters #final character to count to
    shortString=word[wordPos:finalChar]
    print(shortString)

    shortStringVowCount=0

    if 'a' in shortString:
        #print('a test')
        shortStringVowCount+=1

    if 'e' in shortString:
        shortStringVowCount+=1

    if 'i' in shortString:
        shortStringVowCount+=1

    if 'o' in shortString:
        shortStringVowCount+=1

    if 'u' in shortString:
        shortStringVowCount+=1

    print(shortStringVowCount)

    if shortStringVowCount>numVowels:
        numVowels=shortStringVowCount
        finalString=shortString

    wordPos+=1

print(finalString)