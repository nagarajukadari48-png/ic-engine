import streamlit as st
import math

st.title("IC Engine Calculator")

bore = st.number_input("Bore (mm)", value=80.0)
stroke = st.number_input("Stroke (mm)", value=100.0)
cyl = st.number_input("Cylinders", value=4, step=1)
cv = st.number_input("Clearance Volume (cc)", value=50.0)

if st.button("Calculate"):
    bore_cm = bore / 10
    stroke_cm = stroke / 10

    swept = (math.pi / 4) * bore_cm**2 * stroke_cm
    displacement = swept * cyl
    compression = (swept + cv) / cv

    st.write("Swept Volume:", round(swept, 2), "cc")
    st.write("Engine Displacement:", round(displacement, 2), "cc")
    st.write("Compression Ratio:", round(compression, 2), ":1")
