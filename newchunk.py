#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys

import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.text()


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for all_urls in website_list:
            url = all_urls[0]
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        print(responses)


COMPANY_TICKERS_EXCHANGE_URL = "https://www.sec.gov/files/company_tickers_exchange.json"
COMPANY_TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
COMPANY_TICKERS_MF_URL = "https://www.sec.gov/files/company_tickers_mf.json"

urls = (COMPANY_TICKERS_EXCHANGE_URL, COMPANY_TICKERS_MF_URL)
website_list = urls


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
