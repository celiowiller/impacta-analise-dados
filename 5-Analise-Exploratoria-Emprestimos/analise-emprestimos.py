# 0. importar os recursos necessarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importar o recursos de metricas estatisticas do scipy
from scipy import stats
'''
importando o recurso stats do scipy - este recurso contem ferramentas estatiticas avançadas para utilizarmos na aplicação; teste estatisticos, distribuiçoes de probabilidade, entre outros 
'''
# importar os recursos necessarios do scikit-learn
from sklearn.model_selection import train_test_split, cross_val_score # aqui, importamos os recursos que auxiliarão na divisão de dados em conjunto de treino e teste para o modelo machine learning

from sklearn.ensemble import RandomForestClassifier # importamos o classificador Random Forest, um dos mais usados para modelos ml; baseado em árvores de decisão combinadas(ensemble);muito robusto e ideal para lidar com dados mistos - numéricos e categoricos

from sklearn.linear_model import LogisticRegression # importamos o LogisticRegression - regressão logistica - modelo mais simples e extremamente util para classificação binaria;usando este recurso podemos classeificar dados em, por exemplo, duas categorias distintas

from sklearn.preprocessing import StandardScaler # importamos o StandardEscaler - fazer uso deste que recurso que procura "padronizar" os dados: transforma os valores par a média 0 e o desvio padrão 1. Isso ajuda os modelos ml que podem ser sensiveis (sofrer influencia) a partir da escala do conjunto como, por exemplo, os modelos: SVM, KNN, ou regressão logistica

from sklearn.pipeline import Pipeline # importamos o Pipeline - recurso que permite criar um "encadeamento de etapas" de pré-processamento de modelagem dos dados. Com isso, garantimos que o pré-processamento aconteça sempre que o modelo for treinado ou avaliado

from sklearn.metrics import classification_report, confusion_matrix # este dois recursos atuam com elementos aplicados à avaliação de modelos; 
# classification_report: retornar algumas métricas como, por exemplo: precisão, f1-score
# confusion_matrix: mostra os erros e acertos por classe  - usando o formato de matriz

# 1. carregamento e preparação dos dados
df = pd.read_csv('Arquivo-Treino.csv') # função read_csv lê arquivo de planilha neste  
# respectivo formato
# print(df.head())
print(df.describe())

# 2. criar uma seleção para obter a mediana dos dados 
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount']).median() # aqui, estamos substituindo valores ausentes - caso ocorram - pela mediana obtida a partir dos valores da propria coluna

# 3. agora, vamos criar uma nova seleção a partir do historico de credito dos solicitantes
df['Credit_History'] = df['Credit_History'].fillna(1.0) # aqui, estamos substituindo valores ausentes - caso ocorram - pelo valor 1.0; este valor representa o historico de credito positivo

# 4. faser uso da função dropna(): é uma função que remove - do df - todas as linhas que possuem valores ausentes - este procedimento é classificado como: LIMPEZA DE DADOS 
df.dropna(
    subset = ['Loan_Status', 'ApplicantIncome', 'Education'], inplace = True
) # inplace = True: esta instrução modificada o df original

# 5. acessar o df a partir da coluna Loan_Status
df['Loan_Status'] = df['Loan_Status'].map({'Y':1, 'N': 0}) # aqui, estamos dizendo o seguinte: ao observar a coluna 'Loan_Status' vamos encontrar valores numericos - 1.0 ou 0.0 - ao "mapear" estes valores, estamos associando a cada um deles uma letra -> Y(sim)  para o status 1 e N(não) para o status 0

print()
print('============ EXIBIÇÃO DOS VALORES ==================')
print()

print('Primeiras Linhas')
print(df.head(5))
print('-------------------------------------------------------')

print('Describe')
print(df.describe())
print('-------------------------------------------------------')

print('Coluna Loan_status')
print(df['Loan_Status'])
print('-------------------------------------------------------')

print('Contagem de valores da coluna Loan_Status')
print(df['Loan_Status'].value_counts())
print('-------------------------------------------------------')

print('Contagem de valores nulos/ausentes do df')
print(df.isnull().sum())
print('-------------------------------------------------------')

print('Contagem de classificação de areas de propriedades')
print(df['Property_Area'].value_counts())
print('-------------------------------------------------------')

