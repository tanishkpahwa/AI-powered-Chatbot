from flask import Flask, render_template, request, jsonify
import college_data
import university_data
import openai

app = Flask(__name__)

openai.api_key = "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"  

def get_ai_response(prompt):
    try: 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"AI Error: {str(e)}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message', '')
    print(f"Received query: {user_message}")

    college_response = college_data.get_response(user_message)
    if college_response:
        return jsonify({"response": college_response})

    university_response = university_data.get_response(user_message)
    if university_response:
        return jsonify({"response": university_response})

    ai_response = get_ai_response(user_message)
    if ai_response:
        return jsonify({"response": f"AI Assistant: {ai_response}"})

    return jsonify({"response": "I apologize, but I couldn't find any information on that."})

if __name__ == '__main__':
    app.run(debug=True)