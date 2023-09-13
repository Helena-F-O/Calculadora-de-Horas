def descontar_intervalo(horas_trabalhadas, intervalo):
    try:
        intervalo = datetime.datetime.strptime(intervalo, "%H:%M")
    except ValueError:
        raise ValueError("Formato de intervalo inválido. Use HH:mm.")

    horas_descontadas = intervalo.hour + intervalo.minute / 60.0
    horas_trabalhadas -= horas_descontadas
    return max(0, horas_trabalhadas)  # Garante que as horas trabalhadas não sejam negativas
