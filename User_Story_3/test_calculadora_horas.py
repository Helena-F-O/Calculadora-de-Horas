def test_calculo_horas_invertidas(self):
    # Teste para cálculo de horas trabalhadas com horários invertidos
    self.assertAlmostEqual(calcular_horas_trabalhadas("16:30", "08:00"), 8.5, places=2)
    self.assertAlmostEqual(calcular_horas_trabalhadas("17:00", "09:00"), 8.0, places=2)
    self.assertAlmostEqual(calcular_horas_trabalhadas("04:00", "22:30"), 5.5, places=2)
