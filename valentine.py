import streamlit as st

st.set_page_config(page_title="A Special Message", page_icon="❤️")

# We are using 'background-image' now to use your Vecteezy link
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/000/273/173/small/Valentines_Day_121_A.jpg");
        background-size: cover;
        background-position: center;
    }}
    
    /* This makes the titles dark red and the white box more solid */
    h1, h2 {{
        color: #8b0000 !important;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.9) !important;
        padding: 15px;
        border-radius: 15px;
    }}

    /* This makes the 'important question' text dark and readable */
    .stMarkdown p {{
        color: #5a0000 !important;
        text-align: center;
        font-weight: bold;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 5px;
        border-radius: 10px;
    }}

    /* This fixes the yellow box text you saw in your screenshot */
    .stAlert p {{
        color: #664d03 !important;
        font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("Hi Soya! ❤️")
st.markdown("## I have an imporant question!")

st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lTQF0ODLLjhza/giphy.gif")

st.write("Will you be my valentine")

col1, col2 = st.columns(2)

with col1:
    if st.button("YES! 😍"):
        st.balloons()
        st.success("YAY! I can't wait! Best Valentine's ever! 🌹✨")

with col2:
    if st.button("No 😢"):
        st.warning("Error: This button is broken. Please try the other one!")
