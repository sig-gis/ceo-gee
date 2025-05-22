create .env file in project root:

APP_NAME=ceoGee
HOST=localhost
PORT=8088
DEBUG=True
RELOAD=True
GEE_SERVICE_ACCOUNT=""
GEE_PRIVATE_KEY=""

python3 -m venv venv
source venv/vin/activate
pip3 install -r requirements.tx
python3 run.py

in a separate terminal, test with:
curl -X POST http://localhost:8088/gee/initialize/ \
  -H "Content-Type: application/json" \
  -d '{"ee_account": "your-service-account@project.iam.gserviceaccount.com", "ee_key_path": "/path/to/your/key.json"}'
