import asyncio
from playwright.async_api import async_playwright

# Define Global variable
context, pw, brs = None, None, None
search, name, passw = None, None, None

async def init():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False, slow_mo=5000)
    
    context0 = await browser.new_context()
    await context0.tracing.start(screenshots=True, snapshots=True, sources=True)
    global context, pw, brs
    context, pw, brs = context0, playwright, browser


async def login_page1():
    global context
    page = await context.new_page()
    await page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    await page.get_by_role("link", name="Sign In").click()
    await page.locator("#Catalog").get_by_role("textbox").nth(0).fill("abc")
    await page.locator("#Catalog").get_by_role("textbox").nth(1).fill("abc@123")
    await context.tracing.stop(path = "trace1.zip")

async def search_page2():
    global context
    page = await context.new_page()
    await page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    await page.locator('#SearchContent').get_by_role('textbox').fill("cat")


async def main():
    global context, pw, brs
    await init()
    task = []
    task.append(asyncio.create_task(login_page1()))
    task.append(asyncio.create_task(search_page2()))
    await asyncio.gather(*task)
    # await qa.get_by_role("button", name="Login").click()
    await brs.close()
    await pw.stop()
    
asyncio.run(main())