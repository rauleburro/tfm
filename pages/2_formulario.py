import streamlit as st

# Title
st.title("Herramienta estandarizada para la Evaluación del Bruxismo (STAB)")

mandatory_fields = {}

# # Basic Information (Mandatory Fields)

mandatory_fields["Correo"]: st.text_input("1. Correo")
mandatory_fields["Nombre Completo"]: st.text_input("2. Nombre Completo")
mandatory_fields["Genero"]: st.radio(
    "3. Sexo", ["Femenino", "Masculino", "Otro"], index=None)
mandatory_fields["Edad"]: st.number_input(
    "4. Edad", min_value=0, max_value=120, step=1)
mandatory_fields["Peso"]: st.number_input(
    "5. Peso (kg)", min_value=0.0, step=0.1)
mandatory_fields["Altura"]: st.number_input(
    "6. Altura (cm)", min_value=0.0, step=0.1)
mandatory_fields["Estado civil"]: st.radio("7. ¿Cuál es tu estado civil actual?", [
    "Casado", "Conviviendo como casado", "Divorciado", "Separado", "Viudo", "Soltero"], index=None)
mandatory_fields["Educacion"]: st.radio("8. ¿Cuál es nivel más alto de escolaridad que has completado?", [
    "Escuela obligatoria <16 años", "Escuela secundaria (preparatoria) hasta los 18 años",
    "Algunos estudios universitarios (sin grado)", "Graduado universitario", "Posgrado"
], index=None)

# Bruxism-related questions
mandatory_fields = {
    "A1.1": st.radio("9. A1.1 ¿Con qué frecuencia aprietas o rechinas los dientes cuando estás dormido en el último mes?", [
        "Nunca", "Menos de una noche al mes", "1-3 noches al mes", "1-3 noches a la semana", "4-7 noches a la semana", "No lo sé"], index=None),

    "A2.1": st.radio("10. A2.1 ¿Con qué frecuencia rechinas tus dientes durante el día?", [
        "Nunca", "Un poco", "Algunas veces", "La mayoría del tiempo", "Todo el tiempo", "No lo sé"], index=None),

    "A2.2": st.radio("11. A2.2 ¿Con qué frecuencia aprietas tus dientes durante el día?", [
        "Nunca", "Un poco", "Algunas veces", "La mayoría del tiempo", "Todo el tiempo", "No lo sé"], index=None),

    "A2.3": st.radio("12. A2.3 ¿Con qué frecuencia realizas movimientos de claqueteo con tus dientes durante el día?", [
        "Nunca", "Un poco", "Algunas veces", "La mayoría del tiempo", "Todo el tiempo", "No lo sé"], index=None),

    "A2.4": st.radio("13. A2.4 ¿Con qué frecuencia haces contracturas musculares sin contacto dentario durante el día?", [
        "Nunca", "Un poco", "Algunas veces", "La mayoría del tiempo", "Todo el tiempo", "No lo sé"], index=None),

    "Dolor": st.radio("14. A3 En los últimos 30 días, ¿tuvo dolor en el área de la articulación de la mandíbula o la sien?", [
        "Sí", "No"], index=None),
}

st.radio("15. A3.1 En los últimos 30 días, ¿duración del dolor en la mandíbula o sien?", [
         "Sin dolor", "El dolor viene y va", "El dolor está siempre presente"], index=None)

st.radio("16. A3.2 En los últimos 30 días, ¿has tenido dolor o rigidez en la mandíbula al despertar?", [
         "No", "Sí"], index=None)

st.radio("17. A3.3 En los últimos 30 días, ¿has tenido la limitación de apertura bucal?", [
         "No", "Sí"], index=None)

st.multiselect("18. A3.4 En los últimos 30 días, ¿cambiaron algunas actividades el dolor en tu mandíbula o sien?", [
    "Masticar alimentos duros", "Abrir la boca o mover la mandíbula", "Hábitos mandibulares", "Otras actividades", "No"])

st.radio("19. A3.5 En los últimos 30 días, ¿has tenido algún ruido en la articulación de la mandíbula?", [
         "No", "Sí"], index=None)

st.multiselect("20. A3.6 En los últimos 30 días, ¿tuviste dolor muscular en la mandíbula en algún momento del día?", [
    "Despertar", "Desayuno", "Almuerzo", "Cena", "No tengo dolor"])

