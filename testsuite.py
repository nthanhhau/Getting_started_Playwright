from playwright.sync_api import sync_playwright, expect

def test_case_01(s_browser_type='chromium', i_slow_mo=0, s_device='', b_tracing=True, b_headless=True,
                  url='https://petstore.octoperf.com/actions/Catalog.action', s_default_path="Document/test_case_01", b_video=False):
    with sync_playwright() as pw:
        if s_browser_type == 'chromium':
            browser = pw.chromium.launch(headless=b_headless, slow_mo=i_slow_mo)
        elif s_browser_type == 'firefox':
            browser = pw.firefox.launch(headless=b_headless, slow_mo=i_slow_mo)
        else:
            browser = pw.webkit.launch(headless=b_headless, slow_mo=i_slow_mo)
        dv = {}
        if s_device != '':
            dv = pw.devices[s_device]
        if b_video:
            dv.update({"record_video_dir":s_default_path})

        context = browser.new_context(**dv)
        
        if b_tracing:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # open a page for testing
        page = context.new_page()
        page.goto(url)
        print(f"Welcome to website: {page.title}")
        page.locator('#SearchContent').get_by_role('textbox').fill("fish")
        page.get_by_role('button', name='Search').click()
        page.screenshot(path=f"{s_default_path}/fishes.png")
        expect(page.locator("#Catalog").get_by_role("link")).to_have_count(4)
        page.get_by_role("link", name="Return to Main Menu").click()
        print("Back to home page!")
        
        for link in page.locator("#SidebarContent").get_by_role("link").all():
            link.click()
            page.get_by_role("link", name="Return to Main Menu").click()
        # assert len(page.locator("#SidebarContent").get_by_role("link").all()) == 5
        expect(page.locator("#SidebarContent").get_by_role("link")).to_have_count(5)

        if b_tracing:
            context.tracing.stop(path = f"{s_default_path}/trace.zip")
        page.close()
        context.close()

   
def test_case_02(s_browser_type='chromium', i_slow_mo=0, s_device='', b_tracing=True, b_headless=True,
                  url='https://petstore.octoperf.com/actions/Catalog.action', s_default_path="Document/test_case_02", b_video=False):
    with sync_playwright() as pw:
        if s_browser_type == 'chromium':
            browser = pw.chromium.launch(headless=b_headless, slow_mo=i_slow_mo)
        elif s_browser_type == 'firefox':
            browser = pw.firefox.launch(headless=b_headless, slow_mo=i_slow_mo)
        else:
            browser = pw.webkit.launch(headless=b_headless, slow_mo=i_slow_mo)
        
        dv = {}
        if s_device != '':
            dv = pw.devices[s_device]
        if b_video:
            dv.update({"record_video_dir":s_default_path})

        context = browser.new_context(**dv)
        
        if b_tracing:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # open a page for testing
        page = context.new_page()
        page.goto(url)
        print(f"Welcome to website: {page.title}")
        page.get_by_role("link", name="Sign In").click()
        expect(page.get_by_text("Please enter your username and password.")).to_be_visible()
        page.screenshot(path=f"{s_default_path}/login_form.png")
        page.locator("#Catalog").get_by_role("textbox").nth(0).fill("abc")
        page.locator("#Catalog").get_by_role("textbox").nth(1).fill("abc@123")
        page.get_by_role("button", name="Login").click()
        expect(page.get_by_text("Invalid username or password.  Signon failed.")).to_be_visible()
        page.screenshot(path=f"{s_default_path}/login_wrong.png")

        if b_tracing:
            context.tracing.stop(path = f"{s_default_path}/trace.zip")
        page.close()
        context.close()
        

