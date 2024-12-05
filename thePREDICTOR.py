def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    """
    Predictive AI for moving the paddle to align with the ball's trajectory.
    Keeps only the previous ball position in memory using function attributes.
    """
    # Ball's current position
    ball_x, ball_y = ball_frect.pos

    # Paddle's center
    paddle_center_y = paddle_frect.pos[1] + paddle_frect.size[1] / 2
    safety_distance = paddle_frect.size[1] / 4  # 1/4 the length of the paddle
    paddle_width = paddle_frect.size[0]  # Width of the paddle

    # Define the median axis
    median_axis = table_size[1] / 2

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

    # Define the margin for paddle movement
    upper_margin = paddle_center_y + safety_distance
    lower_margin = paddle_center_y - safety_distance

    # Check if the ball is close to the paddle on the x-axis
    is_ball_close_x = abs(ball_x - paddle_frect.pos[0]) < (paddle_width / 4)

    # Check if the ball is within the safety margin in the y-axis
    if lower_margin < predicted_y < upper_margin and is_ball_close_x:
        # New logic based on median axis
        if paddle_center_y < median_axis:
            print("Paddle is below the median axis. Moving paddle up.")
            return "up"
        elif paddle_center_y > median_axis:
            print("Paddle is above the median axis. Moving paddle down.")
            return "down"

    # Old logic if new conditions are not met
    if lower_margin < predicted_y < upper_margin:
        print("Ball is within the safety margin. Paddle stays still.")
        return None  # Stay still if within margin
    elif predicted_y < lower_margin:
        print("Ball is below the paddle. Moving paddle up.")
        return "up"
    elif predicted_y > upper_margin:
        print("Ball is above the paddle. Moving paddle down.")
        return "down"