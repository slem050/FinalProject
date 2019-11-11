def SearchForBookCode(currentNode, code):
    LettersOfCode = GetLettersFromCode(code.split("/")[1])
    requiredArea = code.split("/")[0]
    existingArea = currentNode.split("/")[0]
    if requiredArea != existingArea:
        return False
    SplittedNode = currentNode.split("/")[1]
    bookRanges = SplittedNode.split(",")
    #########################
    if LettersOfCode[0] == 'x':
        return CheckForMagazines(bookRanges, code.split("/")[1])
    return CheckLetterForGeneralBooks(bookRanges, code.split("/")[1])


def CheckForMagazines(bookRanges, code):
    LettersOfCode = code.split(".")[0]
    SecondLetterOfcode = code.split(".")[1][:1]
    NumbersOfcode = code.split(".")[1][1:]
    for i in range(0, len(bookRanges)):
        ranges = bookRanges[i].split("-")
        RangeFrom = ranges[0]
        RangeTo = ranges[1]
        FirstLettersRangeFrom = RangeFrom.split(".")[0]
        SecondLetterRangeFrom = RangeFrom.split(".")[1][:1]
        NumbersRangeFrom = RangeFrom.split(".")[1][1:]
        FirstLettersRangeTo = RangeTo.split(".")[0]
        SecondLetterRangeTo = RangeTo.split(".")[1][:1]
        NumbersRangeTo = RangeTo.split(".")[1][1:]
        if FirstLettersRangeFrom[0] <= LettersOfCode[0] <= FirstLettersRangeTo[0]:
            # if FirstLettersRangeFrom[0] > LettersOfCode[0]:
            #     return False
            if FirstLettersRangeFrom[0] == LettersOfCode[0]:
                if len(FirstLettersRangeFrom) == 2 or len(FirstLettersRangeFrom) == 3 and len(LettersOfCode) == 1:
                    continue
                if FirstLettersRangeFrom[1] is not None and LettersOfCode[1] is not None:
                    if FirstLettersRangeFrom[1] > LettersOfCode[1]:
                        continue
                    if FirstLettersRangeFrom[1] == LettersOfCode[1]:
                        if len(FirstLettersRangeFrom) == 3 and len(LettersOfCode) < len(FirstLettersRangeFrom):
                            continue
                        if FirstLettersRangeFrom[2] is not None and LettersOfCode[2] is not None:
                            if FirstLettersRangeFrom[2] > LettersOfCode[2]:
                                continue
                            if FirstLettersRangeFrom[2] == LettersOfCode[2]:
                                if SecondLetterRangeFrom == SecondLetterOfcode:
                                    if not checkNumbersRangeFrom(NumbersRangeFrom, NumbersOfcode):
                                        continue
                                if SecondLetterRangeFrom > SecondLetterOfcode:
                                    continue
            if FirstLettersRangeTo[0] == LettersOfCode[0]:
                if len(LettersOfCode) == 2 or len(LettersOfCode) == 3 and len(FirstLettersRangeTo) == 1:
                    continue
                if FirstLettersRangeTo[1] is not None and LettersOfCode[1] is not None:
                    if FirstLettersRangeTo[1] < LettersOfCode[1]:
                        continue
                    if FirstLettersRangeTo[1] == LettersOfCode[1]:
                        if len(LettersOfCode) == 3 and len(LettersOfCode) > len(FirstLettersRangeTo):
                            continue
                        if FirstLettersRangeTo[2] is not None and LettersOfCode[2] is not None:
                            if FirstLettersRangeTo[2] < LettersOfCode[2]:
                                continue
                            if FirstLettersRangeTo[2] == LettersOfCode[2]:
                                if FirstLettersRangeTo == SecondLetterOfcode:
                                    if not checkNumbersRangeTo(NumbersRangeTo, NumbersOfcode):
                                        continue
                                if SecondLetterRangeTo < SecondLetterOfcode:
                                    continue
            return True

    return False


def checkNumbersRangeTo(numberRange, NumberCode):
    if len(NumberCode) > len(numberRange):
        for i in range(0, len(numberRange) - len(NumberCode)):
            NumberCode += '0'
        if int(NumberCode) > int(numberRange):
            return False
    elif len(NumberCode) == len(numberRange):
        if int(NumberCode) > int(numberRange):
            return False
    else:
        if int(NumberCode[0:len(numberRange)]) == int(numberRange):
            return False
        if int(NumberCode[0:len(numberRange)]) > int(numberRange):
            return False


