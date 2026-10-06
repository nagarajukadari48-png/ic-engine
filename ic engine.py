import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="IC Engine Calculator",
    page_icon="⚙️",
    layout="centered"
)

# Title
st.title("⚙️ IC Engine Calculator")
st.write("Calculate swept volume, engine displacement, and compression ratio.")

st.divider()

# Inputs
st.subheader("Enter Engine Parameters")

bore = st.number_input(
    "Bore Diameter (mm)",
    min_value=0.1,
    value=80.0,
    step=0.1
)

stroke = st.number_input(
    "Stroke Length (mm)",
    min_value=0.1,
    value=100.0,
    step=0.1
)

cylinders = st.number_input(
    "Number of Cylinders",
    min_value=1,
    value=4,
    step=1
)

clearance_volume = st.number_input(
    "Clearance Volume per Cylinder (cc)",
    min_value=0.1,
    value=50.0,
    step=0.1
)

# Calculate button
if st.button("🔢 Calculate", type="primary"):

    # Convert mm to cm
    bore_cm = bore / 10
    stroke_cm = stroke / 10

    # Swept volume per cylinder
    swept_volume = (math.pi / 4) * (bore_cm ** 2) * stroke_cm

    # Total engine displacement
    total_displacement = swept_volume * cylinders

    # Compression ratio
    compression_ratio = (
        swept_volume + clearance_volume
    ) / clearance_volume

    # Results
    st.divider()
    st.subheader("📊 Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Swept Volume / Cylinder",
            f"{swept_volume:.2f} cc"
        )

    with col2:
        st.metric(
            "Engine Displacement",
            f"{total_displacement:.2f} cc"
        )

    st.metric(
        "Compression Ratio",
        f"{compression_ratio:.2f}:1"
    )

    # Detailed calculation
    st.subheader("🧮 Calculation Details")

    st.write(
        f"**Swept Volume per Cylinder:** "
        f"{swept_volume:.2f} cc"
    )

    st.write(
        f"**Total Engine Displacement:** "
        f"{swept_volume:.2f} × {cylinders} = "
        f"{total_displacement:.2f} cc"
    )

    st.write(
        f"**Compression Ratio:** "
        f"({swept_volume:.2f} + {clearance_volume:.2f}) "
        f"/ {clearance_volume:.2f} = "
        f"{compression_ratio:.2f}:1"
    )

st.divider()

st.caption("IC Engine Calculator | Built with Python & Streamlit")

Run cheyyadaniki

First terminal lo:

pip install streamlit


Then file ni app.py ani save chesi:

streamlit run app.py


Browser lo app open avutundi.

Streamlit.io lo deploy cheyyadaniki

Project folder ila undali:

IC-Engine-Calculator/
│
├── app.py
└── requirements.txt


requirements.txt lo:

streamlit


Then GitHub ki upload chesi Streamlit Community Cloud lo New app → repository select → app.py select → Deploy cheyyachu.

Kavali ante next step lo nice professional UI + engine diagram + Brake Power + Torque + BMEP + Thermal Efficiency anni add chesi complete IC Engine Calculator app code kuda prepare chestha.
