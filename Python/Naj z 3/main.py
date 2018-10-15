def max_of_two(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        return firstNumber
    return secondNumber


def max_of_three(firstNumber, secondNumber, thirdNumber):
    return max_of_two(firstNumber, max_of_two(secondNumber, thirdNumber))


print(max_of_three(3, 6, -5))
