card = input("Enter card number: ")
if len (card)==16 and card.isdigit():
    print("*" * 12 + card[-4:])
else:
    print("error")