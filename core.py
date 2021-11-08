import datetime
import uuid
import banco_de_dados

from typing import Dict, List


class Core:
    def __init__(self):
        self.base_incidentes = banco_de_dados.base_incidentes
        self.base_acoes = banco_de_dados.base_acoes

    def valida_incidente(self, gatilho: List[Dict]):
        if self.base_incidentes:
            for incidente_da_base in self.base_incidentes:
                if incidente_da_base.get('acoes'):
                    for acao_da_base in self.base_acoes:
                        if acao_da_base.get('gatilhos') == gatilho.gatilhos:
                            return True
                    return False
                else:
                    return False
        else:
            return False

    def valida_acao(self, gatilho: List[Dict]):
        if self.base_acoes:
            for acao_da_base in self.base_acoes:
                if acao_da_base.get('gatilhos') == gatilho.gatilhos:
                    return True
            return False
        else:
            return False

    def retorna_acao(self, gatilho: List[Dict]):
        for acao_da_base in self.base_acoes:
            if acao_da_base.get('gatilhos') == gatilho.gatilhos:
                return acao_da_base

    def retornar_incidente(self, gatilho: List[Dict]):
        codigo_acao = self.retorna_acao(gatilho).get('codigo')
        for incidente_da_base in self.base_incidentes:
            if codigo_acao in incidente_da_base.get('acoes'):
                return incidente_da_base

    def cria_incidente(self, gatilho: List[Dict]):
        novo_incidente = {
            "codigo": uuid.uuid4(),
            "dataInicio": datetime.datetime.now(),
            "dataFim": "",
            "status": "ABERTO",
            "ocorrencias": 1,
            "acoes": [],
        }
        existe_acao = self.valida_acao(gatilho)
        if existe_acao:
            acoes_tmp = novo_incidente['acoes']
            acoes_tmp.append(self.retorna_acao(gatilho).get('codigo'))
            novo_incidente.update({'acoes': acoes_tmp})
            self.base_incidentes.append(novo_incidente)
            return {'message': 'Incidente criado e relacionado à ação.'}
        else:
            return {'message': 'Necessário criar uma nova ação para esse problema. Time XPTO acionado para cadastro.'}

    def contabiliza_ocorrencia(self, gatilho: List[Dict]):
        incidente = self.retornar_incidente(gatilho)
        incidente['ocorrencias'] += 1

    def comunicacao(self, gatilho: List[Dict]):
        msg_return = {
            'Externo': '',
            'Interno': ''
        }

        quantidade_de_ocorrencias = self.retornar_incidente(gatilho).get('ocorrencias')

        acao = self.retorna_acao(gatilho)

        if acao.get('comunicacaoExterna').get('minimoOcorrencia') <= quantidade_de_ocorrencias:
            msg_return['Externo'] = (
                f"Mensagem '{acao.get('comunicacaoExterna').get('mensagem')}' "
                f"enviada para os clientes pelo canal '{acao.get('comunicacaoExterna').get('canal')}' \n"
            )  # Comunica externamente

        for i in range(1, len(acao.get('comunicacaoInterna'))+1):
            if (acao.get('comunicacaoInterna')[-i].get('volumeOcorrencias') is not None and \
                    acao.get('comunicacaoInterna')[-i].get('volumeOcorrencias') <= quantidade_de_ocorrencias) or \
                    (int((datetime.datetime.now() - self.retornar_incidente(gatilho).get('dataInicio')).seconds/60) >= acao.get('comunicacaoInterna')[-i].get('tempoOcorrendo')):
                msg_return['Interno'] = (
                    f"Comunicado de alerta enviado para '{acao.get('comunicacaoInterna')[-i].get('paraQuem')}"
                )
                return msg_return

        return {'message': 'Problema contabilizado.'}
