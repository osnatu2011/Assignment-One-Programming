                            # Question 2
try:
    test1 = int(input("Enter test 1 Score: "))
    test2 = int(input("Enter test 2 Score: "))
    test3 = int(input("Enter test 3 Score: "))

    average_score = (test1 + test2 + test3) / 3

    print(f"You scored {test1} on the first test")
    print(f"You scored {test2} on the second test")
    print(f"You scored {test3} on teh third test")
    print(f"So, your average score is {average_score}")
except ValueError:
    print("Please input numbers only")