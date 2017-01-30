import random
playing = False
chip_pool = 100
bet=1
restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit"
#Hearts,Diamonds,Clubs,Spades
suits = ('H','D','C','S')
ranking = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
card_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.suit + self.rank
    def grab_suit(self):
        return self.suit
    def grab_rank(self):
        return self.rank
    def draw(self):
        print((self.suit+self.rank))
class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.ace=False
    def __str__(self):
        hand_comp=""
        for card in self.cards:
            card_name=card.__str__()
            hand_comp+=" "+card_name
        return 'The hand has %s'%hand_comp
    def card_add(self,card):
        self.cards.append(card)
        if card.rank=='A':
            self.ace=True
        self.value+=card_val[card.rank]
    def calc_value(self):
        if(self.ace==True and self.value<12):
            return self.value+10
        else:
            return self.value
    def draw(self,hidden):
        if hidden==True and playing == True:
            starting_card=1
        else:
            starting_card=0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw()
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
    def __str__(self):
        deck_comp=""
        for card in self.cards:
            deck_comp+=" "+deck_comp.__str__()
        return "The deck has" +deck_comp
def make_bet():
    global bet
    bet=0
    print('What amount of chips would you like to bet?')
    while bet==0:
        bet_comp=input()
        bet_comp=int(bet_comp)
        if bet_comp>=1 and bet_comp<=chip_pool:
            bet = bet_comp
        else:
            print('Invalid bet, you only have '+ str(chip_pool)+' remaining')
def deal():
    global result,playing,deck,player_hand,dealer_hand,chip_pool,bet
    #creates deck
    deck=Deck()
    #shuffles deck
    deck.shuffle()
    #Set's up bet
    make_bet()
    #sets hands
    player_hand=Hand()
    dealer_hand=Hand()
    #deals out cards
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    result="(h)it or (s)tand?"
    if playing==True:
        print('Fold')
        chip_pool-=bet
    playing=True
    game_step()
def hit():
    global playing,chip_pool,deck,player_hand,dealer_hand,result,bet
    #if hand is in play add card
    if playing:
        if player_hand.calc_value()<=21:
            player_hand.card_add(deck.deal())
        print("Player hand is %s"%player_hand)
        if player_hand.calc_value()>21:
            result='BUSTED HAHAHAHA        '+restart_phrase
            chip_pool-=bet
            playing=False
    else:
        result="Sorry, can't hit        "+restart_phrase
    game_step()
def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet
    if playing==False:
        if player_hand.calc_value()>0:
            result="Sorry, can't stand"
    else:
        while dealer_hand.calc_value()<17:
            dealer_hand.card_add(deck.deal())
        if dealer_hand.calc_value()>21:
            result="Dealer busts!!!!! OH YEA        "+restart_phrase
            chip_pool+=bet
            playing=False
        elif dealer_hand.calc_value()<player_hand.calc_value():
            result="you beat dealer!        " + restart_phrase
            chip_pool+=bet
            playing=False
        elif dealer_hand.calc_value()==player_hand.calc_value():
            result="Tied!!        "+restart_phrase
            playing=False
        else:
            result="Dealer wins :(        "+restart_phrase
            chip_pool-=bet
            playing=False
    game_step()
def game_step():
    print("")
    print('Player hand is: '),
    player_hand.draw(hidden=False)
    print('Player hand total is: ' + str(player_hand.calc_value()))

    print("Dealer hand is: "),
    dealer_hand.draw(hidden=True)
    #if game round is over
    if playing==False:
        print("--- for a total of " + str(dealer_hand.calc_value()))
        print("Chip total: "+ str(chip_pool))
    else:
        print("with another card hidden upside down")
    print(result)
    player_input()
def game_exit():
    print("Thanks for playing you addict")
    exit()
def player_input():
    plin = input().lower()
    if plin=='h':
        hit()
    elif plin=='s':
        stand()
    elif plin=='d':
        deal()
    elif plin=='q':
        game_exit()
    else:
        print("What do you think you're typing, type the correct response idiot")
def intro():
    statement="Welcome to the awesome Blackjack!!"
    st2="I hope you know how to play if not then google it or something"
    st3="what person doesn't know how to play blackjack. Fine, closest to 21 wins, aces are 1 or 11."
    print(statement)
    print(st2)
    print(st3)
    print()
#creats deck
deck=Deck()
#shuffles
deck.shuffle()
#creates player
player_hand=Hand()
dealer_hand=Hand()
intro()
deal()