import os

def filtrar_livros_por_avaliacao(arquivo_entrada: str, arquivo_saida: str):
    """
    Filtra livros de um arquivo com base em sua avaliação e em critérios
    específicos no título, salvando o resultado em um novo arquivo.

    Args:
        arquivo_entrada: O caminho para o arquivo de texto contendo títulos
                         de livros e suas avaliações em linhas alternadas.
        arquivo_saida: O caminho para o arquivo de texto onde os resultados
                       filtrados serão salvos.
    """
    notaveis = []
    linha_anterior = ""

    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            # `enumerate` nos permite obter o índice e o valor da linha
            for indice, linha_atual in enumerate(f):
                linha_atual = linha_atual.strip()
                
                # Linhas pares (índice 1, 3, 5...) contêm as avaliações.
                # A contagem de `enumerate` começa em 0.
                if (indice + 1) % 2 == 0:
                    try:
                        avaliacao = float(linha_atual)
                        if avaliacao >= 4.08:
                            # Condição 1: A linha anterior (título) não tem "#"
                            # Condição 2: A linha anterior (título) tem "#1"
                            if "#" not in linha_anterior or "#1" in linha_anterior:
                                # Adiciona o título e a avaliação correspondente
                                notaveis.append(linha_anterior + os.linesep)
                    except ValueError:
                        print(
                            f"Aviso: O conteúdo '{linha_atual}' na linha {indice + 1} "
                            "não é um número decimal e será ignorado."
                        )
                
                # Atualiza a linha anterior para a próxima iteração
                linha_anterior = linha_atual

    except FileNotFoundError:
        print(f"Erro: O arquivo de entrada '{arquivo_entrada}' não foi encontrado.")
        return

    try:
        # Cria e escreve no arquivo de saída
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.writelines(notaveis)
        print(f"Processamento concluído. Resultados salvos em '{arquivo_saida}'.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo de saída '{arquivo_saida}': {e}")


# --- Exemplo de Uso ---

# 1. Para testar, vamos criar um arquivo de exemplo com o conteúdo esperado.
conteudo_exemplo = [
    "Um Livro Excelente",
    "4.95",
    "Saga Fantástica #1",
    "4.8",
    "Livro Mediano",
    "3.5",
    "Outro Livro Bom",
    "4.1", # Menor que 4.08, não será incluído
    "Saga Fantástica #2", # Tem "#", mas não é "#1", não será incluído
    "4.7",
    "Livro com avaliação textual",
    "ótima", # Gerará um aviso
    "Clássico da Ficção #1",
    "5.0"
]

# 2. Define os nomes dos arquivos e executa a função
NOME_ARQUIVO_ENTRADA = "books_alternating_between_title_and_rating.txt"
NOME_ARQUIVO_SAIDA = "livros_sob_critérios.txt"
filtrar_livros_por_avaliacao(NOME_ARQUIVO_ENTRADA, NOME_ARQUIVO_SAIDA)