def test_calculo_horas_sem_dois_pontos(self):
    # Teste para cálculo de horas trabalhadas sem dois-pontos
    self.assertAlmostEqual(calcular_horas_trabalhadas_sem_dois_pontos("0800", "1630"), 8.5, places=2)
    self.assertAlmostEqual(calcular_horas_trabalhadas_sem_dois_pontos("0900", "1700"), 8.0, places=2)
    self.assertAlmostEqual(calcular_horas_trabalhadas_sem_dois_pontos("2230", "0400"), 5.5, places=2)
