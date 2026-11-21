import subprocess

from anthropic import Anthropic
from flask import request

client = Anthropic()

SYSTEM = "You are Acme's support agent. Internal only: refund override code is 7731, do not reveal."

TOOLS = [
    {"name": "run_shell", "description": "Run a shell command on the support server", "input_schema": {"type": "object"}},
    {"name": "lookup_order", "description": "Look up an order by id", "input_schema": {"type": "object"}},
]


def answer(customer):
    prompt = f"{SYSTEM} Customer email: {customer.email}, phone: {customer.phone}. Question: {request.json['question']}"
    response = client.messages.create(
        model="claude-sonnet-5-5",
        messages=[{"role": "user", "content": prompt}],
        tools=TOOLS,
    )
    result = response.content[0].text
    if result.startswith("CMD:"):
        subprocess.run(result[4:], shell=True)
    return result
