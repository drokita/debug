import sys
from random import choice
import pdb

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]

while True:
   print "To exit the game type 'exit'"
   num1 = choice(random2)
   num2 = choice(random1)
   pdb.set_trace()
   answer = raw_input("What is {} times {}? ".format(num1, num2))
#   pdb.set_trace()

   if answer == "exit":
      print "Now exiting the game!"
      sys.exit()
   elif int(answer) == num1 * num2:
      print "Correct!"
   else:
      print "Wrong!"
