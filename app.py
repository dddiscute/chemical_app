from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# 简化的数据结构
compounds = {
    '108-95-2': {'name': '苯酚', 'pka': 9.95},
    '121-12-0': {'name': '甲基酚', 'pka': 10.2},
    '108-39-4': {'name': '间甲酚', 'pka': 10.2},
    '106-44-5': {'name': 'p-甲酚', 'pka': 10.0},
    '88-74-1': {'name': '2-氯酚', 'pka': 8.4},
    '95-89-7': {'name': '3-氯酚', 'pka': 8.6},
    '100-39-0': {'name': '4-氯酚', 'pka': 9.3},
    '120-82-1': {'name': '2,4-二氯酚', 'pka': 7.8},
    '97-95-0': {'name': '2,4,6-三氯酚', 'pka': 6.0},
    '87-86-5': {'name': '五氯酚', 'pka': 5.3},
    '88-75-5': {'name': '2-硝基酚', 'pka': 7.2},
    '100-02-7': {'name': '4-硝基酚', 'pka': 7.1},
    '51-28-5': {'name': '2,4-二硝基酚', 'pka': 4.0},
    '88-89-1': {'name': '2,4,6-三硝基酚', 'pka': 0.4},
    '1980/5/7': {'name': '双酚 A', 'pka': 9.6},
    '84852-15-3': {'name': '4-非基酚', 'pka': 10.0},
    '130-64-4': {'name': '4-叔辛基酚', 'pka': 9.8}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/compound/<cas>')
def get_compound(cas):
    if cas not in compounds:
        return jsonify({'error': 'Compound not found'}), 404
    return jsonify(compounds[cas])

@app.route('/api/compounds')
def get_compounds():
    return jsonify([{'cas_number': cas, **data} for cas, data in compounds.items()])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 