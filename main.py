'''
  The Minty Turtle Scribe is a program made to print words of the user's choice on the canvas.
  Rather than printing them with the [t.write("string"), where t is Turtle], this program uses
  Turtle to draw them on the screen.
'''

#Imports
import turtle
import string

#Variables & Setup
ended = False

turtle.setup()
turtle.screensize(10000, 10000, 'white')

t = turtle.Turtle()

I = int(0)

height = int(150)
new_coord = int(height / 3 * 2)

t.speed(100)

#Functions
def space():
  t.up()
  t.forward(new_coord)


def letter_A():
  #Make Letter A
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(height / 2)
  t.right(90)
  t.forward(height)
  t.left(180)
  t.forward(height / 2)
  t.left(90)
  t.forward(height / 2)

  #Move to new coordinate
  t.up()
  t.left(90)
  t.forward(height / 2)
  t.left(90)
  t.forward(new_coord)


def letter_B():
  #Making Letter B
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(height / 3)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 3)
  t.left(180)
  t.forward(height / 3)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 5 + 7)
  t.right(45)
  t.forward(height / 3 - 4)

  #Move to new coordinates
  t.up()
  t.left(180)
  t.forward(new_coord)


def letter_C():
  #Make letter C
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(height / 3 * 1.5)
  t.right(180)
  t.forward(height / 3 * 1.5)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(height / 3 * 1.5)

  #Go to new coordinates
  t.up()
  t.left(180)
  t.forward(height / 3 * 1.5)
  t.left(180)
  t.forward(new_coord)

#Initiation
def letter_D():
  #Making Letter D
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(height / 3)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 1.37)
  t.right(45)
  t.forward(height / 5)
  t.right(45)
  t.forward(height / 3)

  #Move to new coordinates
  t.up()
  t.left(180)
  t.forward(new_coord)

def letter_E():
  #Variables for clarity and debugging
  stem = height / 3 * 1.5
  half_height = height / 2

  #Draw the base and first stem
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(stem)

  #Go back and draw the second stem
  t.up()
  t.right(180)
  t.forward(stem)
  t.left(90)
  t.forward(half_height)
  t.down()
  t.left(90)
  t.forward(stem)

  #Go back and draw the final stem
  t.up()
  t.right(180)
  t.forward(stem)
  t.left(90)
  t.forward(half_height)
  t.down()
  t.left(90)
  t.forward(stem)

  #Move to next coords
  t.up()
  t.right(180)
  t.forward(stem)
  t.right(180)
  t.forward(new_coord)


def letter_F():
  #Variables for clarity
  stem = height / 3 * 1.5
  half_height = height / 2

  #Make the base and top
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(stem)

  #Go back and draw the middle stem
  t.right(180)
  t.forward(stem)
  t.left(90)
  t.forward(half_height)
  t.left(90)
  t.forward(stem)

  #Return and go to new coords
  t.up()
  t.right(180)
  t.forward(stem)
  t.left(90)
  t.forward(half_height)
  t.left(90)
  t.forward(new_coord)


def letter_G():
  #Variables for clarity
  stem = height / 3 * 1.5
  half_stem = stem / 2
  half_height = height / 2

  #Draw the top and left side
  t.down()
  t.left(90)
  t.forward(height)
  t.right(90)
  t.forward(stem)

  #Go back to the bottom
  t.right(180)
  t.forward(stem)
  t.left(90)
  t.forward(height)

  #Draw the bottom line
  t.left(90)
  t.forward(stem)

  #Draw the hook
  t.left(90)
  t.forward(stem)
  t.left(90)
  t.forward(half_stem)

  #Move to new coords
  t.up()
  t.right(180)
  t.forward(half_stem)
  t.right(90)
  t.forward(stem)
  t.right(90)
  t.forward(stem)
  t.right(180)
  t.forward(new_coord)


def letter_H():
  #Variables for clarity
  stem = height / 3 * 1.5
  half_height = height / 2

  #Draw the base
  t.down()
  t.left(90)
  t.forward(height)

  #Go back and draw the middle
  t.bk(half_height)
  t.right(90)
  t.fd(stem)

  #Draw the second base
  t.right(90)
  t.forward(half_height)
  t.bk(height)

  #Go to new coords
  t.up()
  t.fd(half_height)
  t.right(90)
  t.forward(stem)
  t.left(90)
  t.fd(half_height)
  t.left(90)
  t.fd(new_coord)


