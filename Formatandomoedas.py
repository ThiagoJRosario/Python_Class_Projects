from utilidadescev import Moeda, Dado
import módulos


num = Dado.leiaDinheiro('Digite um valor R$: ')
Moeda.resumo(num)  # type: ignore