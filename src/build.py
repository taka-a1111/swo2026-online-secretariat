import json
faq=[
 ("何時間から契約できますか？","月20時間からご契約戴けます。",[]),
 ("契約期間の縛りはありますか？","特にありません。",[("お申し込みのプランによって、作業が可能な期間がございます。",False)]),
 ("業務の依頼が可能な時間帯は、何時から何時までですか？","対応時間は、土日・祝日を除く、平日の10時から17時までです。",[]),
 ("想定より作業工数がかからず、時間が余った場合はどうなりますか？","無料で、次月まで時間を繰り越すことが可能です。",[("※ ただし、契約終了月は翌月への繰り越しはできません。",True)]),
 ("業務開始するにあたって「作業マニュアル」は必要ですか？","不要です。",[("作業内容の整理や手順の作成からご支援させて戴きます。お気軽にお問い合わせください。<br>ただし、すでに存在している「作業マニュアル」などの共有をお願いします。",False)]),
 ("コミュニケーションはどうやってとりますか？","基本的にメールにてやりとりさせて戴きます。",[("社内・広報ＳＮＳ・ビジネスチャットの対応に関してもご要望に応じてご相談ください。",False)]),
 ("当初想定していた作業以外に追加で依頼は可能ですか？","お時間内であれば対応可能な内容か否か検討させて戴きます。",[("お時間が不足している場合は追加契約となります。",False)]),
 ("担当するアシスタントはどのように決定されますか？","依頼いただく作業内容を伺い、適切なアシスタントを選任させて戴きます。",[]),
 ("アシスタントの変更指名は可能ですか？","アシスタントの変更や指名は承りかねます。",[]),
]
blocks=[]
for q,a,subs in faq:
    sub=''.join('<span class="sub%s">%s</span>'%(' note' if n else '',x) for x,n in subs)
    blocks.append('      <dl class="qa"><dt><span class="mark">Q</span><span>%s</span></dt><dd><span class="mark">A</span><span><span>%s</span>%s</span></dd></dl>'%(q,a,sub))
ld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a+"".join(x.replace("<br>","") for x,_ in subs)}} for q,a,subs in faq]}
imgs=json.load(open('imgs.json'))
t=open('template.html',encoding='utf8').read()
s=t.replace('{{FAQ}}','\n'.join(blocks)).replace('{{JSONLD}}',json.dumps(ld,ensure_ascii=False,indent=1))
for k,v in imgs.items(): s=s.replace('{{IMG:%s}}'%k,v)
assert '{{' not in s
open('index.html','w',encoding='utf8').write(s)
print(len(s.encode())//1024,'KB')
