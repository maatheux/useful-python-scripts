import asyncio
import os
import sys
from extract_zip import extractZip
from convert_xlsx_to_csv import convertXlsxToCsv
from move_previous_csv_file import movePreviousCsvFile
from playwright.async_api import async_playwright
from file_exists import fileExists

user = sys.argv[1]
password = sys.argv[2]


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("url")

        await page.get_by_label("Login").fill(user)
        await page.fill("input[name='Senha']", password)
        await page.get_by_text('Entrar').click()

        await page.goto("url")

        recently_database = (await page.get_by_role("option").nth(1).text_content()).strip()

        if not fileExists(r"Downloads\{}".format(recently_database)):
            async with page.expect_download() as download_info:
                await page.locator("#nome").select_option(label=recently_database)

            download = await download_info.value

            user_dir = os.path.expanduser('~')

            final_path = os.path.join(user_dir, r"Downloads\{}".format(recently_database))

            await download.save_as(final_path)
        else:
            sys.exit("Não há uma base nova!")

        await browser.close()

    await asyncio.sleep(1)
    extractZip(
        final_path,
        r"\block\Bases\Historico"
    )

    await asyncio.sleep(1)
    movePreviousCsvFile()

    await asyncio.sleep(1)
    convertXlsxToCsv(
        os.path.join(
            r"\block\Bases\Historico",
            recently_database.replace("zip", "xlsx")
        ),
        os.path.join(
            r"\block\Bases",
            recently_database.replace("zip", "csv")
        )
    )


if __name__ == '__main__':
    asyncio.run(main())
