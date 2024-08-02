[![Author](https://img.shields.io/badge/Dev-Nadi%20Duno-blueviolet%20)](https://portfolio-nadi.vercel.app/)
[![Social](https://img.shields.io/twitter/follow/nadiduno?label=%40nadiduno&style=social)](https://twitter.com/nadiduno)
[![Linkedin](https://img.shields.io/badge/in-Nadi%20Duno-blue)](https://www.linkedin.com/in/nadiduno/)
<br />
<br />

## Lâmpada Inteligente

Código: O código Python apresentado simula um sistema de controle de uma lâmpada inteligente, integrado com um sensor de luminosidade e com a assistente virtual Alexa.

## Funcionalidades:

* Classe Lampada: Representa uma lâmpada com os métodos ligar e desligar para controlar seu estado.
* Classe SensorLuminosidade: Simula um sensor de luminosidade, retornando um valor aleatório entre 0 e 100 para representar a intensidade da luz.
* Interação com a Alexa: A função on_intent simula a interação com a Alexa, permitindo ligar e desligar a lâmpada por comandos de voz.
* Controle automático: O código verifica a luminosidade atual e desliga a lâmpada se estiver acima de um determinado limite, simulando um comportamento de economia de energia.

## Fluxo:

* Inicialização: Cria-se uma instância da classe Lampada e SensorLuminosidade.
* Interação com a Alexa: A função on_intent é chamada, simulando um comando de voz para ligar a lâmpada.
* Leitura do sensor: A luminosidade atual é medida.
* Decisão: Se a luminosidade estiver acima do limite estabelecido, a lâmpada é desligada automaticamente.

## Em resumo:

O código demonstra como usar a programação orientada a objetos em Python para criar um sistema simples de automação residencial, integrando um dispositivo (lâmpada) com um sensor e uma interface de usuário (Alexa). O sistema é capaz de responder a comandos de voz e tomar decisões baseadas em dados do sensor, proporcionando um exemplo básico de como a Internet das Coisas pode ser implementada.

![Languages](https://img.shields.io/badge/%3C%2F%3E-languages-lightgrey)<br/>
[Python](https://www.python.org/)
<br/>

~~~ Python - POO
class LightBulb:
  def __init__(self):
      self.state = False

  def turn_on(self):
      self.state = True
      print("A lâmpada foi ligada.")

  def turn_of(self):
      self.state = False
      print("A lâmpada foi desligada.")
~~~

~~~python - Simulating Alexa
def on_intent(intent_request):
    intent_name = intent_request['intent']['name']

    if intent_name == "LigarLampada":
        light.turn_on()
    elif intent_name == "DesligarLampada":
        light.turn_of()
~~~

~~~python - Sensor
class SensorLuminosity:
    def metric_luminosity(self):
        import random
        return random.randint(0, 100)
~~~

[👩‍💻 Ver codigo](https://github.com/nadiduno/LampPoo/blob/main/main.py)