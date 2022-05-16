def personal_data(**kwargs):
    return ' '.join(kwargs.values())
print(personal_data (name = input('enter name'), surname = input('enter surname'), year = input('enter year'), city = input('enter city'), email = input('enter email'), telephone = input('input telephone')))
