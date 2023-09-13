import unittest
from calculadora_horas import calcular_horas_trabalhadas

class TestCalculadoraHoras(unittest.TestCase):

    def test_calculo_horas_trabalhadas(self):
        # Teste para cálculo de horas trabalhadas
        self.assertAlmostEqual(calcular_horas_trabalhadas("08:00", "16:30"), 8.5, places=2)
        self.assertAlmostEqual(calcular_horas_trabalhadas("09:00", "17:00"), 8.0, places=2)
        self.assertAlmostEqual(calcular_horas_trabalhadas("22:30", "04:00"), 5.5, places=2)

    def test_formato_invalido(self):
        # Teste para formato de hora inválido
        with self.assertRaises(ValueError):
            calcular_horas_trabalhadas("08:00", "4:30")
        with self.assertRaises(ValueError):
            calcular_horas_trabalhadas("08:00", "16-30")

if __name__ == '__main__':
    unittest.main()
