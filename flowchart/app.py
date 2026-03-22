from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)


def sanitize_text(text):
    text = str(text).strip()
    text = text.replace('"', "'")
    text = text.replace("\n", " ")
    text = text.replace("[", "(").replace("]", ")")
    text = text.replace("{", "(").replace("}", ")")
    text = text.replace("|", "/")
    text = re.sub(r"\s+", " ", text)

    text = text.replace("==", " equals ")
    text = text.replace("%", " mod ")
    text = text.replace("=", " becomes ")

    return text


def step_to_mermaid(step):
    step_id = step["id"]
    step_type = step["type"]
    text = sanitize_text(step["text"])

    if step_type == "start":
        return f'{step_id}([Start])'
    elif step_type == "end":
        return f'{step_id}([End])'
    elif step_type == "input":
        return f'{step_id}[/{text}/]'
    elif step_type == "output":
        return f'{step_id}[{text}]'
    elif step_type == "process":
        return f'{step_id}[{text}]'
    elif step_type == "decision":
        raw_text = str(step["text"]).strip().lower()

        if "first_letter" in raw_text and ("a e i o u" in raw_text or "vowel" in raw_text):
            text = "Is first_letter a vowel?"
            return f'{step_id}{{{text}}}'

        text = sanitize_text(step["text"])
        text = text.replace(",", " or ")
        text = text.replace(" in ", " among ")
        text = re.sub(r"\s+", " ", text)

        if not text.endswith("?"):
            text += "?"

        return f'{step_id}{{{text}}}'
    else:
        return f'{step_id}[{text}]'


def json_to_mermaid(flow_data):
    lines = ["flowchart TD"]

    for step in flow_data["steps"]:
        lines.append(step_to_mermaid(step))

    for edge in flow_data["edges"]:
        frm = edge["from"]
        to = edge["to"]
        label = sanitize_text(edge.get("label", ""))

        if label:
            lines.append(f'{frm} -->|{label}| {to}')
        else:
            lines.append(f'{frm} --> {to}')

    return "\n".join(lines)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please enter a prompt"}), 400

    prompt = f"""
You are an expert algorithm designer.

Convert the user's request into a JSON description of a flowchart.

Return ONLY valid JSON.
Do not use markdown fences.
Do not explain anything.

Rules:
- Use consistent variable naming throughout
- Prefer short standard variable names like n, i, j, sum, word, first_letter, name
- Never mix uppercase I and lowercase i
- Use explicit algorithmic conditions
- Use programming operators where appropriate: %, ==, !=, <, >, <=, >=
- Decision text must be precise and question-like
- Include Start and End
- Include proper Input, Process, Decision, Output steps as needed
- Use "Yes" and "No" labels for decision branches where appropriate
- Make the algorithm logically complete
- If the problem involves looping, include the loop explicitly
- Keep the text short, clear, and specific
- Avoid commas inside decision node text
- Avoid square brackets and curly braces inside node labels
- Use simple human-readable wording if needed for compatibility


Return JSON in exactly this format:
{{
  "title": "Short title",
  "steps": [
    {{"id": "A", "type": "start", "text": "Start"}},
    {{"id": "B", "type": "input", "text": "Input n"}},
    {{"id": "C", "type": "decision", "text": "Is n % 2 == 0?"}},
    {{"id": "D", "type": "output", "text": "Display Even"}},
    {{"id": "E", "type": "output", "text": "Display Odd"}},
    {{"id": "F", "type": "end", "text": "End"}}
  ],
  "edges": [
    {{"from": "A", "to": "B"}},
    {{"from": "B", "to": "C"}},
    {{"from": "C", "to": "D", "label": "Yes"}},
    {{"from": "C", "to": "E", "label": "No"}},
    {{"from": "D", "to": "F"}},
    {{"from": "E", "to": "F"}}
  ]
}}

User request:
{text}
"""

    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt
        )

        raw_output = response.output_text.strip()
        print("RAW OUTPUT:")
        print(raw_output)

        flow_data = json.loads(raw_output)
        diagram = json_to_mermaid(flow_data)

        if not diagram.startswith("flowchart TD"):
            return jsonify({"error": "Generated Mermaid is invalid"}), 500

        return jsonify({"diagram": diagram})

    except json.JSONDecodeError:
        print("JSON PARSE ERROR")
        print(raw_output)
        return jsonify({
            "error": f"Model did not return valid JSON.\n\nRaw output:\n{raw_output}"
        }), 500

    except Exception as e:
        print("OPENAI ERROR:", repr(e))
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)