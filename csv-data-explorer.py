# Zephaniah Ackah-Blay



# Imports
import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib as plt


# 1. Title and Subheader
st.title('Data Analysis')
st.subheader('Data Analysis using Python & Streamlit')





#2. Upload Dataset
upload = st.file_uploader('Upload Your Dataset (In CSV Format)')

if upload is not None:
    data=pd.read_csv(upload)
    
    

#3. Show Dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())
            
            
#4. Check Datatype of Each Column
if upload is not None:
    if st.checkbox('DataType of Each Column'):
        st.text('DataTypes')
        st.write(data.dtypes)
        
        
#5. Find Shape of Out Dataset(Number of Rows and Number of Columns)
if upload is not None:
    data_shape=st.radio('What Dimension Do You Want to Check?',('Rows','Columns'))
    
    if data_shape == 'Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])

    if data_shape == 'Columns':
        st.text('Number of Rows')
        st.write(data.shape[1])
        
        
#6. Find Null Values in The Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test == True:
        if st.checkbox('Null Values in the dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success('Congratulations!!!, No Missing Values')
        

#7. Find Duplicate Values in the dataset  
if upload is not None:
    test=data.duplicated().values.any()
    if test == True:
        st.warning('This Dataset Contains Some Dupliocate Values')
        dup=st.selectbox('Do You Want To Remove Duplicated Values?',('Select on','Yes', 'No'))
        if dup=='Yes':
            data=data.drop_duplicates()
            st.success('Duplicates Values are Removed')
        if dup=='No':
            st.text('Duplicate Values Were Not Removed')
            
            
            
#8. Get Overall Statistics
if upload is not None:
    if st.checkbox('Summary of The Dataset'):
        st.write(data.describe(include='all'))
        
        
        
#9. About Section

if st.button('About App'):
    st.text('Built With Streamlit')
    st.text('Thanks To Streamlit')
    
    
    
#10. By
if st.checkbox('By'):
    st.success('Zephaniah Ackah-Blay')
    
    
    
    
    
    
    
    
    
    
    