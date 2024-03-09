import streamlit as st
from modern_select import modern_select

flowers = [
    "Rose",
    "Tulip",
    "Daisy",
    "Orchid",
    "Lily",
    "Sunflower",
    "Daffodil",
    "Hyacinth",
    "Iris",
    "Peony",
]
names = [
    "Oliver Hansen",
    "Van Henry",
    "April Tucker",
    "Ralph Hubbard",
    "Omar Alexander",
    "Carlos Abbott",
    "Miriam Wagner",
    "Bradley Wilkerson",
    "Virginia Andrews",
    "Kelly Snyder",
]
st.subheader("Component with constant args")
selected_value = modern_select(options=flowers)
st.markdown(f"You've clicked {selected_value}")

st.markdown("---")

st.subheader("Component with variable args")
selected_value = modern_select(options=names, size=9)
st.markdown(f"You've clicked {selected_value}")
