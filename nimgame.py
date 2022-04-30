
def user_play(n, m):
    global l
    global k
    global H 
    H = 0
    l = 0
    global u 
    u = 1
    k = int(input('How much pieces you will remove? '))
    while k > m or k <= 0 and n - k < 0:
        print("Oops! Invalid movement. Try again ")
        k = int(input('How much pieces you will remove?')) 
    if k <= m and k != 0:
        n = n - k
        if k == 1:
            print("You removed one piece")
        else:
            print("You removed", k, "pieces")
        if n == 1:
            print("Now", n, "piece remain on the board")
        elif n == 0:
            print("Game over! You win!")
        else:
            print("Now", n, "pieces remain on the board")
            
       

def PC_play(n, m):
    global l
    l = 1
    global u
    u = 2
    global k
    k = 1
    while (n - k) % (m + 1) != 0 and m > k and k > 0 and (n - k) > 0:
        k = k + 1
    n = n - k
    if  k == 1:
        print("The PC removed one piece.")
    if  k != 1:
        print("The PC removed", k, "pieces.")
    if n == 1:
        print("Now", n, "piece remain on the board")
    elif n == 0:
        print("Game over! The PC win")
    else:
        print("Now", n, "pieces on the board")
        
def start_match():
    n = int(input("Type the number of pieces on the board: "))
    m = int(input("Type the number of pieces which can be removed per round: "))
    round = 1
    while n != 0:
        while round != 2:
            round = round + 1
            if n % (m + 1) == 0:
                print("You play!")
                user_play(n, m)
            else:
                print("PC play!")
                PC_play(n, m)
        if u == 2 and n > 0:
            n = n - k
            if n > 0:

                print("You play!")
                user_play(n, m)
        if u == 1 and n > 0:
            n = n - k
            if n > 0:
                print("PC play!")
                PC_play(n, m)
            


def championship():
    start_match()
    if l == 1:
        print("PC: 1 | You: 0")
        H == 1
    if l == 0:
        print("PC: 0 | You: 1")
        H == 0
    start_match()
    if l == 0 and H == 1:
        print("PC: 1 | You: 1")
        r = 1
    if l == 0 and H == 0:
        print("PC: 0 | You: 2")
        r = 2
    if l == 1 and H == 1:
        print("PC: 2 | You: 0")
        r = 3
    if l == 1 and H == 0:
        print("PC: 1 | You: 1")
        r = 4
    start_match()
    if r == 1 and l == 1:
        print("PC: 2 | You: 1")
        print("PC win!")
    if r == 1 and l == 0:
        print("PC: 1 | You: 2")
        print("You win!")    
    if r == 2 and l == 1:
        print("PC: 1 | You: 2")
        print("You win!")
    if r == 2 and l == 0:
        print("PC: 0 | You: 3")
        print("You win!")
    if r == 3 and l == 1:
        print("PC: 3 | You: 0")
        print("PC win!")
    if r == 3 and l == 0:
        print("PC: 2 | You: 1")
        print("PC win!")
    if r == 4 and l == 1:
        print("PC: 2 | You: 1")
        print("PC win!")
    if r == 4 and l == 0:
        print("PC: 1 | You: 2")
        print("You win!")
def match(z):
    while z != 1 and z != 2:
        print("Type the correct number, please") 
        z = int(input("Type here: "))
    if z == 1:
        start_match()
    if z == 2:
        championship()
print("Welcome to the NIM Game! Type a specified number if you: ")
print("1 - Want to play a match ")
print("2 - Want to play a championship ")
z = int(input("Type here: "))
match(z)

    
