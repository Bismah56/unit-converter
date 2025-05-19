import streamlit as st # type: ignore

def convert_units(value: float, unit_from: str, unit_to: str):

    # 1 kilometer = 1000 m
    # 1 meter = 0.001 km
    # 1 kilogram = 1000 g
    # 1 gram = 0.001 kg

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value / 1000
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value / 1000
    else:
        return "Conversion is not supported"

def main():
    st.title("Unit converter")
    st.write("Welcome to Unit converter!")
    value = st.number_input("Enter the value you want to convert:", min_value=0.0)
    unit_from = st.text_input("Enter the value you want to convert from (eg. meters, kilometers, grams, kilograms):")
    unit_to = st.text_input("Enter the value you want to from conversion (eg. meters, kilometers, grams, kilograms):")

    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write(f"**Converted value is:** {result}")

main()