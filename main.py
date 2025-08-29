from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import re

app = FastAPI(title="BFHL API")

FULL_NAME_LOWER = "avr-varshan"         
DOB_DDMMYYYY    = "20022004"        
EMAIL           = "avr.varshan20@gmail.com"
ROLL_NUMBER     = "22BRS1060"


USER_ID = f"{FULL_NAME_LOWER}_{DOB_DDMMYYYY}"
INT_REGEX = re.compile(r"^[+-]?\d+$")  

def classify_item(s: str):
    if isinstance(s, str) and INT_REGEX.match(s):
        return ("number", s, s)
    if isinstance(s, str) and s.isalpha():
        return ("alpha", s.upper(), s)
    return ("special", s, s)

def alternating_caps_reverse(all_letters: list[str]) -> str:
    rev = list(reversed(all_letters))
    out_chars = []
    for i, ch in enumerate(rev):
        out_chars.append(ch.upper() if i % 2 == 0 else ch.lower())
    return "".join(out_chars)

@app.post("/bfhl")
async def bfhl(request: Request):
    try:
        body = await request.json()
        data = body.get("data")
        if not isinstance(data, list):
            raise ValueError("`data` must be an array of strings.")

        even_numbers, odd_numbers = [], []
        alphabets, special_chars = [], []
        letter_stream = []  
        num_sum = 0

        for item in data:
            s = str(item)

            kind, normalized, original = classify_item(s)

            if kind == "number":
                n = int(original)
                (even_numbers if n % 2 == 0 else odd_numbers).append(original)
                num_sum += n
            elif kind == "alpha":
                alphabets.append(normalized)  
                for ch in original:
                    if ch.isalpha():
                        letter_stream.append(ch)
            else:
                special_chars.append(original)

        concat_str = alternating_caps_reverse(letter_stream)

        resp = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_chars,
            "sum": str(num_sum),          
            "concat_string": concat_str,  
        }
        return JSONResponse(status_code=200, content=resp)

    except Exception as e:
        resp = {
            "is_success": False,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "message": str(e),
        }
        return JSONResponse(status_code=400, content=resp)
