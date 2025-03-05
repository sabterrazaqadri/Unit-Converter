import streamlit as st

# Function to handle conversion
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "meters": {"kilometers": 0.001, "centimeters": 100, "feet": 3.28084, "inches": 39.3701},
        "kilometers": {"meters": 1000, "miles": 0.621371},
        "miles": {"kilometers": 1.60934, "meters": 1609.34},
        "grams": {"kilograms": 0.001, "pounds": 0.00220462},
        "kilograms": {"grams": 1000, "pounds": 2.20462},
        "pounds": {"grams": 453.592, "kilograms": 0.453592},
        "celsius": {"fahrenheit": lambda c: (c * 9/5) + 32, "kelvin": lambda c: c + 273.15},
        "fahrenheit": {"celsius": lambda f: (f - 32) * 5/9, "kelvin": lambda f: (f - 32) * 5/9 + 273.15},
        "kelvin": {"celsius": lambda k: k - 273.15, "fahrenheit": lambda k: (k - 273.15) * 9/5 + 32}
    }
    
    if from_unit in conversion_factors and to_unit in conversion_factors [from_unit]:
        factor = conversion_factors[from_unit][to_unit]
        return factor(value) if callable(factor) else value * factor
    else:
        return None
    
# Ap UI
st.title("SRQ Unit Converter")    

categories = {
    "Length": ["meters", "kilometers", "miles", "centimeters", "feet", "inches"],
    "Weight": ["grams", "kilograms", "pounds"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"]
} 

category = st.selectbox("Select Category", list(categories.keys()))
from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Conversion Not Supported")