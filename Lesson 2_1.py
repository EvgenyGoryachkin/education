schedule = [12, None, -77, 'True', True, 9.5, set('abrakadabra'),  frozenset('abrakadabra'), dict(key_1='val_1', key_2='val_2')]
for n, subject in enumerate(schedule, 1):
    print(f"{n}){subject} - {type(subject)}")
