# BFHL FastAPI

A REST API implementation for the BFHL problem statement using FastAPI.

## Endpoint
**POST** `/bfhl`

## Features
- Returns user details (user_id, email, roll_number)
- Separates numbers (odd/even), alphabets (uppercase), and special characters
- Calculates sum of numbers
- Concatenates alphabets in reverse with alternating caps

## Example Request
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
