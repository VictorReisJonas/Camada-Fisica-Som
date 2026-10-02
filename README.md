# Camada Física usando Som

Projeto desenvolvido para a disciplina de Redes de Computadores da UTFPR junto ao professor LUIZ ARTHUR FEITOSA SANTOS

## Objetivo

Transmitir bits de dados (0 e 1) por meio de batidas sonoras com confiabilidade e de maneira interoperável  

## Tecnologias

- Python
- Sounddevice
- Numpy
- IA (para o estruturamento e parte do desenvolvimento do projeto)

## Método 1

Descrição do método de batidas.

Bit 0:
1 batida no mesmo intervalo de verificação

Bit 1:
2 batidasno mesmo intervalo de verificação

Bit Nulo:
3 ou mais batidas no mesmo intervalo de verificação

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

## Como executar adad

Instalar dependências:

pip install -r requirements.txt

Executar:

python src/main.py

## Declaração do Uso de Inteligência Artificial

Como dito pelo professor o uso da IA seria essencial para a realização do projeto, dito isso fui analisando cada tópico solicitado pelo o mesmo e inserindo no chat para ele me dizer como deveria ser implementado da melhor forma o programa.Foi se utilizado a IA Chat GPT para contemplar todos os requisitos solicitados pelo professor, ele me instruiu de como dissertar sobre o PDF de requerimentos e de como fazer cada implementação, suas modificações e alterações de como a estrutura deveria se "mover" foram todas de autoria minha mas a estrutura central foi toda feita com a ajuda da IA

## Declarações finais

Estou enviando o trabalho incompleto pela falta de tempo pois estou a fazer sozinho sem o "microfone" solicitado, enviei 2 email para o professor pedindo para prorrogar a entrega, se você ja prorrogou ignore este Git Hub por agora que haverá muitas mudanças sobre tanto o Método 1(incompleto e incompativél com a descrição apresentada) e o Método 2(Ainda em desenvolvimento)

## Licença

MIT
