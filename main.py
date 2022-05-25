import random

def choose():

    words = ['rainbow', 'computer',
            'science', 'programming',
            'foxtrot', 'lebronjames']

    pick = random.choice(words) 
    return pick

def jumble(word):

    random_word = random.sample(word, len(word))

    jumbled = ''.join(random_word)

    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is :', p1)
    print(p2n, 'Your score is :', p2)

    check_win(p1n, p2n, p1, p2)

    print('Thanks for playing...')

def check_win(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("winner is:", player1)
    elif p2score > p1score:
        print("winner is:", player2)
    else:
        print("Draw...Well played!")


def play():

  p1name = input("player 1, Please enter your name:")
  print(p1name)
  p2name = input("player 2, Please enter your name:")

  pp1 = 0
  pp2 = 0

  turn = 0

  while True:
    
    picked_word = choose()

    qn = jumble(picked_word)
    print("jumbled word is: ", qn)

    if turn % 2 == 0:

        print(p1name, "Your Turn.")

        ans = input("What's in your mind? ")

        if ans == picked_word:

            pp1 += 1

            print("Your score is :", pp1)

            turn+=1

        else: 
          print("Better luck next time...")

          print(p2name, "Your turn.")

          ans = input("What's in your mind? ")

          if ans == picked_word:

            pp2 += 1

            print("Your score is :", pp2)

          else:
            print("Better luck next time...correct word is :", picked_word)

          c = int(input("press 1 to continue and 0 to quit:"))

          if c == 0:
  
              thank(p1name, p2name, pp1, pp2)
              break
   
    else:

        print(p2name, "Your turn.")
        ans = input("what is in your mind? ")

        if ans == picked_word:
            pp2 += 1
            print("Your score is :", pp2)
            turn += 1

        else: 
          print("Better luck next time...")
          print(p1name, "Your turn.")
          ans = input("What's in your mind? ")

          if ans == picked_word:
              pp1 += 1
              print("Your score is :", pp1)

          else:
            print("Better luck next time...correct word is :", picked_word)
          
            c = int(input("press 1 to continue and 0 to quit:"))

            if c == 0:
  
              thank(p1name, p2name, pp1, pp2)
              break
          
        c = int(input("press 1 to continue and 0 to quit:"))
        if c == 0:
  
              thank(p1name, p2name, pp1, pp2)
              break
          
play()
