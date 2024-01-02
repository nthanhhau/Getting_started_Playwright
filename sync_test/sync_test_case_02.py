from playwright.sync_api import sync_playwright

qa, pw, brs = None, None, None

def a():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python/docs/pom")
    global qa, pw, brs
    qa, pw, brs = page, playwright, browser

def b():
    a()
    qa.get_by_role("button", name="Search").click()
    qa.get_by_placeholder("Search docs").click()
    qa.get_by_placeholder("Search docs").fill("abc")

b()
qa.screenshot(path="abc.png")
qa.get_by_placeholder("Search docs").fill("def")
qa.screenshot(path="def.png")
brs.close()
pw.stop()