import streamlit as st
st.title("Mobile app")
st.subheader("hello here we are") 
st.text("welcome here")
st.write("choose your favorite color")
color= st.selectbox("your fav color:", ["green","blue","white"])
## how to use the variable 
st.write(f"you choose :{color}.beautiful color")
st.success("you choose color successfully")
## button 
if st.button("make food"):
    st.success("your food started preparing")
    ##checkbox
add_salt=st.checkbox("add the salt")
if add_salt:
    st.write("salt added in the food")
    ## radio button
salt_type=st.radio("pick the salt type in it: ",["sweet","salty",
"wonder"  ])    
st.write(f"selected the {salt_type} in it")
## select box
fruit= st.selectbox("choose fruits:" ,["apple","bnana","mango"])
st.write(f"selected one: {fruit} in it")
## slider
heat_level=st.slider("so heat level", 2 ,7 ,6)
st.write(f"selected level {heat_level} in these")
## with input
temp_level=st.number_input("how much" , min_value=1,
max_value=23 , step=1)
st.write(f"selected sugar level {temp_level} in these ")
## text input
name=st.text_input("enter your name")
if name:
    st.write(f"welcome here Mr. {name}")
    ## date input dob
dob=st.date_input("slect your DOB")  
st.write(f"selected DOB level {dob}")  
    

