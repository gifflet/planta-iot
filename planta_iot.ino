//Author:splait

#define pino_sinal_analogico A0
#define SECO 0
#define MODERADO 1
#define UMIDO 2
 
int valor_analogico;
int ultimo_estado = -1;
int estado_atual;

void setup()
{
  Serial.begin(9600);
  pinMode(pino_sinal_analogico, INPUT);
}
 
void loop()
{
  //Le o valor do pino A0 do sensor
  valor_analogico = analogRead(pino_sinal_analogico);
 
  //Solo com umidade alta
  if (valor_analogico > 0 && valor_analogico < 400)
  {
    estado_atual = UMIDO;
  }
  //Solo com umidade moderada
  if (valor_analogico > 400 && valor_analogico < 800)
  {
    estado_atual = MODERADO;
  }
  //Solo com umidade baixa
  if (valor_analogico > 800 && valor_analogico < 1024)
  {
    estado_atual = SECO;
  }
  if(ultimo_estado != estado_atual){
    ultimo_estado = estado_atual;
    Serial.print(estado_atual);
  }
  delay(100);
}