# This is the first test case for testing Web
print("This is a section for testing!")
import re
# import pytest
from playwright.sync_api import sync_playwright, expect, Page




def test_has_title(url="https://playwright.dev/", title="Playwright"):

   with sync_playwright() as p:
       browser = p.chromium.launch(headless=False)
       page = browser.new_page()
       page.goto(url=url)


       # Expect a title "to contain" a substring.
       # expect(page).to_have_title(re.compile(title))
       assert page.get_by_text("GET STARTED").is_visible() == True
       browser.close()


def test_get_started_link(page:Page):
    
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
