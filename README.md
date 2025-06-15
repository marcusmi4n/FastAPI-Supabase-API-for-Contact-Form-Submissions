# FastAPI + Supabase Contact Submission API

## Description
A small FastAPI endpoint that inserts form data into a Supabase table called `contacts`.

## Setup
1. Create table `contacts` with columns: name, email, message.
2. Install:
```bash
pip install fastapi uvicorn supabase

3. Run: uvicorn main:app --reload