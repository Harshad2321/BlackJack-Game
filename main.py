import random
import art
def deal_card():
    cards_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards_value)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    total_sum=sum(cards)
    return total_sum

def compare(user__score, cp_score):
    if user__score == cp_score:
        return "Draw 🙃"
    elif cp_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user__score == 0:
        return "Win with a Blackjack 😎"
    elif user__score > 21:
        return "You went over. You lose 😭"
    elif cp_score > 21:
        return "Opponent went over. You win 😁"
    elif user__score > cp_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game_on():
    print(art.logo)
    game_over=False
    user_cards = []
    computer_cards = []
    computer_score=-1
    user_score=-1
    
    for a in range(2):
        user_cards.append(deal_card())
        computer_cards.append((deal_card()))
    
    while not game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards:{user_cards},current score:{user_score}")
        print("Computer's First Card:",computer_cards[0])
    
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            user_deal=input("Type 'yes' to get another card,type 'no' to pass:").lower()
            if user_deal == 'yes':
                user_cards.append(deal_card())
            else:
                game_over=True
    
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    
    print(f"Your final hand:{user_cards} and final score:{user_score}")
    print(f"computer's final score:{computer_score}")
    print(compare(user_score,computer_score))
while input("Do You want to play a game of BlackJack?Type 'yes' or 'no' :").lower()=='yes':
    print("\n"*50)
    game_on()
else:
    print("Thank You For Playing With Us.Come Again.")
