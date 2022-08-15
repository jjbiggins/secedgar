#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


import aiohttp  # pip install aiohttp
import aiofiles  # pip install aiofiles



REPORTS_FOLDER = "reports"
FILES_PATH = os.path.join(REPORTS_FOLDER, "files")



def download_files_from_report(urls):
    os.makedirs(FILES_PATH, exist_ok=True)
    sema = asyncio.BoundedSemaphore(5)

    async def fetch_file(url):
        fname = url.split("/")[-1]


        async with sema, aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                assert resp.status == 200
                data = await resp.read()
                print(data)


        async with aiofiles.open(
            os.path.join(FILES_PATH, fname), "wb"
        ) as outfile:
            await outfile.write(data)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(fetch_file(url)) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


COMPANY_TICKERS_EXCHANGE_URL= "https://www.sec.gov/files/company_tickers_exchange.json"
COMPANY_TICKERS_URL= "https://www.sec.gov/files/company_tickers.json"
COMPANY_TICKERS_MF_URL= "https://www.sec.gov/files/company_tickers_mf.json"

urls = [COMPANY_TICKERS_EXCHANGE_URL, COMPANY_TICKERS_URL]
