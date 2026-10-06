import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page()
        errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
        await pg.goto(sys.argv[1],wait_until='networkidle')
        for w in [320,375,390,414,768,1024,1280,1440]:
            await pg.set_viewport_size({'width':w,'height':900}); await pg.wait_for_timeout(200)
            sw=await pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            over=await pg.evaluate('''[...document.querySelectorAll('.plan-price')].map(e=>e.scrollWidth-e.clientWidth).filter(x=>x>0).length''')
            print(w,'hscroll',sw,'price_overflow',over)
        print('h1',await pg.evaluate('document.querySelectorAll("h1").length'),
              'headings',await pg.evaluate('[...document.querySelectorAll("h1,h2,h3")].map(e=>e.tagName+":"+e.textContent.trim().slice(0,14))'))
        print('anchors',await pg.evaluate('[...document.querySelectorAll("a[href^=\'#\']")].map(a=>a.getAttribute("href")+":"+!!document.querySelector(a.getAttribute("href")))'))
        print('links',await pg.evaluate('[...document.querySelectorAll("a")].map(a=>a.href)'))
        print('font',await pg.evaluate('getComputedStyle(document.body).fontFamily'))
        await pg.set_viewport_size({'width':1280,'height':900})
        await pg.emulate_media(media='print')
        await pg.pdf(path='print_live.pdf',format='A4',print_background=True)
        print('errors',errs)
        await b.close()
asyncio.run(main())
