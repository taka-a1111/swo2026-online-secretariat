import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':int(sys.argv[2]),'height':900})
        await pg.goto(sys.argv[1],wait_until='networkidle'); await pg.wait_for_timeout(500)
        await pg.screenshot(path=sys.argv[3],full_page=True)
        r=await pg.evaluate('''()=>{const o={};for(const s of ['.hero','#about','#price','#faq','.closing','.footer']){const e=document.querySelector(s);const r=e.getBoundingClientRect();o[s]=[Math.round(r.top+scrollY),Math.round(r.bottom+scrollY)]}return o}''')
        print(r); await b.close()
asyncio.run(main())
