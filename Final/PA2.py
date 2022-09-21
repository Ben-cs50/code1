

# List of global containers
positive_words_list = []
negative_words_list = []
review_words_list   = []

review_positive_arr = []
review_negative_arr = []
not_review_positive_arr = []
not_review_negative_arr = []

review_positive_per = []
review_negative_per = []

not_review_positive_per = []
not_review_negative_per = []



# Positive and negative files names 
positive_text_file = "positive-words.txt"
negative_text_file = "negative-words.txt"



# Welcome part of the Applications
def Welcome_App():
    hello_welcome = """********************************
    Welcome To Review Bot  \n    
    Enter name of file :    \n"""
    print(hello_welcome)
    check_file_exist()                    
   


def check_file_exist():
        review_file_name_is  =  input("==> ") 
        # User Input File name   
        try:
            with open(review_file_name_is ,"r") as reviewFile:
                 
                 for line in reviewFile:
                    # print(line)
                    if(line != "\n"):
                         # Add all the words in list and remove "\n" at the end
                        review_words_list.append(line.rstrip()) 
        
        except:
            # Give user Another chance to input file name
            print("\nfile Not Found Try Again !!!\n")
            check_file_exist()
                        
        
Welcome_App()             
        

# Open positive file and store words in list
with open(positive_text_file,"r") as positiveFile:
    for line in positiveFile:
        # Add all the words in list and remove "\n" at the end
        positive_words_list.append(line.rstrip()) 
        # print(line)
            
# # Open Negative file and store words in list
with open(negative_text_file,"r") as negativeFile:
    for line in negativeFile:
        # Add all the words in list and remove "\n" at the end
        negative_words_list.append(line.rstrip()) 
        # print(line)
 
 
 
#  TODO (1)  (Advanced Section)  add not to every positive and negative words at front
not_positive_word_list = []
for index in positive_words_list:
    notAdded = "not " + index
    not_positive_word_list.append(notAdded)
    
not_negative_word_list = []
for index in negative_words_list:
    notAdded = "not " + index
    not_negative_word_list.append(notAdded)
    
    
    
for review in review_words_list:
    review_arr = review.split(" ") 
    # print(review_arr)
    review_positive = [(w, review_arr.count(w), len(review_arr),review_arr) for w in set(review_arr) if w in positive_words_list]
    review_negative = [(w, review_arr.count(w), len(review_arr),review_arr) for w in set(review_arr) if w in negative_words_list]
    print(review_positive)
    review_positive_arr.append(review_positive)
    review_negative_arr.append(review_negative)
    
       
# TODO (2) (Advanced Section) search if such words are available.
for review in review_words_list:
        not_review_positive = []
        not_review_negative = []
        for word in not_positive_word_list:
            if word in review:
                not_review_positive.append(word)
        for word in not_negative_word_list:
            if word in review:
                not_review_negative.append(word)
                      
    
        not_review_positive_arr.append(not_review_positive)
        not_review_positive_arr.append(not_review_negative)


# print(not_review_positive_arr)    
# print( not_review_negative_arr)    


for i in review_positive_arr:
    box = []
    count_review = 0
    Total = 0
    for j in i:
        count_review += j[1]
    Total = len(j[3])
    box.append(count_review)
    box.append(Total)
    review_positive_per.append(box)
     
     
        
for i in review_negative_arr:
    box = []
    count_review = 0
    Total = 0
    for j in i:
        count_review += j[1]
    Total = len(j[3])
    box.append(count_review)
    box.append(Total)
    review_negative_per.append(box)
    
    
        
for i in not_review_negative_arr:
    box = []
    box.append(len(i))
    not_review_negative_per.append(box)
   
   
    
for i in not_review_positive_arr:
    box = []
    box.append(len(i))
    not_review_positive_per.append(box)
    
       
  
  
