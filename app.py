import streamlit as st
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
