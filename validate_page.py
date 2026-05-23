import asyncio
from playwright.async_api import async_playwright
import os

async def validate_page():
    page_url = f"file:///workspace/off-market-real-estate-lead-engine/sales_page/index.html"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        errors = []
        console_errors = []

        # Capture console errors
        page.on("console", lambda msg: console_errors.append(f"{msg.type}: {msg.text}") if msg.type == "error" else None)

        # Capture page errors
        page.on("pageerror", lambda exc: errors.append(str(exc)))

        try:
            await page.goto(page_url, wait_until="networkidle")
            await asyncio.sleep(1)

            print("Page loaded successfully!")
            print(f"Title: {await page.title()}")

            # Check for any failed resources
            failed_requests = []
            page.on("response", lambda response: failed_requests.append(f"FAILED: {response.url}") if response.status >= 400 else None)

            await page.reload(wait_until="networkidle")

            if errors:
                print("\n⚠️ Page Errors:")
                for e in errors:
                    print(f"  - {e}")
            else:
                print("✓ No page errors")

            if console_errors:
                print("\n⚠️ Console Errors:")
                for e in console_errors:
                    print(f"  - {e}")
            else:
                print("✓ No console errors")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

asyncio.run(validate_page())