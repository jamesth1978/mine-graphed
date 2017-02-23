import unittest


class SkillzTest(unittest.TestCase):
    def test(self):
        array = [1,3,5,6,5,2,8,9,1,12]
        print(array)
        swapped = True

        while(swapped):
            swapped = False
            for i in range(1,len(array)-1):
                if(array[i-1]>array[i]):
                    temp = array[i-1]
                    array[i-1] = array[i]
                    array[i] = temp
                    swapped = True

        print(array)

        #remove dupes
        #TODO has a bug - the '1' is missing
        result = []
        for i in range(1,len(array)):
            temp = array[i-1]
            if(temp!=array[i]):
                result.append(array[i])

        print("testUsing primitives: ")
        print(result)

    def testUsingDict(self):
        array = [1,3,5,6,5,2,8,9,1,12]
        countDict = dict()

        for i in range(0,len(array)):
            if(array[i] in countDict):
                countDict[array[i]] += 1
            else:
                countDict[array[i]] = 1

        keys = countDict.keys()
        print("testUsingDict: ")
        print(keys)

    def testUsingSet(self):
        array = [1, 3, 5, 6, 5, 2, 8, 9, 1, 12]
        numSet = set()
        for i in array:
            numSet.add(i)

        print("testUsingSet: ")
        print(numSet)