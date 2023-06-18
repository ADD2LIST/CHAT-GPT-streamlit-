import streamlit as st

st.title("m3u8 Link Player")

# Input field for m3u8 link
m3u8_link = st.text_input("Enter m3u8 link:")

# Input field for m3u8 playlist link
playlist_link = st.text_input("Enter m3u8 playlist link:")

# Validate and display the video player for m3u8 link
if m3u8_link:
    st.video(m3u8_link)

# Validate and display the video player for m3u8 playlist link
if playlist_link:
    st.video(playlist_link)
    
