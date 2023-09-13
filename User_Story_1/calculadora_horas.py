import datetime

def calcular_horas_trabalhadas(hora_inicio, hora_termino):
    try:
        hora_inicio = datetime.datetime.strptime(hora_inicio, "%H:%M")
        hora_termino = datetime.datetime.strptime(hora_termino, "%H:%M")
    except ValueError:
        raise ValueError("Formato de horário inválido. Use HH:mm.")

    if hora_termino < hora_inicio:
        hora_termino += datetime.timedelta(days=1)  # Lida com casos onde o término é no dia seguinte

    horas_trabalhadas = hora_termino - hora_inicio
    return horas_trabalhadas.total_seconds() / 3600  # Retornar horas trabalhadas como float

