import art
print(art.logo)


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators={"+":add,"-":subtract,"*":multiply,"/":divide}


def calculator():
    first_num = float(input("Enter your first number: "))
    should_continue = True
    while should_continue:
        for keys in operators:
            print(keys)
        operations = input("Select the operation you want to do: ")
        second_num = float(input("Enter your next number: "))
        result = operators[operations](first_num, second_num)
        print(f"{first_num} {operations} {second_num} = {result}")

        previous_result = input(
            "Do you want to continue with the previous result.Type 'y' for yes or 'n' for new calculation: ").lower()
        if previous_result == "y":
            first_num=result
        else:
            should_continue = False
            print("\n" * 100)
            calculator()
calculator()




