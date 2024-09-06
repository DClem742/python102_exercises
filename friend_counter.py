ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}
def countFriends(oldDictionary):
    newDictionary = oldDictionary.copy()
    newDictionary ['friends_count'] = len(newDictionary['friends'])
    return newDictionary

    print(countFriends(ramit))