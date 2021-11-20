current_hand = [2, 7, 4, 9, 3, 5]
card_dict = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
summa = 0
keys = list(card_dict.keys())
for i in current_hand:
    if i in keys:
        summa += card_dict[i]
    else: print('error')
print(summa)
