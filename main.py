class LightBulb:
  def __init__(self):
      self.state = False

  def turn_on(self):
      self.state = True
      print("A lâmpada foi ligada.")

  def turn_of(self):
      self.state = False
      print("A lâmpada foi desligada.")

#Silmulando a Biblioteca ```alexa ask-sdk
def on_intent(intent_request):
    intent_name = intent_request['intent']['name']

    if intent_name == "LigarLampada":
        light.turn_on()
    elif intent_name == "DesligarLampada":
        light.turn_of()


# Criando uma instância da lâmpada
light = LightBulb()

#light.turn_on()

# Simulando a interação com a Alexa para ligar "Alexa LigarLampada"
on_intent({'intent': {'name': 'LigarLampada'}})

light.turn_of()
