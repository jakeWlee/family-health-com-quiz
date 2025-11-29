import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="The Wounded Storyteller Quiz", page_icon="📖")

st.title("📖 What Is Your Illness Narrative Style?")
st.write("""
Sociologist Arthur Frank (*The Wounded Storyteller*) identified three main ways people tell the story of their health struggles. 
These aren't "good" or "bad"—they are maps of how we make sense of pain. 

**Take this 10-question quiz to find out which narrative you are currently living.**
""")

# --- STYLING (Academic/Bookish Theme) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #Fdfbf7; /* Off-white book paper color */
    }
    h1, h2, h3, p, div, label, span {
        color: #2c3e50 !important; /* Dark Ink Blue/Grey */
    }
    div.stButton > button {
        background-color: #34495e; /* Navy Blue Button */
        color: white !important;
        border-radius: 5px;
    }
    div.stButton > button:hover {
        background-color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("---")

# --- QUIZ DATA ---
# The options are manually scrambled so A, B, and C represent different categories in each question.

quiz_data = [
    {
        "question": "1. You just received a difficult diagnosis or hit a health setback. What is your very first thought?",
        "options": [
            {"text": "I need to find the right treatment immediately so I can get back to my normal life.", "type": "Restitution Narrative"},
            {"text": "This is a challenge that is going to change who I am, and I need to be ready to learn from it.", "type": "Quest Narrative"},
            {"text": "My life is over. I don't know how I'm going to get through the next hour, let alone the next year.", "type": "Chaos Narrative"},
        ]
    },
    {
        "question": "2. How do you view your doctors and medical providers?",
        "options": [
            {"text": "They are confusing, distant, or unhelpful. Nobody seems to be listening to how much I'm suffering.", "type": "Chaos Narrative"},
            {"text": "They are mechanics. Their job is to fix the 'broken part' of me so I can function again.", "type": "Restitution Narrative"},
            {"text": "They are guides. They can help medically, but the healing journey is up to me.", "type": "Quest Narrative"},
        ]
    },
    {
        "question": "3. While you’re sick a friend asks, 'How are you holding up?' How do you answer?",
        "options": [
            {"text": "I tell them about the insights I've gained about life and what actually matters to me now.", "type": "Quest Narrative"},
            {"text": "I say, 'I'm just focusing on the meds. Once I finish this round, I'll be fine.'", "type": "Restitution Narrative"},
            {"text": "I honestly can't explain it. It's just a mess of symptoms and I feel like I'm drowning.", "type": "Chaos Narrative"},
        ]
    },
    {
        "question": "4. You’re going through a breakup. How do you view the old you before this event?",
        "options": [
            {"text": "The 'Old Me' is the goal. I am working every day to be be happy and good again.", "type": "Restitution Narrative"},
            {"text": "The 'Old Me' is gone. I am grieving them, but I am becoming someone new.", "type": "Quest Narrative"},
            {"text": "The 'Old Me' feels like a dream I can't remember. I am trapped in the 'Bad Me' now.", "type": "Chaos Narrative"},
        ]
    },
    {
        "question": "5. Which statement resonates with you the most when you’re dealing with personal issues?",
        "options": [
            {"text": "I’m stuck in a whirlpool, spinning without control and being pulled under.", "type": "Chaos Narrative"},
            {"text": "It’s like changing a flat tire, I’ll be ready to hit the road again soon.", "type": "Restitution Narrative"},
            {"text": "I’m traveling through a dark forest, but I will emerge with a map to show others.", "type": "Quest Narrative"},
        ]
    },
    {
        "question": "6. When you are in pain, what do you tell yourself?",
        "options": [
            {"text": "This pain serves a purpose. It is teaching me empathy or resilience.", "type": "Quest Narrative"},
            {"text": "This pain makes no sense. It is random, cruel, and endless.", "type": "Chaos Narrative"},
            {"text": "This pain is temporary. It will go away once I get medicine.", "type": "Restitution Narrative"},
        ]
    },
    {
        "question": "7. How do you view the future after recovery?",
        "options": [
            {"text": "I can’t think about the future. I’m just trying to survive right now.", "type": "Chaos Narrative"},
            {"text": "I see myself as a more mature individual and who will guide others going through similar troubles.", "type": "Quest Narrative"},
            {"text": "I’m healthy again, able to do what I was doing before I got sick.", "type": "Restitution Narrative"},
        ]
    },
    {
        "question": "8. What frustrates you most about other people's reactions to your troubles?",
        "options": [
            {"text": "When they try to find a silver lining immediately. They don't understand how horrible this is.", "type": "Chaos Narrative"},
            {"text": "When they treat me like a victim. I want them to see I'm still the same capable person.", "type": "Restitution Narrative"},
            {"text": "When they downplay the meaningfulness of the experience. It impacted me profoundly.", "type": "Quest Narrative"},
        ]
    },
    {
        "question": "9. If you could write a memoir about a rough experience, what would the title be?",
        "options": [
            {"text": "*Rebound: How to Bounce Back from Adversity*", "type": "Restitution Narrative"},
            {"text": "*Lessons from my Low Points*", "type": "Quest Narrative"},
            {"text": "*My Terrible, Horrible, No Good, Very Bad Day*", "type": "Chaos Narrative"},
        ]
    },
    {
        "question": "10. Ultimately, what do you hope to achieve after facing adversity?",
        "options": [
            {"text": "Transformation. To use this suffering to become a better person.", "type": "Quest Narrative"},
            {"text": "Survival. Just getting through it is the only goal right now.", "type": "Chaos Narrative"},
            {"text": "Cure. Have things go back to how it was before and put it all behind me.", "type": "Restitution Narrative"},
        ]
    }
]

# --- COLLECT USER ANSWERS ---
user_answers = {}

for i, q_data in enumerate(quiz_data):
    st.subheader(q_data["question"])
    options_text = [opt["text"] for opt in q_data["options"]]
    # We use a unique key for each radio button so Streamlit tracks them separately
    choice = st.radio(f"Select an option for Question {i+1}:", options_text, key=f"q{i}")
    
    # Map back to type
    for opt in q_data["options"]:
        if opt["text"] == choice:
            user_answers[i] = opt["type"]

st.markdown("---")

# --- CALCULATE RESULTS ---
if st.button("Analyze My Narrative"):
    
    scores = {
        "Restitution Narrative": 0, 
        "Chaos Narrative": 0, 
        "Quest Narrative": 0
    }
    
    for answer in user_answers.values():
        scores[answer] += 1
    
    max_score = max(scores.values())
    winners = [cat for cat, score in scores.items() if score == max_score]
    
    # --- DISPLAY RESULTS ---
    
    if len(winners) > 1:
        st.header("You are between narratives.")
        st.write("You are currently transitioning between stories, likely moving from one phase to another.")
    else:
        st.header(f"You are living the: {winners[0]}")

    for winner in winners:
        
        if winner == "Restitution Narrative":
            st.info("🩺 **The Restitution Narrative**")
            st.write("""
                **"Yesterday I was healthy, today I am sick, but tomorrow I will be healthy again."**
                
                This is the most common narrative in modern culture. It focuses on the **Cure**.
                
                *   **The Hero:** Medicine, technology, and your own willpower.
                *   **The Plot:** You view illness as a temporary interruption. You are focused on 'beating' the sickness and returning to your pre-illness self.
                *   **The Trap:** If the illness is chronic or doesn't have a cure, this story can become frustrating because the 'happy ending' (total recovery) keeps moving further away.
            """)
            
        elif winner == "Chaos Narrative":
            st.warning("💥 **The Chaos Narrative**")
            st.write("""
                **"And then... and then... and then..."**
                
                Arthur Frank calls this the 'anti-narrative' because it lacks a clear beginning, middle, and end. It focuses on **Loss of Control**.
                
                *   **The Hero:** None. The illness is in control.
                *   **The Plot:** You feel overwhelmed. The story is hard to tell because new symptoms or problems keep happening before you can process the old ones.
                *   **The Reality:** This is a very real, very valid place to be during acute trauma or worsening illness. It requires patience and listening from others, not advice.
            """)
            
        elif winner == "Quest Narrative":
            st.success("🏔️ **The Quest Narrative**")
            st.write("""
                **"I wouldn't have chosen this, but I have changed because of it."**
                
                This narrative accepts that suffering is part of the journey. It focuses on **Meaning**.
                
                *   **The Hero:** You (The Wounded Storyteller).
                *   **The Plot:** You aren't necessarily 'cured,' but you are 'healed' in a spiritual or emotional sense. You use your experience to gain insight, advocate for others, or find new purpose.
                *   **The Power:** This allows you to integrate the illness into your life story rather than just trying to erase it.
            """)

    with st.expander("See your score breakdown"):
        st.write(scores)

