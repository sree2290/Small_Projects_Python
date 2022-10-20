import streamlit as st
st.title('Flames Calculator')

title = st.text_input('Your Name')
title2 = st.text_input("Crush Name")

def Flames(name1,name2):
    namestr = name1 + name2

    for c in namestr:
        if namestr.count(c) != 1:
            # counting common letters
            namestr = namestr.replace(c,"")

    # print("FLAMES....")


    number = len(namestr) % 6
    rel = ""

    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection "
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 0:
        rel += "Siblings"
    else:
        pass

    return rel

if st.button('Check'):
    st.title(Flames(title,title2))

st.text("                ")
st.text("                ")
st.text("                ")
st.text("                ")
st.text("                ")
st.text("                ")

st.text('Made with Love <3')
