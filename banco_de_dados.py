# Esses dados seriam buscados no banco de dados. Simplificamos em listas para ficar mais fácil a exemplificação da POC.

base_incidentes = []
base_acoes = [{
    "nome": "MS de Login sem resposta",
    "codigo": "0001",
    "gatilhos": [
        {
            "servico": "login",
            "retorno": "503"
        },
        {
            "servico": "login",
            "retorno": "404"
        }
    ],
    "grupoUsuarios": "select [cpf,cnpj]...",
    "comunicacaoExterna": {
        "minimoOcorrencia": 5,
        "canal": "Push",
        "mensagem": "Infelizmente nosso app está indisponível, avisaremos quando voltar"
    },
    "comunicacaoInterna": [
        {
            "volumeOcorrencias": 10,
            "tempoOcorrendo": 5,
            "paraQuem": "Analista N1"
        },
        {
            "volumeOcorrencias": 5,
            "tempoOcorrendo": 20,
            "paraQuem": "Analista N2"
        },
        {
            "volumeOcorrencias": None,
            "tempoOcorrendo": 60,
            "paraQuem": "Coordenação"
        }
    ]
}]
