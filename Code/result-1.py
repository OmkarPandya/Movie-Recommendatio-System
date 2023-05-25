import pickle

import pandas as pd
import streamlit as st


def Recommend_Movies(movie):
    Mv_Indx = Mvs[Mvs['title'] == movie].index[0]
    Dstncs = Smlrt[Mv_Indx]
    Mvs_Lst = sorted(list(enumerate(Dstncs)), reverse=True, key=lambda x: x[1])[1:6]

    # enumerate to store the movie indexes, list to create list of tuples, sorted reverse to
    # sort in descending order, key to sort according to distances and not the indices, [1:6] to suggest 5 most
    # similar movies

    Movies_Recommended = []
    for n in Mvs_Lst:
        Mv_ID = n[0]
        Movies_Recommended.append(Mvs.iloc[n[0]].title)

    return Movies_Recommended


Mv_Dict = pickle.load(open('mv_dict.pkl', 'rb'))
Mvs = pd.DataFrame(Mv_Dict)

Smlrt = pickle.load(open('Smlrt.pkl', 'rb'))

st.title('Movie Recommendation System')

Mv_Ttl = st.selectbox(
    'Select Movie of your choice',
    Mvs['title'].values

)

if st.button('Recommend'):
    Recommendations = Recommend_Movies(Mv_Ttl)
    'Based on your choice of movie, you may like the following movies :-'
    ''
    j = 1
    for i in Recommendations:
        st.write(j, i)
        j = j + 1
