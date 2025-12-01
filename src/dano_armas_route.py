from flask import Blueprint, request, jsonify
from db.database_util import get_db

dano_armas_bp = Blueprint("dano-armas", __name__)

@dano_armas_bp.get("/dano-armas")
def consultar_dano_armas():
    conn = get_db()
    cursor = conn.cursor()

    sql = "SELECT * FROM dano_armas"
    dano_armas = cursor.fetchall()

    arma_list = [dict(arma) for arma in dano_armas]

    return jsonify({"content": arma_list})

@dano_armas_bp.post("/dano-armas")
def criar_dano_arma():
    json = request.get_json()