import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Family Narrative Quiz", page_icon="🧬")

st.title("🧬 What Is Your 'Family Narrative' Style?")
st.write("""
Based on the research paper *"Sense-making, Socialization, and Stigma,"* this quiz analyzes 
how your family talked (or didn't talk) about mental health, and what role you play today 
as a result of those stories.
""")

# --- HOMEY THEME (Minimal CSS) ---
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
# Mapped based on the academic themes:
# A -> Caution/Vigilant Historian
# B -> Struggle/Compassionate Contextualizer
# C -> Silence/Cycle Breaker
# D -> Awareness/Genetic Detective

quiz_data = [
    {
        "question": "1. Picture Thanksgiving dinner. Your Aunt brings up a cousin who has been 'acting out.' How does your mom respond?",
        "options": [
            {"text": "She lowers her voice: 'He’s going off the rails just like your grandfather. Stay away from that chaos.'", "type": "Vigilant Historian"},
            {"text": "She sighs: 'He’s been under so much pressure at work and went through that bad breakup. It’s a lot.'", "type": "Compassionate Contextualizer"},
            {"text": "She changes the subject immediately. We don't talk about 'issues' at the dinner table.", "type": "Cycle Breaker"},
            {"text": "She uses it as a teaching moment: 'This is why we all need to take care of our health. Genetics are real.'", "type": "Genetic Detective"},
        ]
    },
    {
        "question": "2. When your parents told you stories about family members with mental illness, what was the 'vibe'?",
        "options": [
            {"text": "The Warning: It was a scary cautionary tale. A 'don't let this happen to you' speech.", "type": "Vigilant Historian"},
            {"text": "The Struggle: It was a story about hardship—like losing a job or a loved one—that triggered their illness.", "type": "Compassionate Contextualizer"},
            {"text": "The Mystery: I only heard bits and pieces. I had to play detective to figure out why Uncle Bob disappeared.", "type": "Cycle Breaker"},
            {"text": "The Biology Class: It was very factual. 'We have high anxiety in our DNA, so watch out for symptoms.'", "type": "Genetic Detective"},
        ]
    },
    {
        "question": "3. The study discusses 'External Attributions' (blaming the situation) vs. 'Internal Attributions' (blaming the person). How does your parent explain their own bad days?",
        "options": [
            {"text": "'I'm just stressed because of *you kids* and work.' (Blaming the stressor)", "type": "Vigilant Historian"},
            {"text": "'I'm feeling overwhelmed because of that thing that happened years ago, so I need a break.' (Contextualizing)", "type": "Compassionate Contextualizer"},
            {"text": "They don't explain. They just lock the bedroom door.", "type": "Cycle Breaker"},
            {"text": "'My brain chemistry is off today, so I need to manage my meds/routine.' (Blaming the illness)", "type": "Genetic Detective"},
        ]
    },
    {
        "question": "4. How did hearing (or not hearing) these family stories make you feel about your *own* mental health?",
        "options": [
            {"text": "Terrified. I feel like I'm walking on eggshells waiting to 'turn into' them.", "type": "Vigilant Historian"},
            {"text": "Empathetic. I realized even my parents are just people trying to figure it out.", "type": "Compassionate Contextualizer"},
            {"text": "Confused/Curious. I had to go to college or the internet to actually learn what mental illness is.", "type": "Cycle Breaker"},
            {"text": "Prepared. I know the signs and symptoms to look for in myself.", "type": "Genetic Detective"},
        ]
    },
    {
        "question": "5. Who is the primary storyteller (or 'Lynchpin') in your family regarding health?",
        "options": [
            {"text": "My Mom. She holds all the warnings, secrets, and judgments.", "type": "Vigilant Historian"},
            {"text": "My Dad (or parent figure). He drops truth bombs about life struggles while we are driving or fishing.", "type": "Compassionate Contextualizer"},
            {"text": "Me. I’m the one dragging the secrets out of them.", "type": "Cycle Breaker"},
            {"text": "It's a group effort, usually involving medical terms and factual updates.", "type": "Genetic Detective"},
        ]
    },
    {
        "question": "6. Finally, what is the biggest lesson you took away from your family's 'Narrative Inheritance'?",
        "options": [
            {"text": "Caution: Mental illness makes people unpredictable, so I need to be careful.", "type": "Vigilant Historian"},
            {"text": "Context: Bad things happen to good people, and that can trigger mental health struggles.", "type": "Compassionate Contextualizer"},
            {"text": "Change: We need to stop hiding things. I'm going to talk about this openly.", "type": "Cycle Breaker"},
            {"text": "Awareness: I have a genetic map of my brain, so I can spot the red flags early.", "type": "Genetic Detective"},
        ]
    }
]

