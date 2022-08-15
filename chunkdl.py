#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import asyncio
import aiohttp

async def fetch1(sem, session, url):
    async with sem, session.get(url) as response:
        async for chunk in response.content.iter_chunked(4096):
            return chunk

async def fetch(sem, session, url):
    async with sem, session.get(url) as response:
        return await response.text()


async def fetch_all(urls, loop):
    sem = asyncio.Semaphore(4) 
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(
            *[fetch1(sem, session, url) for url in urls]
        )

        print(results)
        return results


# testing
if __name__ == "__main__":
    urls = ( COMPANY_TICKERS_EXCHANGE_URL, COMPANY_TICKERS_MF_URL)
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(fetch_all(urls, loop))

