import streamlit as st
import numpy as np


st.title('Multiplica números')

a=st.selectbox('digite o primeiro número: ',np.arange(1,11))
b=st.selectbox('digite o segundo número: ',np.arange(1,11))
c=st.write('o resultado é : {}'.format(a*b))
