# Personal Finance (Django) - Local dev instructions

1. Tạo virtualenv & cài phụ thuộc
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Copy .env.example -> .env và điền biến (OPENAI_API_KEY nếu muốn test AI)

3. Áp migrations và tạo superuser
python manage.py migrate
python manage.py createsuperuser

4. Chạy server
python manage.py runserver

5. Chạy check budgets (manual / cron)
python manage.py check_budgets --month=2026-07

6. Gọi API AI report (token required)
POST /api/ai/report/ JSON {"month":"2026-07"} with Bearer token
