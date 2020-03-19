from mappable import mappable
import sys

def main():
    s1 = str(sys.argv[1]) #take from command line
    s2 = str(sys.argv[2]) #take from command line
    ourClass = mappable() #creates a mappable class
    ourClass.isMappable(s1, s2) #uses the isMappable from the mappable class


if __name__ == "__main__":
    main()
