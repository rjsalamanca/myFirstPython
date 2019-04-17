def make_madlib(name,programming_language,food,name_of_person_beside_you, dinner_last_night,adj):
    name = make_first_caps(name)
    name_of_person_beside_you = make_first_caps(name_of_person_beside_you)
    print('you are calling madlib. thank you for your support')
    return print('\n%s is learning %s. Today %s ate %s and it was delicious. %s saw %s eating and said they were a messy eater. %s was %s and threw %s at %s.\n' % (name,language,name,food,name_of_person_beside_you,name,name_of_person_beside_you,adj,dinner_last_night,name))

def make_first_caps(make_name_caps):
    return make_name_caps.capitalize()

name = input('What is your name: ')
language = input('What programming language are you learning: ')
food = input('What did you eat for lunch: ')
name2 = input('Who is sitting next to you: ')
food2 = input('What did you eat last night: ')
adj = input('Adjective: ')

make_madlib(name,language,food,name2,food2,adj)