from src.database.models import ReservaDB


def test_crear_reserva_retorna_201_y_persiste_en_db(client_con_bd, db_session):

    payload = {
        "cliente_email": "test@correo.com",
        "zona": "VIP",
        "cantidad": 2
    }

    respuesta = client_con_bd.post("/reservas/concierto-2026", json=payload)

    assert respuesta.status_code == 201

    reserva_en_db = db_session.query(ReservaDB).filter(
        ReservaDB.cliente_email == "test@correo.com"
    ).first()

    assert reserva_en_db is not None
    assert reserva_en_db.cliente_email == "test@correo.com"