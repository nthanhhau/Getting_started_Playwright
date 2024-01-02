# 🎭 Playwright framework use Python programing language

## [Documentation](https://playwright.dev/python/) | [API reference](https://playwright.dev/python/docs/api/class-playwright)

Playwright is a framework for Web Testing and Automation. It has been issued since 2020 by MS.
It allows testing [Chromium](https://www.chromium.org/Home), [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [WebKit](https://webkit.org/) with a single API. Playwright is built to enable cross-browser web automation.

|          | Linux | macOS | Windows |
|   :---   | :---: | :---: | :---:   |
| Chromium <!-- GEN:chromium-version -->121.0.6167.16<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| WebKit <!-- GEN:webkit-version -->17.4<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Firefox <!-- GEN:firefox-version -->120.0.1<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |

Looking for Playwright for [Python](https://playwright.dev/python/docs/intro), [.NET](https://playwright.dev/dotnet/docs/intro), or [Java](https://playwright.dev/java/docs/intro)?

### A look at the comparation between Playwright and Selenium
| Criteria    | Playwright | Selenium |
| :---:       | :---:      | :---:    |
| Architecture| WebSocket connection | WebDriver API |
| Browser Support | Chromium, Firefox, and WebKit | Chrome, Safari, Firefox, Opera, Edge, and IE |
| Language Support | Java, Python, .NET C#, TypeScript and JavaScript | Java, Python, C#, Ruby, Perl, PHP, and JavaScript |
| Operating System Support | Windows, Mac OS and Linux | Windows, Mac OS, Linux and Solaris |
| Community Support | Smaller but growing set of community resources | Large, established collection of documentation and support options |
| Execution speed | Faster | Slower |

## Capabilities

### Resilient • No flaky tests

**Auto-wait**. Playwright waits for elements to be actionable prior to performing actions. It also has a rich set of introspection events. The combination of the two eliminates the need for artificial timeouts - a primary cause of flaky tests.

**Web-first assertions**. Playwright assertions are created specifically for the dynamic web. Checks are automatically retried until the necessary conditions are met.

**Tracing**. Configure test retry strategy, capture execution trace, videos and screenshots to eliminate flakes.

### No trade-offs • No limits

Browsers run web content belonging to different origins in different processes. Playwright is aligned with the architecture of the modern browsers and runs tests out-of-process. This makes Playwright free of the typical in-process test runner limitations.

**Multiple everything**. Test scenarios that span multiple tabs, multiple origins and multiple users. Create scenarios with different contexts for different users and run them against your server, all in one test.

**Trusted events**. Hover elements, interact with dynamic controls and produce trusted events. Playwright uses real browser input pipeline indistinguishable from the real user.

### Full isolation • Fast execution

**Browser contexts**. Playwright creates a browser context for each test. Browser context is equivalent to a brand new browser profile. This delivers full test isolation with zero overhead. Creating a new browser context only takes a handful of milliseconds.

**Log in once**. Save the authentication state of the context and reuse it in all the tests. This bypasses repetitive log-in operations in each test, yet delivers full isolation of independent tests.

## Installation

Playwright has its own test runner for end-to-end tests, we call it Playwright Test.

### Using pip command

```Shell
# Install the Pytest plugin:
pip install pytest-playwright
# Install the default browsers, they consist of chromium, fierfox and webkit:
playwright install
# Or install a specific browser
playwright install webkit
```
## Writting the first tests
### Overall for the terms: Locators, Actions and Assertion
**Locators** are the central piece of Playwright's auto-waiting and retry-ability. Generally, locators represent a way to find element(s) on the page at any moment. [More details](https://playwright.dev/python/docs/locators)
```Python
# Some examples for locator
page.get_by_label("User Name")
page.get_by_label("Password")
page.get_by_role("button", name="Sign in")
```

**Action** is the way Playwright can interact with HTML Input elements such as text inputs, checkboxes, radio buttons, select options, mouse clicks, type characters, keys and shortcuts as well as upload files and focus elements.[More details](https://playwright.dev/python/docs/input)
```Python
# Some examples for action
page.get_by_label("User Name").fill("admin")
page.get_by_label("Password").fill("Admin123@")
page.get_by_role("button", name="Sign in").click()
```

**Assertion** is like a validation for a status of locator. [More details](https://playwright.dev/python/docs/test-assertions)
```Python
# Some examples for assertion
expect(page).to_have_title("Welcome")
expect(page.get_by_role("button", name="Sign in")).to_be_enabled()
expect(page.get_by_text("Name"), "should be logged in").to_be_visible()
```
### An example test using Pytest Playwright
```Python
import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))
```

### An example test using Sync library
```Python
import re
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as sync:
    browser = sync.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
    page.close()
    browser.close()
```

### An example test using Async library
```Python
import re
import asyncio
from playwright.async_api import async_playwright, expect

async def take_screenshot(browser_type):

    browser = await browser_type.launch()
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://playwright.dev/")
    await expect(page).to_have_title(re.compile("Playwright"))
    await browser.close()

async def main():
    async with async_playwright() as p:
        await take_screenshot(p.chromium)

asyncio.run(main())
```
## Generating tests
Playwright will open two windows, a browser window where you interact with the website you wish to test and the Playwright Inspector window where you can record your tests, copy the tests, clear your tests as well as change the language of your tests. [More details](https://playwright.dev/python/docs/codegen-intro)

```Shell
# url is able to be empty or not
playwright codegen <url>
```
<img alt="codegen" src="https://github.com/nthanhhau/Getting_started_Playwright/blob/main/Document/codegent.png" />

## Running & Debugging tests and Trace viewer
### Running tests
```Shell
pytest <options>
```
Some options:
|Options|Description|
|   :---   | :---: |
| --headed | Display UI during testing |
| --browser webkit or firefox or chromium  | Browser is used for testing|
| --tracing on | To create a traceviewer|
| --slomo= value in ms | Create delay to see the actions easy|
| --video=on/off/retain-on-failure | options of video feature|
| --output=path | To store traceviewer and video|

### Debugging tests
```Shell
PWDEBUG=1 pytest -s <test_file>
```
<img alt="codegen" src="https://github.com/nthanhhau/Getting_started_Playwright/blob/main/Document/debug_mode.png" />

### Trace viewer
Capture all the information to investigate the test failure. Playwright trace contains test execution screencast, live DOM snapshots, action explorer, test source and many more.
```Shell
# Need to add a "--tracing on" option for pytest
pytest --tracing on

# To open traceview
playwright show-trace trace.zip
```
<img alt="codegen" src="https://github.com/nthanhhau/Getting_started_Playwright/blob/main/Document/traceview.png" />

## Demo some tests
