import streamlit as st

from song_generator import LyricsGenerator


st.header("Lyrics Generator")
st.text('In the style of Taylor Swift')

song_input = st.text_area('Enter the starting of your song', help='Keep it short: 15-20 words')

part  = st.radio('Chose which part of the song the input represents:', ['Verse 1', 'Intro'])

generate = st.button('Generate Lyrics')

if generate:
    with st.spinner('Generating Lyrics for your song....'):
        rest_of_the_song = LyricsGenerator().run(
            key=st.secrets['OPENAI_API_KEY'], 
            input_lyrics=song_input.strip(), 
            input_verse=part)

    st.text(rest_of_the_song)



