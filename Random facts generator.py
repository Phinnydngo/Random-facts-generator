import randfacts as rf

print('Random Facts')
x = ''

while x == '':
    print('Press enter for fact')
    x = input()
    fact = rf.get_fact()
    print(fact)

