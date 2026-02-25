import pymongo
import urllib.parse
from bson import ObjectId
from datetime import datetime

# --- CONFIGURATION ---
username = ""
password = "" # The @ is fine here, we will escape it below

# 1. Escape the password (converts @ to %40)
escaped_password = urllib.parse.quote_plus(password)

# 2. Use your EXACT cluster address from your previous message
cluster_address = ""

# 3. Construct the URI correctly
MONGO_URI = f""

client = pymongo.MongoClient(MONGO_URI)
db = client['workelate_db']
buckets_col = db['buckets']

# --- YOUR STRICT TEMPLATE DATA ---
user_id = ObjectId()
board_id = ObjectId()

from bson import ObjectId
from datetime import datetime

# Common IDs to keep relationships consistent
user_id = ObjectId()
board_id = ObjectId()

example_data = [
    # 1. UI/UX DESIGN
    {
        "bucketName": "🎨 Design Assets",
        "bucketIndex": 2,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Create High-Fidelity Wireframes",
                "cardDescription": "Design the main dashboard and mobile views in Figma.",
                "taskStatus": "doing",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-26", "dueDate": "2026-03-01", "dueTime": "02:00 PM", "status": "In Progress"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Design"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 2. BACKEND API
    {
        "bucketName": "⚙️ Backend API",
        "bucketIndex": 3,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "User Authentication JWT",
                "cardDescription": "Implement login and signup using JWT tokens.",
                "taskStatus": "todo",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-25", "dueDate": "2026-03-05", "dueTime": "11:59 PM", "status": "Pending"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Backend"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 3. MARKETING
    {
        "bucketName": "📣 Social Media Blast",
        "bucketIndex": 4,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Schedule LinkedIn Posts",
                "cardDescription": "Prepare 3 posts about the new feature launch.",
                "taskStatus": "done",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-20", "dueDate": "2026-02-24", "dueTime": "09:00 AM", "status": "Completed"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Marketing"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 4. BUG FIXES
    {
        "bucketName": "🐛 Critical Bugs",
        "bucketIndex": 5,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Fix Login SSL Error",
                "cardDescription": "Investigate the TLS alert error on production.",
                "taskStatus": "doing",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-25", "dueDate": "2026-02-25", "dueTime": "05:00 PM", "status": "Urgent"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Urgent"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 5. CONTENT CREATION
    {
        "bucketName": "✍️ Documentation",
        "bucketIndex": 6,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Write API Docs",
                "cardDescription": "Detail all endpoints for the external dev team.",
                "taskStatus": "todo",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-03-01", "dueDate": "2026-03-10", "dueTime": "06:00 PM", "status": "Future Task"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Documentation"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 6. HR & RECRUITING
    {
        "bucketName": "👥 Hiring",
        "bucketIndex": 7,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Interview Node.js Dev",
                "cardDescription": "Technical round for candidate Rahul.",
                "taskStatus": "doing",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-26", "dueDate": "2026-02-26", "dueTime": "11:00 AM", "status": "Scheduled"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["HR"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 7. QA TESTING
    {
        "bucketName": "🧪 QA & Testing",
        "bucketIndex": 8,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Unit Test Dashboard",
                "cardDescription": "Write Jest tests for the main chart components.",
                "taskStatus": "todo",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-03-02", "dueDate": "2026-03-04", "dueTime": "04:00 PM", "status": "Planned"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Testing"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 8. FINANCE
    {
        "bucketName": "💰 Finance/Invoicing",
        "bucketIndex": 9,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Submit Monthly Expense Report",
                "cardDescription": "Compile all receipts for Feb 2026.",
                "taskStatus": "todo",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-28", "dueDate": "2026-03-02", "dueTime": "12:00 PM", "status": "Financial"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["Admin"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    },

    # 9. DEVOPS
    {
        "bucketName": "☁️ Infrastructure",
        "bucketIndex": 10,
        "boardId": board_id,
        "createdBy": user_id,
        "bucketStatus": True,
        "cards": [
            {
                "cardTitle": "Migrate to AWS S3",
                "cardDescription": "Move all static assets from local storage to S3.",
                "taskStatus": "doing",
                "cardStatus": True,
                "createdBy": user_id,
                "cardassignees": [user_id],
                "cardDate": {"startDate": "2026-02-24", "dueDate": "2026-03-05", "dueTime": "10:00 PM", "status": "In Progress"},
                "checklist": [], "cardActivity": [], "logs": [], "attachments": [], "urls": [], "cardMembers": [], "cardLabel": ["DevOps"]
            }
        ],
        "createdAt": datetime.utcnow(), "updatedAt": datetime.utcnow()
    }
]
def seed_database():
    try:
        # 1. Verify Connection
        client.admin.command('ping')
        print("✅ Success! Connected and Authenticated.")

        # 2. CLEANUP: Delete old documents to avoid the "Same Greeting" issue
        # This ensures you only have these 9 fresh examples in your DB.
        delete_result = buckets_col.delete_many({})
        print(f"🧹 Cleaned up {delete_result.deleted_count} old documents.")

        # 3. INSERT MANY: Use insert_many for your list of 9 examples
        result = buckets_col.insert_many(example_data)
        
        print(f"✅ Success! {len(result.inserted_ids)} documents inserted.")
        print("First ID inserted:", result.inserted_ids[0])

    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    seed_database()