def checkNumbersRangeFrom(numberRange, NumberCode):
    if len(NumberCode) > len(numberRange):
        for i in range(0, len(numberRange) - len(NumberCode)):
            NumberCode += '0'
        if int(NumberCode) < int(numberRange):
            return False
    elif len(NumberCode) == len(numberRange):
        if int(NumberCode) < int(numberRange):
            return False
    else:
        if int(NumberCode[0:len(numberRange)]) == int(numberRange):
            return False
        if int(NumberCode[0:len(numberRange)]) < int(numberRange):
            return False


def CheckLetterForGeneralBooks(bookRanges, LettersOfCode):
    # the Schema of the book's code is divided as  : (letters)(numbers)sectionA.(numbers)SectionB.(letter)
    # (numbers)SectionC(year)
    LettersOfCodeSectionA = LettersOfCode.split(".")[0]
    NumbersOfCodeSectionA = LettersOfCode.split(".")[0]
    if len(LettersOfCode.split("."))==3:
        NumbersOfCodeSectionA+="."+LettersOfCode.split(".")[1]
    # NumbersOfCodeSectionB = LettersOfCode.split(".")[1]
    LettersOfCodeSectionC = LettersOfCode.split(".")[2]
    NumbersOfCodeSectionC = LettersOfCode.split(".")[2]
    for i in range(0, len(bookRanges)):
        ranges = bookRanges[i].split("-")
        RangeFrom = ranges[0]
        RangeTo = ranges[1]
        LettersOfCodeSectionARangeFrom = GetLettersFromCode(RangeFrom.split(".")[0])
        NumbersOfCodeSectionARangeFrom = GetFirstNumbersFromCode(RangeFrom.split(".")[0])
        if len(RangeFrom.split("."))==3:
            NumbersOfCodeSectionARangeFrom+="."+RangeFrom.split(".")[1]
        LettersOfCodeSectionCRangeFrom = GetLettersFromCode(RangeFrom.split(".")[2])
        NumbersOfCodeSectionCRangeFrom = GetFirstNumbersFromCode(RangeFrom.split(".")[2])
        LettersOfCodeSectionARangeTo = GetLettersFromCode(RangeTo.split(".")[0])
        NumbersOfCodeSectionARangeTo = GetFirstNumbersFromCode(RangeTo.split(".")[0])
        if len(RangeTo.split(".")[0])==3:
            NumbersOfCodeSectionARangeTo+="."+RangeTo.split(".")[1]
        LettersOfCodeSectionCRangeTo = GetLettersFromCode(RangeTo.split(".")[2])
        NumbersOfCodeSectionCRangeTo = RangeTo.split(".")[2]
        if LettersOfCodeSectionARangeFrom[0] <= LettersOfCodeSectionA[0] <= LettersOfCodeSectionARangeTo[0]:
            # if FirstLettersRangeFrom[0] > LettersOfCode[0]:
            #     return False
            if LettersOfCodeSectionARangeFrom[0] == LettersOfCodeSectionA[0]:
                if len(LettersOfCodeSectionARangeFrom)==1 and len(LettersOfCodeSectionA)==1:
                    if int(NumbersOfCodeSectionARangeFrom)>int(NumbersOfCodeSectionA):
                        continue
                    if int(NumbersOfCodeSectionARangeFrom)==int(NumbersOfCodeSectionA):
                        if LettersOfCodeSectionC<LettersOfCodeSectionCRangeFrom:
                            continue
                        elif LettersOfCodeSectionC==LettersOfCodeSectionCRangeFrom:
                            if not checkNumbersRangeFrom(NumbersOfCodeSectionCRangeFrom,NumbersOfCodeSectionC):
                                continue
                if len(LettersOfCodeSectionARangeFrom) == 2 or len(LettersOfCodeSectionARangeFrom) == 3 and len(LettersOfCodeSectionA) == 1:
                    continue
                if LettersOfCodeSectionARangeFrom[1] is not None and LettersOfCodeSectionA[1] is not None:
                    if LettersOfCodeSectionARangeFrom[1] > LettersOfCodeSectionA[1]:
                        continue
                    if LettersOfCodeSectionARangeFrom[1] == LettersOfCodeSectionA[1]:
                        if len(LettersOfCodeSectionARangeFrom) == 3 and len(LettersOfCodeSectionA) < len(LettersOfCodeSectionARangeFrom):
                            continue
                        if len(LettersOfCodeSectionARangeFrom) == 2 and len(LettersOfCodeSectionA) == 2:
                            if int(NumbersOfCodeSectionARangeFrom) > int(NumbersOfCodeSectionA):
                                continue
                            if int(NumbersOfCodeSectionARangeFrom) == int(NumbersOfCodeSectionA):
                                if LettersOfCodeSectionC < LettersOfCodeSectionCRangeFrom:
                                    continue
                                elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeFrom:
                                    if not checkNumbersRangeFrom(NumbersOfCodeSectionCRangeFrom, NumbersOfCodeSectionC):
                                        continue
                        if LettersOfCodeSectionARangeFrom[2] is not None and LettersOfCodeSectionA[2] is not None:
                            if LettersOfCodeSectionARangeFrom[2] > LettersOfCodeSectionA[2]:
                                continue
                            if LettersOfCodeSectionARangeFrom[2] == LettersOfCodeSectionA[2]:
                               if int(NumbersOfCodeSectionARangeFrom) > int(NumbersOfCodeSectionA):
                                  continue
                               if int(NumbersOfCodeSectionARangeFrom) == int(NumbersOfCodeSectionA):
                                    if LettersOfCodeSectionC < LettersOfCodeSectionCRangeFrom:
                                        continue
                                    elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeFrom:
                                         if not checkNumbersRangeFrom(NumbersOfCodeSectionCRangeFrom,
                                                                         NumbersOfCodeSectionC):
                                            continue
            if LettersOfCodeSectionARangeTo[0] == LettersOfCodeSectionA[0]:
                if len(LettersOfCodeSectionARangeTo)==1 and len(LettersOfCodeSectionA)==1:
                    if int(NumbersOfCodeSectionARangeTo)>int(NumbersOfCodeSectionA):
                        continue
                    if int(NumbersOfCodeSectionARangeTo)==int(NumbersOfCodeSectionA):
                        if LettersOfCodeSectionC<LettersOfCodeSectionCRangeTo:
                            continue
                        elif LettersOfCodeSectionC==LettersOfCodeSectionCRangeTo:
                            if not checkNumbersRangeTo(NumbersOfCodeSectionCRangeTo,NumbersOfCodeSectionC):
                                continue
                if len(LettersOfCodeSectionARangeTo) == 2 or len(LettersOfCodeSectionARangeTo) == 3 and len(LettersOfCodeSectionA) == 1:
                    continue
                if LettersOfCodeSectionARangeTo[1] is not None and LettersOfCodeSectionA[1] is not None:
                    if LettersOfCodeSectionARangeTo[1] > LettersOfCodeSectionA[1]:
                        continue
                    if LettersOfCodeSectionARangeTo[1] == LettersOfCodeSectionA[1]:
                        if len(LettersOfCodeSectionARangeTo) == 3 and len(LettersOfCodeSectionA) < len(LettersOfCodeSectionARangeTo):
                            continue
                        if len(LettersOfCodeSectionARangeTo) == 2 and len(LettersOfCodeSectionA) == 2:
                            if int(NumbersOfCodeSectionARangeFrom) > int(NumbersOfCodeSectionA):
                                continue
                            if int(NumbersOfCodeSectionARangeFrom) == int(NumbersOfCodeSectionA):
                                if LettersOfCodeSectionC < LettersOfCodeSectionCRangeFrom:
                                    continue
                                elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeFrom:
                                    if not checkNumbersRangeFrom(NumbersOfCodeSectionCRangeFrom, NumbersOfCodeSectionC):
                                        continue
                        if LettersOfCodeSectionARangeTo[2] is not None and LettersOfCodeSectionA[2] is not None:
                            if LettersOfCodeSectionARangeTo[2] > LettersOfCodeSectionA[2]:
                                continue
                            if LettersOfCodeSectionARangeTo[2] == LettersOfCodeSectionA[2]:
                               if int(NumbersOfCodeSectionARangeTo) > int(NumbersOfCodeSectionA):
                                  continue
                               if int(NumbersOfCodeSectionARangeTo) == int(NumbersOfCodeSectionA):
                                    if LettersOfCodeSectionC < LettersOfCodeSectionCRangeTo:
                                        continue
                                    elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeTo:
                                         if not checkNumbersRangeTo(NumbersOfCodeSectionCRangeTo,
                                                                         NumbersOfCodeSectionC):
                                            continue
            return True
    return False


