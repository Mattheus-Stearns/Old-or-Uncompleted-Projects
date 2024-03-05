from phevaluator import evaluate_cards
from random import randint

deck = ["As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd"]


class Cards:
    def shuffle():
        tempDeck = ["As", "2s", "3s", "4s", "5s", "6s", "7s", "8s", "9s", "Ts", "Js", "Qs", "Ks", "Ah", "2h", "3h", "4h", "5h", "6h", "7h", "8h", "9h", "Th", "Jh", "Qh", "Kh", "Ac", "2c", "3c", "4c", "5c", "6c", "7c", "8c", "9c", "Tc", "Jc", "Qc", "Kc", "Ad", "2d", "3d", "4d", "5d", "6d", "7d", "8d", "9d", "Td", "Jd", "Qd", "Kd"]
        shuffledDeck = []
        counter = len(deck) - 1
        while counter >= 0:
            randomNum = randint(0, counter)
            shuffledDeck.append(tempDeck[randomNum])
            tempDeck.pop(randomNum)
            counter -= 1
        return shuffledDeck

    def deal():
        global river, hands, pos1, pos2, pos3, pos4, pos5, flop, turn
        pos1 = [shuffledDeck[0], shuffledDeck[5]]
        pos2 = [shuffledDeck[1], shuffledDeck[6]]
        pos3 = [shuffledDeck[2], shuffledDeck[7]]
        pos4 = [shuffledDeck[3], shuffledDeck[8]]
        pos5 = [shuffledDeck[4], shuffledDeck[9]]
        hands = [pos1, pos2, pos3, pos4, pos5]
        
        flop = shuffledDeck[13:16]
        
        turn = [shuffledDeck[17]]
        turn += flop
        
        river = [shuffledDeck[19]]
        river += turn
    
    def find_repeat(numbers):
        seen = set()
        for num in numbers:
            if num in seen:
                return num
            seen.add(num)

        return set
        
    def evaluate(p1fold, p2fold, p3fold, p4fold, p5fold):
        global evals, sortedEvals, pos1, pos2, pos3, pos4, pos5, highestHand, repeatedEval

        pos1 += river
        pos2 += river
        pos3 += river
        pos4 += river
        pos5 += river


        if p1fold == False:
            pos1eval = evaluate_cards(pos1[0], pos1[1], pos1[2], pos1[3], pos1[4], pos1[5], pos1[6])
        else:
            pos1eval = 7463
        if p2fold == False:
            pos2eval = evaluate_cards(pos2[0], pos2[1], pos2[2], pos2[3], pos2[4], pos2[5], pos2[6])
        else:
            pos2eval = 7463
        if p3fold == False:
            pos3eval = evaluate_cards(pos3[0], pos3[1], pos3[2], pos3[3], pos3[4], pos3[5], pos3[6])
        else:
            pos3eval = 7463
        if p4fold == False:
            pos4eval = evaluate_cards(pos4[0], pos4[1], pos4[2], pos4[3], pos4[4], pos4[5], pos4[6])
        else:
            pos4eval = 7463
        if p5fold == False:
            pos5eval = evaluate_cards(pos5[0], pos5[1], pos5[2], pos5[3], pos5[4], pos5[5], pos5[6])
        else:
            pos5eval = 7463

        
        evals = [pos1eval, pos2eval, pos3eval, pos4eval, pos5eval]
        sortedEvals = [pos1eval, pos2eval, pos3eval, pos4eval, pos5eval]

        highestHand = []
        sortedEvals.sort()
        repeatedEval = Cards.find_repeat(sortedEvals)
        if type(repeatedEval) == int:
            for i in range(0, 5):
                if evals[i] == repeatedEval:
                    highestHand.append(i + 1)
        else:
            for i in range(0, 5):
                if evals[i] == sortedEvals[0]:
                    highestHand.append(i + 1)            
        return highestHand

class Players:
    def make_decision(hand_strength, pot_size, bet_size):
        weak_threshold = 0.2
        moderate_threshold = 0.4
        strong_threshold = 0.7
        very_strong_threshold = 0.9
        
        pot_odds = bet_size / (pot_size + bet_size)

        if hand_strength < weak_threshold:
            if pot_odds < 0.1:  
                return "Fold"
            else:
                return "Call"
        elif hand_strength < moderate_threshold:
            if pot_odds < 0.3:
                return "Call"
            else:
                return "Raise"
        elif hand_strength < strong_threshold:
            if pot_odds < 0.5:
                return "Bet"
            else:
                return "Raise"
        elif hand_strength < very_strong_threshold:
            if pot_odds < 0.5:
                return "Bet"
            else:
                return "Call"
        else:
            return "Raise"






stacks = [1000, 1000, 1000, 1000, 1000]
#hand_strength = 1 - (evaluated_card / 7462)


counter = 0

pot = 0
bet = 0
shuffledDeck = Cards.shuffle()
Cards.deal()
print(hands)
print(river)
print(Cards.evaluate(False, False, False, False, False))




