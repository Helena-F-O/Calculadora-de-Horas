def test_desconto_intervalo(self):
    # Teste para desconto de intervalo
    self.assertAlmostEqual(descontar_intervalo(8.5, "00:30"), 8.0, places=2)
    self.assertAlmostEqual(descontar_intervalo(8.0, "01:00"), 7.0, places=2)
    self.assertAlmostEqual(descontar_intervalo(5.5, "00:15"), 5.25, places=2)

def test_formato_invalido_intervalo(self):
    # Teste para formato de intervalo inválido
    with self.assertRaises(ValueError):
        descontar_intervalo(8.5, "30")
    with self.assertRaises(ValueError):
        descontar_intervalo(8.0, "1-00")
