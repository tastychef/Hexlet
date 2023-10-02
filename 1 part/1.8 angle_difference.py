def diff(angle1, angle2):
    max_angle = max(angle1, angle2) % 360
    min_angle = min(angle1, angle2) % 360
    result = 0
    if max_angle - min_angle <= 180:
        result = max_angle - min_angle
    else:
        result = (360 - max_angle) + min_angle
    return abs(result)