# --- COLLECT USER ANSWERS ---
user_answers = {}

for i, q_data in enumerate(quiz_data):
    st.subheader(q_data["question"])
    options_text = [opt["text"] for opt in q_data["options"]]
    choice = st.radio(f"Select an option for Question {i+1}:", options_text, key=f"q{i}")
    
    for opt in q_data["options"]:
        if opt["text"] == choice:
            user_answers[i] = opt["type"]

st.markdown("---")

# --- CALCULATE & SHOW RESULTS ---
if st.button("Get Your Result"):
    
    # 1. Calculate Scores
    scores = {
        "Compassionate Contextualizer": 0, 
        "Vigilant Historian": 0, 
        "Genetic Detective": 0, 
        "Cycle Breaker": 0
    }
    
    for answer in user_answers.values():
        scores[answer] += 1
    
    # 2. Find the Highest Score
    max_score = max(scores.values())
    
    # 3. Find ALL categories that have that score (Handles Ties)
    winners = [cat for cat, score in scores.items() if score == max_score]
    
    # 4. Display Logic
    if len(winners) == 1:
        st.header(f"You are: {winners[0]}")
    else:
        st.header(f"You are a Mix! ⚖️")
        st.write(f"You have a unique blend of **{len(winners)} styles**.")
        st.markdown("---")

    # 5. Loop through winners and show the cards
    for winner in winners:
        
        if winner == "Compassionate Contextualizer":
            st.info("💙 **The Compassionate Contextualizer**")
            st.write("""
                **Based on the theme of 'Struggle Narratives.'**
                
                Your family stories focused on *why* things happened. You didn't just hear that your aunt was 'crazy'; you heard about the grief, the job loss, or the trauma that led to her depression. 
                
                **Your Narrative Legacy:** You learned the lesson of **Understanding**. You don't judge people for their mental health; you look for the context. You are the friend everyone comes to because you actually listen.
            """)

        elif winner == "Vigilant Historian":
            st.warning("📜 **The Vigilant Historian**") 
            st.write("""
                **Based on the theme of 'Caution Narratives.'**
                
                Your family stories were often cautionary tales. You were told about the 'wild' relative or the 'dangerous' cousin as a warning. 
                
                **Your Narrative Legacy:** You learned the lesson of **Caution**. You might harbor a little bit of fear regarding mental health, but you are also hyper-aware of the consequences of untreated illness. You walk the straight and narrow because you know exactly what happens when you don't.
            """)

        elif winner == "Genetic Detective":
            st.success("🧬 **The Genetic Detective**") 
            st.write("""
                **Based on the lesson of 'MI Awareness.'**
                
                Your family didn't shy away from the facts. You learned early on that mental illness runs in the family, just like blue eyes or high blood pressure.
                
                **Your Narrative Legacy:** You took the lesson of **Awareness** to heart. You aren't scared—you're prepared. You monitor your own mental health and you’re the first one to tell a friend, "Hey, have you thought about seeing a doctor for that?"
            """)

        elif winner == "Cycle Breaker":
            st.error("🔄 **The Cycle Breaker**") 
            st.write("""
                **Based on 'Narrative Intervention.'**
                
                Your family might not have had the best communication skills—maybe there was silence, secrecy, or stigma. But you are flipping the script. 
                
                **Your Narrative Legacy:** You are taking the old stories of silence and turning them into open conversations. You are becoming the new 'Lynchpin' for your family, ensuring the next generation hears stories that validate their feelings rather than shaming them.
            """)

    # Optional: Show the breakdown
    with st.expander("See your score breakdown"):
        st.write(scores)