def letter_I():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 2

  #Draw letter I
  t.down()
  t.fd(stem)
  t.bk(h_s)
  t.left(90)
  t.fd(height)
  t.left(90)
  t.fd(h_s)
  t.bk(stem)

  #Move to new coords
  t.up()
  t.fd(h_s)
  t.left(90)
  t.fd(height)
  t.right(90)
  t.fd(h_s)
  t.right(180)
  t.fd(new_coord)


def letter_J():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 1.5

  #Draw base and neck
  t.down()
  t.fd(h_s)
  t.left(90)
  t.fd(height)

  #Draw roof
  t.left(90)
  t.fd(h_s)
  t.bk(h_s * 2)

  #Move to new coords
  t.up()
  t.fd(h_s)
  t.left(90)
  t.fd(height)
  t.right(90)
  t.fd(h_s)
  t.right(180)
  t.fd(new_coord * 1.2)
  
def letter_K():
  #Variables for clarity
  stem = height / 3 * 2.1
  h_s = stem / 2
  h_h = height / 2
  
  #Draw neck
  t.down()
  t.left(90)
  t.fd(height)

  #Go back and draw hands
  t.bk(h_h)
  t.right(45)
  t.fd(stem)
  t.bk(stem)
  t.right(90)
  t.fd(stem)

  #Move to new coords
  t.up()
  t.bk(stem)
  t.right(45)
  t.fd(h_h)
  t.left(90)
  t.fd(new_coord)
    
def letter_L():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 2
  h_h = height / 2

  #Draw base and neck
  t.down()
  t.left(90)
  t.fd(height)
  t.bk(height)
  t.right(90)
  t.fd(stem)

  #Go to new coords
  t.up()
  t.bk(stem)
  t.fd(new_coord)
  
def letter_M():
  #Variables for clarity
  stem = height / 3 * 1.3

  #Draw Left Neck
  t.down()
  t.left(90)
  t.fd(height)

  #Draw left arm
  t.right(135)
  t.fd(stem)

  #Draw right arm
  t.left(90)
  t.fd(stem)

  #Draw right neck
  t.right(135)
  t.fd(height)

  #Move to new coords
  t.up()
  t.bk(height)
  t.right(-135)
  t.bk(stem)
  t.left(-90)
  t.bk(stem)
  t.right(-135)
  t.bk(height)
  t.left(-90)
  t.fd(new_coord * 1.2)
  
def letter_N():
  #Variables for clarity
  stem = height / 3 * 1.3
  hy = height * 1.1
  
  #Draw left neck
  t.down()
  t.left(90)
  t.fd(height)

  #Draw arm
  t.right(155)
  t.fd(hy)

  #Draw neck
  t.left(155)
  t.fd(height)

  #Move to new coords
  t.up()
  t.bk(height)
  t.left(-155)
  t.bk(hy)
  t.right(-155)
  t.bk(height)
  t.left(-90)
  t.fd(new_coord)
  
def letter_O():
  #Variables for clarity
  stem = height / 3 * 1.41
  h_s = stem / 2
  n_h = height / 1.22

  #Draw left leg
  t.up()
  t.left(90)
  t.fd(n_h - n_h / 1.25)
  t.down()
  t.fd(n_h / 1.25)

  #Draw turn and head
  t.right(45)
  t.fd(h_s)
  t.right(45)
  t.fd(h_s)

  #Draw right half
  t.right(45)
  t.fd(h_s)
  t.right(45)
  t.fd(n_h / 1.25)
  t.right(45)
  t.fd(h_s)
  t.right(45)
  t.fd(h_s)
  t.right(45)
  t.fd(h_s)

  #Move to new coords
  t.up()
  t.left(135)
  t.fd(n_h - n_h / 1.25)
  t.left(90)
  t.fd(new_coord * 1.1)
  
def letter_P():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_h = height / 2

  #Draw neck and top
  t.down()
  t.left(90)
  t.fd(height)
  t.right(90)
  t.fd(h_h)
  t.right(90)
  t.fd(h_h)
  t.right(90)
  t.fd(h_h)

  #Move to new coord
  t.up()
  t.left(90)
  t.fd(h_h)
  t.left(90)
  t.fd(new_coord)
  
