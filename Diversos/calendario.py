import calendar

ano = 2022
mes = 6

# Exibindo o calendário no formato padrão
calendario = calendar.month(ano, mes)
print(calendario)
print('-'*80)

# Defininindo o primeiro dia da semana para o Domingo
calendario = calendar.setfirstweekday(6)
calendario = calendar.month(ano, mes)
print(calendario)
print('-'*80)

# Exibindo o calendário anual
calendario = calendar.TextCalendar(calendar.SUNDAY).formatyear(ano)
print(calendario)
print('-'*80)
