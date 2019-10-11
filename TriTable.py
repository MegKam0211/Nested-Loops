# Write a program that uses nested for loops to create the following number pyramid.

# 1
# 2     4       
# 3     6       9
# 4     8       12      16
# 5     10      15      20      25
# 6     12      18      24      30      36
# 7     14      21      28      35      42      49
# 8     16      24      32      40      48      56      64
# 9     18      27      36      45      54      63      72      81

#for x in range(1, 10): #to execute from 1 to 9
 #   for y in range(1, x+1): #to execute same number of times as x
  #      print((x*y))

# finish up the loop 
# tips x*y  make sure you cast them to int
#n = 9
#num = 1
#for row in range(1,n+1):
 #   for col in range(1, row+1): #for  each col, print out the same num as row eg. 2 col = 2 row
  #      print(num, end = "   ")
   #     num = num*row
    #for row in range(1, row+1):
      #  print(col*row, end = "   ")    

for row in range(1, 10): #execute 1-9 because we have 9 rows
    for col in range(1, row+1): #executes same number of columns as rows
        print(int(row*col), end="     ") #each number row multiplied by each number col ie 9*9=81. the "   " executes 5 spaces between each number (I don't really know the number of spaces, was just guessing) 
    print(end="\n") #prints each col range in new line
        