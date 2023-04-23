def notas(* num, sit = False):

    """
    -> Analisa várias notas e situações.
    :param num: Notas
    :param sit: Situação (opcional)
    :return: Dicionário com várias informações sobre as notas e a situação.
    """

    result = dict()
    result['Total'] = len(num)
    result['Maior'] = max(num)
    result['Menor'] = min(num)
    result['Média'] = sum(num) / len(num)
    if sit:
        if result['Média'] < 7:
            result['Situação'] = 'Ruim'
        elif 7 <= result['Média'] < 8:
            result['Situação'] = 'Razoável'
        else:
            result['Situação'] = 'Boa'

    return result

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
print('-=' * 37)
help(notas)