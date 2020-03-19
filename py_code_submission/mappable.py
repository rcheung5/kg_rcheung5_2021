class mappable:
    def __init__(self):
        self.classMade = True
    def isMappable(self, s1, s2):
        """ uses a hash table (aka dictionary in python) to go through s1 once
        and check if the letters in s1 have at most 1 other letter in s2 that
        correlates """
        ourHash = {}
        for index in range(len(s1)):
            if s1[index] not in ourHash:
                ourHash[s1[index]] = s2[index]
            else:
                if ourHash[s1[index]] != s2[index]:
                    print("false")
                    return
        print("true")
        return

