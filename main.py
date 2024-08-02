class Lampada:
  def __init__(self):
      self.estado = False

  def ligar(self):
      self.estado = True
      print("A lâmpada foi ligada.")

  def desligar(self):
      self.estado = False
      print("A lâmpada foi desligada.")


# Criando uma instância da lâmpada
lampada = Lampada()
lampada.ligar()
lampada.desligar()
