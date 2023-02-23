def promotion(come, pay, per_head, pack):
    total = (pack // come) * (pay * per_head) + (pack % come) * per_head
    return total

come = int(input())
pay = int(input())
per_head = int(input())
pack = int(input())
print(promotion(come, pay, per_head, pack))
