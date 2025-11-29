from flask import Blueprint, request, jsonify
from db.database_util import get_db

dices_bp = Blueprint("dices", __name__)

@dices_bp.get("/dices")
def consultar_dices():
    conn = get_db()
    cursor = conn.cursor()

    valor_faces = request.args.get("valor_faces")
    params = {}

    sql = "SELECT * FROM dices WHERE 1=1 "

    if valor_faces is not None:
        params["valor_faces"] = valor_faces
        sql += " AND valor_faces = :valor_faces "

    sql += " ORDER BY valor_faces"

    cursor.execute(sql, params)
    dices = cursor.fetchall()

    dices_list = [dict(dice) for dice in dices]

    return jsonify({"content": dices_list})


@dices_bp.get("/dices/<dice_key>")
def obter_dices(dice_key: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dices WHERE dice_key = ?", (dice_key,))
    dice = cursor.fetchone()

    if dice is None:
        return (jsonify({"erro": f"O dice_key({dice_key}) informado não existe!"}), 404)

    return jsonify(dict(dice))