import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto(sys.argv[1],wait_until='networkidle')
        for w in [320,390,769,820,900,1024,1280,1414,1920]:
            await pg.set_viewport_size({'width':w,'height':900}); await pg.wait_for_timeout(150)
            r=await pg.evaluate('''()=>[...document.querySelectorAll('.btn')].map(e=>{const last=e.lastElementChild.getBoundingClientRect(),box=e.getBoundingClientRect();return Math.round(box.right-last.right)})''')
            print(w,'arrow-to-edge px',r)
        await b.close()
asyncio.run(main())
