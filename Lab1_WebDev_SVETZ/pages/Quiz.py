import random
import streamlit as st

st.header("Quiz: What Phineas and Ferb character are you?")
st.image("Lab1_WebDev_SVETZ/Images/charecters.jpg", width=400)
st.write("Question 1: What would you do if you had a free Saturday?")
answer1 = st.radio(#NEW
    "Choose one:",
    ["Build something amazing","Hang out with friends","Try to prove something","Work on a secret plan"])

st.write("")
st.write("Question 2: How would you describe yourself?")
answer2 = st.selectbox(#NEW
    "Choose one:",
    ["Creative", "Quiet", "Determined", "Caring"])
st.write("")
st.write("Question 3: I like to...")
answer3 = st.multiselect(#NEW
    "select all that apply:",
    ["Build things", "Hang out with my friends", "Solve mysteries", "Come up with crazy ideas"])

st.write("")
st.write("Question 4: How adventurous are you?")
st.image("Lab1_WebDev_SVETZ/Images/adventure.jpg", width=400)
answer4 = st.slider(  #NEW
    "Choose a level:",
    1,
    10)

st.write("")
st.write("Question 5: What would your reaction to becoming mayor be?")
st.image("Lab1_WebDev_SVETZ/Images/mayor.jpg", width=400)
answer5 = st.radio(
    "Choose one:",
    ["Freak out and tell your mom", "Immediately start working on ways to improve the city", "Silently contemplate your next moves", "Commence stage 3 of your plan for world domination"])

st.write("")
st.write("Question 6: What is your favorite color?")
answer6 = st.radio(
    "Choose one:",
    ["Teal","Green","Red","Purple"])

def whatchar(answer1,answer2,answer3,answer4,answer5, answer6):
    isabella = 0
    phineas = 0
    candice = 0
    doof = 0
    ferb = 0
    perry = 0

    if answer1 == "Build something amazing":
        phineas+=1
    elif answer1 == "Hang out with friends":
        isabella+=1
    elif answer1 == "Try to prove something":
        candice+=1
    elif answer1 == "Work on a secret plan":
        doof+=1

    if answer2 == "Creative":
        phineas+=1
    elif answer2 == "Quiet":
        ferb+=1
    elif answer2 == "Determined":
        candice+=1
    elif answer2 == "Caring":
        isabella+=1

    if "Build things" in answer3:
        phineas += 1
    if "Hang out with my friends" in answer3:
        isabella += 1
    if "Solve mysteries" in answer3:
        perry += 1
    if "Come up with crazy ideas" in answer3:
        doof += 1

    if answer4 >= 5:
        phineas+=1
    elif answer4 <5:
        candice+=1
    
    if answer5 == "Freak out and tell your mom":
        candice+=1
    elif answer5 == "Immediately start working on ways to improve the city":
        phineas+=1
    elif answer5 == "Silently contemplate your next moves":
        ferb+=1
    elif answer5 == "Commence stage 3 of your plan for world domination":
        doof+=1

    if answer6 == "Teal":
        perry +=1
    elif answer6 == "Green":
        ferb+=1
    elif answer6 == "Red":
        phineas+=1
    elif answer6 == "Purple":
        doof+=1

    characters = ["Phineas", "Isabella", "Candace", "Doofenshmirtz", "Ferb", "Perry"]

    scores = [phineas, isabella, candice, doof, ferb, perry]

    highest = max(scores)

    winners = []

    for i in range(len(scores)):
        if scores[i] == highest:
            winners.append(characters[i])

    return random.choice(winners)

character = whatchar(answer1, answer2, answer3, answer4, answer5, answer6)

st.write("You are:", character)










