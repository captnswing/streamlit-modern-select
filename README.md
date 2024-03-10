# streamlit-modern-select

Streamlit component that allows you to display a selectbox with size >= 1

## Installation instructions

```sh
pip install streamlit-modern-select
```

## Usage instructions

```python
import streamlit as st
from streamlit_modern_select import streamlit_modern_select

options = ["a", "b", "c", "d", "e"]
value = streamlit_modern_select(options, size=3)
st.write(f"You selected {value}")
```
