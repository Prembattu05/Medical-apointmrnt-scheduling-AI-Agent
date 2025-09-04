import streamlit as st
import pandas as pd
from datetime import datetime

# Load datasets
patients_df = pd.read_csv("patients.csv")
doctors_df = pd.read_excel("doctors.xlsx")
appointments_df = pd.read_excel("appointments.xlsx")

st.set_page_config(page_title="AI Scheduler", page_icon="🤖", layout="wide")
st.title("🤖 AI Appointment Scheduler")

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.patient = None
    st.session_state.appointment = {}
    st.session_state.messages = []

def bot_say(message):
    st.session_state.messages.append(("bot", message))

def user_say(message):
    st.session_state.messages.append(("user", message))

# Display chat history
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")

# ---------------- Conversation Steps ----------------
if st.session_state.step == 0:
    bot_say("👋 Hello! I can help you schedule an appointment. What is your first name?")
    name = st.text_input("Enter your first name:")
    dob = st.text_input("Enter your date of birth (YYYY-MM-DD):")
    if st.button("Continue"):
        user_say(f"My name is {name}, DOB {dob}")
        patient = patients_df[(patients_df["first_name"] == name) & (patients_df["dob"] == dob)]
        if not patient.empty:
            st.session_state.patient = patient.iloc[0].to_dict()
            bot_say("Welcome back! You are a returning patient. You get a 30-minute slot.")
        else:
            st.session_state.patient = {"first_name": name, "dob": dob, "is_returning": False}
            bot_say("Welcome! You are a new patient. You get a 60-minute slot.")
        st.session_state.step = 1
        st.experimental_rerun()

elif st.session_state.step == 1:
    bot_say("Which doctor would you like to see?")
    doctor = st.selectbox("Choose your doctor:", doctors_df["doctor"].unique())
    date = st.selectbox("Choose appointment date:", doctors_df["date"].unique())
    st.session_state.appointment["doctor"] = doctor
    st.session_state.appointment["date"] = date
    if st.button("Next"):
        user_say(f"I choose {doctor} on {date}")
        st.session_state.step = 2
        st.experimental_rerun()

elif st.session_state.step == 2:
    patient = st.session_state.patient
    duration = 30 if patient.get("is_returning", False) else 60
    doctor = st.session_state.appointment["doctor"]
    date = st.session_state.appointment["date"]

    slots = doctors_df[
        (doctors_df["doctor"] == doctor) &
        (doctors_df["date"] == date) &
        (doctors_df["is_available"])
    ]
    bot_say("Here are available time slots:")
    slot = st.selectbox("Choose time slot:", slots["slot_start"].unique())
    st.session_state.appointment["slot"] = slot
    st.session_state.appointment["duration"] = duration
    if st.button("Next "):
        user_say(f"I select {slot}")
        st.session_state.step = 3
        st.experimental_rerun()

elif st.session_state.step == 3:
    bot_say("Please provide your insurance details.")
    carrier = st.text_input("Insurance Carrier:")
    member = st.text_input("Member ID:")
    group = st.text_input("Group Number:")
    if st.button("Confirm Appointment"):
        st.session_state.appointment["insurance"] = {
            "carrier": carrier, "member": member, "group": group
        }
        user_say("I have provided insurance details.")
        st.session_state.step = 4
        st.experimental_rerun()

elif st.session_state.step == 4:
    patient = st.session_state.patient
    appt_id = len(appointments_df) + 1
    doctor = st.session_state.appointment["doctor"]
    date = st.session_state.appointment["date"]
    slot = st.session_state.appointment["slot"]
    duration = st.session_state.appointment["duration"]

    # Save to appointments.xlsx
    appointments_df.loc[len(appointments_df)] = [
        appt_id, patient.get("patient_id", "N/A"),
        patient["first_name"], doctor, date, slot,
        f"{int(slot.split(':')[0]) + duration // 60}:00",
        "new" if not patient.get("is_returning", False) else "returning",
        True, "confirmed", "", "", "", "", "None"
    ]
    appointments_df.to_excel("appointments.xlsx", index=False)

    bot_say(f"✅ Appointment confirmed! Your ID is {appt_id}.")
    bot_say("📄 A New Patient Intake Form will be sent to your email (mock).")
    bot_say("📅 You will receive 3 reminders before your visit.")
    st.session_state.step = 5

elif st.session_state.step == 5:
    st.success("Conversation completed! Scroll up to see the chatbot history.")
    st.subheader("📊 Latest Appointments")
    st.dataframe(appointments_df.tail(5))
