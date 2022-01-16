def main():
    print()
    print('Welcome to tic-tac-toe game.')
    print()
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    print(f'{a}|{b}|{c}')
    print('+-+-+')
    print(f'{d}|{e}|{f}')
    print('+-+-+')
    print(f'{g}|{h}|{i}')
    input_choice = None
    while not has_winner(a,b,c,d,e,f,g,h,i): 
     input_choice = int(input("x's turn to choose a number(1-9): "))


     if input_choice == a :
        a = 'x'
     elif input_choice == b :
         b = 'x'
     elif input_choice == c :
         c = 'x'
     elif input_choice == d :
         d = 'x'
     elif input_choice == e :
         e = 'x'
     elif input_choice == f :
         f = 'x'
     elif input_choice == g :
         g = 'x'
     elif input_choice == h :
         h = 'x'
     elif input_choice == i :
         i = 'x'

     print_game(a,b,c,d,e,f,g,h,i)
     input_choice = int(input("o's turn to choose a number(1-9): "))
     if input_choice == a:
         a = 'o'
     elif input_choice == b:
         b = 'o'
     elif input_choice == c:
         c = 'o'
     elif input_choice == d:
         d = 'o'
     elif input_choice == e:
         e = 'o'
     elif input_choice == f:
         f = 'o'
     elif input_choice == g:
         g = 'o'
     elif input_choice == h:
         h = 'o'
     elif input_choice == i:
         i = 'o'
     print_game(a,b,c,d,e,f,g,h,i)

    print('Well played!!')    

     
def print_game(a,b,c,d,e,f,g,h,i):
    print(f'{a}|{b}|{c}')
    print('+-+-+')
    print(f'{d}|{e}|{f}')
    print('+-+-+')
    print(f'{g}|{h}|{i}')
def has_winner(a,b,c,d,e,f,g,h,i):
    return (a == b == c or
    d == e == f or
    g == h == i or 
    a == d == g or
    b == e == h or
    c == f == i or
    a == e == i or 
    g == e == c )
if __name__ == "__main__":      
    main()