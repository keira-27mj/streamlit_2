import streamlit as st
import pandas as pd 
import numpy as np

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit application.")
st.button("Click me!")

nombre = st.text_input("Enter your name:")

st.write(f"Hello, {nombre}!")

st.header("This is a header")
st.subheader("This is a subheader")

st.markdown("This is a **markdown** text with *italic* and **bold** formatting.")
st.latex(r"E = mc^2")

st.code("""
  def hello_world():
      print("Hello, World!")      

""")

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")

st.dataframe({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})

st.line_chart({
    'data': [1, 3, 2, 4, 3, 5]
})  
st.bar_chart({
    'data': [1, 2, 3, 4, 5]
})
st.map({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.41, -122.42]
})

# sidebar: ver a la izquierda:
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar content.")

with st.sidebar:
    st.header("Sidebar Header")
    st.button("Sidebar Button")


x = st.slider("Select a value:", 0, 100, 50)
st.write(f"You selected: {x}")

st.checkbox("Check me out!")

st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])

st.selectbox("Select an item:", ["Item 1", "Item 2", "Item 3"])

st.multiselect("Select multiple items:", ["Item A", "Item B", "Item C"])            

st.date_input("Select a date:")

st.time_input("Select a time:")

st.file_uploader("Upload a file:")

# st.progress(70)

# st.balloons()

st.success("This is a success message.")
st.info("This is an info message.")

col1, col2 = st.columns(2)
with col1:
    x2 = st.slider("Select a value in column 1:", 0, 100, 25)
    
with col2:
    st.write(f"You selected: {x2}")
    
# chart_data = =pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
chart_data = pd.DataFrame(
    {
        'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'b': [5, 3, 6, 2, 7, 4, 8, 1, 9, 0, 11, 13, 12, 14, 15, 16, 18, 17, 19, 20],
        'c': [2, 4, 1, 3, 5, 7, 6, 8, 10, 9, 12, 11, 14, 13, 15, 17, 16, 18, 20, 19]
    }
)

st.line_chart(chart_data)
st.error("This is an error message.")

st.warning("This is a warning message.")  


# st.spinner("Loading..."):
#     import time
#     time.sleep(2)   
# st.success("Operation completed successfully!")


# corro el código desde el terminal con:
# streamlit run streamlit_app.py
  
