from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/process_string', methods=['POST'])
def process_string():
    print(request.data.decode('utf-8'))
    hub_id = request.json.get('hub_id')

    if hub_id is None:
        return jsonify({'error': 'Input string not provided'}), 400

    # Process the input string here
    hub_id = int(hub_id)

    is_vacant = hub_id % 2 == 0

    return jsonify({'Vacant': is_vacant})


if __name__ == '__main__':
    app.run()
