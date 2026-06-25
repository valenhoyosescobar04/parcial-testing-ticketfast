import pytest
from pathlib import Path
from playwright.sync_api import Page, expect


def test_reserva_vip_muestra_total_correcto(page: Page):

    ruta = Path(__file__).parent / "mock_frontend.html"
    page.goto(ruta.as_uri())

    page.get_by_test_id("input-email-cliente").fill("cliente@correo.com")
    page.get_by_test_id("select-zona-evento").fill("VIP")
    page.get_by_test_id("input-cantidad-asientos").fill("1")
    page.get_by_test_id("btn-confirmar-reserva").click()

    resumen = page.get_by_test_id("seccion-resumen-total")
    expect(resumen).to_contain_text("150.000")