import streamlit as st
import pymongo
import requests
import json
import urllib.parse
from datetime import datetime
import os
import time
import certifi
from dotenv import load_dotenv

# Load credentials
load_dotenv()

# --- CONFIGURATION ---
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "").strip()
MONGO_USERNAME = ""
MONGO_PASSWORD = ""
MONGO_CLUSTER = ""

escaped_password = urllib.parse.quote_plus(MONGO_PASSWORD)
MONGO_URI = f""

@st.cache_resource
def init_connection():
    return pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())

client = init_connection()
db = client["workelate_db"]
buckets_col = db["buckets"]

def get_ai_summary_stateful(task_data, task_count):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501"
    }
    
    prompt_content = f"""
    Act as the automated notification system for 'Workelate'.
    USER: Meet
    TIME: {datetime.now().strftime('%I:%M %p')}
    TASKS: {task_count}
    DATA: {json.dumps(task_data)}
    
    STYLE:
    - Line 1: Professional greeting with time.
    - Line 2: High-level status summary.
    - Line 3: One specific priority Action Item.
    - Line 4: Punchy closing.
    - MAX 50 WORDS.
    """
    
    payload = {
        "model": "arcee-ai/trinity-mini:free",
        "messages": [{"role": "user", "content": prompt_content}],
        "temperature": 0.7,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        res_json = response.json()
        return res_json['choices'][0]['message'].get('content')
    except Exception as e:
        return f"❌ Notification Error: {str(e)}"

def parse_time(time_str):
    time_str = time_str.lower().strip()
    try:
        if 'min' in time_str: return float(time_str.split('min')[0].strip()) * 60
        elif 's' in time_str: return float(time_str.split('s')[0].strip())
        return float(time_str)
    except: return 30

# --- UI SETUP ---
st.set_page_config(page_title="Workelate", page_icon="🔔")
st.title("🔔 Workelate Daily Brief")

with st.sidebar:
    st.header("Settings")
    run_loop = st.toggle("🚀 Active Notifications", value=False)
    interval_input = st.text_input("Frequency", "30 s")
    
    if st.button("Clear DB"):
        buckets_col.delete_many({})
        st.experimental_rerun()

# --- THE LOGIC ---
if not run_loop:
    st.info("Toggle 'Active Notifications' to start your morning feed.")
else:
    # 1. FETCH DATA
    raw_data = list(buckets_col.find({"bucketStatus": True}))
    all_tasks = []
    for bucket in raw_data:
        for card in bucket.get('cards', []):
            all_tasks.append({"B": bucket.get('bucketName'), "S": card.get('taskStatus')})

    # 2. SHOW NOTIFICATION
    if not all_tasks:
        st.info("All clear! No tasks for now. ☕")
    else:
        summary_counts = {}
        for t in all_tasks:
            key = f"{t['B']} [{t['S']}]"
            summary_counts[key] = summary_counts.get(key, 0) + 1
        
        with st.spinner("Syncing..."):
            greeting = get_ai_summary_stateful(summary_counts, len(all_tasks))
        
        # UI "Card" styling
        st.markdown(f"""
        <div style="padding:20px; border-radius:10px; border-left: 5px solid #ff4b4b; background-color: #f0f2f6; color: #31333F;">
            {greeting.replace('', '')}
        </div>
        """, unsafe_allow_html=True)
        st.toast("Updated just now")

    # 3. THE TIMER (Instead of while True)
    wait_time = parse_time(interval_input)
    time.sleep(wait_time)
    st.rerun() # This refreshes the page automatically