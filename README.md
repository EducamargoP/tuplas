# 📗 Exercícios com Tuplas em Python

Este repositório contém exercícios práticos e anotações sobre o uso de **tuplas** (`tuple`) em Python, parte dos meus estudos de programação em 2025. As tuplas são estruturas **imutáveis**, ideais para dados que não precisam ser alterados.

---

## 🧪 Lista de Exercícios

### 01 – Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com números de 0 a 20 por extenso.  
O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

---

### 02 – Tabela do Brasileirão
Crie uma tupla preenchida com os **20 primeiros colocados** do Campeonato Brasileiro.  
Exiba:
- Os 5 primeiros times
- Os 4 últimos colocados
- Os times em ordem alfabética

---

### 03 – Números Aleatórios
Gere **cinco números aleatórios** entre 1 e 100 usando a biblioteca `random` e armazene-os em uma **tupla**.

---

### 04 – Tupla com Valores Digitados
Leia **quatro valores inteiros** pelo teclado e guarde-os em uma **tupla**.  
Depois, mostre:
- Quantas vezes apareceu o número 9
- Em que posição foi digitado o primeiro 3
- Quais foram os números pares

---

### 05 – Produtos e Preços
Crie uma **tupla única** com nomes de produtos e seus respectivos preços.  
Depois, exiba os dados de forma tabulada.

---

### 06 – Vogais nas Palavras
Crie uma tupla com várias palavras.  
Para cada palavra, identifique e exiba as **vogais** que ela contém.

---

## 📘 Anotações sobre Tuplas

### 🔹 1. O que são tuplas?
- Semelhantes às listas, mas **imutáveis**
- Representadas por **parênteses**: `( )`

### 🔹 2. Sintaxe
Mesmo sem os parênteses, o Python interpreta como tupla:
```python
tupla = 1, 2, 3
```

### 🔹 3. Tupla com um único valor
Precisa de **vírgula** para ser reconhecida como tupla:
```python
tupla = (4,)  # sem a vírgula é só um número inteiro
```

### 🔹 4. Tuplas com `range`
Podemos gerar uma tupla diretamente de um `range`:
```python
tupla = tuple(range(5))
```

### 🔹 5. Desempacotamento
Tuplas exigem que o número de variáveis para desempacotar seja exatamente o mesmo:
```python
a, b, c = (1, 2, 3)  # válido
```

### 🔹 6. Sem métodos de alteração
Por serem imutáveis, tuplas **não têm** métodos como `.append()` ou `.remove()`.

---

## 🔢 Operações matemáticas com tuplas numéricas

Se os valores forem inteiros:
```python
tupla = (1, 2, 3, 4, 5)
sum(tupla)
max(tupla)
min(tupla)
```

---

## ➕ Concatenação de Tuplas
Embora imutáveis, é possível concatenar tuplas:
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
nova = tupla1 + tupla2
```

---

## 🎯 Quando usar tuplas?

- Quando os dados não precisam ser modificados
- Para tornar o código mais seguro
- Tuplas são mais rápidas que listas na execução

---

## 🔍 Acesso por índice
Funciona da mesma forma que nas listas:
```python
tupla = ("A", "B", "C")
print(tupla[1])  # 'B'
```

---

## ✂️ Slicing
É possível fazer fatiamento:
```python
tupla = (0, 1, 2, 3, 4, 5)
print(tupla[1:5:2])
```

---

## 🧬 Copiando tuplas
Como tuplas são imutáveis, a cópia é simplesmente uma nova referência:
```python
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
nova_tupla = tupla1 + tupla2
print(nova_tupla)
```

---

Pronto para programar com tuplas? Explore os exercícios e veja como essa estrutura pode deixar seu código mais rápido, limpo e seguro. 🚀