'''
Por que a instrução acima é importante?
 1 - modelos ML não operam, de forma alguma, com valores NaN (not-a-number)
 2 - os tratamentos, descritos acima, evitam a perda de dados(evitando "dropar/quebrar" linhas inteiras)
 3 - as operações acima tornam o modelo ML mais robusto e estavel; por exemplo, se for, também, aplicado a novos dados 

 df.dropna(subset=['Loan_Status', 'ApplicationIncome', 'Education'], inplace=True): aqui, criamos um subconjunto com as colunas indicadas na operação; removendo as linhas, deste subset, com valores ausentes(NaN) 
 inplace=True: modifica o df orignal sem a necessidade de fazer uma reatribuição de 
valores

 df['Loan_Status'] = df['Loan_Status'].map({'Y':1, 'N':0}): toda a vez que se encontrar a chave/key Y, ela deve ter o valor 1 associado; a mesma coisa para a linha com o caracter N - deve ter o valor 0 associado; significa estamos "convertendo" valores categoricos- Y, N - em valores numericos binarios - 1, 0;

'''


# vamos observar algumas variaveis categoricas (baseadas em texto)
# acessando a coluna Credit_History 
print('Contagem de valores da coluna Credit_History')
obs_1 = df['Credit_History'].value_counts()
print(obs_1)
print('-------------------------------------------------------')
# observar a coluna Loan_Status
print('Obervação de Loan_Status')

obs_2 = df.pivot_table(
    values = 'Loan_Status',
    index = ['Credit_History'],
    aggfunc = 'mean'
)
print(obs_2)
'''
acima, o bloco de código consegue detectar a senguinte tendencia:
os candidatos que possuem historico de emprestimos tendem - com altas taxas
de probabilidade de aprovação (média de 80%) - a conseguir emprestimo
'''
print('-------------------------------------------------------')

print('observar o grafico que mostra o comportamento da renda dos candidatos')
renda_candidato = df['ApplicantIncome'].hist(bins = 50, figsize = (10, 6))
# hist() -> é uma função que gerar um histograma (grafico) para observar comportamentos
# de variaveis; bins -> indica que este histograma será composto por barras verticais e divide os valores da coluna em 50 intervalos(classes)
plt.title('Distribuição da renda dos Solicitantes')
plt.xlabel('Renda(ApplicantIncome)')
plt.ylabel('Frequencia')
plt.show()
print('-------------------------------------------------------')

print('observar o grafico que mostra o comportamento da renda dos candidatos - considerando Education')
df.boxplot(column = ['ApplicantIncome'], by = ['Education'])
# hist() -> é uma função que gerar um histograma (grafico) para observar comportamentos
# de variaveis; bins -> indica que este histograma será composto por barras verticais e divide os valores da coluna em 50 intervalos(classes)
plt.title('Distribuição da renda dos Solicitantes x Educação')
plt.xlabel('Renda(ApplicantIncome)')

plt.show()
print('-------------------------------------------------------')

print('observar o grafico que mostra o comportamento do montante de emprestimos')
montante_emprestimos = df['LoanAmount'].hist(bins = 50, figsize = (10, 6))
# hist() -> é uma função que gerar um histograma (grafico) para observar comportamentos
# de variaveis; bins -> indica que este histograma será composto por barras verticais e divide os valores da coluna em 50 intervalos(classes)
plt.title('Distribuição do montante de emprestimos')
plt.xlabel('Montante(LoanAmount)')
plt.ylabel('Frequencia')
plt.show()
print('-------------------------------------------------------')

print('observar o grafico que mostra o comportamento da renda dos candidatos - considerando Education')
df.boxplot(column = ['LoanAmount'])
# hist() -> é uma função que gerar um histograma (grafico) para observar comportamentos
# de variaveis; bins -> indica que este histograma será composto por barras verticais e divide os valores da coluna em 50 intervalos(classes)
plt.title('numero de candidatos a um emprestimo x montante solicitado')
plt.xlabel('Montante(LoanAmount)')

plt.show()
print('-------------------------------------------------------')

# graficos para observar se tendencias se confirman ou se podemos encontrar novas tendencias
print('Analise grafica de historico de credito')
grafico = plt.figure(figsize = (10, 6))
ax1 = grafico.add_subplot(121)
ax1.set_xlabel('historico de Credito')
ax1.set_ylabel('Candidatos/Applicant')
ax1.set_title('Analise grafica de historico de credito')
obs_1.plot(kind = 'bar', ax = ax1)
# plt.show()
print('-------------------------------------------------------')

print('observar a tendencia obtida a partir de outro ponto de observação')
ax2 = grafico.add_subplot(122)
ax2.set_xlabel('Historico de Credito')
ax2.set_ylabel('Probabilidade de obter emprestimo')
ax2.set_title('Tendencia de obtenção de emprestimo')
obs_2.plot(kind = 'bar', ax = ax2)
plt.show()


