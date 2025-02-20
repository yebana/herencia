import streamlit as st

st.title("Calculadora de Reparto de Herencia, Powered by @yebana")

# Recoger datos básicos
edad_viudez = st.number_input("¿Edad de la viuda/viudo en el momento del reparto de la herencia?", min_value=0, max_value=120, value=65)
num_hijos = st.number_input("¿Cuántos hijos tienen?", min_value=0, max_value=20, value=2)
herencia_total = st.number_input("¿Cuál es el monto total de la herencia (en euros)?", min_value=0.0, value=100000.0)

if st.button("Calcular Reparto"):
    # Cálculos del reparto
    # En régimen de gananciales, la mitad es para el cónyuge viudo
    mitad_gananciales = herencia_total / 2
    
    # La otra mitad se reparte:
    # - Usufructo para el cónyuge viudo (depende de la edad)
    # - El resto se reparte entre los hijos
    
    herencia_a_repartir = mitad_gananciales
    
    # Cálculo del usufructo según la edad del viudo/a
    porcentaje_usufructo = (89 - edad_viudez) / 100
    # Aseguramos que el porcentaje esté entre 0 y 1
    porcentaje_usufructo = max(0, min(1, porcentaje_usufructo))
        
    valor_usufructo = herencia_a_repartir * porcentaje_usufructo
    
    # Cálculo para los hijos
    if num_hijos > 0:
        herencia_por_hijo = (herencia_a_repartir - valor_usufructo) / num_hijos
    else:
        herencia_por_hijo = 0

    # Mostrar resultados
    st.header("Resultados del Reparto")
    
    st.write(f"**Parte del cónyuge viudo:**")
    st.write(f"- Por gananciales: {mitad_gananciales:,.2f}€")
    st.write(f"- Por usufructo: {valor_usufructo:,.2f}€")
    st.write(f"**Total cónyuge viudo: {(mitad_gananciales + valor_usufructo):,.2f}€**")
    
    if num_hijos > 0:
        st.write(f"\n**Parte para cada hijo:**")
        st.write(f"- Cantidad por hijo: {herencia_por_hijo:,.2f}€")
        st.write(f"**Total hijos: {(herencia_por_hijo * num_hijos):,.2f}€**")
    else:
        st.write("\nNo hay hijos para el reparto de la herencia.")
