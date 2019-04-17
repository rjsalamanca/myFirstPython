def make_madlib(person,subject):
    return 'your name is %s and your fav subject is %s' % (person,subject)

thisGuy = input('Name: ')
sub = input('Subject: ')

print(make_madlib(thisGuy,sub))
print('you are calling madlib. thank you for your support')