print('-------------------------------------------------------')
obs_3 = pd.crosstab(df['Credit_History'], df['Gender'])
obs_3.plot(
    kind = 'bar', stacked = True, color = ['red', 'blue']
)
plt.show()
'''
acima, detectamos a seguinte tendencia:

pessoas do genero masculino são maioria com historico de credito; tendencia de 
genero msculino obter credito
'''


# 2. ANALISE ESTATISTICA AVANÇADA (SCIPY)

# teste de normalidade - de shapiro -  para a coluna ApplicantIncome (coluna de renda do solicitante do emprestimo)
shapiro_stat, shapiro_p = stats.shapiro(df['ApplicantIncome'])
# exibir
print(f'\nShapiro-Wilk (normalidade de renda): p = {shapiro_p: .4f}')
# shapiro_p: valor-p(p-value): o valor mais importante na analise que estamos fazendo
# shapiro_stat: valor estatitisco do teste

# condicional para a analise da distribuição de renda 
if shapiro_p < 0.05: # representa 5% de probabilidade máxima de cometer erro
    print('-> A renda ***NÃO segue a distruibição normal')
else:
    print('-> A renda segue distribuição normal')

# fazer uma comparação de renda "olhando" para o nivel educacional - graduados e não-graduados
grad = df[df['Education'] == 'Graduate']['ApplicantIncome'] 
non_grad = df[df['Education'] == 'Not Graduate']['ApplicantIncome'] 
# exibir
print('valores das flags booleanas Graduate, Not Graduate')
print(grad)
print('---------------------------------------------------------------')
print(non_grad)

# teste Levene para observar o comportamento dos dados dos graduados e não-graduados
levene_stat, levene_p = stats.levene(grad, non_grad)
# escolher os 
if shapiro_p < 0.05 or levene_p < 0.05:
    stat, p = stats.mannwhitneyu(grad, non_grad)
    print(f'\nMann-Whitney U teste: p = {p: .4f}')
else:
    stat, p = stats.ttest_ind(grad, non_grad)
    print(f'\nTest t independente: p = {p: .4f}')
# student - o test t Student
print('--------------------------------------------------')
# correlação entre renda e valor do emprestimo
pearson_corr, pearson_p = stats.pearsonr(df['ApplicantIncome'], df['LoanAmount'])
print(f'\nCorrelação de Pearson entre renda e valor do emprestimo: r = {pearson_corr: .2f}, p = {pearson_p: .4f}')

# corrleção de spearman
spearman_corr, spearman_p = stats.spearmanr(df['ApplicantIncome'], df['LoanAmount']) 
print(f'\nCorrelação de Spearman: rho = {spearman_corr: .2f}, p = {spearman_p: .4f}')

# 3. MODELAGEM  COM PIPELINE (SCIKIT-LEARN)

# seleção dos contextos de dados
features = ['ApplicantIncome', 'LoanAmount', 'Credit_History']
X = df[features] # um conjunto de dados com as colunas listadas acima; será o conjunto de dados de entrada do modelo
y = df['Loan_Status'] # o label (target) da classifição; 'Loan_Status'  é a variavel que estamos tentando prever (prever se o emprestimo será concedido a partir: da renda, do montante solicitado, e do historico de credito)


# separar os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# pipeline (sequencia de passos automatizados) com escalonamento e random forest
pipeline_rf = Pipeline([
    ('scaler', StandardScaler()), 
    ('model', RandomForestClassifier(random_state=42))
])

pipeline_rf.fit(X_train, y_train)
y_pred_rf = pipeline_rf.predict(X_test)

# exibe
print('\n[Random Forest] Relatório de Classificação:')
print(classification_report(y_test, y_pred_rf))
print()
print('\nMatriz de confusão')
print(confusion_matrix(y_test, y_pred_rf))

print('---------------------------------------------------')
# validação cruzada
cv_scores = cross_val_score(pipeline_rf, X, y, cv=5)
print(f'Validação cruzada (Random Forest) - Precisão/Acuracia média: {cv_scores.mean(): .4f}')

print('---------------------------------')
# importancia das features (Random Forest)
model_rf = pipeline_rf.named_steps['model']
importancias = pd.Series(model_rf.feature_importances_, index=features).sort_values(ascending=False)
print('\nIMportância das varaveis(Random Forest): ')
print(importancias)
print('---------------------------------')

# gráfico da importancia das vars
importancias.plot(kind='barh', color='green')
plt.title('Importância das variaveis')
plt.xlabel('Importância')
plt.tight_layout()
plt.show()