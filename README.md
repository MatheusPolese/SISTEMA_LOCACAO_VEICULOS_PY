# SISTEMA_LOCACAO_VEICULOS_PY

Tema e objetivo:
Modelar e programar um sistema de locadora veiculos utilizando pilares e padrões de Programação Orientada a Objetos na linguagem de python.

Diagrama de Classes: https://lucid.app/lucidchart/70afaf0d-3681-4ff2-b225-3864ade17abd/edit?viewport_loc=-888%2C-11%2C2197%2C1073%2C0_0&invitationId=inv_aa561a14-db48-46bc-b96f-1f1035c92ce2

Padrões de projeto utilizados: Factory para a criação de classes filhas de veículo que compartilhavam os mesmos métodos, e Strategy para definir uma estratégia de desconto para carros alugados por um período igual ou maior que 7 dias.

O sistema é uma Locadora de Veículos em terminal dividida em 4 partes:
veiculos.py: Cadastra carros usando o padrão Factory Method (Categorias: Econômico, SUV e VAN, cada uma com seu preço de diária fixo).
cliente.py: Gerencia o cadastro de Pessoas Físicas (CPF) e Jurídicas (CNPJ), valida e-mails @gmail.com e conta quantos aluguéis o cliente já fez.
aluguel.py: Realiza a locação calculando o custo total pelos dias locados, aplicando o desconto conforme o padrão Strategy, e bloqueia a locação se as datas de reserva coincidirem com outro aluguel.
menu.py: Une tudo criando uma interface interativa no terminal para o usuário navegar pelas opções de cadastro e locação.

Pilares Utilizados:
Abstração e Herança:
Cliente(Classe Abstrata)-> Cliente_fisico e Cliente_Juridico.
Encapsulamento:
As classes clientes, veiculos e aluguem todos tem atributos privados acessados apenas via getters e alterados via setters.
Polimorfismo:
O método Diaria() teve a mesma aplicabilidade mesmo em diferentes classes.
O método exibir_cliente() foi implementado tanto na classe de pessoa física quanto na jurídica.

Dificuldades Encontradas: Tive dificuldade em armazenar os objetos criados nas classes Veiculo e Cliente, pois precisaria utilizá-los mais tarde para vinculá-los na classe Aluguel.
Como resolvi: Criei uma classe de banco de dados para cada entidade. Isso facilitou muito a criação de métodos e possibilitou mudar o status estático de "alugado" ou "não alugado" para um sistema que realmente permite realizar reservas de uma data a outra, aproximando-se de como funciona no mundo real.

Dificuldades Encontradas: Estava utilizando testes condicionais (if/else) muito extensos para definir o preço de locação de cada veículo.
Como resolvi: Implementei o padrão de projeto Factory (Fábrica), tornando a classe Veiculo abstrata e transformando cada categoria de veículo em uma classe distinta, com seu próprio cálculo de preço.

Principal Aprendizado: Acredito que construí uma base sólida de Programação Orientada a Objetos neste projeto. Consegui compreender a relevância de dominar os pilares da POO no desenvolvimento de um sistema, além de entender a importância de planejar o projeto previamente, como nos diagramas e de saber como versionar o código (usar Git/commits).

Utilizei IA como ferramenta de apoio.
Ferramenta(s): Gemini Flash 3.5
Finalidade: Utilizei a ferramenta para resolução de duvidas pontuais e pesquisa, da mesma maneira que se utiliza Navegadores para pesquisa.
Validação: Declaro que todo o código gerado foi lido, testado e e ajustado conforme as
necessidades específicas do projeto e da disciplina. A responsabilidade pela arquitetura,
decisões de design e correção do código é de minha total responsabilidade.
