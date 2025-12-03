import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://observador.padraodofonseca.com.br/bdoserver2.7/odw3.jsp")
    page.locator("input[type=\"text\"]").click()
    page.locator("input[type=\"text\"]").fill("lopez")
    page.locator("input[type=\"password\"]").click()
    page.locator("input[type=\"password\"]").fill("Padrao@2021")
    page.get_by_role("button", name="Entrar").click()
    page.get_by_role("combobox", name="Executar...").click()
    page.get_by_role("combobox", name="Executar...").fill("2753")
    page.get_by_role("combobox", name="Executar...").press("Enter")
    page.locator("iframe").nth(1).content_frame.locator(".selectize-input").click()
    page.locator("iframe").nth(1).content_frame.get_by_text("1", exact=True).click()
    page.locator("iframe").nth(1).content_frame.get_by_role("button", name="Executar").click()
    with page.expect_download() as download_info:
        page.locator("iframe").nth(1).content_frame.get_by_role("link", name="(Clique aqui para gerar o").click()
    download = download_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

