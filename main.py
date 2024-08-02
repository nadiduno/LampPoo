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

#Simulando um sensor 
class SensorLuminosity:
    def metric_luminosity(self):
        # Simulação: retorna um valor aleatório entre 0 e 100
        import random
        return random.randint(0, 100)

# Criando uma instância da lâmpada
light = LightBulb()

# Criando uma instância do sensor
sensor = SensorLuminosity()

#light.turn_on()

# Simulando a interação com a Alexa para ligar "Alexa LigarLampada"
on_intent({'intent': {'name': 'LigarLampada'}})

#light.turn_of()

# Usando o sensor para desligar-a

lighting_current = sensor.metric_luminosity()

if lighting_current > 30:
    light.turn_of()
