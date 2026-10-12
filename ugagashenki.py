import random
secret = random.randint(1, 100)
attems = 0 
print('Я загадал число от 0 до 100, попробуй отгадать пупсик)')
while True:
    guess = int(input('Your variant:'))
    attems += 1 
    if guess < secret:
        print('more')
    elif guess > secret:
        print('low')
    else:
        print('Yyyyyyeeeees, this is ', secret, 'your attempts: ', attems)
        break
