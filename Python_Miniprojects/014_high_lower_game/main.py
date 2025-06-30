from art import logo, vs
from game_data import data
import random
print(logo)

def format_data(account):
    #Fomat the account data into printable format
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, {account_descr}, {account_country}"

def follower(account):
    account_follower = account['follower_count']
    return account_follower

score = 0
game_continue = True
account_b = random.choice(data)
while game_continue:
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    #Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a = follower(account_a)
    b = follower(account_b)

    def check_answer(guess, a, b):
        ##Get follower count of each account
        if (guess == 'a' and a > b) or (guess == 'b' and b > a):
            print("You're right!")
            #True 반환 -> 정답 -> 점수 증가, 게임 계속 진행
            return True
        else:
            print("Sorry, that's wrong.")
            #False 반환 -> 오답 -> game_continue = False -> 게임 종료
            return False
    #조건이 False면 else 실행
    if check_answer(guess, a, b):
        score += 1
        print(f"Your current score: {score}")
    else:
        game_continue = False
        print(f"Final score: {score}")
