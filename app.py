import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="The Wounded Storyteller Quiz", page_icon="📖")

st.title("📖 What Is Your Illness Narrative Style?")
st.write("""
Sociologist Arthur Frank (*The Wounded Storyteller*) identified three main ways people tell the story of their health struggles. 
No narrative is inherently bad. Each one has a purpose and reflects how we make sense of our pain.

**Take this 10-question quiz to find out which narrative resonates with you!**
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
if st.button("Get My Results"):
    
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
            st.markdown("""
            ### *"Yesterday I was healthy, today I am sick, but tomorrow I will be healthy again."*
            
            **What this is:**
            This is the "medical ideal." It views illness as a temporary enemy to be defeated. Your primary focus is finding the cure, fixing the broken part, and returning to the person you were before this happened.
            
            ---
            
            #### ⚖️ The Pros & Cons
            *   **The Strength:** This mindset provides incredible motivation. It fuels compliance with medical treatment, keeps morale high, and works perfectly for temporary illnesses (like a broken leg or the flu).
            *   **The Shadow Side:** It is fragile. If the illness becomes chronic or a cure isn't possible, this narrative collapses. You may feel like a "failure" because you aren't getting better, leading to denial or deep frustration.
            
            #### 🚀 How to Move Forward
            *   **If you have a treatable condition:** Keep going. This narrative is serving you well.
            *   **If you have a chronic condition:** Be careful. Trying to force a Restitution story on a permanent reality can lead to burnout. You might benefit from exploring the **Quest Narrative**, where the goal shifts from "cure" to "healing" (finding peace even without a cure).
            """)
            
        elif winner == "Chaos Narrative":
            st.warning("💥 **The Chaos Narrative**")
            st.markdown("""
            ### *"And then... and then... and then..."*
            
            **What this is:**
            Arthur Frank calls this the "anti-narrative" because it has no structure. It is the story of being overwhelmed. You feel swept along by the illness, with no control over the plot. This usually happens during acute trauma, new diagnoses, or severe relapses.
            
            ---
            
            #### ⚖️ The Pros & Cons
            *   **The Strength:** It is the most honest depiction of suffering. It refuses to sugarcoat the pain or pretend things are okay when they aren't. It demands attention.
            *   **The Shadow Side:** It is isolating. Because the story is hard to listen to (and has no happy ending yet), friends and family often pull away. It traps you in the immediate moment, making it impossible to imagine a future.
            
            #### 🚀 How to Move Forward
            *   **Acceptance:** Don't force yourself to find a "silver lining" yet. You are in the storm. Survival is enough.
            *   **Find a Confidant:** You need a listener who won't try to "fix" you, but who can just witness the pain.
            *   **The Exit:** Chaos is usually a phase. Eventually, as you regain a tiny bit of agency, you will likely move toward a **Restitution** (seeking help) or **Quest** (finding meaning) narrative.
            """)
            
        elif winner == "Quest Narrative":
            st.success("🏔️ **The Quest Narrative**")
            st.markdown("""
            ### *"I wouldn't have chosen this, but I have changed because of it."*
            
            **What this is:**
            This narrative accepts that the old version of you is gone. Instead of trying to go back, you use the illness as a catalyst for transformation. You believe that suffering, while terrible, has given you specific insights, empathy, or a new purpose.
            
            ---
            
            #### ⚖️ The Pros & Cons
            *   **The Strength:** It grants you agency. Even if you can't control the disease, you control the *meaning* of it. It often leads to community building, advocacy, and deep emotional peace.
            *   **The Shadow Side:** It can turn into toxic positivity. If forced too early, it can make you feel like you aren't allowed to just be sad or angry. Not every moment needs to be a profound lesson.
            
            #### 🚀 How to Move Forward
            *   **Share your story:** Quest narrators heal by helping others. Consider writing, support groups, or mentoring.
            *   **Stay Grounded:** Remember that getting "Quest" doesn't mean you are only this narrative. It is okay to have days where you just want to be fixed (**Restitution**) or feel all of your emotions(**Chaos**).
            """)


    with st.expander("See your score breakdown"):
        st.write(scores)

st.write("""
Frank, Arthur W. The Wounded Storyteller: Body, Illness, and Ethics. 2nd ed., University of Chicago Press, 2013.
""")
