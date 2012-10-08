def tooth_value(tooth_weight):
    values_used = {20:0, 10:0, 5:0, 1:0, .5:0}
    value = tooth_weight * 0.5
    while value > 0:
        print(value)
        if value >= 20:
            values_used[20]+=1
            value -= 20
        elif value >= 10:
            values_used[10]+=1
            value -= 10
        elif value >= 5:
            values_used[5]+=1
            value -= 5
        elif value >= 1:
            values_used[1]+=1
            value -= 1
        elif value >= .5:
            values_used[.5]+=1
            value -= .5
    return values_used

print(tooth_value(103))
