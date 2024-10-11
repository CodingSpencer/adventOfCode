import csv
import re

def main():
    arrayArray = collectNums()
    numbers = getNums(arrayArray)
    print(arraySum(numbers))

def arraySum(numbers):
    return sum(numbers)

def getNums(arrayArray):
    numbers = []
    for array in arrayArray:
        count = len(array)
        if count == 0:
            number = 0
        elif count == 1:
            number = f'{array[0]}{array[0]}'
        else:
            number = f'{array[0]}{array[count -1]}'
        numbers.append(int(number))
    return numbers

def collectNums():
    arrayArray = []
    with open ('2023/Day_1/numbers_list.csv', 'r') as numbers_list:
        for line in numbers_list:
            arrayArray.append(re.findall('[0-9]', line))
    return arrayArray

if __name__ == "__main__":
    main()