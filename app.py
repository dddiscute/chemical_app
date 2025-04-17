from flask import Flask, render_template, jsonify, request
import os
import sqlite3
import pandas as pd

app = Flask(__name__)

# 数据库路径
DATABASE = 'chemicals.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# 确保数据库和表存在
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        # 创建化合物表
        conn.execute('''
            CREATE TABLE IF NOT EXISTS compounds (
                cas_number TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                pka REAL NOT NULL
            )
        ''')
        
        # 插入示例数据
        compounds_data = [
            ('108-95-2', '苯酚', 9.95),
            ('121-12-0', '甲基酚', 10.2),
            ('108-39-4', '间甲酚', 10.2),
            ('106-44-5', 'p-甲酚', 10.0),
            ('88-74-1', '2-氯酚', 8.4),
            ('95-89-7', '3-氯酚', 8.6),
            ('100-39-0', '4-氯酚', 9.3),
            ('120-82-1', '2,4-二氯酚', 7.8),
            ('97-95-0', '2,4,6-三氯酚', 6.0),
            ('87-86-5', '五氯酚', 5.3),
            ('88-75-5', '2-硝基酚', 7.2),
            ('100-02-7', '4-硝基酚', 7.1),
            ('51-28-5', '2,4-二硝基酚', 4.0),
            ('88-89-1', '2,4,6-三硝基酚', 0.4),
            ('1980/5/7', '双酚 A', 9.6),
            ('84852-15-3', '4-非基酚', 10.0),
            ('130-64-4', '4-叔辛基酚', 9.8)
        ]
        
        conn.executemany('INSERT OR REPLACE INTO compounds (cas_number, name, pka) VALUES (?, ?, ?)',
                        compounds_data)
        conn.commit()
        conn.close()

# 初始化数据库
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/compound/<cas>')
def get_compound(cas):
    conn = get_db_connection()
    compound = conn.execute('SELECT * FROM compounds WHERE cas_number = ?',
                          (cas,)).fetchone()
    conn.close()
    
    if compound is None:
        return jsonify({'error': 'Compound not found'}), 404
        
    return jsonify({
        'name': compound['name'],
        'pka': compound['pka']
    })

@app.route('/api/compounds')
def get_compounds():
    conn = get_db_connection()
    compounds = conn.execute('SELECT * FROM compounds').fetchall()
    conn.close()
    
    return jsonify([{
        'cas_number': c['cas_number'],
        'name': c['name'],
        'pka': c['pka']
    } for c in compounds])

# Vercel 需要这个
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 