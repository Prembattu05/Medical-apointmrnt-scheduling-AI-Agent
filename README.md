# Medical-apointmrnt-scheduling-AI-Agent
This is an AI which will schedule the appointments for the people by separating the no show and other categories.

This is a Streamlit-based chatbot that simulates a medical appointment scheduler.  
It uses synthetic patient, doctor, and appointment datasets.  

## Features
- Collects patient info (name, DOB, doctor, location)
- Detects **new vs returning patients** (60 vs 30 mins slot rule)
- Shows available doctor slots
- Captures insurance details
- Confirms booking & saves to Excel
- Sends intake form (mock)
- Prepares reminders (to be extended)

## Project Structure
- `app.py` → chatbot app
- `patients.csv` → synthetic patient records
- `doctors.xlsx` → doctor availability
- `appointments.xlsx` → confirmed appointments
- `requirements.txt` → dependencies

## Running Locally
```bash
pip install -r requirements.txt
streamlit run app.py
