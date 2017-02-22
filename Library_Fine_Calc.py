""" This program calculates the fine amount for a library system 
based on the difference between the return date and due date"""

return_date=raw_input()
due_date=raw_input()
r=[int(i) for i in return_date.split(" ")] #1 way of converting string array to int array for comparisons
d=map(int,due_date.split(" ")) #2nd way for converting string array to int array for comparisons
fine=0 
# no fine if return date <= due date
if (r[2] > d[2]): # returned after the expected calender year
    fine=10000
elif (r[1] > d[1]):  
    if (r[2] == d[2]):   # same year but returned past the calender month
        fine = 500 * (r[1]-d[1])
elif (r[0] > d[0]):
    if (r[1] == d[1]):   # same year, same month but returned past the calender day
        fine = 15 * (r[0]-d[0])
print fine;
