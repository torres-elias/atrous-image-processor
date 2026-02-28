import json
import math

class Parametros:
    def __init__(self, caminho_arquivo='parametros.json'):
        # 1. Dicionário com funções lambda (elimina a necessidade dos @staticmethod)
        self._mapa_ativacoes = {
            "relu": lambda x: max(0.0, float(x)),
            "sigmoid": lambda x: 1 / (1 + math.exp(-x))
        }
        
        # 2. Leitura e criação direta dos atributos
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                params = json.load(arquivo)
                
            self.mascara = params.get('mascara')
            self.stride = params.get('stride')
            self.taxa_r = params.get('taxa_r')
            self.nome_ativacao = params.get('ativacao', '').lower()
            
            # Valida e associa a função de ativação
            if self.nome_ativacao not in self._mapa_ativacoes:
                raise ValueError(f"Função de ativação '{self.nome_ativacao}' não suportada.")
            
            self.funcao_ativacao = self._mapa_ativacoes[self.nome_ativacao]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Erro ao processar o arquivo '{caminho_arquivo}': {e}")
            self.funcao_ativacao = None

    def aplicar_ativacao(self, valor):
        """Aplica a função de ativação carregada a um valor específico."""
        if not self.funcao_ativacao:
            raise AttributeError("A função de ativação não foi carregada corretamente.")
        return self.funcao_ativacao(valor)

    def exibir_resumo(self):
        """Imprime o estado atual dos parâmetros."""
        print("=== Estado da Operação ===")
        print(f"Máscara: {self.mascara}\nStride: {self.stride}\nTaxa r: {self.taxa_r}\nAtivação: {self.nome_ativacao}")
        print("==========================\n")








teste = Parametros()

# Exibir os parâmetros que foram salvos nos atributos (self.mascara, etc.)
teste.exibir_resumo()

# usando um método da classe para testar o cálculo
valor_entrada = -25
resultado = teste.aplicar_ativacao(valor_entrada)

print(f"Resultado da ativação para a entrada {valor_entrada} : {resultado}\n")