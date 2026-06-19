import re

text = open('index.html','r',encoding='utf-8').read()

# Find the old showPullResults function
pattern = r'function showPullResults\(results,idx\)\{.*?^\}'
m = re.search(pattern, text, re.DOTALL | re.MULTILINE)
if not m:
    print("NOT FOUND")
    exit(1)

old = m.group(0)
print(f"FOUND: {len(old)} chars")

new = """function showPullSequence(results,idx){
  const total=results.length;
  if(idx>=total){showPullSummary(results);return;}
  const p=results[idx],dup=results.slice(0,idx).some(r=>r.id===p.id);
  const rc={'common':'普通','rare':'稀有','epic':'史诗','legend':'传说'};
  const rcls='r'+p.r.charAt(0).toUpperCase()+p.r.slice(1);
  const card=document.getElementById('grCard');
  card.className='gachaCard '+rcls+' animIn';card.style.display='';
  document.getElementById('grIcon').textContent=p.ico;
  document.getElementById('grName').textContent=p.n;
  document.getElementById('grRarity').innerHTML='<span class=\"'+rcls+'\">'+rc[p.r]+'</span>';
  const badge=document.getElementById('grBadge');
  if(dup){badge.className='cardBadge dup';badge.textContent='重复 +'+DUP_GOLD[p.r]+'🪙';}
  else{badge.className='cardBadge new';badge.textContent=p.id==='p20'?'🎉 角色解锁!':'新图鉴解锁!';}
  document.getElementById('grSummary').style.display='none';
  document.getElementById('btnGrClose').style.display='none';
  document.getElementById('gachaResult').classList.add('show');
  setTimeout(function(){
    card.classList.remove('animIn');card.classList.add('animOut');
    setTimeout(function(){card.classList.remove('animOut');showPullSequence(results,idx+1);},300);
  },total>1?1200:1800);
}
function showPullSummary(results){
  var card=document.getElementById('grCard');card.style.display='none';
  var sg=document.getElementById('grSummary');sg.style.display='flex';sg.innerHTML='';
  var counted={};
  results.forEach(function(p){var k=p.id;counted[k]=counted[k]||{ico:p.ico,n:p.n,r:p.r,count:0};counted[k].count++;});
  Object.values(counted).forEach(function(p){
    var rcls='r'+p.r.charAt(0).toUpperCase()+p.r.slice(1);
    var d=document.createElement('div');d.className='si '+rcls;
    d.innerHTML='<div class=\"sico\">'+p.ico+'</div><div>'+p.n+'</div>'+(p.count>1?'<div class=\"sdup\">x'+p.count+'</div>':'');
    sg.appendChild(d);
  });
  document.getElementById('btnGrClose').style.display='';
  document.getElementById('btnGrClose').onclick=function(){
    document.getElementById('gachaResult').classList.remove('show');
    card.style.display='';sg.style.display='none';updateAllDisplays();
    if(results.some(function(r){return r.id==='p20';})){chSel='lifei';buildCharSelect();}
  };
}"""

text = text.replace(old, new)
open('index.html','w',encoding='utf-8').write(text)
print("DONE")

# Verify
text2 = open('index.html','r',encoding='utf-8').read()
if 'showPullSequence' in text2 and 'showPullSummary' in text2 and 'showPullResults' not in text2:
    print("VERIFIED OK")
else:
    print("WARNING: verification failed")
