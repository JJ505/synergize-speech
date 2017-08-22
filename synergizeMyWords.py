from nltk import word_tokenize, pos_tag
import os.path

def synergize(x):
    #unpack the tuple
    word, wordType = x
    if wordType == 'JJ':
        word = "synergizing"
    elif wordType == 'NN':
        word = "revolution"
    return word

#get fileName
gotFileName = False
fileName = ""
print ("Please input name of file")
while not gotFileName:
    fileName = input()
    if os.path.exists(fileName):
        gotFileName = True
    else:
        print ("That file doesn't seem to exist, try another?")

textFile = open(fileName)
newFile = open("synergized.txt", 'w')
for line in textFile:
    tokens = word_tokenize(line)
    result = pos_tag(tokens)
    #synergize will change adj to 'synergizing' and nouns to 'revolution'
    newResult = list(map(synergize, result))
    #characters that do not need spaces before themselves
    stops = "!.?,"
    for i in range(len(newResult)):
        newFile.write(newResult[i])
        if i+1 < len(newResult) and newResult[i+1] not in stops:
            newFile.write(' ')
    newFile.write('\n')
    
#notify user that file has been created
print("stored synergy in synergized.txt")
#close unused resources
textFile.close()
newFile.close()
