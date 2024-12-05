def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """
    Predictive AI for moving the paddle to align with the ball's trajectory.
    Keeps only the previous ball position in memory using function attributes.
    """
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

    #IF y pos // 2 
    

    # Predict ball's y-position when it reaches the paddle's x-coordinate
    if velocity_x != 0:
        steps_to_paddle = abs((paddle_frect.pos[0] - ball_x) / velocity_x)
        predicted_y = ball_y + steps_to_paddle * velocity_y

        # Handle bounces off top and bottom edges
        if predicted_y < 0 or predicted_y > table_size[1]:
            predicted_y = predicted_y % (2 * table_size[1])  # Fold into the valid range
            if predicted_y > table_size[1]:
                predicted_y = 2 * table_size[1] - predicted_y  # Reflect back from edge
    else:
        # If no x-velocity, move paddle toward the current ball position
        predicted_y = ball_y

    # Decide whether to move "up" or "down"
    if paddle_center_y < predicted_y:
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

    
