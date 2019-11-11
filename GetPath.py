#!/usr/bin/env python
import networkx as nx
from ConnectToDB import BuildAll
import sys


G = BuildAll()


# This script is build in two sections
def FindTheNode(graph, Code):
    for u, a in graph.nodes(data=True):
        # print(a['data'])
        if SearchForType(a['data'], Code):
            return u
    return None


def SearchForType(Node, Code):
    TheType = Code.split("/")[0]
    if int(TheType) == 0:
        return SearchForBookCode(Node, Code)
    elif int(TheType) == 1:
        return SearchForRoom(Node, Code)


# this function checks if the neighborhood node is relevant for current node
def SearchForToilets(Node):
    for visiting_node in nx.bfs_tree(G, Node):
        if G.node[visiting_node].get('data').split("/")[3] == "1":
            return nx.shortest_path(G, source=1, target=visiting_node)


# print(SearchForToilets(15))
def SearchForBookCode(currentNode, code):
    LettersOfCode = GetLettersFromCode(code.split("/")[2])
    # print(LettersOfCode)
    requiredArea = code.split("/")[1]
    existingArea = currentNode.split("/")[0]
    if requiredArea != existingArea:
        return False
    SplittedNode = currentNode.split("/")[1]
    bookRanges = SplittedNode.split(",")
    #########################
    if currentNode.split("/")[1] == "ALL":
        return False
    if LettersOfCode[0] == 'X':
        return CheckForMagazines(bookRanges, code.split("/")[2])
    return CheckLetterForGeneralBooks(bookRanges, code.split("/")[2])


def CheckForMagazines(bookRanges, code):
    LettersOfCode = code.split(".")[0]
    SecondLetterOfcode = code.split(".")[1][:1]
    NumbersOfcode = code.split(".")[1][1:]
    for i in range(0, len(bookRanges)):
        if bookRanges == "ALL":
            continue
        ranges = bookRanges[i].split("-")
        if ranges[0].split(".")[0][0] != "X":
            continue
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
                if len(FirstLettersRangeFrom) == 2 or len(FirstLettersRangeFrom) == 3:
                    if len(LettersOfCode) == 1:
                        continue
                if len(FirstLettersRangeFrom) >= 2 and len(LettersOfCode) >= 2:
                    if FirstLettersRangeFrom[1] > LettersOfCode[1]:
                        continue
                    if FirstLettersRangeFrom[1] == LettersOfCode[1]:
                        if len(FirstLettersRangeFrom) == 3 and len(LettersOfCode) < len(FirstLettersRangeFrom):
                            continue
                        if len(FirstLettersRangeFrom) >= 3 and len(LettersOfCode) >= 3:
                            if FirstLettersRangeFrom[2] > LettersOfCode[2]:
                                continue
                            if FirstLettersRangeFrom[2] == LettersOfCode[2]:
                                if SecondLetterRangeFrom == SecondLetterOfcode:
                                    if not checkNumbersRangeFrom(NumbersRangeFrom, NumbersOfcode):
                                        continue
                                if SecondLetterRangeFrom > SecondLetterOfcode:
                                    continue

            if FirstLettersRangeTo[0] == LettersOfCode[0]:
                if len(LettersOfCode) == 2 or len(LettersOfCode) == 3:
                    if len(FirstLettersRangeTo) == 1:
                        continue
                if len(FirstLettersRangeTo) >= 2 and len(LettersOfCode) >= 2:
                    if FirstLettersRangeTo[1] < LettersOfCode[1]:
                        continue
                    if FirstLettersRangeTo[1] == LettersOfCode[1]:
                        if len(LettersOfCode) == 3 and len(LettersOfCode) > len(FirstLettersRangeTo):
                            continue
                        if len(FirstLettersRangeTo) >= 3 and len(LettersOfCode) >= 3:
                            if FirstLettersRangeTo[2] < LettersOfCode[2]:
                                continue
                            if FirstLettersRangeTo[2] == LettersOfCode[2]:
                                if SecondLetterRangeTo == SecondLetterOfcode:
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
    return True


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
    return True


