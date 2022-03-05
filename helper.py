def possible_word_finder1(all_word_list,guess_list,clue_list,counter):

    possible_words = list()
    for word in all_word_list:
        if (word_obeys_rules(word,guess_list,clue_list,counter)):
            possible_words.append(word)


    return possible_words

def word_obeys_rules(word,g_list,c_list,counter):
    green_index_dict = dict()
    yellow_index_dict = dict()
    blacks_list = list()
    non_exist_list = list()
    for i in range(counter):
        if g_list[i] == "-1" or c_list[i] == "-1": # test
            print("ERROR in word_obeys_rules function")
            return False
        else:
            curr_guess = g_list[i] #example :  brain
            current_colors = c_list[i] # example GGYBB
            for i in range(len(curr_guess)):
                if current_colors[i] == "G":
                    green_index_dict[i] = curr_guess[i]
                elif current_colors[i] == "Y":
                    yellow_index_dict[curr_guess[i]] = i
                elif current_colors[i] == "0":
                    blacks_list.append(curr_guess[i])
    # basic green and yellow checks
    for k,v in green_index_dict.items(): # index = key, value = character;
        if ( word[k] != v ):
            return False
    for k,v in yellow_index_dict.items(): # key = character, value = index;
        if ( word[v] == k ):
            return False
        elif k not in word:
            return False
    ## basic checks are done here, now we check if a character is both green and yellow
    ## and if a character is gray while it was also green or yellow in an other place | done
    ## also these won't be super comprehensive I only take care of 1 green/yellow and 1 gray, or 1 green and yellow
    
    # returns false if non existing characters are inside the word
    existing_characters = list(green_index_dict.values()) + list(yellow_index_dict.keys())
    for character in blacks_list:
        if character not in existing_characters: # 
            if character in word:
                return False
            #non_exist_list.append(character)

    # now checking if 1 green and 1 yellow
    yellow_chars_list = list(yellow_index_dict.keys())
    for k,v in green_index_dict.items():
        if v in yellow_chars_list and yellow_index_dict[v] != k:
            word2 = word[0:k] + "9" + word[k+1:]
            if v not in word2:
                return False


    
    return True


if __name__ == "__main__":
    
    #with open("allowed_guesses.txt") as f:
    with open('word_list.txt') as f:
        word_list = f.readlines()
        
    print(len(word_list))
    
    guesses = ["-1"]*6
    clues = ["-1"]*6 # colors
    #possible_words_steps = ["-1"] * 6
    #possible_words_steps[0] = word_list
    counter = 0
    flag = True ## more than 1 possible word
    while (counter < 6 and flag):
        #print(f"Enter guess {counter+1}:")
        curr_guess = input(f"Enter guess {counter+1}:" )
        curr_guess = curr_guess.lower()
        #print(f"Enter colors of guess {counter+1}: (Not in word = 0, Green = G, Yellow = Y) ")
        curr_colors = input(f"Enter colors of guess {counter+1}: (Not in word = 0, Green = G, Yellow = Y) ")
        confirmation = input("Do you confirm, Y/N or press B to go back 1 step ")
        if (len(curr_guess) != 5 or len(curr_colors) != 5):
            print("It msut be a 5 letter word, incorrect input")
        elif (confirmation == "Y"): ## increase counter at the end
            guesses[counter] = curr_guess
            clues[counter] = curr_colors
            counter +=1
            possible_words = possible_word_finder1(word_list,guesses,clues,counter)
            if (len(possible_words) == 1):
                flag = False
            #print(f"There are {len(possible_words)} possible words, do you want to show them? Y/N")
            listing_confimation = input(f"There are {len(possible_words)} possible words, do you want to show them? Y/N " )
            if listing_confimation == "Y":
                print(possible_words)
            else:
                print("I am not showing the words then..")
        elif (confirmation =="N"):
            pass
            # do nothing
        elif (confirmation == "B"):
            counter-=1
