cidade = str(input('Nome da cidade: ')).strip()
print('O nome da cidade começa com "Santo?" {}'.format('santo' in cidade.split()[0].lower()))

# cidade = str(input('Nome da cidade: ')).strip()
# print(cidade.lower()[:5] == 'santo')