import streamlit as st  # Importing the Streamlit library

#X1
# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
st.header("Section 1")  # Adds a section header — good for breaking content into parts
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
st.text("Simple text")  # Displays plain, unformatted text — like a basic message
st.markdown("**Bold** and *italic* text")  # Markdown lets you add simple formatting like bold and italics

# Display data
st.write("Automatic data display")  # Streamlit's flexible method — handles strings, numbers, dataframes, and more
st.code("print('Hello World')", language='python')  # Nicely formats code blocks with syntax highlighting
st.latex(r"\int_{a}^{b} x^2 dx")  # Renders LaTeX math formulas — great for equationscd

#X2
# Section 2 with unique keys
st.header("Section 2")
name = st.text_input("Enter your name", "John Doe", key="name_input")
description = st.text_area("Description", "Write something...", key="description_area")

# Numeric input with unique keys
age = st.number_input("Age", min_value=0, max_value=120, value=25, key="age_input")
score = st.slider("Score", 0, 100, 50, key="score_slider")

# Selection widgets with unique keys
option = st.selectbox("Choose an option", ["A", "B", "C"], key="option_select")
options = st.multiselect("Multiple options", ["X", "Y", "Z"], key="multi_select")

# Date and time with unique keys
date = st.date_input("Select date", key="date_input")
time = st.time_input("Select time", key="time_input")

# Buttons and checkbox with unique keys
if st.button("Click me", key="action_button"):
    st.write("Button clicked!")
    
if st.checkbox("Show/Hide", key="toggle_checkbox"):
    st.write("Visible content")

#X3

st.header("Section 3")
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

# Expander with unique key
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar with unique key
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"], key="sidebar_select")