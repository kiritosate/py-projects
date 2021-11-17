# simple bubble sort algo
# by kiritosate

class BubbleSort:

    def __init__(self) -> None:
        
        while True:

            listtosort = input("enter list or numbers separated by a comma: ")
            clean = listtosort.split(',')
            length = len(clean)

            for i in range(length):

                for j in range(length):

                    if clean[i] < clean[j-1]:

                        temp = clean[i]
                        clean[i] = clean[j-1]
                        clean[j-1] = temp

            print(clean)


if __name__ == '__main__':
    BubbleSort()


