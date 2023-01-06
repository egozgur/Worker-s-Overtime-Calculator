
def main():
    input_hour = float(input("Enter the assigned total task length (in half-hour(s)): "))  # get total task lenght from user as input_hour
    amount_arr = []
    hours = []
    hour = 0.5
    
    for x in range(int(input_hour * 2)):  #multiple input_hour with 2 for set the loop range 
        amount_arr.append(input("Enter the payment value (in TL) for task portion ID " + str(x + 1) + " having length " + str(hour) + " hour(s):"))  # get payment values from user to array name as amount_arr
        hours.append(hour)  # add 
        hour += 0.5

    hours_with_divided_amount = dict() #we set a dictionary for hold hour and amount together like key and value  
    for i in range(int(input_hour * 2)):   
        hours_with_divided_amount[i / 2 + 0.5] = int(amount_arr[i]) / (hours[i] / 0.5) #we have simplified the quantities by half-hour slices
    
    sorted_by_amount = dict(sorted(hours_with_divided_amount.items(), key=lambda x: x[1], reverse=True)) #we have sorted the dictionary from big to small in the form of key and value

    final_hours = dict() #we set a dictionary for hours(0.5,1,1.5..)  
    index = 0
    local_total = 0.0
    
    for key in sorted_by_amount.keys():
        local_total += key
        if local_total == input_hour:
            final_hours[index] = key
            break
        else:
            final_hours[index] = key
            index += 1
    
    real_hours = [] 
    for elem in final_hours.keys():  # only loops to keys(0.5,1,1.5) of payment values 
        real_hours.append(int(final_hours[elem] * 2)) # we multiple the final_hours with 2 to set portion id's (thats why we used dictionary.wanted to call them together )
    
    day = 1
    for i in real_hours:
        print("On Day " + str(day) + " do task portion with ID " + str(i) )
        day += 1
    print("The most profitable completion of the assigned task takes " + str(day-1) + " day(s).")

if __name__ == "__main__":
    main()