def letter_Q():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 2

  #Draw Box
  t.down()
  t.left(90)
  t.fd(height)
  t.right(90)
  t.fd(stem)
  t.right(90)
  t.fd(height)
  t.right(90)
  t.fd(stem)

  #Draw q line
  t.up()
  t.bk(h_s)
  t.right(90)
  t.fd(h_s / 2)
  t.down()
  t.right(135)
  t.fd(h_s * 1.6)

  #Move to new coords
  t.up()
  t.bk(h_s * 1.6)
  t.right(-135)
  t.bk(h_s / 2)
  t.right(-90)
  t.fd(h_s / 2)
  t.right(180)
  t.fd(new_coord / 1.2)
  
def letter_R():
  #Variables for clarity and debugging
  stem = height / 3 * 2
  h_h = height / 2

  #Make letter P
  letter_P()

  #Reverse the move to new coords
  t.up()
  t.left(180)
  t.fd(new_coord)
  t.right(90)
  t.fd(h_h)

  #Add the leg
  t.right(135)
  t.down()
  t.fd(stem)

  #Go back and move to new coords
  t.up()
  t.bk(stem)
  t.right(-135)
  t.bk(h_h)
  t.right(90)
  t.fd(new_coord)
  
def letter_S():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_h = height / 2

  #Make letter s
  t.down()
  t.fd(stem)
  t.left(90)
  t.fd(h_h)
  t.left(90)
  t.fd(h_h)
  t.right(90)
  t.fd(h_h)
  t.right(90)
  t.fd(stem)

  #Move to new coords
  t.up()
  t.right(90)
  t.fd(height)
  t.right(90)
  t.fd(stem)
  t.right(180)
  t.fd(new_coord)
  
def letter_T():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 2
  h_h = height / 2

  #Draw letter T
  t.up()
  t.fd(h_s)
  t.down()
  t.left(90)
  t.fd(height)
  t.left(90)
  t.bk(h_s)
  t.fd(stem)

  #Go to new coords
  t.up()
  t.bk(h_s)
  t.left(90)
  t.fd(height)
  t.right(90)
  t.fd(h_s)
  t.right(180)
  t.fd(new_coord)  
  
def letter_U():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 2
  h_h = height / 2

  #Draw letter U
  t.down()
  t.left(90)
  t.fd(height)
  t.bk(height)
  t.right(90)
  t.fd(stem)
  t.left(90)
  t.fd(height)
  t.bk(height)

  #Go to next coord
  t.up()
  t.left(90)
  t.fd(stem)
  t.left(180)
  t.fd(new_coord)
  
def letter_V():
  #Variables for clarity
  stem = height / 2 * 2.1
  h_s = stem / 2
  h_h = height / 2

  #Draw letter V
  t.up()
  t.left(90)
  t.fd(height)
  t.right(165)
  t.down()
  t.fd(stem)
  t.left(150)
  t.fd(stem)

  #Return and go to new coords
  t.up()
  t.bk(stem)
  t.left(-150)
  t.bk(stem)
  t.right(-165)
  
  t.bk(height)
  t.right(90)
  t.fd(new_coord)
  
def letter_W():
  #Variables for clarity
  stem = height / 2 * 2
  h_s = stem / 2
  h_h = height / 2

  #Draw W
  t.up()
  t.left(90)
  t.fd(height)
  t.right(170)
  t.down()
  t.fd(stem)
  t.left(160)
  t.fd(stem)
  t.right(160)
  t.fd(stem)
  t.left(160)  
  t.fd(stem)

  #Go to new coords
  t.up()
  t.bk(stem)
  t.left(-160)
  t.bk(stem)
  t.right(-160)
  t.bk(stem)
  t.left(-160)
  t.bk(stem)
  t.right(-170)
  t.bk(height)
  t.right(90)
  t.fd(new_coord * 1.2)
  
def letter_X():
  #Variables for clarity
  stem = height / 2 * 2.13
  h_s = stem / 2
  h_h = height / 2

  #Draw letter x
  t.up()
  t.left(90)
  t.fd(height)
  t.right(160)
  t.down()
  t.fd(stem)
  
  t.up()
  t.right(110)

  t.right(90)
  t.fd(height)

  t.down()
  t.left(160)
  t.fd(stem)

  #Go to new coords
  t.up()
  t.left(110)
  t.fd(new_coord / 1.2)
  
