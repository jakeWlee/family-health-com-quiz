import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Coping Style Quiz", page_icon="🧠")

st.title("🧠 Mental Health Coping Style Quiz")
st.write("""
Answer the following 10 questions to discover your primary 'Coping Persona.' 
There are no wrong answers—just different ways of processing the world.
""")

# --- HOMEY THEME (Minimal CSS) ---
# This small block changes the background to a warm cream 
# and the text to a softer dark brown/grey.
st.markdown("""
    <style>
    .stApp {
        background-color: #FFFDF5; /* Warm Cream Background */
    }
    h1, h2, h3, p, div, label, span {
        color: #4E342E !important; /* Dark Coffee Text */
    }
    div.stButton > button {
        background-color: #8D6E63; /* Earthy Brown Button */
        color: white !important;
        border-radius: 8px;
    }
    div.stButton > button:hover {
        background-color: #6D4C41;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("---")

# --- DATA: QUESTIONS & ANSWERS ---
# Each question has a 'text' and a list of 'options'.
# Each option is a dictionary with the 'answer' text and the assigned 'type'.
quiz_data = [
    {
        "question": "1. Something upsetting just happened. What’s your immediate instinct?",
        "options": [
            {"text": "Put on headphones, start working, or find something to take your mind off it.", "type": "Active Distractor"},
            {"text": "Call a friend or partner immediately to vent and let the feelings out.", "type": "Expressive Connector"},
            {"text": "Analyze the situation to find the root cause and fix it.", "type": "Pragmatic Strategist"},
            {"text": "Retreat to a quiet space to think through what happened alone.", "type": "Introspective Observer"},
        ]
    },
    {
        "question": "2. A friend comes to you in tears. How do you react?",
        "options": [
            {"text": "You listen quietly and offer a calm presence, but don't say much.", "type": "Introspective Observer"},
            {"text": "You listen, but your mind goes straight to offering advice or solutions.", "type": "Pragmatic Strategist"},
            {"text": "You try to cheer them up with a joke or suggest doing an activity to distract them.", "type": "Active Distractor"},
            {"text": "You empathize deeply, hug them, and validate their pain.", "type": "Expressive Connector"},
        ]
    },
    {
        "question": "3. You’re feeling anxious before a big event. What do you do?",
        "options": [
            {"text": "Check the logistics, make a checklist, and prepare so nothing goes wrong.", "type": "Pragmatic Strategist"},
            {"text": "Scroll social media or keep yourself incredibly busy until the event starts.", "type": "Active Distractor"},
            {"text": "Talk to someone about how nervous you are to feel less alone.", "type": "Expressive Connector"},
            {"text": "Find a corner to meditate, breathe, or visualize the outcome privately.", "type": "Introspective Observer"},
        ]
    },
    {
        "question": "4. You’re arguing with a partner or family member. What is your style?",
        "options": [
            {"text": "You express exactly how their actions made you feel emotionally.", "type": "Expressive Connector"},
            {"text": "You shut down and go silent; you need to process your thoughts before speaking.", "type": "Introspective Observer"},
            {"text": "You try to change the subject or walk away to avoid the tension.", "type": "Active Distractor"},
            {"text": "'Let’s stick to the facts.' You want to solve the disagreement logically.", "type": "Pragmatic Strategist"},
        ]
    },
    {
        "question": "5. Someone you trust asks, 'How are you really doing?'",
        "options": [
            {"text": "You deflect with humor: 'Living the dream! Anyway, how are you?'", "type": "Active Distractor"},
            {"text": "You give a status report: 'Stressed, but I'm handling it by doing X and Y.'", "type": "Pragmatic Strategist"},
            {"text": "You say, 'I'm okay,' because you prefer to keep your inner world private.", "type": "Introspective Observer"},
            {"text": "You answer honestly and vulnerably, potentially tearing up.", "type": "Expressive Connector"},
        ]
    },
    {
        "question": "6. You find yourself crying or feeling overwhelmed. How do you handle it?",
        "options": [
            {"text": "You analyze why you are crying and journal or reflect on the trigger.", "type": "Introspective Observer"},
            {"text": "You wipe your face immediately and find a task to do so you don't dwell on it.", "type": "Active Distractor"},
            {"text": "You feel frustrated by the loss of control and try to 'pull yourself together.'", "type": "Pragmatic Strategist"},
            {"text": "You lean into it—crying is a natural release and you feel better after.", "type": "Expressive Connector"},
        ]
    },
    {
        "question": "7. You’re stuck in a 'rut' or feeling low. What gets you out of it?",
        "options": [
            {"text": "Connection. Spending quality time with people who love you.", "type": "Expressive Connector"},
            {"text": "Stimulation. Starting a new video game, binge-watching a show, or a night out.", "type": "Active Distractor"},
            {"text": "Action. Cleaning the house, hitting the gym, or reorganized your calendar.", "type": "Pragmatic Strategist"},
            {"text": "Solitude. Time alone in nature or a quiet room to recharge your battery.", "type": "Introspective Observer"},
        ]
    },
    {
        "question": "8. You accomplished something huge! How do you celebrate?",
        "options": [
            {"text": "Feel a quiet sense of pride and enjoy a peaceful evening.", "type": "Introspective Observer"},
            {"text": "Review the success, acknowledge the win, and set the next goal.", "type": "Pragmatic Strategist"},
            {"text": "Throw a party or call everyone to share the excitement.", "type": "Expressive Connector"},
            {"text": "Enjoy the adrenaline rush for a moment, then move on to the next thrill.", "type": "Active Distractor"},
        ]
    },
    {
        "question": "9. What is your biggest 'Red Flag' that your mental health is slipping?",
        "options": [
            {"text": "You feel physically exhausted or engage in risky/impulsive behavior.", "type": "Active Distractor"},
            {"text": "You withdraw completely and stop answering texts or interacting.", "type": "Introspective Observer"},
            {"text": "You feel needy, over-sensitive, or unable to self-soothe without others.", "type": "Expressive Connector"},
            {"text": "You become rigid, obsessive about details, or overly controlling.", "type": "Pragmatic Strategist"},
        ]
    },
    {
        "question": "10. Ideally, how do you view mental health?",
        "options": [
            {"text": "It’s about being open, vulnerable, and connected to others.", "type": "Expressive Connector"},
            {"text": "It’s a deeply personal journey of self-awareness and understanding.", "type": "Introspective Observer"},
            {"text": "It’s about resilience and pushing forward despite the difficulties.", "type": "Active Distractor"},
            {"text": "It’s something to be managed and optimized through good habits.", "type": "Pragmatic Strategist"},
        ]
    }
]

# --- COLLECT USER ANSWERS ---
user_answers = {}

for i, q_data in enumerate(quiz_data):
    st.subheader(q_data["question"])
    # We use just the text for the radio button labels
    options_text = [opt["text"] for opt in q_data["options"]]
    choice = st.radio(f"Select an option for Question {i+1}:", options_text, key=f"q{i}")
    
    # Map the chosen text back to its type
    # (We look through the options list to find the type associated with the selected text)
    for opt in q_data["options"]:
        if opt["text"] == choice:
            user_answers[i] = opt["type"]

st.markdown("---")

# --- CALCULATE & SHOW RESULTS ---
if st.button("Get Your Result"):
    
    # 1. Tally the scores
    scores = {
        "Pragmatic Strategist": 0,
        "Expressive Connector": 0,
        "Introspective Observer": 0,
        "Active Distractor": 0
    }

    for answer_type in user_answers.values():
        scores[answer_type] += 1

    # 2. Find the winner
    # (This logic picks the highest score. If there is a tie, it picks the first one encountered)
    winner = max(scores, key=scores.get)
    
    # 3. Display the Result
    st.success(f"Your dominant style is: **{winner}**")
    
    # 4. Custom Descriptions
    if winner == "Pragmatic Strategist":
        st.header("🔧 The Pragmatic Strategist")
        st.write("""
        **"Let's fix this."**
        You view mental health as a puzzle to be solved. You value logic, routine, and action plans. 
        When things get tough, you research solutions, make to-do lists, and focus on 'doing' rather than just 'feeling.'
        
        **Your Strength:** Resilience and high-functioning capability during crises.
        **Your Challenge:** You risk intellectualizing your feelings rather than processing them, which can lead to burnout.
        """)
        
    elif winner == "Expressive Connector":
        st.header("🤝 The Expressive Connector")
        st.write("""
        **"I need to talk about this."**
        You process emotions through connection. You prioritize vulnerability and feel safest when you can share your burden with others.
        You are often the person your friends turn to because you are an excellent listener.
        
        **Your Strength:** You de-stigmatize emotions and build strong support networks.
        
        **Your Challenge:** You can become dependent on external validation to feel better.
        """)
        
    elif winner == "Introspective Observer":
        st.header("🧘 The Introspective Observer")
        st.write("""
        **"I need some time alone."**
        You process things internally. You value privacy, solitude, and deep reflection. 
        You don't run from your feelings, but you prefer to understand them fully in private before sharing them with the world.
        
        **Your Strength:** Deep self-awareness and the ability to self-soothe.
        **Your Challenge:** You risk isolating yourself; people may assume you are fine when you are actually struggling.
        """)
        
    elif winner == "Active Distractor":
        st.header("🚀 The Active Distractor")
        st.write("""
        **"Keep moving forward."**
        You deal with difficult emotions by staying in motion. Whether it's work, hobbies, or social events, you prefer to keep busy.
        You are often high-energy and productive, using activity to keep anxiety at bay.
        
        **Your Strength:** You are great at compartmentalizing and getting things done even when life is hard.
        **Your Challenge:** If you never slow down to feel, the emotions may eventually catch up to you in a crash.
        """)

    # Optional: Show the breakdown
    with st.expander("See your score breakdown"):
        st.write(scores)
