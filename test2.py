import asyncio
import os
from pyppeteer import launch

async def main():
    user_profile = os.environ['USERPROFILE']
    chrome_exe = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    user_data_dir = os.path.join(user_profile, "AppData", "Local", "Google", "Chrome", "User Data")

    print(f"Usando user_data_dir: {user_data_dir}")

    browser = await launch(
        headless=False,
        executablePath=chrome_exe,
        args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            f"--user-data-dir={user_data_dir}",
            "--profile-directory=Default"
        ]
    )
    page = await browser.newPage()
    await page.goto("https://example.com")
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.run(main())
