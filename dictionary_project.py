dictionary={}
while True:
    print("/n Dictionary Management Program")
    print("1.Add a word to the dictionary")
    print("2.Search a word for the meaning")
    print("3.Display all the words")
    print("4.Update a meaning in dictionary")
    print("5.Delete a word in dictionary")
    print("6.Exit from the programm")
    
    choice=input("choose the option:")
    
    if choice == "1":
        word=input("enter the word:").lower()
        meaning=input("enter the meaning:")
        dictionary[word]=meaning
        print("Word added successfully")
    elif choice =="2":
            word=input("enter the word:").lower()
            if word in dictionary:
             print(f"meaning:",{dictionary[word]})
            else:
             print("word is not available in dictionary")
    elif choice=="3":
        for word,meaning in dictionary.items():
            print(f"{word}:{meaning}")
    elif choice=="4":
        word=input("enter the word:")
        if word in dictionary:
            updated_meaning=input("enter the new meaning:")
            dictionary[word]=updated_meaning
            print("meaning uodated successfully")   
        else:
            print("word not found in dictionary")  
    elif choice=="5":
        word=input("enter the word:")
        if word in dictionary:
            dictionary.pop(word)
            print("word deleted successfully") 
        else:
            print("word not found in the dictionary")
    elif choice=="6":
        print(" you are going to exit the program")
        break
    else:
     print("choose the correct choice ")      
            

            