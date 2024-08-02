class LightBulb:
  def __init__(self):
      self.state = False

  def turn_on(self):
      self.state = True
      print("A lâmpada foi ligada.")

  def turn_of(self):
      self.state = False
      print("A lâmpada foi desligada.")

# Criando uma instância da lâmpada
light = LightBulb()
light.turn_on()
light.turn_of()