st.multiselect("21. A3.6.1 En los últimos 30 días, ¿tuviste rigidez en la mandíbula?", [
    "Despertar", "Desayuno", "Almuerzo", "Cena", "No tengo dolor"])

st.multiselect("22. A3.7 ¿Eres consciente de los siguientes síntomas?", [
    "Fatiga mandibular", "Dientes apretados", "Dolor en sienes", "Mandíbula bloqueada", "Dificultad al abrir", "Click articular", "No tengo síntomas"])

st.radio("23. A3.8 ¿En los últimos 30 días, has tenido algún dolor de cabeza en las sienes?", [
         "No", "Sí"], index=None)

st.number_input("24. A3.8.1 En caso afirmativo, ¿cuántos días al mes?",
                min_value=0, max_value=31, step=1)

mandatory_fields = {
    "A3.9": st.multiselect("25. A3.9 ¿Experimentas alguno de los siguientes síntomas en caso de deterioro dental existente?", [
        "Sensibilidad y/o dolor", "Problemas funcionales (dificultades para masticar y comer)", "Deterioro de la apariencia estética (dientes comprometidos)", "Desgaste del tejido dental duro y de restauraciones", "Dificultad en el habla", "Ninguno"]),

    "A3.10": st.radio("26. A3.10 ¿Tienes ruidos o zumbidos en los oídos (tinnitus)?", [
        "No", "Sí"], index=None),

    "A3.10.1": st.multiselect("27. A3.10.1 En caso afirmativo, ¿en qué momento del día?", [
        "Por la mañana", "Durante el día", "Antes de dormir", "Todo el día", "No lo sé"]),

    "A3.12": st.radio("28. A3.12 ¿Experimentas pérdida de saliva durante la noche?", [
        "No experimento", "A veces", "Regularmente", "Siempre", "Todas las noches y otras prendas de cama se mojan"], index=None),

    "A3.12.1": st.radio("29. A3.12.1 ¿Experimentas pérdida de saliva durante la siesta?", [
        "No experimento", "A veces", "Regularmente", "Siempre", "Todas las noches y otras prendas de cama se mojan"], index=None),

    "B1.1": st.markdown("30. B1.1 En la últimas dos semanas, ¿con qué frecuencia ha sido molestado por los siguientes problemas?"),

    "B1.1.1": st.radio("31. B1.1.1 Sentirse nervioso, ansioso o tenso?", [
        "Nada", "3 días a la semana", "4 días a la semana", "5-7 días a la semana"], index=None),

    "B1.1.2": st.radio("32. B1.1.2 No poder dejar de preocuparse o controlar la preocupación", [
        "Nada", "3 días a la semana", "4 días a la semana", "5-7 días a la semana"], index=None),

    "B1.1.3": st.radio("33. B1.1.3 Poco interés o placer en hacer cosas", [
        "Nada", "3 días a la semana", "4 días a la semana", "5-7 días a la semana"], index=None),

    "B1.1.4": st.radio("34. B1.1.4 Sentirse deprimido, triste o sin esperanza", [
        "Nada", "3 días a la semana", "4 días a la semana", "5-7 días a la semana"], index=None),

    "B1.2": st.markdown("35. B1.2 Considere qué tan bien describen las siguientes afirmaciones sus comportamientos y acciones"),

    "B1.2.1": st.radio("36. B1.2.1 Busco formas creativas de cambiar situaciones difíciles", [
        "No me describe en absoluto", "No me describe", "Neutral", "Me describe", "Me describe muy bien"], index=None),

    "B1.2.2": st.radio("37. B1.2.2 Independientemente de lo que me suceda, creo que puedo controlar mi reacción ante ello", [
        "No me describe en absoluto", "No me describe", "Neutral", "Me describe", "Me describe muy bien"], index=None),

    "B1.2.3": st.radio("38. B1.2.3 Creo que puedo crecer de manera positiva enfrentando situaciones difíciles", [
        "No me describe en absoluto", "No me describe", "Neutral", "Me describe", "Me describe muy bien"], index=None),

    "B1.2.4": st.radio("39. B1.2.4 Busco activamente formas de reemplazar las pérdidas que encuentro en la vida", [
        "No me describe en absoluto", "No me describe", "Neutral", "Me describe", "Me describe muy bien"], index=None),

    "B2": st.markdown("40. B2 Evaluación de Condiciones Relacionadas con el Sueño"),

    "B2.1": st.multiselect("40. B2.1 Marque las preguntas que ha respondido positivamente", ["Ronca fuerte", "Se siente a menudo cansado, fatigado o somnoliento durante el día", "Alguien ha observado que deja de respirar o se atraganta/ se ahoga durante el sueño",
                                                                                             "Tiene o está siendo tratado por presión arterial alta", "Índice de masa corporal superior a 35", "Edad mayor de 50 años", "Tamaño del cuello grande (43 cm o más para hombres, 41 cm o más para mujeres)", "Género = Masculino", "Ninguno"]),

    "B2.2": st.multiselect("41. B2.2 Indique qué afirmaciones pueden aplicarse a usted", ["Tengo dificultades para conciliar el sueño", "Los pensamientos pasan por mi mente y me impiden dormir", "Anticipo un problema con el sueño varias veces a la semana",
                                                                                          "Me despierto y no puedo volver a dormir", "Me preocupo por cosas y tengo problemas para relajarme", "Me despierto temprano en la mañana antes de lo que me gustaría", "Me quedo despierto durante media hora o más antes de quedarme dormido", "No me pasa"]),

    "B2.3": st.multiselect("42. B2.3 Indique qué afirmaciones pueden aplicarse a usted", ["Aparte del ejercicio, todavía siento tensión muscular en mis piernas", "He notado (o otros han comentado) que partes de mi cuerpo se sacuden durante el sueño", "Me han dicho que pateo por la noche", "Cuando intento dormir, experimento una sensación de dolor o de hormigueo en las piernas",
                                                                                          "Experimento dolor y calambres en las piernas por la noche", "A veces no puedo mantener las piernas quitas por la noche", "Simplemente tengo que moverlas para sentirme cómodo", "A pesar de que dormí durante la noche, me siento somnoliento durante el día", "No me pasa"]),

    "B2.4": st.radio("43. B2.4 ¿Con qué frecuencia duerme boca abajo, basándose en el último mes?", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "B3.1": st.markdown("44. B3.1 ¿Con qué frecuencia realiza cada uno de los hábitos, basándose en el último mes?"),

    "Q7": st.radio("Q7. Mantener la mandíbula adelantada o hacia un lado", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q8": st.radio("45. Q8. Presionar la lengua con fuerza contra los dientes", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q9": st.radio("46. Q9. Colocar la lengua entre los dientes", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q10": st.radio("47. Q10. Morder, masticar o jugar con la lengua, mejillas o labios", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q11": st.radio("48. Q11. Mantener la mandíbula en una posición rígida o tensa, como para empujar o proteger la mandíbula", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q12": st.radio("49. Q12. Sostener objetos entre los dientes o morder objetos como cabello, pipa, lápiz, bolígrafos, dedos, uñas, etc.", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q13": st.radio("50. Q13. Masticar chicle", ["Nunca", "Un poco de veces", "Algunas veces",
                                                 "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q14": st.radio("51. Q14. Tocar un instrumento musical que involucre el uso de la boca o la mandíbula", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q15": st.radio("52. Q15. Apoyarse con la mano en la mandíbula, como sosteniendo o descansando la barbilla en la mano", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q16": st.radio("53. Q16. Masticar alimentos solo de un lado", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q17": st.radio("54. Q17. Comer entre comidas", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q18": st.radio("55. Q18. Hablar de manera sostenida (por ejemplo: profesores, en ventas o atención al cliente)", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q19": st.radio("56. Q19. Cantar", ["Nunca", "Un poco de veces", "Algunas veces",
                                        "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q20": st.radio("57. Q20. Bostezar", ["Nunca", "Un poco de veces", "Algunas veces",
                                          "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "Q21": st.radio("58. Q21. Sostener el teléfono entre la cabeza y los hombros", [
        "Nunca", "Un poco de veces", "Algunas veces", "La mayoría de las veces", "Todas las veces", "No sé"], index=None),

    "B3.2": st.number_input("59. B3.2 Indique el tiempo promedio/día de uso del teléfono inteligente"),

    "B3.3": st.multiselect("60. B3.3 ¿Ha sido diagnosticado o sufre de posibles signos de alguna de las siguientes condiciones?", [
        "Discinesia orofacial", "Distonía oromandibular", "Enfermedad de parkinson", "Enfermedad de huntington", "Síndrome de tourette", "Espasmos hemifaciales", "Discinesia tardía", "NINGUNA"]),

    "B3.4": st.radio("61. B3.4 Evaluación de la enfermedad por reflujo gastroesofágico: Presenta reflujo o acidez estomacal o regurgitacion?", [
        "Sí", "No"], index=None),
}
st.radio("62. B3.4.1 En caso afirmativo con que frecuencia?", [
         "Nunca", "1 dia a la semana", "2-3 dias a la semana", "4-7 dias a la semana"], index=None)

mandatory_fields = {
    "B3.5": st.multiselect("63. B3.5 ¿Ha sido diagnosticado con alguna de las siguientes condiciones?", ["Artritis reumatoide", "Lupus", "Otros trastornos reumáticos sistémicos, incluida la fibromialgia",
                                                                                                         "Otras condiciones sistémicas, incluida la esclerosis sistémica, la polimialgia reumática, la enfermedad mixta del tejido conectivo", "NINGUNA"]),

    "B3.6": st.radio("64. B3.6 ¿Ha sido diagnosticada por trastorno por déficit de atención e hiperactividad?", [
        "No", "Sí"], index=None),

    "B4.3": st.radio("68. B4.3 ¿Fuma o usa productos de tabaco?",
                     ["No", "Sí", "Dejé de fumar"], index=None),
}
st.number_input(
    "69. B4.3.1 En caso afirmativo, ¿cuántos cigarrillos fuma al día?", min_value=0, step=1)

mandatory_fields = {
    "B4.4": st.radio("70. B4.4 ¿Consume bebidas alcohólicas?",
                     ["No", "Sí", "Dejé de beber"], index=None)
}
st.number_input(
    "71. B4.4.1 En caso afirmativo, ¿cuál es su ingesta aproximada de estas bebidas alcohólicas (vaso/día)?", min_value=0, step=1)

mandatory_fields = {
    "B4.5": st.radio("72. B4.5 ¿Bebe regularmente bebidas carbonatadas (cola, RedBull, Sprite, Fanta)?", [
        "No", "Sí", "Dejé de beber"], index=None)
}
st.number_input(
    "73. B4.5.1 En caso afirmativo, ¿cuál es su ingesta aproximada (vasos/día)?", min_value=0, step=1)

mandatory_fields = {
    "B4.6": st.radio("74. B4.6 ¿Bebe o come regularmente jugos o frutas cítricas (limón, naranja, toronja)?", [
        "No", "Sí", "Dejé de beber"], index=None)
}
st.number_input(
    "75. B4.6.1 En caso afirmativo, ¿Cuál es su ingesta aproximada (vasos o cantidad/día)?", min_value=0, step=1)

mandatory_fields = {
    "B4.7": st.radio("76. B4.7 ¿Bebe regularmente café, té u otras bebidas con cafeína?", [
        "No", "Sí", "Dejé de beber"], index=None)
}
st.number_input(
    "77. B4.7.1 En caso afirmativo, ¿Cuál es su ingesta aproximada (tazas/día)?", min_value=0, step=1)

mandatory_fields = {
    "B5.1": st.radio("78. B5.1 ¿Sabe de alguien en su familia (padre, madre, hijos) que haya tenido algún historial de bruxismo?", [
        "No", "Sí", "No lo sé"], index=None),

    "B5.2": st.radio("79. B5.2 ¿Sabe de alguien en su familia (padre, madre, hijos) que tenga desgaste dental?", [
        "No", "Sí", "No lo sé"], index=None),

    "B5.3": st.radio("80. B5.3 ¿Sabe de alguien en su familia (padre, madre, hijos) que tenga apnea del sueño?", [
        "No", "Sí", "No lo sé"], index=None),

    "B5.4": st.radio("81. B5.4 ¿Sabe de alguien en su familia (padre, madre, hijos) que tenga dolor facial no dental?", [
        "No", "Sí", "No lo sé"], index=None),

    "B5.5": st.radio("82. B5.5 ¿Sabe de alguien en su familia (padre, madre, hijos) que tenga enfermedad por reflujo gastroesofágico?", [
        "No", "Sí", "No lo sé"], index=None)
}
# Submit button with validation
if st.button("Enviar respuestas"):
    missing_fields = [key for key,
                      value in mandatory_fields.items() if not value]

    if missing_fields:
        st.warning(
            f"⚠️ Por favor, responde todas las preguntas obligatorias antes de enviar: {', '.join(missing_fields)}")
    else:
        st.success("¡Gracias por completar el cuestionario!")
