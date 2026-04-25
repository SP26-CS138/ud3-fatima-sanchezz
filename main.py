'''
DEVELOPER(S): Fatima Sanchez
COLLABORATORS: Github Copilot/chat
DATE: April 24, 2026
'''

"""
This program will help users determine how much money they need to spend on textbooks and if they can afford it. 

The intention of this program is to facilitate budgeting of textbook costs for students.
There will be calculations of the cost of textbooks and how much it would cost a student to buy them. 
Then students will be able to input their financial aid and money they have saved to determine whether or not they can afford their textbooks. 
"""

##########################################
# IMPORTS:

##########################################
# FUNCTIONS:
##########################################
def calc_textbook_cost (classes, price_textbook):
    '''This function will determine the overall costs of all the textbooks'''
    calc_textbook_cost = classes * price_textbook
    return calc_textbook_cost

def calc_aid_cost (textbook_cost, aid):
    '''This function will calculate the costs of textbooks after financial aid.'''
    return textbook_cost - aid

def calc_cost_diff (costs_total, mon_saved):
    '''This function will calculate the cost of textbooks after knowing how much that user has saved.'''
    return mon_saved - costs_total

def text_save (data):
    '''This function will save the information we have calculated into a text file.'''
    with open ("text_save.txt", "w") as file: 
        file.write ("Textbook costs summary\n")
        for key, value in data.items ():
            file.write (f"{key}: {value}\n")
        file.write ("------------------------------")
    print ("\nReport has been successfully saved to text_save.txt")

def support_list():
    '''This function will open the lists of financial support related resources.'''
    with open ('financialresources.txt', 'r') as r:
        list = r.readlines()
    print (list)


##########################################
# MAIN PROGRAM:
##########################################
def main():
    print ("------------------------------")
    print ("Welcome to the Textbook Cost Calculator!")
    print ("------------------------------")

    try: 
        # Get user input for all the functions we need
        student_name = input ("what is your name?")
        classes = int(input ("How many classes are you taking that require at textbook?\n"))
        price_textbook = float(input ("What is the average price of a textbook for you classes?\n"))
        aid = float(input("How much financial aid do you have for textbooks?\n"))
        mon_saved = float(input ("How much money do you have saved for textbooks?\n"))

        # Call the functions for calculations
        textbook_cost = calc_textbook_cost (classes, price_textbook)
        costs_total = calc_aid_cost (textbook_cost, aid)
        cost_diff = calc_cost_diff (costs_total, mon_saved)

        # Save the data to file
        data_summary = {
            "Student Name": student_name,
            "Total Textbook Cost": f"${textbook_cost:.2f}",
            "Total Financial Aid": f"${aid:.2f}",
            "Total Cost After Aid": f"${costs_total:.2f}",
            "Money Saved": f"${mon_saved:.2f}",
            "Cost Difference": f"${cost_diff:.2f}"
              }
        text_save(data_summary)
        
        #final output to user 
        print ("\n------------------------------")
        print (f"Hello {student_name}, here is your textbook cost summary:")
        print (f"Total textbook costs: ${textbook_cost:.2f}")
        print (f"Total financial aid: ${aid:.2f}")
        print (f"Total cost after aid: ${costs_total:.2f}")
        print (f"Total cost after knowing how much you have saved: ${cost_diff:.2f}")
        print ("------------------------------")

        if cost_diff >= 0:
            print ("You can afford your textbooks! Great job budgeting!")
        else: 
            print (f"Unfortunately you cannot afford your textbooks. You are short by ${abs(cost_diff):.2f}")
            print ("Listed below are the direct websites to financial support resources at MiraCosta College.")
            support_list()
    except ValueError:
        print ("Invalid input. Please put valid numbers for the questions above.")
if __name__ == "__main__":
    main()
