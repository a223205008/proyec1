import streamlit as st
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de los estilos de gráficos
sns.set(style="whitegrid")

# Diccionario de codones a aminoácidos
codones_a_aminoacidos = {
    'ATA': 'Ile', 'ATC': 'Ile', 'ATT': 'Ile', 'ATG': 'Met', 
    'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACT': 'Thr', 
    'AAC': 'Asn', 'AAT': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 
    'AGC': 'Ser', 'AGT': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 
    'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu', 
    'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCT': 'Pro', 
    'CAC': 'His', 'CAT': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 
    'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGT': 'Arg', 
    'GTA': 'Val', 'GTC': 'Val', 'GTG': 'Val', 'GTT': 'Val', 
    'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCT': 'Ala', 
    'GAC': 'Asp', 'GAT': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 
    'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGT': 'Gly', 
    'TCA': 'Ser', 'TCC': 'Ser', 'TCG': 'Ser', 'TCT': 'Ser', 
    'TTC': 'Phe', 'TTT': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu', 
    'TAC': 'Tyr', 'TAT': 'Tyr', 'TAA': 'Stop', 'TAG': 'Stop', 
    'TGC': 'Cys', 'TGT': 'Cys', 'TGA': 'Stop', 'TGG': 'Trp', 
    'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu'
}

# Función para traducir un codón de ADN a un aminoácido
def traducir_codon(codon):
    """
    Traducir un codón de ADN a un aminoácido utilizando el diccionario.
    """
    return codones_a_aminoacidos.get(codon, 'Desconocido')

# Función para traducir una secuencia de ADN completa a su secuencia de proteínas
def traducir_adn_a_proteina(secuencia_adn):
    """
    Convierte una secuencia de ADN en su correspondiente secuencia de proteína.
    """
    proteina = []
    # Asegurarnos de que la longitud sea múltiplo de 3 para obtener codones completos
    secuencia_adn = secuencia_adn.upper()
    for i in range(0, len(secuencia_adn), 3):
        codon = secuencia_adn[i:i+3]
        if len(codon) == 3:
            proteina.append(traducir_codon(codon))
    return ''.join(proteina)

# Función para contar los aminoácidos presentes en la proteína
def contar_aminoacidos(proteina):
    """
    Función para contar los aminoácidos presentes en la secuencia de proteína.
    """
    contador = Counter(proteina)
    return contador

# Función para graficar la comparación de proteínas
def graficar_comparacion_barras_apiladas(aminoacidos_contados_1, aminoacidos_contados_2):
    """
    Función para graficar la comparación de los aminoácidos en dos proteínas usando barras apiladas.
    """
    # Obtener los aminoácidos y sus cantidades
    aminoacidos_1 = list(aminoacidos_contados_1.keys())
    cantidades_1 = list(aminoacidos_contados_1.values())

    aminoacidos_2 = list(aminoacidos_contados_2.keys())
    cantidades_2 = list(aminoacidos_contados_2.values())

    # Crear un conjunto de aminoácidos único para ambas proteínas
    todos_aminoacidos = set(aminoacidos_1 + aminoacidos_2)
    todos_aminoacidos = list(todos_aminoacidos)
    
    # Reorganizar las listas para que todos los aminoácidos estén en el mismo orden
    cantidades_1_completa = [aminoacidos_contados_1.get(amino, 0) for amino in todos_aminoacidos]
    cantidades_2_completa = [aminoacidos_contados_2.get(amino, 0) for amino in todos_aminoacidos]

    # Crear la gráfica de barras apiladas
    fig, ax = plt.subplots(figsize=(10, 6))

    # Barras apiladas
    ax.bar(todos_aminoacidos, cantidades_1_completa, label='Secuencia 1', color='skyblue')
    ax.bar(todos_aminoacidos, cantidades_2_completa, bottom=cantidades_1_completa, label='Secuencia 2', color='salmon')

    # Etiquetas y título
    ax.set_title('Comparación de Aminoácidos entre Proteína 1 y Proteína 2')
    ax.set_xlabel('Aminoácidos')
    ax.set_ylabel('Cantidad')
    ax.legend()

    # Mostrar la gráfica
    st.pyplot(fig)

# Título de la app
st.title('Comparador de Secuencias de ADN y Análisis de Proteínas')

# Descripción en la barra lateral
st.sidebar.title("Descripción de Conceptos")

# Agregar texto explicativo sobre proteínas, nucleótidos y similitud genética
st.sidebar.write("""
**Proteínas**: Las proteínas son moléculas formadas por cadenas de aminoácidos, que a su vez son codificadas por las secuencias de ADN. Estas proteínas realizan una variedad de funciones dentro de las células, como enzimas, estructuras y señales.

**Nucleótidos**: Los nucleótidos son las unidades básicas del ADN. Cada nucleótido está formado por un azúcar, un fosfato y una base nitrogenada (adenina, timina, citosina o guanina). Las secuencias de nucleótidos en el ADN determinan la información genética que codifica para las proteínas.

**Similitud Genética**: Los seres vivos comparten un alto grado de similitud genética en sus secuencias de ADN. Esta similitud se refleja en las secuencias de proteínas que producen. Las pequeñas diferencias genéticas entre especies pueden dar lugar a las diversas características y funciones biológicas que los hacen únicos, pero la mayor parte del ADN es común entre organismos cercanamente relacionados.
""")

# Incluir una imagen relacionada con genética
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/9/99/DNA_double_helix.png", caption="Estructura del ADN", use_column_width=True)

# Introducción de las secuencias de ADN
seq1 = st.text_area('Introduce la primera secuencia de ADN (Ej. Humano)', height=200)
seq2 = st.text_area('Introduce la segunda secuencia de ADN (Ej. Chimpancé)', height=200)

# Botón para realizar la comparación
if st.button('Comparar Secuencias'):
    if seq1 and seq2:
        # Traducción de las secuencias de ADN a proteínas
        proteina1 = traducir_adn_a_proteina(seq1)
        proteina2 = traducir_adn_a_proteina(seq2)

        if proteina1 and proteina2:
            # Mostrar las proteínas traducidas
            st.write(f'Proteína 1 (Secuencia 1): {proteina1}')
            st.write(f'Proteína 2 (Secuencia 2): {proteina2}')

            # Contar los aminoácidos presentes
            aminoacidos_contados_1 = contar_aminoacidos(proteina1)
            aminoacidos_contados_2 = contar_aminoacidos(proteina2)

            # Mostrar los resultados de la comparación de proteínas
            st.write("
