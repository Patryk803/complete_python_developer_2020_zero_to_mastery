#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# iterate over picture
# if 0 -> print ''
# if 1 -> print *


for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', end='') # We use end to don't go to new line \n
        else:
            print(' ', end='') # We use end to don't go to new line \n
    print('\n')

# Better Version below


fill = '*'
empty = ' '
for row in picture:
    for pixel in row:
        if (pixel): # We don't need pixel == 1 as pixel itself is a TRUE value
            print(fill, end='') # We use end to don't go to new line \n
        else:
            print(empty, end='') # We use end to don't go to new line \n
    print('\n')