from fastapi import FastAPI
import random

app = FastAPI()

#store OTPs
otp_store = {}

def send_otp(email: str):
  #Generate a 6 digit otp
  otp = str(random.randint(100000,999999))
  otp_store[email] = otp
  return {"email": email, "otp": otp, "message": "OTP generated successfully"}

@app.post("/very-otp")
def verify_otp(email: str, otp: str):
  if email not in otp_store:
    return {"success": False, "message": "No OTP found for this emaail"}
    if otp_store[email] != otp:
      return {"success": False, "message": "Invalid OTP"}
      #if OTP is correct delete it
del otp_store[email]
return {"success": True, "message": "Account verified successfully"}
