num_list = []

def binary_conversion(num):
    if num >= 1:
        binary_conversion(num // 2)
        num_list.append(num % 2)
    return num_list


cards = [[], [], [], [], [], []]


def fill_cards():
    global num_list
    for i in range(1, 64):
        list_nums = binary_conversion(i)
        while len(list_nums) < 6:
            list_nums.insert(0, 0)
        for j in range(6):
            if list_nums[j] == 1:
                cards[j].append(i)
        num_list = []

def gameplay():
    print("Choose a number between 1 and 63")
    user_input = input("Type start if you want to play")
    if user_input == "start":
        sum_so_far = 0
        fill_cards()
        if cards[0][0] != 1:
            cards.reverse()
        for i in range(6):
            print(cards[i])
            user_answer = input("Is your number in the following? (Y/N)")
            if user_answer == "Y":
                sum_so_far += cards[i][0]
        print("I have read your mind! Your number is - " + str(sum_so_far) + "\n Is it correct? ")
        answer = input("Y/N")
        if answer == "N":
            print("You did not think of a number from 1 and 63, please think again.")
            gameplay()


gameplay()
