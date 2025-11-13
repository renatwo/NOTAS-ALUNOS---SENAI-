#SISTEMA DE NOTAS - ALUNOS 

notas = {
    'alunos': [],
    'notas_aluno': []
}

for i in range(3):
    senha = input('Senha: ')
    if senha == '1234':
        acesso = input('Deseja verifica a média de um aluno? ')
        while acesso == 'sim':
            print('Sistema de notas Escolares')
            nome = input('Nome: ')
            n1 = float(input('Nota1: '))
            n2 = float(input('Nota1: '))
            n3 = float(input('Nota1: '))
            notas['alunos'].append(nome)
            notas_aluno = notas['notas_aluno'].extend([n1, n2, n3])
            media = sum(notas['notas_aluno']) / len(notas['notas_aluno'])
            print('A Média do aluno', nome, 'é', media)
            print(notas)
            acesso = input('Deseja verificar outro aluno? ')

else:
    print('conta bloqueada')

input('Digite enter para sair: ')
