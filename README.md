# Planta IoT - Monitore o seu estado 
Este projeto foi desenvolvido para arduino e desktop, seguindo o esquema abaixo **(com exceção da utilização dos leds)** : 
<img src="https://uploads.filipeflop.com/2016/06/Circuito-sensor-de-solo-umidade-arduino.png" alt="drawing" width="600px"/>

## Requisitos

### Software
 - [Python 2.7](https://www.python.org/downloads/)
	 - [tweepy](https://pypi.org/project/tweepy/)
	 - [serial](https://pypi.org/project/pyserial/)
 - [Arduino IDE](https://www.arduino.cc/en/Main/Software#download)

### Hardware
<center>
Sensor de umidade de solo (YL-69)<br>
<img src="https://uploads.filipeflop.com/2017/07/sensor-de-umidade-do-solo-higrmetro-modulo-arduino-pic-22453-MLB20230474993_012015-O.jpg" alt="drawing" width="200px"/> <br><br>
Módulo chip comparador (LM393)<br>
<img src="https://uploads.filipeflop.com/2017/07/450xN-1-2.jpg" alt="drawing" width="200px"/> <br><br>
</center>

## Como isso funcionamento?
Cada mudança do estado de umidade da terra detectada faz com que o arduino escreva na porta serial o estado atual de umidade recebido. Para isso, é necessário iniciar a comunicação serial e habilitar a entrada analógica `A0`, como podemos ver no arquivo `planta_iot.ino`:
```c
#define  pino_sinal_analogico A0

void setup() {
	//Inicia a comunicação serial
	Serial.begin(9600);
	//Habilita entrada analógica A0
	pinMode(pino_sinal_analogico, INPUT);
}
```
O processo de monitoração é continuo, tendo uma curta interrupção de 100 milissegundos:
```c
void loop() {

	//Le o valor do pino A0 do sensor
	valor_analogico = analogRead(pino_sinal_analogico);

	//Solo com umidade alta
	if (valor_analogico > 0 && valor_analogico < 400) {
		estado_atual = UMIDO;
	}
	//Solo com umidade moderada
	if (valor_analogico > 400 && valor_analogico < 800) {
		estado_atual = MODERADO;
	}
	//Solo com umidade baixa
	if (valor_analogico > 800 && valor_analogico < 1024) {
		estado_atual = SECO;
	}
	if(ultimo_estado != estado_atual) {
		ultimo_estado = estado_atual;
		Serial.print(estado_atual);
	}
	delay(100);
}
```

Os bytes escritos, pelo arduino, na porta serial são lidos na outra ponta dessa comunicação, no desktop, pelo `arduino_tweet.py`. Cada byte lido é interpretado para um estado de umidade e cada estado de umidade possui uma mensagem apropriada para servir de conteúdo para um tweet. É necessário realizar o [procedimento de obter as credenciais](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html) para a utilização da api do twitter. Após realizado, substituir os respectivos valores das seguintes variáveis no arquivo `arduino_tweet.py`:
```python
#twitter application credentials
consumer_key="CONSUMER_KEY"
consumer_secret="CONSUMER_SECRET"

#twitter user credentials
access_token="ACCESS_TOKEN"
access_token_secret="ACCESS_TOKEN_SECRET"
```