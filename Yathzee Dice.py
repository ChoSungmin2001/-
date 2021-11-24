while True :
    print("YAHTZEE Dice에 오신 걸 환영합니다!")
    print()
    print("1. 게임하기")
    print()
    print("3. 종료하기")
    print()

    menu = int(input("메뉴를 선택하세요"))

    if menu == 3 :
        print("게임을 종료합니다")
        break
        
    if menu == 1 :
        
        import random
        
        dice = [0,0,0,0,0]
        throw = 0 
    score = 0
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0
    score6 = 0
    score7 = 0
    score8 = 0
    score9 = 0
    score10 = 0
    score11 = 0
    score12 = 0
    score13 = 0
    score_SUM = 0
    score_bonus = 0
    score_Total_score = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_11 = 0
    count_12 = 0
    count_13 = 0
    check = 0
       
    score_list = ['Ones','Twos','Threes','Fours','Fives','Sixes','Three of a kind','Four of a kind','Chance','Yathzee', 'Full house', 'Small straight', 'Large straight']
    
    Game_over = False
    while not Game_over: 
        def roll():
            return random.randint(1,6)
        
        def check_ones(d):
            sum = 0
            for x in range(5):
                if d[x] == 1:
                    sum = sum + d[x]
            return(sum)
        def check_twos(d):
            sum = 0
            for x in range(5):
                if d[x] == 2:
                    sum = sum + d[x]
            return(sum)
        def check_threes(d):
            sum = 0
            for x in range(5):
                if d[x] == 3:
                    sum = sum + d[x]
            return(sum)
        def check_fours(d):
            sum = 0
            for x in range(5):
                if d[x] == 4:
                    sum = sum + d[x]
            return(sum)
        def check_fives(d):
            sum = 0
            for x in range(5):
                if d[x] == 5:
                    sum = sum + d[x]
            return(sum)
        def check_sixes(d):
            sum = 0
            for x in range(5):
                if d[x] == 6:
                    sum = sum + d[x]
            return(sum)
        
        def check_Three_of_a_kind(d):
            sum = 0
            for x in range(7):
                if dice.count(x) == 3 or dice.count(x) == 4 or dice.count(x) == 5:
                    sum = sum + dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
            return(sum)
        
        def check_Four_of_a_kind(d):
            sum = 0
            for x in range(7):
                if dice.count(x) == 4 or dice.count(x) == 5:
                    sum = sum + dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
            return(sum)
        
        def check_Chance(d):
            sum = 0
            sum = sum + dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
            return(sum)
        
        def check_Yathzee(d):
            sum = 0
            for x in range(5):
                if dice.count(x) == 5:
                    sum = sum + 50
            return(sum)
        
        def check_Full_house(d):
            sum = 0 
            arr = [0]*6
            for num in dice:
                arr[num-1]+=1
            if 2 in arr and 3 in arr:
                    sum = sum + 25
            return(sum)
        
        def check_Small_straight(d):
            sum = 0
            if set(dice) in [{1,1,2,3,4},{1,2,2,3,4},{1,2,3,3,4},{1,2,3,4,4},{1,2,3,4,5},{1,2,3,4,6},{2,2,3,4,5},{2,3,3,4,5},{2,3,4,4,5},{2,3,4,5,5},{2,3,4,5,6},{1,3,4,5,6},{3,3,4,5,6},{3,4,4,5,6},{3,4,5,5,6},{3,4,5,6,6}]:
                sum = sum + 30
                return(sum)
            return 0
            
        def check_Large_straight(d):
            sum = 0
            if len(set(dice)) == 5 and set(dice) in [{1,2,3,4,5}, {2,3,4,5,6}]:
                sum = sum + 40
                return(sum)
            return 0
               
        for x in range(5):
            dice[x] = roll()
        throw = 1
        print("dice roll " + str(throw) + " is " + str(dice))
        
        while throw < 3:
            selected = input("Throw which dice?")
            for x in range(5):
                if str(x+1) in selected:
                    dice[x] = roll()
                    print("throwing " + str(x+1))
                else:
                    print("holding " + str(x+1))
            throw += 1
            dice.sort()
            print("dice roll " + str(throw) + " is " + str(dice))
        
                  
        print("End")
        
        print("Ones: " + str(check_ones(dice)))
        print("Twos: " + str(check_twos(dice)))
        print("Threes: " + str(check_threes(dice)))
        print("Fours: " + str(check_fours(dice)))
        print("Fives: " + str(check_fives(dice)))
        print("Sixes: " + str(check_sixes(dice)))
        print("Three of a kind: " + str(check_Three_of_a_kind(dice)))
        print("Four of a kind: " + str(check_Four_of_a_kind(dice)))
        print("Chance: " + str(check_Chance(dice)))
        print("Yathzee!: " + str(check_Yathzee(dice)))
        print("Full house: " + str(check_Full_house(dice)))
        print("Small straight: " + str(check_Small_straight(dice)))
        print("Large straight: " + str(check_Large_straight(dice)))
        
        number_valid = False
        while not number_valid :
            number_to_score = input("What combinations do you want to score? ")
            
            if number_to_score in score_list:
                number_valid = True
                score_list.remove(number_to_score)
            elif number_to_score == 'Check':
                print()
                print('----------------------------------------')
                print('|                          |   player  |')
                print('----------------------------------------')
                print('|           Ones           |     ' + str(score1) + '     |')
                print('----------------------------------------')
                print('|           Twos           |     ' + str(score2) + '     |')
                print('----------------------------------------')
                print('|          Threes          |     ' + str(score3) + '     |')
                print('----------------------------------------')
                print('|          Fours           |     ' + str(score4) + '     |')
                print('----------------------------------------')
                print('|          Fives           |     ' + str(score5) + '     |')
                print('----------------------------------------')
                print('|          Sixes           |     ' + str(score6) + '     |')
                print('========================================')
                print('|           SUM            |           |')
                print('----------------------------------------')
                print('|          Bonus           |           |')
                print('========================================')
                print('|     Three of a kind      |     ' + str(score7) + '     |')
                print('----------------------------------------')
                print('|      Four of a kind      |     ' + str(score8) + '     |')
                print('----------------------------------------')
                print('|        Full house        |     ' + str(score9) + '     |')
                print('----------------------------------------')
                print('|      Small Straight      |     ' + str(score10) + '     |')
                print('----------------------------------------')
                print('|      Large Straight      |     ' + str(score11) + '     |')
                print('----------------------------------------')
                print('|         Chance           |     ' + str(score12) + '     |')
                print('----------------------------------------')
                print('|         YATHZEE          |     ' + str(score13) + '     |')
                print('========================================')
                print('|       Total score        |           |')
                print('----------------------------------------')      
            else:
                print()
                print("Try again. What combinations do you REALLY want to score?")
                       
            if number_to_score == 'Ones':
                score1 = score1 + int(str(check_ones(dice)))
                print("Your score is " + str(check_ones(dice)))
                count_1 = count_1 + 1
            
            if number_to_score == 'Twos':
                score2 = score2 + int(str(check_twos(dice)))
                print("Your score is " + str(check_twos(dice)))
                count_2 = count_2 + 1
                
            if number_to_score == 'Threes':
                score3 = score3 + int(str(check_threes(dice)))
                print("Your score is " + str(check_threes(dice)))
                count_3 = count_3 + 1
                
            if number_to_score == 'Fours':
                score4 = score4 + int(str(check_fours(dice)))
                print("Your score is " + str(check_fours(dice)))
                count_4 = count_4 + 1
            
            if number_to_score == 'Fives':
                score5 = score5 + int(str(check_fives(dice)))
                print("Your score is " + str(check_fives(dice)))
                count_5 = count_5 + 1
            
            if number_to_score == 'Sixes':
                score6 = score6 + int(str(check_sixes(dice)))
                print("Your score is " + str(check_sixes(dice)))
                count_6 = count_6 + 1
            
            if number_to_score == 'Three of a kind':
                score7 = score7 + int(str(check_Three_of_a_kind(dice)))
                print("Your score is " + str(check_Three_of_a_kind(dice)))
                count_7 = count_7 + 1
                
            if number_to_score == 'Four of a kind':
                score8 = score8 + int(str(check_Four_of_a_kind(dice)))
                print("Your score is " + str(check_Four_of_a_kind(dice)))
                count_8 = count_8 + 1
            
            if number_to_score == 'Full house':
                score9 = score9 + int(str(check_Full_house(dice)))
                print("Your score is " + str(check_Full_house(dice)))
                count_9 = count_9 + 1
                
            if number_to_score == 'Small straight':
                score10 = score10 + int(str(check_Small_straight(dice)))
                print("Your score is " + str(check_Small_straight(dice)))
                count_10 = count_10 + 1
                
            if number_to_score == 'Large straight' : 
                score11 = score11 + int(str(check_Large_straight(dice)))
                print("Your score is " + str(check_Large_straight(dice)))
                count_11 = count_11 + 1
                
            if number_to_score == 'Chance':
                score12 = score12 + int(str(check_Chance(dice)))
                print("Your score is " + str(check_Chance(dice)))
                count_12 = count_12 + 1
                
            if number_to_score == 'Yathzee':
                score13 = score13 + int(str(check_Yathzee(dice)))
                print("YOUR SCORE IS " + str(check_Yathzee(dice)))
                count_13 = count_13 + 1
            
            if count_1 >= 1:
                pass
            if count_2 >= 1:
                pass
            if count_3 >= 1:
                pass
            if count_4 >= 1:
                pass
            if count_5 >= 1:
                pass
            if count_6 >= 1:
                pass
            if count_7 >= 1:
                pass
            if count_8 >= 1:
                pass
            if count_9 >= 1:
                pass
            if count_10 >= 1:
                pass
            if count_11 >= 1:
                pass
            if count_12 >= 1:
                pass
            if count_13 >= 1:
                pass
        
        if len(score_list) == 0:
            Game_over = True
            score_SUM = score_SUM + score1 + score2 + score3 + score4 + score5 + score6
            if score_SUM >= 63:
                score_bonus = score_bonus + 35
            score_Total_score = score_Total_score + score_SUM + score_bonus + score7 + score8 + score9 + score10 + score11 + score12 + score13
            print()
            print()
            print('----------------------------------------')
            print('|                          |   player  |')
            print('----------------------------------------')
            print('|           Ones           |     ' + str(score1) + '     |')
            print('----------------------------------------')
            print('|           Twos           |     ' + str(score2) + '     |')
            print('----------------------------------------')
            print('|          Threes          |     ' + str(score3) + '     |')
            print('----------------------------------------')
            print('|          Fours           |     ' + str(score4) + '     |')
            print('----------------------------------------')
            print('|          Fives           |     ' + str(score5) + '     |')
            print('----------------------------------------')
            print('|          Sixes           |     ' + str(score6) + '     |')
            print('========================================')
            print('|           SUM            |     ' + str(score_SUM) + '     |')
            print('----------------------------------------')
            print('|          Bonus           |     ' + str(score_bonus) + '     |')
            print('========================================')
            print('|     Three of a kind      |     ' + str(score7) + '      |')
            print('----------------------------------------')
            print('|      Four of a kind      |     ' + str(score8) + '     |')
            print('----------------------------------------')
            print('|        Full house        |     ' + str(score9) + '     |')
            print('----------------------------------------')
            print('|      Small Straight      |     ' + str(score10) + '     |')
            print('----------------------------------------')
            print('|      Large Straight      |     ' + str(score11) + '     |')
            print('----------------------------------------')
            print('|         Chance           |     ' + str(score12) + '     |')
            print('----------------------------------------')
            print('|         YATHZEE          |     ' + str(score13) + '     |')
            print('========================================')
            print('|       Total score        |     ' + str(score_Total_score) + '     |')
            print('----------------------------------------')      
            
            break
            
            
                
            
                
             
                
        
            
        
                
            
            
            
                 
            
            
                
         
            
            
            
            
        
        

        
        
            
        