def letter_Y():
  #Variables for clarity
  stem = height / 3 * 1.5
  h_s = stem / 2
  ss = h_s * 1.65

  #Draw base
  t.up()
  t.fd(h_s)

  t.down()
  t.left(90)
  t.fd(height / 1.4)

  t.left(45)
  t.fd(ss)

  t.up()
  t.bk(ss)
  t.right(90)
  t.down()
  t.fd(ss)

  #Go to new coords
  t.up()
  t.bk(ss)
  t.left(45)
  t.bk(height / 1.4)
  t.left(90)
  t.fd(h_s)
  t.right(180)
  t.fd(new_coord)
  
def letter_Z():
  #Variables for clarity
  stem = height / 3 * 1.5
  
  #Draw letter Z
  t.down()
  t.fd(stem)
  t.bk(stem)
  t.left(63)
  t.fd(height * 1.12)

  t.right(63)
  t.left(180)
  t.fd(stem)

  #Go to new coord
  t.up()
  t.left(90)
  t.fd(height)
  t.left(90)
  t.fd(new_coord)
    
#def fillable_A():
def fillable_A():
  t.begin_fill()
  t.circle(1, 180)
  t.end_fill()
def printRed(string):
  print("\033[1;31;40m" + string + "\033[0;34;40m")


#Initiation Step 1 -> Prompts the user to enter a word
def num_there(s):
  return any(i.isdigit() for i in s)



#Repeat the code unless 'close-program' is entered
while ended == False:
  word = str(input("What word would you like to print? "))
  new_word = word.upper()
  
  special_chars = string.punctuation
  bools = list(map(lambda char: char in special_chars, word))
  
  if any(bools):
    printRed("Word contains special characters. Cannot print.")
  elif num_there(word):
    printRed("Word contains numbers. Cannot print.")
  else:
    print("ask mr paolino about the gold challenge -> lower and uppercase words?")
    for i in range(I, len(new_word)):
      if new_word[I].isspace():
        space()
        I = I + 1
      elif new_word[I] == "A":
        letter_A()
        I = I + 1
      elif new_word[I] == "B":
        letter_B()
        I = I + 1
      elif new_word[I] == "C":
        letter_C()
        I = I + 1
      elif new_word[I] == "D":
        letter_D()
        I = I + 1
      elif new_word[I] == "E":
        letter_E()
        I = I + 1
      elif new_word[I] == "F":
        letter_F()
        I = I + 1
      elif new_word[I] == "G":
        letter_G()
        I = I + 1
      elif new_word[I] == "H":
        letter_H()
        I = I + 1
      elif new_word[I] == "I":
        letter_I()
        I = I + 1
      elif new_word[I] == "J":
        letter_J()
        I = I + 1
      elif new_word[I] == "K":
        letter_K()
        I = I + 1
      elif new_word[I] == "L":
        letter_L()
        I = I + 1
      elif new_word[I] == "M":
        letter_M()
        I = I + 1
      elif new_word[I] == "N":
        letter_N()
        I = I + 1
      elif new_word[I] == "O":
        letter_O()
        I = I + 1
      elif new_word[I] == "P":
        letter_P()
        I = I + 1
      elif new_word[I] == "Q":
        letter_Q()
        I = I + 1
      elif new_word[I] == "R":
        letter_R()
        I = I + 1
      elif new_word[I] == "S":
        letter_S()
        I = I + 1
      elif new_word[I] == "T":
        letter_T()
        I = I + 1
      elif new_word[I] == "U":
        letter_U()
        I = I + 1
      elif new_word[I] == "V":
        letter_V()
        I = I + 1
      elif new_word[I] == "W":
        letter_W()
        I = I + 1
      elif new_word[I] == "X":
        letter_X()
        I = I + 1
      elif new_word[I] == "Y":
        letter_Y()
        I = I + 1
      elif new_word[I] == "Z":
        letter_Z()
        I = I + 1
      else:
        printRed("Sorry, I didn't understand that. Could you say that again?")
else:
  exit()
    