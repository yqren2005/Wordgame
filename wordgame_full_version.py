from wordgame_single_version import *

def isValidWord2(word, hand):
    newhand = hand.copy()
    for char in word:
        if char in newhand.keys() and newhand[char] > 0:
            newhand[char] -= 1
        else:
            return False
    return True

def compChooseWord(hand, wordDict, n):
    """
    Given a hand and a wordDict, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordDict can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordDict: dictionary (string -> 1)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestscore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    result = None
    # For each word in the wordList
    for word in wordDict:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord2(word, hand):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > bestscore:
                # Update your best score, and best word accordingly
                bestscore = score
                result = word
    # return the best word you found.
    return result

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalscore = 0
    wordDict = dict((key, 1) for key in wordList)
    while calculateHandlen(hand) > 0:
        print "Current Hand:",
        displayHand(hand)
        result = compChooseWord(hand, wordDict, n)
        if result != None:
            totalscore += getWordScore(result, n)
            hand = updateHand(hand, result)
            print '''"%s" earned %d points. Total: %d points\n''' %(result, getWordScore(result, n), totalscore)
        else:
            break
    print "Total score: %d points.\n" %totalscore

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    while True:
        ans = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        print
        if ans == 'e':
            break
        elif ans == 'r' and len(hand) == 0:
            print "You have not played a hand yet. Please play a new hand first!\n"
        elif ans in ['n', 'r']:
            while True:
                ans2 = raw_input("Enter u to have yourself play, c to have the computer play: ")
                print
                if ans == 'n' and ans2 in ['u', 'c']:
                    hand = dealHand(HAND_SIZE)
                if ans2 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif ans2 == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print "Invalid command.\n"
        else:
            print "Invalid command.\n"
        
# Build data structures used for entire session and play game
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