def CheckLetterForGeneralBooks(bookRanges, LettersOfCode):
    # the Schema of the book's code is divided as  : (letters)(numbers)sectionA.(numbers)SectionB.(letter)
    # (numbers)SectionC(year)
    LettersOfCodeSectionA = GetLettersFromCode(LettersOfCode.split(".")[0])
    NumbersOfCodeSectionA = GetFirstNumbersFromCode(LettersOfCode.split(".")[0])
    LettersOfCodeSectionC = ""
    NumbersOfCodeSectionC = ""
    if len(LettersOfCode.split(".")) == 3:
        NumbersOfCodeSectionA += "." + LettersOfCode.split(".")[1]
        LettersOfCodeSectionC = LettersOfCode.split(".")[2]
        NumbersOfCodeSectionC = LettersOfCode.split(".")[2]
    else:
        LettersOfCodeSectionC = LettersOfCode.split(".")[1]
        NumbersOfCodeSectionC = LettersOfCode.split(".")[1]
    for i in range(0, len(bookRanges)):
        ranges = bookRanges[i].split("-")
        RangeFrom = ranges[0]
        RangeTo = ranges[1]
        LettersOfCodeSectionARangeFrom = GetLettersFromCode(RangeFrom.split(".")[0])
        NumbersOfCodeSectionARangeFrom = GetFirstNumbersFromCode(RangeFrom.split(".")[0])
        LettersOfCodeSectionCRangeFrom = ""
        NumbersOfCodeSectionCRangeFrom = ""
        if len(RangeFrom.split(".")) == 3:
            NumbersOfCodeSectionARangeFrom += "." + RangeFrom.split(".")[1]
            LettersOfCodeSectionCRangeFrom = GetLettersFromCode(RangeFrom.split(".")[2])
            NumbersOfCodeSectionCRangeFrom = GetFirstNumbersFromCode(RangeFrom.split(".")[2])
        else:
            LettersOfCodeSectionCRangeFrom = GetLettersFromCode(RangeFrom.split(".")[1])
            NumbersOfCodeSectionCRangeFrom = GetFirstNumbersFromCode(RangeFrom.split(".")[1])
        LettersOfCodeSectionARangeTo = GetLettersFromCode(RangeTo.split(".")[0])
        NumbersOfCodeSectionARangeTo = GetFirstNumbersFromCode(RangeTo.split(".")[0])
        LettersOfCodeSectionCRangeTo = ""
        NumbersOfCodeSectionCRangeTo = ""
        if len(RangeTo.split(".")[0]) == 3:
            NumbersOfCodeSectionARangeTo += "." + RangeTo.split(".")[1]
            LettersOfCodeSectionCRangeTo = GetLettersFromCode(RangeTo.split(".")[2])
            NumbersOfCodeSectionCRangeTo = RangeTo.split(".")[2]
        else:
            LettersOfCodeSectionCRangeTo = GetLettersFromCode(RangeTo.split(".")[1])
            NumbersOfCodeSectionCRangeTo = RangeTo.split(".")[1]
        if LettersOfCodeSectionARangeFrom[0] <= LettersOfCodeSectionA[0] <= LettersOfCodeSectionARangeTo[0]:
            # if FirstLettersRangeFrom[0] > LettersOfCode[0]:
            #     return False
            if LettersOfCodeSectionARangeFrom[0] == LettersOfCodeSectionA[0]:
                if len(LettersOfCodeSectionARangeFrom) == 1 and len(LettersOfCodeSectionA) == 1:
                    if float(NumbersOfCodeSectionARangeFrom) > float(NumbersOfCodeSectionA):
                        continue
                    if float(NumbersOfCodeSectionARangeFrom) == float(NumbersOfCodeSectionA):
                        if LettersOfCodeSectionC < LettersOfCodeSectionCRangeFrom:
                            continue
                        elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeFrom:
                            if not checkNumbersRangeFrom(NumbersOfCodeSectionCRangeFrom, NumbersOfCodeSectionC):
                                continue
                if len(LettersOfCodeSectionARangeFrom) == 2 or len(LettersOfCodeSectionARangeFrom) == 3:
                    if len(LettersOfCodeSectionA) == 1:
                        continue
                if len(LettersOfCodeSectionARangeFrom) >= 2 and len(LettersOfCodeSectionA) >= 2:
                    if LettersOfCodeSectionARangeFrom[1] > LettersOfCodeSectionA[1]:
                        continue
                    if LettersOfCodeSectionARangeFrom[1] == LettersOfCodeSectionA[1]:
                        if len(LettersOfCodeSectionARangeFrom) == 3 and len(LettersOfCodeSectionA) < len(
                                LettersOfCodeSectionARangeFrom):
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
                        if len(LettersOfCodeSectionARangeFrom) >= 3 and len(LettersOfCodeSectionA) >= 3:
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
                if len(LettersOfCodeSectionARangeTo) == 1 and len(LettersOfCodeSectionA) == 1:

                    if float(NumbersOfCodeSectionARangeTo) < float(NumbersOfCodeSectionA):
                        continue
                    if float(NumbersOfCodeSectionARangeTo) == float(NumbersOfCodeSectionA):
                        if LettersOfCodeSectionC < LettersOfCodeSectionCRangeTo:
                            continue
                        elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeTo:
                            if not checkNumbersRangeTo(NumbersOfCodeSectionCRangeTo, NumbersOfCodeSectionC):
                                continue
                if len(LettersOfCodeSectionARangeTo) == 2 or len(LettersOfCodeSectionARangeTo) == 3:
                    if len(LettersOfCodeSectionA) == 1:
                        continue
                if len(LettersOfCodeSectionARangeTo) >= 2 and len(LettersOfCodeSectionA) >= 2:
                    if LettersOfCodeSectionARangeTo[1] < LettersOfCodeSectionA[1]:
                        continue
                    if LettersOfCodeSectionARangeTo[1] == LettersOfCodeSectionA[1]:
                        if len(LettersOfCodeSectionARangeTo) == 3 and len(LettersOfCodeSectionA) < len(
                                LettersOfCodeSectionARangeTo):
                            continue
                        if len(LettersOfCodeSectionARangeTo) == 2 and len(LettersOfCodeSectionA) == 2:
                            if float(NumbersOfCodeSectionARangeFrom) > float(NumbersOfCodeSectionA):
                                continue
                            if float(NumbersOfCodeSectionARangeFrom) == float(NumbersOfCodeSectionA):
                                if LettersOfCodeSectionC < LettersOfCodeSectionCRangeFrom:
                                    continue
                                elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeFrom:
                                    if not checkNumbersRangeFrom(NumbersOfCodeSectionCRangeFrom, NumbersOfCodeSectionC):
                                        continue
                        if len(LettersOfCodeSectionARangeTo) >= 3 and len(LettersOfCodeSectionA) >= 3:
                            if LettersOfCodeSectionARangeTo[2] > LettersOfCodeSectionA[2]:
                                continue
                            if LettersOfCodeSectionARangeTo[2] == LettersOfCodeSectionA[2]:
                                if float(NumbersOfCodeSectionARangeTo) > float(NumbersOfCodeSectionA):
                                    continue
                                if float(NumbersOfCodeSectionARangeTo) == float(NumbersOfCodeSectionA):
                                    if LettersOfCodeSectionC < LettersOfCodeSectionCRangeTo:
                                        continue
                                    elif LettersOfCodeSectionC == LettersOfCodeSectionCRangeTo:
                                        if not checkNumbersRangeTo(NumbersOfCodeSectionCRangeTo,
                                                                   NumbersOfCodeSectionC):
                                            continue
            return True
    return False


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


