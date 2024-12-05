import math
def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving
    
    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle. 
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively
    
    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the 
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively
    
    The coordinates look as follows:
    
     0             x
     |------------->
     |
     |             
     |
 y   v
    '''          
    
    # Ball's current position
    ball_x, ball_y = ball_frect.pos

    # Paddle's center
    paddle_center_y = paddle_frect.pos[1] + paddle_frect.size[1] / 2

    # Initialize memory for the first call
    if not hasattr(pong_ai, "previous_ball_position"):
        pong_ai.previous_ball_position = [ball_x, ball_y]
        return "up" if paddle_center_y > ball_y else "down"

    # Retrieve previous position
    prev_ball_x, prev_ball_y = pong_ai.previous_ball_position

    # Calculate velocity
    velocity_x = ball_x - prev_ball_x
    velocity_y = ball_y - prev_ball_y

    # Update memory to only store the current position
    pong_ai.previous_ball_position = [ball_x, ball_y]


    #IF moving away from paddle --> steps = steps to other paddle + steps from other paddle to our paddle
        #IF paddle x < other paddle x and ball positive x velocity,
        #IF paddle x > other paddle x and ball negative x velocity

    if velocity_x == 0:
        return "up"

    if (paddle_frect.pos[0] < other_paddle_frect.pos[0]) == (velocity_x > 0):
        steps = (abs(ball_x - other_paddle_frect.pos[0]) + abs(paddle_frect.pos[0] + other_paddle_frect.pos[0])) / velocity_x
    else:
        steps = abs((paddle_frect.pos[0] - ball_x) / velocity_x)

    ypos = steps * velocity_y + ball_y


    #IF y pos // board length % 2 == 1, then move to ypos%boardlength
    #ELSE move to boardlength - ypos%boardlength
    if math.trunc(ypos / table_size[1]) % 2 == 0:
        ypos = abs(math.fmod(ypos, table_size[1]))
    else:
        ypos = table_size[1] - abs(math.fmod(ypos, table_size[1]))

    if paddle_center_y < ypos:
        return "down"
    else:
        return "up"


    #Locate paddle x position and find game board size to get bounds of things

    #Create txt file if doesn't exist, write current ball center pos
    #return "up"

    #If txt file exists compute x and y velocity
    #write x pos, y pos of ball to txt file
    #divide board x direction size by x velocity to get number of steps until ball contacts paddle
        #cheeky division modulus stuff to translate infinite coordinates to real coords

    #multiply that number by y velocity to get y position
    #do imaginary thingies to find y position of ball contact
    
    #move center of paddle towards that

    
