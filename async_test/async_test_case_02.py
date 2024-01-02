import asyncio
from playwright.async_api import async_playwright, expect

async def test2(browser_type):

    browser = await browser_type.launch(headless=False, slow_mo=2000)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://global.account.xiaomi.com/fe/service/register/email?_locale=vi_VN&source=&region=VN&sid=passport&qs=_locale%3Dvi_VN&callback=https%3A%2F%2Faccount.xiaomi.com&_uRegion=TW")
    await page.locator("input[name=\"email\"]").fill("abc@gmail.com")
    await page.locator("input[name=\"password\"]").fill("Abc@123de")
    await page.locator("input[name=\"repassword\"]").fill("Abc@123de")
    signin = page.get_by_role("button", name="Tiếp theo")
    await expect(signin).to_be_enabled()
    await page.screenshot(path=f'async_test/example-{browser_type.name}.png')
    await browser.close()


async def main():
    async with async_playwright() as p:
        await test2(p.chromium)


asyncio.run(main())