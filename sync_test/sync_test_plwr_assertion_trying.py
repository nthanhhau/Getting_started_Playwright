
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium
    pre_context = browser.launch(headless=False, slow_mo=200)
    context = pre_context.new_context()
    page = context.new_page()
    page.goto("https://www.thegioididong.com/")
    a = page.locator(".owl-stage > div:nth-child(6) > a").first
    expect(a).not_to_be_in_viewport()
    page.screenshot(path="sync_test/before.png")
    # the hover action will be 
    expect(a).to_be_in_viewport(timeout=10000) # this line is to verify Playwright assertion trying many time
    page.screenshot(path="sync_test/after.png")
    print(page.title)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)