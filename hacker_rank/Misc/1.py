# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
for _ in xrange(N):
    turn_no = int(raw_input())
    iteration = (turn_no-1)/4 
    extra = turn_no % 4
    if extra == 1:
        x_cord = 1 + iteration * 2
        y_cord = 0 + iteration * -2
    elif extra == 2:
        x_cord = 1 + iteration * 2
        y_cord = 2 + iteration * 2
    elif extra == 3:
        x_cord = -2 + iteration * -2
        y_cord = 2 + iteration * 2 
    elif extra == 0:
        x_cord = -2+ iteration * -2
        y_cord = -2 + iteration * -2
        
    print str(x_cord) + " " + str(y_cord)