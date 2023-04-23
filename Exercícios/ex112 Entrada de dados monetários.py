from ex112.utilidadescev import moeda
from ex112.utilidadescev.dado import leiaDin

valor = leiaDin('Digite um valor: R$')
moeda.resumo(valor, 20, 12)
