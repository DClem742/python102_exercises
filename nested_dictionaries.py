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
print(ramit['email'])

print(ramit['interests'][0])

for f in ramit ['friends']:
    if f['name'] == 'Jasmine':
        print(f['email'])

for f in ramit ['friends']:
    if f['name'] == 'Jan':
        print(f['interests'][1])
