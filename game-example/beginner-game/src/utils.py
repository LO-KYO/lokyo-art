def generate_random_number(min_value, max_value):
    import random
    return random.randint(min_value, max_value)

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def update_score(current_score, points):
    return current_score + points

def reset_score():
    return 0