# def CheckFirstLetterOfCode(bookRanges, LettersOfCode):
#     FlagInitialLetters = True
#     FlagEndingLetters = True
#     lettersCodeBook = GetLettersFromCode(LettersOfCode)
#     for i in range(0, len(bookRanges)):
#         ranges = bookRanges[i].split("-")
#         RangeFrom = ranges[0]
#         RangeTo = ranges[1]
#         InitialLetters1 = RangeFrom[0]
#         EndingLetters1 = RangeTo[0]
#         if InitialLetters1 <= lettersCodeBook[0] <= EndingLetters1:
#             # checks the numbers, get the starting number of range and ending number of range and check if the book code is between them
#             InitialNumbers = GetFirstNumbersFromCode(RangeFrom)
#             endingNumbers = GetFirstNumbersFromCode(RangeTo)
#             NumbersOfCode = GetFirstNumbersFromCode(LettersOfCode)
#             if lettersCodeBook[0] == InitialLetters1:
#                 if lettersCodeBook[0] != 'x':
#                     if len(InitialLetters1) == 1:
#                         if NumbersOfCode < InitialNumbers:
#                             FlagInitialLetters = False
#                     else:
#                         FlagInitialLetters = False
#                 # if the length of the initial letter more than one means that the book code is not in the range for example : AB45. --- A173.
#                 return True
#             if EndingLetters1 == lettersCodeBook[0]:
#                 if len(EndingLetters1) == 1:
#                     if lettersCodeBook[0] != 'x':
#                         if int(NumbersOfCode) > int(endingNumbers):
#                             FlagEndingLetters = False
#             return FlagInitialLetters and FlagEndingLetters
#             # if the length of the initial letter more than one means that the book code is not in the range for example : AB45. --- A173
#     return False
#
#
# def CheckSecondLetterOfCode(bookRanges, LettersOfCode):
#     lettersCodeBook = GetLettersFromCode(LettersOfCode)
#     FlagNumbersIn = True
#     FlagNumbersEn = True
#     for i in range(0, len(bookRanges)):
#         ranges = bookRanges[i].split("-")
#         RangeFrom = ranges[0]
#         RangeTo = ranges[1]
#         InitialLetters1 = RangeFrom[0]
#         EndingLetters1 = RangeTo[0]
#         if InitialLetters1 <= lettersCodeBook[0] <= EndingLetters1:
#             InitialNumbers = GetFirstNumbersFromCode(RangeFrom)
#             endingNumbers = GetFirstNumbersFromCode(RangeTo)
#             NumbersOfCode = GetFirstNumbersFromCode(LettersOfCode)
#             if len(InitialLetters1) == 1 and len(EndingLetters1) == 1:
#                 return True
#             if len(InitialLetters1) == 2:
#                 if lettersCodeBook[0] == RangeFrom[0]:
#                     if lettersCodeBook[1] == RangeFrom[1]:
#                         if int(InitialNumbers) < int(NumbersOfCode):
#                             FlagNumbersIn = False
#                     if lettersCodeBook[1] < RangeFrom[1]:
#                         FlagNumbersIn = False
#             if len(EndingLetters1) == 1 and EndingLetters1[0] == lettersCodeBook[0]:
#                 FlagNumbersEn = False
#             if len(EndingLetters1) == 2:
#                 if lettersCodeBook[0] == RangeTo[0]:
#                     if lettersCodeBook[1] == RangeTo[1]:
#                         if int(endingNumbers) > int(NumbersOfCode):
#                             FlagNumbersEn = False
#                     if lettersCodeBook[1] < RangeFrom[1]:
#                         FlagNumbersEn = False
#             return FlagNumbersEn and FlagNumbersIn
#     return False


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
    return numbers


# print(GetLettersFromCode("0/R101"))
# print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/R101"))
print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/B50"))
print(SearchForBookCode("0/RC105.-T10.,AB101.-C4./140,141/yes", "0/X50"))
print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/C1"))
print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/C10"))
print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/C1"))
