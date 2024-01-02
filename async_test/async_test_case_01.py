import asyncio
from playwright.async_api import async_playwright

async def test(browser_type):
    browser = await browser_type.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    await page.get_by_role("link", name="www.mybatis.org").click()
    await page.get_by_role("link", name="Products").click()
    await page.get_by_role("link", name="Contribute").click()
    await page.get_by_role("link", name="Sponsors").click()
    await page.locator("#PageList1").get_by_role("link", name="Home").click()
    await page.screenshot(path=f'example-{browser_type.name}.png')
    print(f"Test is completed on browser {browser_type.name}")

async def main():
    async with async_playwright() as p:
        tasks = []
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            tasks.append(asyncio.create_task(test(browser_type)))
        await asyncio.gather(*tasks)

asyncio.run(main())