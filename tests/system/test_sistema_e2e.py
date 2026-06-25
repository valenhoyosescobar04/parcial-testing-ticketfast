import os
import httpx
import pytest

BASE_URL = os.getenv("API_URL", "http://localhost:8001")


@pytest.fixture(scope="module")
def cliente_http():
    with httpx.Client(base_url=BASE_URL, timeout=10.0) as client:
        yield client


def test_flujo_reserva_general_y_total_recaudado(cliente_http):

    evento_id = "sistema-evento-xyz"

    # PASO 1: crear reserva
    payload = {
        "cliente_email": "sistema@correo.com",
        "zona": "General",
        "cantidad": 3
    }
    resp_post = cliente_http.post(f"/reservas/{evento_id}", json=payload)
    assert resp_post.status_code == 201

    # PASO 2: consultar resumen
    resp_get = cliente_http.get(f"/reservas/{evento_id}/resumen")
    assert resp_get.status_code == 200

    # PASO 3: validar total — General: 50000 * 3 = 150000
    data = resp_get.json()
    assert data["total_recaudado"] == 150000.0