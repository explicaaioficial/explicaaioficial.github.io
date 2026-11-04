import os, shutil
from PIL import Image
OUT='site'; shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT+'/img')
ID='/mnt/project-files/identidade/'
for n in ['mecanica','casa','grana']:
    Image.open(ID+f'perfil-{n}-1080.png').convert('RGB').resize((320,320),Image.LANCZOS).save(f'{OUT}/img/{n}.jpg',quality=88)
shutil.copy('/mnt/project-files/grana-002/planilha_dividas_explicaai.xlsx', OUT+'/planilha_dividas_explicaai.xlsx')
# fotos dos produtos (quadradas, fundo branco); fonte em _fonte/produtos/
FONTE=os.path.dirname(os.path.abspath(__file__))+'/produtos/'
def foto(src,box,dst):
    im=Image.open(FONTE+src).convert('RGB')
    if box: im=im.crop(box)
    w,h=im.size; s=max(w,h); bg=Image.new('RGB',(s,s),'white'); bg.paste(im,((s-w)//2,(s-h)//2))
    bg.resize((240,240),Image.LANCZOS).save(f'{OUT}/img/{dst}',quality=88)
foto('multimetro.png',None,'p-multimetro.jpg')
foto('compressor.png',(60,140,460,1110),'p-compressor.jpg')

ICON={
 'ig':'<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg>',
 'tt':'<svg viewBox="0 0 24 24"><path d="M14 3v11.5a3.5 3.5 0 1 1-3.5-3.5"/><path d="M14 3c.5 3 2.5 5 5.5 5"/></svg>',
 'yt':'<svg viewBox="0 0 24 24"><rect x="2.5" y="5.5" width="19" height="13" rx="4"/><path d="M10 9.3v5.4l4.6-2.7z" fill="currentColor"/></svg>',
 'gift':'<svg viewBox="0 0 24 24"><rect x="3.5" y="9" width="17" height="11.5" rx="2"/><path d="M2.5 9h19M12 9v11.5M12 9c-2-4-6-4-6-1.5S10 9 12 9c2 0 6 1 6-1.5S14 5 12 9"/></svg>',
 'cart':'<svg viewBox="0 0 24 24"><path d="M3 4h2.5l2.3 10.5h10.4L20.5 7H7"/><circle cx="9.5" cy="19" r="1.4"/><circle cx="17" cy="19" r="1.4"/></svg>',
 'star':'<svg viewBox="0 0 24 24"><path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.4 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/></svg>',
}
NICHO={
 'mecanica':dict(nome='Mecânica',titulo='Explica Aí · Mecânica',cor='#FF5A3C',tinta='#fff',frase='Tudo que tem motor, explicado do jeito simples.',
   produtos=[dict(t='Mini compressor de pneu',s='Do vídeo do ABS · palavra PNEU',href='https://meli.la/1pUrf72',ico='cart',img='p-compressor.jpg')]),
 'casa':dict(nome='Casa',titulo='Explica Aí · Casa e Obra',cor='#FFC928',tinta='#0F1A66',frase='Obra, elétrica e encanamento sem mistério.',
   produtos=[dict(t='Multímetro digital',s='Do vídeo do disjuntor · palavra MULTÍMETRO',href='https://meli.la/2dDvaiA',ico='cart',img='p-multimetro.jpg')]),
 'grana':dict(nome='Grana',titulo='Explica Aí · Dinheiro',cor='#22C55E',tinta='#0F1A66',frase='O dinheiro do dia a dia, explicado sem enrolação.',
   produtos=[dict(t='Planilha grátis: todas as dívidas num lugar só',s='Do vídeo do rotativo · palavra JUROS',href='../planilha_dividas_explicaai.xlsx',ico='gift',dl=True)]),
}
CSS='''
:root{--azul:#1D33C9;--amarelo:#FFC928;--coral:#FF5A3C;--tinta:#0F1A66;--branco:#fff}
*{box-sizing:border-box;margin:0}
body{background:var(--azul);color:var(--tinta);font-family:'Fredoka',system-ui,sans-serif;font-weight:500;min-height:100vh;
 background-image:radial-gradient(rgba(255,255,255,.09) 2px,transparent 2px);background-size:26px 26px}
main{max-width:460px;margin:0 auto;padding:34px 16px 40px;display:flex;flex-direction:column;align-items:center}
.ava{width:132px;height:132px;border-radius:50%;border:6px solid #fff;box-shadow:6px 6px 0 var(--tinta);display:block}
h1{margin-top:16px;color:#fff;font-weight:700;font-size:27px;text-align:center;line-height:1.1;
 text-shadow:3px 3px 0 var(--tinta)}
.arroba{margin-top:8px;background:var(--c);color:var(--ct);font-weight:700;font-size:15px;padding:4px 14px;border-radius:99px;
 border:3px solid #fff;box-shadow:3px 3px 0 var(--tinta);transform:rotate(-2deg)}
.frase{margin-top:14px;color:#fff;font-size:16px;text-align:center;opacity:.95}
h2{align-self:flex-start;margin:28px 0 10px 4px;color:var(--amarelo);font-weight:700;font-size:15px;letter-spacing:.08em;text-transform:uppercase}
a.bt,.bt{width:100%;display:flex;align-items:center;gap:14px;text-decoration:none;color:var(--tinta);background:#fff;
 border:4px solid #fff;outline:3px solid var(--tinta);outline-offset:-7px;border-radius:20px;padding:14px 16px;margin-bottom:14px;
 box-shadow:5px 5px 0 var(--tinta);transition:transform .08s,box-shadow .08s}
a.bt:active{transform:translate(4px,4px);box-shadow:1px 1px 0 var(--tinta)}
.bt .ic{flex:none;width:46px;height:46px;border-radius:14px;background:var(--c);color:var(--ct);display:grid;place-items:center;border:3px solid var(--tinta)}
.bt .ph{flex:none;width:72px;height:72px;border-radius:16px;object-fit:contain;background:#fff;border:3px solid var(--tinta)}
.bt .ic svg{width:26px;height:26px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.bt b{display:block;font-weight:700;font-size:17px;line-height:1.15}
.bt small{display:block;font-size:13.5px;opacity:.7;margin-top:2px}
.bt.destaque{background:var(--amarelo);border-color:#fff}
.bt.off{cursor:default}
.tag{margin-left:auto;flex:none;font-size:12px;font-weight:700;background:var(--tinta);color:#fff;padding:3px 9px;border-radius:99px}
.rede{display:flex;gap:12px;width:100%}
.rede a{flex:1;text-decoration:none;text-align:center;background:var(--rc);color:var(--rt);font-weight:700;font-size:15px;
 border:4px solid #fff;border-radius:18px;padding:12px 6px;box-shadow:4px 4px 0 var(--tinta)}
.rede a img{width:54px;height:54px;border-radius:50%;border:3px solid #fff;display:block;margin:0 auto 6px}
.aviso{margin-top:22px;color:#fff;opacity:.8;font-size:12.5px;text-align:center;line-height:1.4}
.carimbo{margin-top:26px;border:4px solid var(--amarelo);color:var(--amarelo);font-weight:700;font-size:20px;padding:6px 18px;border-radius:12px;transform:rotate(-6deg)}
'''
HEAD='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#1D33C9">
<link rel="icon" href="{img}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;700&display=swap" rel="stylesheet"><style>{css}</style></head><body><main style="{vars}">'''
FOOT='<div class="carimbo">Tá explicado ✓</div></main></body></html>'
def bt(t,s,href,ico,cls='',tag='',dl=False,img=None):
    ic=f'<img class="ph" src="../img/{img}" alt="{t}">' if img else f'<span class="ic">{ICON[ico]}</span>'
    inner=ic+f'<span><b>{t}</b><small>{s}</small></span>'+(f'<span class="tag">{tag}</span>' if tag else '')
    if not href: return f'<div class="bt off {cls}">{inner}</div>'
    ext='' if href.startswith('.') else ' target="_blank" rel="noopener"'
    return f'<a class="bt {cls}" href="{href}"{ext}{" download" if dl else ""}>{inner}</a>'
def outros(atual,pre):
    out=''.join(f'<a href="{pre}{k}/" style="--rc:{v["cor"]};--rt:{v["tinta"]}"><img src="{pre}img/{k}.jpg" alt="">{v["nome"]}</a>' for k,v in NICHO.items() if k!=atual)
    return f'<div class="rede">{out}</div>'
AVISO='<p class="aviso">Alguns links são de afiliado: você paga o mesmo preço e o Explica Aí ganha uma pequena comissão.</p>'
YT=bt('YouTube · @explicaibr','Os vídeos longos dos 3 nichos','https://www.youtube.com/@explicaibr','yt')
for k,v in NICHO.items():
    os.makedirs(f'{OUT}/{k}')
    h=HEAD.format(title=v['titulo'],desc=v['frase'],img='../img/'+k+'.jpg',css=CSS,vars=f'--c:{v["cor"]};--ct:{v["tinta"]}')
    h+=f'<img class="ava" src="../img/{k}.jpg" alt="Faísca, mascote do Explica Aí"><h1>{v["titulo"]}</h1><div class="arroba">@explicaai.{k}</div><p class="frase">{v["frase"]}</p>'
    h+='<h2>Comentou, ganhou</h2>'
    if v['produtos']:
        for p in v['produtos']:
            h+=bt(p['t'],p['s'],p['href'],p['ico'],'destaque',tag='' if p['href'] else 'em breve',dl=p.get('dl',False),img=p.get('img'))
    else:
        h+=bt('Achados da obra','As ferramentas dos vídeos aparecem aqui',None,'star','destaque',tag='em breve')
    h+='<h2>Siga o Explica Aí</h2>'
    h+=bt('Instagram',f'@explicaai.{k}',f'https://www.instagram.com/explicaai.{k}/','ig')
    h+=bt('TikTok',f'@explicaai.{k}',f'https://www.tiktok.com/@explicaai.{k}','tt')
    h+=YT+'<h2>Os outros perfis</h2>'+outros(k,'../')+AVISO+FOOT
    open(f'{OUT}/{k}/index.html','w').write(h)
# hub (YouTube)
h=HEAD.format(title='Explica Aí',desc='Explicações animadas de como as coisas funcionam.',img='img/mecanica.jpg',css=CSS,vars='--c:#FFC928;--ct:#0F1A66')
h+='<img class="ava" src="img/mecanica.jpg" alt="Faísca"><h1>Explica Aí</h1><div class="arroba">@explicaibr</div><p class="frase">Como as coisas funcionam, em vídeos animados. Escolha o seu assunto:</p><h2>Escolha o perfil</h2>'
for k,v in NICHO.items():
    h+=f'<a class="bt" href="{k}/" style="--c:{v["cor"]};--ct:{v["tinta"]}"><img src="img/{k}.jpg" alt="" style="width:50px;height:50px;border-radius:50%;border:3px solid var(--tinta)"><span><b>{v["titulo"]}</b><small>{v["frase"]}</small></span></a>'
h+='<h2>Assista</h2>'+YT.replace('Os vídeos longos dos 3 nichos','Vídeos longos e Shorts')+AVISO+FOOT
open(f'{OUT}/index.html','w').write(h)
print('ok')
