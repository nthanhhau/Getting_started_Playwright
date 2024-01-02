import re
from playwright.sync_api import Page, expect

def test_has_title(page):
    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_01(page: Page):
    page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    page.locator('#SearchContent').get_by_role('textbox').fill("dog")
    page.get_by_role('button', name='Search').click()
    page.screenshot(path="Document/py_test/dog.png")
    print("The test 1 complete!")
    
def test_02(page):
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="hau").click()
    page.get_by_role("link", name="Apple monitor 24").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("link", name="Add to cart").click()
    page.screenshot(path="Document/py_test/test2.png")
    print("The test 2 complete!")