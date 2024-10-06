from GoogleNews import GoogleNews
import streamlit as st

inp_query = st.text_input("Enter the query:")
googlenews = GoogleNews()
googlenews.search(inp_query)
result = googlenews.result()
if st.button("Search News"):    
    for news in result[:2]:  # Show only top 2 results
        st.write(f"**Title:** {news['title']}")    