🌅 Workelate Morning Briefing AI
================================

> **Smart, glanceable morning notifications for your task workflow.**

Workelate is an AI-powered notification layer built on top of MongoDB. It aggregates high-volume task data (even 100+ tasks) and transforms it into a concise, modern "SaaS-style" morning briefing delivered to your dashboard every 30 seconds.

✨ Features
----------

*   **🔄 Live-Sync Loop:** Automatically polls MongoDB at user-defined intervals (30s, 1m, etc.) without page refreshes.
    
*   **🧠 Intelligent Aggregation:** Pre-processes 100+ raw documents into status-based counts to keep AI prompts fast and cost-effective.
    
*   **🤖 SaaS-Style Tone:** Uses the Arcee-AI Trinity-Mini model via OpenRouter to deliver professional, punchy notifications tailored for a "Product App" experience.
    
*   **📊 Database Resilience:** Handles SSL handshakes and connection timeouts natively via certifi and pymongo.
    

🚀 Getting Started
------------------

### 1\. Prerequisites

*   Python 3.9+
    
*   A MongoDB Atlas Cluster
    
*   An [OpenRouter](https://openrouter.ai/) API Key
    

### 2\. Installation

Clone the repository and install the dependencies:

Bash

`   pip install streamlit pymongo requests python-dotenv certifi   `

### 3\. Environment Setup

Create a .env file in the root directory and add your credentials:

Code snippet

`   OPENROUTER_API_KEY=your_key_here   `

### 4\. Database Seeding

To populate your MongoDB with the 9 professional task categories, run the seed script:

Bash

`   python seed_db.py   `

### 5\. Launch the App

Bash

`   streamlit run app.py   `

🛠️ Technical Architecture
--------------------------

### **The Data Pipeline**

1.  **Extraction:** The app pulls all documents where bucketStatus is True.
    
2.  **Aggregation:** Instead of sending raw JSON, the app maps tasks to a Bucket | Status dictionary.
    
3.  **Synthesis:** The AI receives the map and a "SaaS Brand Voice" instruction set.
    
4.  **Delivery:** The UI renders the briefing inside a custom CSS notification card.
    

### **Configuration**

**VariableDescription**interval\_inputHow often the app checks for new data.temperatureSet to 0.7 for consistent brand tone.modelPowered by arcee-ai/trinity-mini:free.

📝 SaaS Notification Template
-----------------------------

The AI is instructed to follow this strict product-centric format:

> **Greeting:** "Good morning, Meet! It’s 08:30 AM."
> 
> **Status:** "You have 45 active tasks across 9 projects."
> 
> **Action:** "Priority: Focus on 'Backend API' testing."
> 
> **Closing:** "Let's get after it."
