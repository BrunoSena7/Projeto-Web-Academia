nota_01 = float(input('Digite a primeira nota do aluno e tecle enter:\n'))
nota_02 = float(input('Digite a segunda nota do aluno e tecle enter:\n'))
nota_03 = float(input('Digite a terceira nota do aluno e tecle enter:\n'))              

media_do_aluno = (nota_02 + nota_01 + nota_03)/3

# Aluno aprovado media_do_aluno >=7.0
# Aluno está reprovado

if media_do_aluno >= 7.0: 
    print (' bloco de codigo if.')
    print (' - ' *  15)
    print (" O aluno está aprovado")
    print ('Fim do bloco if')

elif media_do_aluno < 7.0 and media_do_aluno >= 2.0 :
        print (' bloco de codigo elif.')
        print (' - ' *  15)
        print (" O aluno está aprovado")
        print ('Fim do bloco elif')


else:
    print ('Bloco else')
    print (' - ' *  15)
    print (' O aluno está reprovado')
    print(' Fim do bloco else')

print (' - '*  15)
print (' Fim do programa')