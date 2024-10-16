import pickle
import streamlit as st
import pandas as pd

# Function for recommending books
def recommend(book, books, similarity):
    index = books[books['original_title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_book_names = []
    recommend_book_posters = []
    
    for i in distances[1:11]:
        recommend_book_names.append(books.iloc[i[0]].original_title)
        recommend_book_posters.append(books.iloc[i[0]].image_url)

    return recommend_book_names, recommend_book_posters

# Main function to handle the BookPal recommendation logic
def book_recommendation():
    # Load the books data and similarity model
    with open('./models/books_list.pkl', 'rb') as f:
        books = pd.read_pickle(f)

    with open('./models/book_similarity.pkl', 'rb') as f:
        similarity = pd.read_pickle(f)

    # Dropdown to select a book from the list
    book_list = books['original_title'].values
    selected_book = st.selectbox("Enter The Book's Name", book_list)

    # Button to show book recommendations
    if st.button('Show Recommendations'):
        st.divider()
        
        recommended_book_names, recommended_book_posters = recommend(selected_book, books, similarity)

        # Columns with horizontal padding
        col1, col2, col3, col4, col5 = st.columns(5)
        _, _, _, _, _ = st.columns(5)
        col6, col7, col8, col9, col10 = st.columns(5)

        # Display image and text of each recommended book
        for i in range(1, 11):
            with eval(f'col{i}'):
                st.image(recommended_book_posters[i-1])
                st.write(recommended_book_names[i-1])

        with _:
            st.write("#")
