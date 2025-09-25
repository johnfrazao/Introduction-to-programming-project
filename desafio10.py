
resp = str(input('O paciente tem febre? [S/N] ')).upper().strip()[0]
if resp == 'S':

    resp = str(input('O paciente tem tosse? [S/N] ')).upper().strip()[0]
    if resp == 'S':

        resp = str(input('O paciente sente falta de ar? [S/N] ')).upper().strip()[0]
        if resp == 'S':

            print('Diagnóstico: Suspeita de pneumonia. Procure um médico imediatamente.')
        else:
            print('Diagnóstico: Pode ser uma gripe ou um resfriado forte.')

    else:
        resp = str(input('O paciente tem manchas vermelhas na pele? [S/N] ')).upper().strip()[0]
        if resp == 'S':

            print('Diagnóstico: Suspeita de Dengue ou Zika. Procure um médico.')
        else:
            print('Diagnóstico: Febre de causa inderterminada. Monitore.')
else:
    resp = str(input('O paciente tem dor de garganta? [S/N] ')).upper().strip()[0]
    if resp == 'S':
        print('Diagnóstico: Possível infecção de garganta. Monitore.')
    else:
        print('Diagnóstico: Sintomas não conclusivos. Continue monitorando.')
