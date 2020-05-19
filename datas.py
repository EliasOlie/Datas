#Recebe uma data qualquer

rdata = input('Insira uma data: ')

#Substitui o caractere '/'(barra) por espaço em branco

data = rdata.replace('/', '')

#Pega fatias da variável data e distribuí em novas variáves de dia, mes e ano

dia = data[0:2]
mes = data[2:4]
ano = data[4:8]

#lista dos meses de 30 e 31 dias

mes_30 = ['04', '06', '09', '11']
mes_31 = ['01', '03', '05', '07', '08', '10', '12']

#Checa se a data maior que zero e menor igual a 30 e esta na lista dos meses de 30 dias
#e retorna válido e faz o mesmo processo para os de 31 dias

if dia > '0' and dia <= '30' and mes in mes_30:
    print('válido')
elif dia > '0' and dia <= '31' and mes in mes_31:
    print('válido')



#Checa se o ano é bissexto (Multiplo de 4 não multiplo de 100 e multiplo de 400) se for bissexto anob(ano bissexto) é true
#se não False (o bloco else pode ser implicitado em python)

if int(ano)%4 == 0 and int(ano)%100 !=0 or int(ano)%400 ==0:
    anob = True
else:
    anob = False


#por fim checa se o mês é fevereiro se for fevereiro checa se o ano é bissexto se for aceita a variável dia até o dia 29
#se não for bissexto (and not anob) fevereiro só vai até o dia 28!

if mes == '02' and anob and dia <= '29':
    print('valido')
elif mes == '02'  and not anob and dia <= '28':
    print('valido')
  
#Se nenhum desse argumentos forem válidos a data é invalida!

else:
    print('Invalido')    
