import streamlit as st

st.title("Family Health Reflection (Prototype)")

st.write("Choose the option that best matches your family:")

choice = st.radio(
    "Which communication style feels most like your family?",
    [
        "We avoid talking about health",
        "We talk openly and emotionally",
        "We only talk when something is serious",
        "We use humor to deal with health stuff"
    ]
)

if st.button("Get Your Result"):
    if choice == "We avoid talking about health":
        st.header("Your Result: The Quiet Strength Family")
        st.write("Your family supports each other through actions more than words.")
    
    elif choice == "We talk openly and emotionally":
        st.header("Your Result: The Heart-on-Sleeve Family")
        st.write("Your family uses emotional expression to cope and connect.")
    
    elif choice == "We only talk when something is serious":
        st.header("Your Result: The Pragmatic Family")
        st.write("Your family balances independence with responsibility.")
    
    elif choice == "We use humor to deal with health stuff":
        st.header("Your Result: The Humor-Heals Family")
        st.write("Your family relies on laughter as a coping mechanism.")
