# Algoritmo de Multiplicação de Karatsuba

## Descrição do Projeto
O algoritmo de Karatsuba é um método eficiente de multiplicação de dois números inteiros grandes, que reduz a complexidade para aproximadamente \(O(n^{\log_2 3})\), tornando-o mais rápido do que a multiplicação tradicional \(O(n^2)\) para números grandes.

### Explicação do Código Linha a Linha
```python
# Função recursiva de Karatsuba para multiplicação eficiente
def karatsuba(x, y):
    # Caso base: se um dos números for menor que 10, retorna a multiplicação direta
    if x < 10 or y < 10:
        return x * y

    # Converte os números para string e calcula o tamanho do maior número
    num1 = str(x)
    num2 = str(y)
    n = max(len(num1), len(num2))
    half = n // 2  # Divide o tamanho pela metade

    # Divide x em a e b, e y em c e d
    a = x // 10**half  # Parte alta de x
    b = x % 10**half   # Parte baixa de x
    c = y // 10**half  # Parte alta de y
    d = y % 10**half   # Parte baixa de y

    # Recursivamente calcula os três produtos necessários
    ac = karatsuba(a, c)  # Produto das partes altas
    bd = karatsuba(b, d)  # Produto das partes baixas
    ad_bc = karatsuba(a + b, c + d) - ac - bd  # Produto cruzado

    # Combina os resultados para obter o produto final
    result = ac * 10**(2*half) + (ad_bc * 10**half) + bd
    return result

# Função principal que solicita entrada do usuário e executa a multiplicação
def main():
    x = int(input("Valor x: "))  # Lê o primeiro número
    y = int(input("Valor y: "))  # Lê o segundo número
    
    # Chama a função de Karatsuba e imprime o resultado
    print(f"Multiplicando {x} por {y}: {karatsuba(x, y)}")

# Chamada da função principal
main()
```

## Como Executar o Projeto
1. Clone este repositório.
2. Certifique-se de ter o Python 3 instalado.
3. Execute no terminal:
   ```bash
   cd {caminho relativo onde este repositório foi clonado}
   python3 main.py
   ```
4. Insira os valores de entrada quando solicitado.

## Relatório Técnico

### Análise da Complexidade Ciclomática

#### Fluxo de Controle da Função `karatsuba(x, y)`
O fluxo de controle da função pode ser representado por um grafo onde cada decisão e chamada recursiva forma um novo nó.

- **Nós (N)**: 7 (blocos de código incluindo decisões e recursões)
- **Arestas (E)**: 8 (transições entre blocos de código)
- **Componentes Conexos (P)**: 1 (apenas um fluxo principal)

A complexidade ciclomática é calculada como:
\[ M = E - N + 2P \]
\[ M = 8 - 7 + 2(1) = 3 \]
Isso indica que a função tem 3 caminhos independentes, condizente com a divisão e recursão do algoritmo.

### Análise da Complexidade Assintótica
- **Melhor caso**: \( O(1) \) quando `x` ou `y` são menores que 10.
- **Caso médio e pior caso**: \( O(n^{\log_2 3}) \approx O(n^{1.585}) \), pois o algoritmo divide `n` ao meio a cada chamada recursiva.
- **Complexidade espacial**: \( O(n) \) devido à profundidade da recursão.
