
import streamlit as st
import pickle
import requests



st.set_page_config(layout="wide", page_icon="🎬",page_title="Movie recommender")
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movies_title=movies['title'].values

st.title('Movie Reccomender System')
st.subheader('Reccomends movie based on content')

def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=708a09b5a0ab52661997cc2b1070ecad&language=en-US'.format(movie_id))
    data=response.json()
    if data['poster_path']==None:
        return data['poster_path']
    else:
         return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    cos_distance=similarity[movie_index] 
    # after this we will sort the similarity with their index and then we will reccommend top 20 similar movies
    movies_list=sorted(list(enumerate(cos_distance)),reverse=True,key=lambda x:x[1])
    movies_list=movies_list[1:11]

    recommended=[]
    recommended_posters=[]
    movie_overview=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id #movies id which are recommended is stored in movie_id to fetch their posters
        
        recommended.append(movies.iloc[i[0]].title)
          #fetching posters from API
        movie_overview.append(movies.iloc[i[0]].overview)
        recommended_posters.append(poster(movie_id))
        # recommended_posters
        # poster(movie_id)
    return recommended,recommended_posters,movie_overview

selected_movie=st.selectbox("enter movie name",movies_title)

if st.button ("Recommend movies"):
    
    recommendations,posters,overview=recommend(selected_movie)
     
    st.subheader("These are the top 10 similar movies related to your search:")
    
    col1,col2,col3,col4=st.columns(4)
    with col1:
        if posters[0]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[0])
        st.write(recommendations[0])
        with st.expander("Overview",expanded=False):
            st.info(overview[0])
    with col2:
        if posters[1]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[1])
        st.write(recommendations[1])
        with st.expander("Overview",expanded=False):
            st.success(overview[1])
    with col3:
        if posters[2]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[2])
        st.write(recommendations[2])
        with st.expander("Overview",expanded=False):
            st.warning(overview[2])
    with col4:
        if posters[3]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[3])
        st.write(recommendations[3])
        with st.expander("Overview",expanded=False):
            st.error(overview[3])
    col5,col6,col7,col8=st.columns(4)
    with col5:
        if posters[4]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[4])
        st.write(recommendations[4])
        with st.expander("Overview",expanded=False):
            st.success(overview[4])
    with col6:
        if posters[5]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[5])
        st.write(recommendations[5])
        with st.expander("Overview",expanded=False):
            st.error(overview[5])
    with col7:
        if posters[6]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[6])
        st.write(recommendations[6])
        with st.expander("Overview",expanded=False):
            st.info(overview[6])
    with col8:
        if posters[7]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[7])
        st.write(recommendations[7])
        with st.expander("Overview",expanded=False):
            st.warning(overview[7])
    col9,col10,col11,col12=st.columns(4)
    with col9:
        
        if posters[8]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[8])
        st.write(recommendations[8])
        with st.expander("Overview",expanded=False):
            st.warning(overview[8])
    with col10:
        if posters[9]==None:
            st.image("images.png",width=255)
        else:
            st.image(posters[9])
        st.write(recommendations[9])
        with st.expander("Overview",expanded=False):
            st.success(overview[9])
   
   