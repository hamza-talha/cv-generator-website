from streamlit.elements import dataframe_selector
from cv import display_data
from os import name
from typing import Text
from google.protobuf.reflection import ParseMessage
from pkg_resources import split_sections
from pathlib import Path
import sqlite3
from sqlite3 import Connection
import streamlit as st
import pandas as pd
import numpy as np
from streamlit.elements.color_picker import ColorPickerMixin
import base64
import streamlit.components.v1 as components
from pandas import option_context
st.set_page_config(layout="wide")
st.markdown('<p class="big-font">CURRICULAM  VITAE</p><br><br><br><br>', unsafe_allow_html=True)
col1, col2 = st.columns(2)


st.markdown("""
<style>
.big-font {
    font-size:70px !important;
    color:purple;
    font-weight:1000;
    text-align:centre;
    margin-left: 200px;
}
.ham {
    font-size:50px ;
    font-weight:500;
    
    color:grey;
    font_weight:1000;
    
}
.sad {
    
    background-color: #3CBC8D;
    
}
.line{
    height: 700px;
    
    border-right: 5px solid white;
    position: absolute;
    right:100%;
}

</style>
""", unsafe_allow_html=True)


with col1:
          
             
       
      
 
       Name=st.markdown("""<form> <p for="name"</p><br> <input id="name" name="name" style="width: 300px;" style="color: red;" type="text" placeholder="Enter Your Name Here"> </form>""", unsafe_allow_html=True)

       st.title("Education:")

       menue=['For school','For college','For universty']
       choice=st.sidebar.selectbox("",menue)

       if choice == "For school":
          school=st.text_input("SCHOOL Education")    
       elif choice == "For college": 
          school=st.text_input("SCHOOL Education")        
          college=st.text_input("COLLEGE Education")
       elif choice == "For universty" :

          school=st.text_input("SCHOOL Education:")        
          college=st.text_input("COLLEGE Education:")
          universty=st.text_input("UNIVERSTY Education:")  

       st.title("Work Experience")
       menue=['cv for education','cv for job']
       choice=st.sidebar.selectbox("",menue)

       if choice == "cv for education":
            work=st.text_input(" ")   
       elif choice == "cv for job":
           
            company=st.text_input("ENTER COMPANY NAME:")
       men=['work experience','1','2','3','4']    
       ice=st.sidebar.selectbox("     ",men)
       if ice == 'work experience':
            work_experience=st.text_area("  ")
       elif ice == '1':
            work_experience1=st.text_area(" ")  
            work_experience2=st.text_input("  ")  
       elif ice == '2':
            work_experience1=st.text_input("                                  ")   
            work_experience2=st.text_input("                                      ")
            work_experience3=st.text_input("      ")    
       elif ice == '3':
            work_experience1=st.text_input("        ")   
            work_experience2=st.text_input("         ")    
            work_experience3=st.text_input("          ")
            work_experience4=st.text_input("            ")
       elif ice == '4':
            work_experience1=st.text_input("              ")   
            work_experience2=st.text_input("                ")    
            work_experience3=st.text_input("                   ")
            work_experience4=st.text_input("                     ")
            work_experience5=st.text_input("                       ")    

       st.title("SKILLS")

       menu=['skills','1','2','3','4']
       chice=st.sidebar.selectbox(" ",menu)
       if chice == 'skills':
            skill1=st.text_input("                              ")
       elif chice == '1':
            skill1=st.text_input("                                ")  
            skill2=st.text_input("                                  ")  
       elif chice == '2':
            skill1=st.text_input("                                    ")   
            skill2=st.text_input("                                         ")
            skill3=st.text_input("                                           ")    
       elif chice == '3':
            skill1=st.text_input("                                              ")   
            skill2=st.text_input("                                                  ")    
            skill3=st.text_input("                                                     ")
            skill4=st.text_input("                                                       ")
       elif chice == '4':
            skill1=st.text_input("                                                          ")   
            skill2=st.text_input("                                                             ")    
            skill3=st.text_input("                                                               ")
            skill4=st.text_input("                                                                 ")
            skill5=st.text_input("                                                                   ")

       date=st.date_input('Date:')

          

with col2:
           
        
         st.write('<p class="ham">PERSONAL INFORMATION</p>', unsafe_allow_html=True)
         
         st.write(""" <p class="line"> </p>""", unsafe_allow_html=True)

         email=st.write("""<form> <p>Email Address:</p> <input id="email" name="email" style="width: 300px; type="email" placeholder="name@example.com"> </form> <BR>""", unsafe_allow_html=True)

         location=st.write("""<P>Home Address: </P> <P><textarea rows="4" cols="30" placeholder="Enter your current home address here...."></textarea></p>""",unsafe_allow_html=True)

         contact=st.write("""<form> <p>Contact Number:</p></label> <input id="email" name="email" style="width: 200px; type="integer" placeholder="0000-0000000"></form><br>""", unsafe_allow_html=True)

         
         D_O_B=st.write("""<p>Date Of Birth:</p></label> <input id="D_O_B" name="D_O_B" style="width: 200px; type="integer" placeholder="00-00-0000"> </form>""", unsafe_allow_html=True)
         st.write(""" <br><p>select your Gender: """, unsafe_allow_html=True)
         gender=st.selectbox('', ('Male', 'Female'))

 
st.sidebar.write("for download or print press ctrl+p and save your cv.")   
    
         