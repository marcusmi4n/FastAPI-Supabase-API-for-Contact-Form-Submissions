from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client

app = FastAPI()

url = "https://your-project.supabase.co"
key = "your-anon-key"
supabase: Client = create_client(url, key)

class Contact(BaseModel):
    name: str
    email: str
    message: str

@app.post("/contact/")
def submit_contact(contact: Contact):
    data = supabase.table("contacts").insert({
        "name": contact.name,
        "email": contact.email,
        "message": contact.message
    }).execute()
    return {"success": True, "data": data}
