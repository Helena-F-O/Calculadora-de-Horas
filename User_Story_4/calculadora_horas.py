def calcular_horas_trabalhadas_sem_dois_pontos(hora_inicio, hora_termino):
    # Remova os dois-pontos se presentes nos horários
    hora_inicio = hora_inicio.replace(":", "")
    hora_termino = hora_termino.replace(":", "")

    return calcular_horas_trabalhadas(hora_inicio, hora_termino)
