from pyppeteer import launch
import asyncio

async def main():
    browser = await launch(
        headless=False,
        executablePath="C:/Program Files/Google/Chrome/Application/chrome.exe"
    )
    page = await browser.newPage()
    await page.goto("https://example.com")
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
