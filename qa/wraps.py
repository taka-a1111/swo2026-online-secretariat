import asyncio,sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto(sys.argv[1],wait_until='networkidle')
        for w in [769,900,1024,1280,1414,1600,1920]:
            await pg.set_viewport_size({'width':w,'height':900}); await pg.wait_for_timeout(150)
            r=await pg.evaluate('''()=>{const out=[];for(const s of ['.col-title','.catch span','.btn','.closing h3','.item-head','.plan-name','.faq-title','.proposal','.sec-title h2']){document.querySelectorAll(s).forEach(e=>{const lh=parseFloat(getComputedStyle(e).lineHeight)||e.getBoundingClientRect().height;const lines=Math.round(e.getBoundingClientRect().height/lh);if(lines>1)out.push(s+':'+e.textContent.trim().slice(0,12)+'×'+lines)})}return out}''')
            print(w, r)
        await b.close()
asyncio.run(main())
