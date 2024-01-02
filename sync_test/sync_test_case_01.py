from playwright.sync_api import sync_playwright, expect, Page

# with sync_playwright() as sync:
#     browser = sync.chromium.launch(slow_mo=2000)
#     context = browser.new_context(record_video_dir="sync_test/")
#     browser = sync.chromium.launch()
#     context = browser.new_context()
#     p = context.new_page()
#     p.goto("https://www.geeksforgeeks.org")
#     # search_box = p.locator("#RA-root > div > div.gfg_home_page_search_background.gfg_home_page_padding > div:nth-child(1) > div.ant-row.ant-row-center.gfg_home_page_search_input > span > span > span.ant-input-affix-wrapper.ant-input-affix-wrapper-lg > input")
#     search_box = p.get_by_role("textbox")
#     search_box.click()
#     search_box.fill("python")
#     p.screenshot(path="sync_test/gfg_01.png")
#     print("The test has been completed! Ready to release the brower...")

#     p.close()
#     browser.close()

def test(page:Page):
    page.goto("https://www.geeksforgeeks.org")
    # search_box = p.locator("#RA-root > div > div.gfg_home_page_search_background.gfg_home_page_padding > div:nth-child(1) > div.ant-row.ant-row-center.gfg_home_page_search_input > span > span > span.ant-input-affix-wrapper.ant-input-affix-wrapper-lg > input")
    search_box = page.get_by_role("textbox")
    search_box.click()
    search_box.fill("python")
    page.screenshot(path="sync_test/gfg_01.png")
    print("The test has been completed! Ready to release the brower...")