def SearchForRoom(node, Code):
    RoomRange = node.split("/")[2]
    Rooms = RoomRange.split(",")
    if Code.split("/")[2] in Rooms:
        return True


def ActiveSearch(currentNode, RequstedNode):
    G = BuildAll()
    if int(RequstedNode.split("/")[0]) == 0 or int(RequstedNode.split("/")[0]) == 1:
        return nx.shortest_path(G, source=int(currentNode), target=int(FindTheNode(G, RequstedNode)))
    else:
        SearchForToilets(currentNode)


# def SearchForToilets(Node):
print(ActiveSearch(sys.argv[1],sys.argv[2]))
# print(SearchForBookCode("0/XB.A53-XB.A7/yes", "0/XA.A5"))
# # False
# print(SearchForBookCode("0/XB.A53-XB.A7,XD.A1-XQ.A7/140,141/yes", "0/XD.A4"))
# # True
# print(SearchForBookCode("0/T57.C668-T60.5.C668,AB101.B1-C4.1.A3/140,141/yes", "0/T58.6.C668"))
# # true
# print(SearchForBookCode("0/T57.C668-T58.5.C668,AB101.B1-C4.1.A3/140,141/yes", "0/T59.C668"))
# # false
# print(SearchForBookCode("0/RC105.-P10.,AB101.-C4./140,141/yes", "0/C1"))
# FindTheNode(G, "2/NB73.A1")
# find_all_paths(G,"1","17"))
# print(FindTheNode(G, "0/2/XBM.A20"))
# print(nx.shortest_path(G, source=1, target=int(FindTheNode(G, "0/2/XBM.A20"))))
# print(nx.shortest_path(G, source=1, target=int(FindTheNode(G, "0/2/XG.A5"))))
