from pptx import Presentation
import streamlit as st
from io import BytesIO
import subprocess
import sys
import script

prs = script.create_ppt("Q4-22")


# save the output into binary form
binary_output = BytesIO()
prs.save(binary_output) 

st.download_button(label = 'Download ppw',
                   data = binary_output.getvalue(),
                   file_name = 'my_power.pptx')	