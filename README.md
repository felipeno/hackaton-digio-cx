# hackaton-digio-cx

Monolito criado para representar a solução elaborada para o Hackaton Digio - CX.

Arquitetura apresentada:
![Arquitetura](https://user-images.githubusercontent.com/62901711/140655826-fbaf2eed-c48c-4acd-a99f-b2b990c3da44.png)

Fluxo de utilização/execução apresentada:
![image](https://user-images.githubusercontent.com/62901711/140655880-3b016059-76da-4418-9739-d060f61c668a.png)

### Tecnologias Utilizadas:
- Python 3.9;
- FastAPI;

### Para instalar o ambiente de produção para utilizar a API:
#### Ps: com Python 3.9 instalado
```console
- pip install pipenv
```

### Depois de instalado, segue o manual e explicação de uso:

##### O fonte é dividido em 3 partes:

- api.py (local onde ficam os endpoints)
- banco_de_dados.py (simulação do banco de dados)
- core.py (o core da nossa aplicação, onde fica o manuseio e resposta da execução)

##### O contexto de utilização segue o fluxo de execução apresentado no diagrama acima. Já cadastramos uma ação no banco de dados.
##### Ação essa que foi configurada da seguinte forma:

- Comunicação externa: Quando um incidente ocorrer por pelo menos 5 vezes, um PUSH NOTIFICATION será enviado para os clientes com possíveis impactos.
- Comunicação interna: É um escalonamento de times com base em incidência de incidentes e tempo de incidente ocorrendo. Configuramos 3 escalonamentos para acionar 3 tipos de times diferentes.

##### Para simplificar a criação da POC, criamos uma API que tem HOST padrão e PORTA 8000.
##### O cenário da solução prevê que as informações que a API irá receber serão provenientes das plataformas de monitoring. Para conseguir exemplificar aqui, vamos receber um POST REQUISITON com um dicionário contendo as informações necessárias
##### Podemos utilizar o Postman, como teste:
![image](https://user-images.githubusercontent.com/62901711/140670488-292e4900-7126-4740-aa8f-a2ed268179c6.png)
Obs: o dicionário utilizado foi o abaixo. Esse dicionário é necessário pois é compatível com a ação já cadastrada no banco.
##### Dicionário:
```console
{
	"gatilhos": [
		{
			"servico": "login",
			"retorno": "503"
		},
		{
			"servico": "login",
			"retorno": "404"
		}
	]
}
```

### Para explorar a POC da solução:
#### Basta inicar o script atráves do api.py, seja via IDE:
![image](https://user-images.githubusercontent.com/62901711/140670620-2f7ad3f6-f52f-4907-950e-e814288c2a95.png)
#### Ou via cmd:
```console
pipenv shell
--uvicorn api:app --reload
```
![image](https://user-images.githubusercontent.com/62901711/140670849-57ab1f9d-4ad9-4562-89bd-e031432ffd93.png)
#### Depois de iniciar, basta utilizar uma plataforma para fazer o POST REQUISITON com o dicionário exemplificado acima. A plataforma utilizada nesse exemplo foi o Postman:
![image](https://user-images.githubusercontent.com/62901711/140670988-1c283ff5-b15a-4016-91a0-06c3f5e508bf.png)

#### Da forma como está configurada a ação no banco de dados, caso requisitado mais de 5 e 10 vezes, começaremos a enviar mensagens internas e externas para os clientes e times de suporte:
![image](https://user-images.githubusercontent.com/62901711/140671112-d220c7af-d745-429a-93b1-790ae890636d.png)
