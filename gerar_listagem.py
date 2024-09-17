import pandas as pd

# Ler o arquivo Excel contendo os dados
df = pd.read_excel ()  # Altere para o caminho do seu arquivo

# Abrir um arquivo de texto para salvar a listagem
with open('dados_faltantes.txt', 'w') as file:
    # Percorrer cada linha do DataFrame e identificar colunas com dados faltantes
    for index, row in df.iterrows():
        missing_columns = []  # Lista para armazenar as colunas que estão faltando
        
        # Verificar se há dados faltantes em cada coluna
        for column in df.columns:
            if pd.isnull(row[column]) or row[column] == "":
                missing_columns.append(column)  # Adicionar à lista de colunas faltantes
        
        # Se houver colunas faltantes, gerar a listagem
        if missing_columns:
            missing_items = ', '.join(missing_columns)  # Transformar a lista de colunas faltantes em uma string
            line = f"{row['NOME']} está faltando os seguintes documentos: {missing_items}\n"
            file.write(line)  # Escrever no arquivo de texto

print("Listagem de dados faltantes salva em 'dados_faltantes.txt'.")
