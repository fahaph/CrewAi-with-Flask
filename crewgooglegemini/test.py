from dotenv import load_dotenv
import os

load_dotenv()

print("Google API Key:", os.getenv("GOOGLE_API_KEY")) # ตรวจสอบว่าถูกโหลดขึ้นมาหรือไม่
