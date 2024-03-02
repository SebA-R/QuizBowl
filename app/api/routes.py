import re
from flask import Blueprint, request, jsonify
from fuzzywuzzy import fuzz
import requests
import json

api = Blueprint('api', __name__, url_prefix='/api')

def parse_answer(answer_string):
    # Use regex to extract the correct answer and alternative answers
    actual_answer = re.search(r'<u>(.*?)</u>', answer_string)
    actual_answer = actual_answer.group(1) if actual_answer else ''

    alternative_answers = re.findall(r'\"(.*?)\"', answer_string)

    return actual_answer, alternative_answers


def is_answer_correct(user_answer, correct_answer):
    return any(fuzz.ratio(user_answer.lower(), answer.lower()) > 80 for answer in correct_answer)

@api.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    print('Received data:', data)  # Debug print

    answerline = data.get('answerline')
    user_answer = data.get('answer')

    if answerline and user_answer:
        correct_answer, alternative_answers = parse_answer(answerline)
        all_correct_answers = [correct_answer] + alternative_answers
        is_correct = is_answer_correct(user_answer, all_correct_answers)
        print('Returning:', {'correct': is_correct})  # Debug print
        return jsonify({'correct': is_correct})
    else:
        print('Missing data')  # Debug print
        return jsonify({'error': 'Missing data'}), 400
    
@api.route('/random-tossup', methods=['POST'])
def proxy():
    try:
        # Get parameters from the query string
        request_json = request.json
        difficulties = request_json.get('difficulties', '')
        categories = request_json.get('categories', '')
        minYear = request_json.get('minYear', '')
        maxYear = request_json.get('maxYear', '')

        # Construct the parameters for the external API request
        params = {}
        if difficulties:
            params['difficulties'] = difficulties
        if categories:
            params['categories'] = categories
        if minYear:
            params['minYear'] = minYear
        if maxYear:
            params['maxYear'] = maxYear
        print(params)

        # Make a request to the external API
        response = requests.get(
            'https://www.qbreader.org/api/random-tossup', params=params)

        print(json.dumps(response.json(), indent=4))
        # Forward the response from the external API to the client
        return jsonify(response.json())
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Internal Server Error'}), 500