#print(review_negative_per)   #[[3, 164], [0, 164], [12, 470], [0, 470], [10, 241], [0, 241], [0, 241], [2, 50], [0, 50], [3, 132]]
#print(review_positive_per)   #[[6, 164], [1, 21], [7, 470], [0, 470], [10, 241], [5, 41], [5, 58], [2, 50], [2, 42], [8, 132]]
combined_pos_neg_list = []  
for index in range(len(review_negative_per)):
    box = [review_positive_per[index][0],
          review_negative_per[index][0],
          review_positive_per[index][1]]
    combined_pos_neg_list.append(box)
    # print(box)    #[7, 12, 470]  # first index is the positive second index negative third index total words 



# Detaiminations of Reviews
count = 0
combined_pos_neg_total_comment = []
for index in combined_pos_neg_list:
    final_list = []
    if index[0] > index[1]:
        comment = f"This comment is a positive review with a positive percentage of {round(index[0]/index[2] * 100)}%"
        final_list = [combined_pos_neg_list[count][0],
                      combined_pos_neg_list[count][1],
                      combined_pos_neg_list[count][2],
                      comment]
        combined_pos_neg_total_comment.append(final_list)
    elif(index[1] > index[0]):
        comment = f"This comment is a Negative review with a negative percentage of {round(index[1]/index[2] * 100)}%" 
        final_list = [combined_pos_neg_list[count][0],
                      combined_pos_neg_list[count][1],
                      combined_pos_neg_list[count][2],
                      comment]
        combined_pos_neg_total_comment.append(final_list)
    elif(index[1] == 0 ):
        comment = f"This comment is a Positive review even though it has equal percentage with Negative with  {round(index[1]/index[2] * 100)}%"  
        final_list = [combined_pos_neg_list[count][0],
                      combined_pos_neg_list[count][1],
                      combined_pos_neg_list[count][2],
                      comment]
        combined_pos_neg_total_comment.append(final_list)         
    elif(index[1] == index[0]):
        comment = f"This comment is a Negative review even though it has equal percentage with positive with  {round(index[1]/index[2] * 100)}%"  
        final_list = [combined_pos_neg_list[count][0],
                      combined_pos_neg_list[count][1],
                      combined_pos_neg_list[count][2],
                      comment]
        combined_pos_neg_total_comment.append(final_list)  
        



# show how many review available and give user chance to choose 

def show_number_reviews():
    show_str = f"""\n*******************************************
        Number of Review available are {len(review_words_list)} \n 
        Select the numbers between 1 and {len(review_words_list)} of Review you want to Anaylse :\n
        to exit the Application enter 'exit' or 'e' \n 
**********************************************************"""     
    print(show_str)  
    user_picked_()  

def user_picked_():
    user_pick = input("==>  ")
    if(user_pick.isnumeric()): 
        if(int(user_pick) > len(review_words_list) or int(user_pick) <= 0 ):
            print(f"please input number between 1 and {len(review_words_list)}\n Try Again !!")
            user_picked_()
        if(int(user_pick) <= len(review_words_list)):
            for line in range(len(review_words_list)):
                if(line == int(user_pick)-1):
                    review_show = review_words_list[int(user_pick)-1]
                    print(f"\nReview \n {review_show} \n\n Analysis of the Review Above : \n")
                    print("\n*******************************************************\n")         
                    print(combined_pos_neg_total_comment[int(user_pick)-1][3])           #Outputs the comment to the user about the review 
                    print("\n*******************************************************\n")         
            user_picked_()            
    elif(user_pick == "exit" or  user_pick == "e"):
        print("\n#############################################\n")
        print("\nThank for using Review Bot Analysis\n\n BYE!!!!!!!!\n\n :( \n") 
        print("\n#############################################\n")
        quit()
        
    else:
        print("Unkown Command try again \n")    
        user_picked_()
                   
    
      
show_number_reviews()        
            
        
# Advanced requirements 
# The structure of words in a sentence can have great impact of 
# the message even if it has more bad negative words 
# than positive words 

# Examples of word structure
    # (1) its not bad to use 
    # Even though the review has more negative words tha positive 
    # the review will be categorised as Positive review since its 
    # conveying positive impression about the product used
    
    
    # Implementation 
    # steps (1) add not to every positive and negative words at front 
    #       (2) search if such words exits 

    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
   

    
       
           
