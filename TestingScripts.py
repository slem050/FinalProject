def SearchForBookCode(currentNode, code):
    LettersOfCode = GetLettersFromCode(code.split("/")[1])
    requiredArea = code.split("/")[0]
    existingArea = currentNode.split("/")[0]
    if requiredArea != existingArea:
        return False
    SplittedNode = currentNode.split("/")[1]
    bookRanges = SplittedNode.split(",")
    #########################
    if len(LettersOfCode) == 1:
        return CheckFirstLetterOfCode(bookRanges, code.split("/")[1])
    elif len(LettersOfCode) == 2:
        if CheckFirstLetterOfCode(bookRanges, code.split("/")[1]):
            return CheckSecondLetterOfCode(bookRanges, code.split("/")[1])
        else:
            return False


def CheckFirstLetterOfCode(bookRanges, LettersOfCode):
    lettersCodeBook = GetLettersFromCode(LettersOfCode)
    for i in range(0, len(bookRanges)):
        ranges = bookRanges[i].split("-")
        RangeFrom = ranges[0]
        RangeTo = ranges[1]
        InitialLetters1 = RangeFrom[0]
        EndingLetters1 = RangeTo[0]
        if InitialLetters1 <= lettersCodeBook[0] <= EndingLetters1:
            # checks the numbers, get the starting number of range and ending number of range and check if the book code is between them
            InitialNumbers = GetFirstNumbersFromCode(RangeFrom)
            endingNumbers = GetFirstNumbersFromCode(RangeTo)
            NumbersOfCode = GetFirstNumbersFromCode(LettersOfCode)
            if lettersCodeBook[0] == InitialLetters1:
                if len(InitialLetters1) == 1:
                    if NumbersOfCode >= InitialNumbers:
                        return True
                    return False
                # if the length of the initial letter more than one means that the book code is not in the range for example : AB45. --- A173.
                return True
            elif EndingLetters1 == lettersCodeBook[0]:
                if len(EndingLetters1) == 1:
                    if int(NumbersOfCode) <= int(endingNumbers):
                        return True
                    else:
                        return False
                return True
            else:
                return True
            # if the length of the initial letter more than one means that the book code is not in the range for example : AB45. --- A173
    return False


def CheckSecondLetterOfCode(bookRanges, LettersOfCode):
    for i in range(0, len(bookRanges)):
        ranges = bookRanges[i].split("-")
        RangeFrom = ranges[0]
        RangeTo = ranges[1]
        InitialLetters1 = RangeFrom[0]
        EndingLetters1 = RangeTo[1]
        if InitialLetters1 <= LettersOfCode[0] <= EndingLetters1:
            return True


def GetLettersFromCode(code):
    Letters = ""
    for x in code:
        if x.isalpha():
            Letters = Letters + x
        elif x.isdigit():
            break
    return Letters


def GetFirstNumbersFromCode(code):
    numbers = ""
    for x in code:
        if x.isdigit():
            numbers = numbers + x
        elif x == '.':
            break
    return numbers


#print(GetLettersFromCode("0/R101"))
#print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/R101"))
test="XA.A193"
test2=test.split(".")[0]
test3=test.split(".")[1][0:]
test4=test3[:1]
print(test2)

print(test3)
# print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/C1"))
# print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/C10"))

