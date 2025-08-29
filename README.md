# BFHL FastAPI

Minimal FastAPI API for the BFHL task. It classifies input into numbers, alphabets, and special characters, returns sums, and builds a reverse alternating-caps string.

## Live API

- **Base URL**: `https://bfhl-fastapi-xaav.onrender.com`
- **Docs**: `/docs` and `/redoc` on the same base URL

## Endpoint

- **Method**: `POST`
- **Route**: `/bfhl`
- **Content-Type**: `application/json`

## Example JSON

**Request body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response body:**
```json
{
  "is_success": true,
  "user_id": "avr-varshan_20022004",
  "email": "avr.varshan20@gmail.com",
  "roll_number": "22BRS1060",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## curl

**Inline JSON:**
```bash
curl -X POST https://bfhl-fastapi-xaav.onrender.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data":["a","1","334","4","R","$"]}'
```

**From a JSON file:**
```bash
echo '{"data":["a","1","334","4","R","$"]}' > payload.json && \
curl -X POST https://bfhl-fastapi-xaav.onrender.com/bfhl \
  -H "Content-Type: application/json" \
  -d @payload.json
```
