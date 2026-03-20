🚀 Overview

This is a Leave Management System API built using Django and Django REST Framework (DRF).

It allows:

User registration & authentication

Applying for leave

Supervisor management

Leave approval/rejection

Role-based access control

🧱 Tech Stack

Backend: Django, Django REST Framework

Authentication: JWT (SimpleJWT)

Database: MySQL / SQLite

API Style: REST

📂 Project Structure
project/
│
├── leave/              # Main app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── project/            # Django settings
│
├── manage.py
└── README.md
🧩 Features
👤 User Management

Register user

Login (JWT)

Role-based access (USER / ADMIN)

📝 Leave Management

Apply leave

View own leaves

Leave status tracking

👨‍💼 Supervisor System

Assign supervisors

Multi-level approval support

✅ Approval Workflow

Approve leave

Reject leave

Track updated_by

🔐 Authentication

Using JWT

Login
POST /auth-login/
Refresh Token
POST /auth-refresh/
📡 API Endpoints
👤 Users
Method	Endpoint	Description
POST	/api/users/	Register
GET	/api/users/	Get current user
📝 Leaves
Method	Endpoint	Description
GET	/api/leaves/	List user leaves
POST	/api/leaves/	Apply leave
GET	/api/leaves/{id}/	Get leave
⚡ Custom Actions
Method	Endpoint	Description
POST	/api/leaves/{id}/approve/	Approve leave
POST	/api/leaves/{id}/reject/	Reject leave
📊 Lookup Tables
Endpoint
/api/leave-types/
/api/leave-date-types/
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/leave-system.git
cd leave-system
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
python manage.py makemigrations
python manage.py migrate
5. Run Server
python manage.py runserver
🧠 Key Concepts Used

ModelViewSet

Serializer separation (Create vs Response)

Dynamic serializers (get_serializer_class)

Custom permissions (get_permissions)

JWT authentication

Custom actions (@action)

🔥 Example Request
Apply Leave
POST /api/leaves/

{
  "leave_type": 1,
  "from_date": "2026-03-20",
  "to_date": "2026-03-22",
  "reason": "Medical"
}
🧪 Testing

You can test APIs using:

Postman

Thunder Client (VS Code)

🚀 Future Improvements

Dashboard analytics

Email notifications

Role-based UI (React frontend)

Leave balance tracking

Multi-level approval workflow

👨‍💻 Author

Kalana Ashen

⭐ Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📜 License

This project is for educational purposes.
