start=True
while start:
    space=[" "," "," "," "," "," "," "," "," "]
    inde=0
    again=True
    game=True
    tie=True
    tri1=0
    tri2=0
    def board():
        index=0
        while index<=8:
            print(space[index],end="|")
            if index==2 or index==5:
                print("\n")
            index+=1
        index=0  
    board()
    while game:
        occu=True
        while occu:
            p1=int(input("player 1 turn choose a place from 1 to 9:"))
            a1=p1-1
            occu=False
            if a1>=0 and a1<=8:
                if space[a1]=="O" or space[a1]=="X":
                    print("==>position is already taken select another place<==")
                    occu=True
            else:
                print("==>enter number with in 1 to 9<==")
                occu=True
        space[a1]="X" 
        index=0 
        board()    
        tri1+=1
        if tri1>=3 or tri2>=3:
            winning=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
            for a,b,c in winning:
                if tie==True:
                    if space[a-1]==space[b-1]==space[c-1]=="O":
                        print("\n.....player 2 win.....")
                        game=False
                        tie=False
                    elif space[a-1]==space[b-1]==space[c-1]=="X":  
                        print("\n.....player 1 win.....")
                        game=False
                        tie=False
                    elif " " not in space:
                        print("\n...Both loss...\n...game tied...")
                        game=False
                        tie=False
                    else:
                        pass
        if game==True:        
            occu=True
            while occu:
                p2=int(input("player 2 turn choose a place from 1 to 9:"))
                a2=p2-1
                occu=False
                if 0<=a2<=8:
                    if space[a2]=="O" or space[a2]=="X":
                        print("==>position is already taken select another place<==")
                        occu=True
                else:
                    print("==>enter a number again with in 1 to 9<==")
                    occu=True
            
            space[a2]="O"
            board()
            tri2+=1    
            if tri1>=3 or tri2>=3:
                winning=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
                for a,b,c in winning:
                    if tie:
                        if space[a-1]==space[b-1]==space[c-1]=="O":
                            print("\n.....player 2 win.....")
                            game=False
                            tie=False
                        elif space[a-1]==space[b-1]==space[c-1]=="X":  
                            print("\n.....player 1 win.....")
                            game=False
                            tie=False
                        elif " " not in space:
                            tie=False
                            game=False
                            print("\n...Game tied...\n...both loss...")
                        else:
                            pass
                        
    
    while again==True and game==False:
        restart=input("Do you want to continue yes or no:")
        restart=restart.upper()
        if restart=='YES':
            game=True
            again=False
        elif restart=='NO':
            start=False
            again=False
            print("-----THANK YOU FOR PLAYING--------")
        else:
            again=True
