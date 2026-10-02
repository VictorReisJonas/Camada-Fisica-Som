# Camada Física usando Som

Projeto desenvolvido para a disciplina de Redes de Computadores da UTFPR junto ao professor LUIZ ARTHUR FEITOSA SANTOS

## Objetivo

Transmitir bits de dados (0 e 1) por meio de batidas sonoras

## Tecnologias

- Python
- Sounddevice
- Numpy
- IA (para o estruturamento e parte do desenvolvimento do projeto)

## Método 1

Descrição do método de batidas.

Bit 0:
1 batida

Bit 1:
2 batidas

Bit Nulo:
3 ou mais batidas

## Configuração

Threshold:
1 (como estou utilizando as batidas como um curto para mandar um sinal fisico até o receptor de som foi necessario ter esse numero irrisório)  

Debounce:
125ms (escolhi esse numero pois achei o mais rapido possivel com uma frequencia boa de envio) 

Janela:
400ms (é o tempo exato que consigo enviar até 3 batidas) 

## Detecção de erros

Como meu projeto foge um pouco da premissa de toques já que usa um curto circuito fisico para enviar o som ao meu computador foi ligeiramente demorado até achar o comprimento certo de onda que meu sistema conseguia detectar

Vi que o sistema contava com muitas batidas simuntaneas (cerca de 20) ao em vez de uma quando eu tocava pois o sistema relacionava qualquer irregulariedade acima de um(1) de comprimento de onda como uma batida asssim tive que pedir auxilio do chat de como implementava um sistema que por um certo tempo enquanto a frequencia fosse acima de 1 o sistema ainda contaria como uma(1) única batida

Adicionar as configurações de como o sistema interpretaria também foi um desafio fiquei dando voltas e voltas tentando fazer o sistema reconhecer o meu "microfone" até achar que a opção de Microfone Interno tava ativado e não o meu OBS:( fiquei quase 30 minutos só tentando ver como fazia o sistema reconhecer o meu microfone pra descobrir que era só isso)

## Como executar

Instalar dependências:

pip install -r requirements.txt

Executar:

python src/main.py

## Vídeo de demonstração

https://www.veed.io/view/c7a3b953-8a3c-4098-877a-4f1b6f5f3e6d?panel=share

## Licença

MIT
