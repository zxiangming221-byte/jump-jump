text = open('D:/games/jump-jump/index.html','r',encoding='utf-8').read()

# 1. Add IMG2
old = "const IMG=new Image();IMG.src='image/54da03339b65fa3e8573988486072b74.png';"
new = "const IMG=new Image();IMG.src='image/54da03339b65fa3e8573988486072b74.png';const IMG2=new Image();IMG2.src='image/ca56734a7a7b856c64b915bc96c6d765.png';"
text = text.replace(old, new)

# 2. Add PRIZES2 pool
old2 = "const RARITY_WEIGHT={common:65,rare:23,epic:10,legend:2};"
pool2 = """const PRIZES2=[{id:'q01',n:'螺丝钉',ico:'🔩',r:'common'},{id:'q02',n:'齿轮',ico:'⚙️',r:'common'},{id:'q03',n:'弹簧',ico:'🪫',r:'common'},{id:'q04',n:'螺母',ico:'🔧',r:'common'},{id:'q05',n:'电路板',ico:'💾',r:'common'},{id:'q06',n:'电线',ico:'🔌',r:'common'},{id:'q07',n:'芯片',ico:'💿',r:'common'},{id:'q08',n:'天线',ico:'📡',r:'common'},{id:'q09',n:'电池',ico:'🔋',r:'common'},{id:'q10',n:'传感器',ico:'📟',r:'common'},{id:'q11',n:'合金装甲',ico:'🛡️',r:'rare'},{id:'q12',n:'离子推进器',ico:'🚀',r:'rare'},{id:'q13',n:'导航仪',ico:'🧭',r:'rare'},{id:'q14',n:'能量核心',ico:'⚡',r:'rare'},{id:'q15',n:'引力透镜',ico:'🔮',r:'rare'},{id:'q16',n:'量子芯片',ico:'🖲️',r:'rare'},{id:'q17',n:'暗物质燃料',ico:'🟣',r:'epic'},{id:'q18',n:'曲速引擎',ico:'🌀',r:'epic'},{id:'q19',n:'星图',ico:'🌌',r:'epic'},{id:'q20',n:'航天器',ico:'🛸',r:'legend'}];\nconst RARITY_WEIGHT={common:65,rare:23,epic:10,legend:2};"""
text = text.replace(old2, pool2)

# 3. Pool state
old3 = "let chSel='chess';"
text = text.replace(old3, "let chSel='chess',_pool='default';")

# 4. Update rollPrize
old4 = """function rollPrize(){
  const total=Object.values(RARITY_WEIGHT).reduce((a,b)=>a+b,0);
  let r=Math.random()*total;
  for(const[k,v]of Object.entries(RARITY_WEIGHT)){r-=v;if(r<=0){const pool=PRIZES.filter(p=>p.r===k);return pool[Math.random()*pool.length|0];}}
  return PRIZES[0];
}"""
new4 = """function rollPrize(){
  const total=Object.values(RARITY_WEIGHT).reduce((a,b)=>a+b,0);
  let r=Math.random()*total;
  const src=_pool==='space'?PRIZES2:PRIZES;
  for(const[k,v]of Object.entries(RARITY_WEIGHT)){r-=v;if(r<=0){const pool=src.filter(p=>p.r===k);return pool[Math.random()*pool.length|0];}}
  return src[0];
}"""
text = text.replace(old4, new4)

# 5. Add LZH effect + update doPull
old5 = """function _gachaLegend(){"""
text = text.replace(old5, """function showLZH(){
  var el=document.getElementById('lzhScreen');el.classList.add('show');
  setTimeout(function(){el.classList.remove('show');},1500);
}
function _gachaLegend(){""")

old5b = """  _gachaPull();showPullSequence(results,0);
}"""
text = text.replace(old5b, """  _gachaPull();showPullSequence(results,0);
  if(results.some(p=>p.id==='q20')){setTimeout(function(){showLZH();},800);}
}""")

# 6. Redeem code HWB7878
old6 = """  else if(code==='zxm38966'){st.gold=0;st.dia=0;saveData();updateAllDisplays();msg.style.color='#e74c3c';msg.textContent='🗑️ 金币钻石已清零';}
  else{msg.style.color='#e74c3c';msg.textContent='❌ 兑换码无效';}"""
text = text.replace(old6, """  else if(code==='zxm38966'){st.gold=0;st.dia=0;saveData();updateAllDisplays();msg.style.color='#e74c3c';msg.textContent='🗑️ 金币钻石已清零';}
  else if(code==='HWB7878'){st.col.add('p20');saveData();updateAllDisplays();msg.style.color='#5b9ad5';msg.textContent='🎉 李飞角色已解锁！';}
  else{msg.style.color='#e74c3c';msg.textContent='❌ 兑换码无效';}""")

# 7. buildCharSelect - add space character
old7 = """  const hasLifei=st.col.has('p20');
  const cg=document.getElementById('charGrid'),chars=[
    {id:'chess',name:'国际象棋兵',chess:!0},
    {id:'lifei',name:'李飞',chess:!1,locked:!hasLifei}
  ];"""
text = text.replace(old7, """  const hasLifei=st.col.has('p20'),hasSpace=st.col.has('q20');
  const cg=document.getElementById('charGrid'),chars=[
    {id:'chess',name:'国际象棋兵',chess:!0},
    {id:'lifei',name:'李飞',img:IMG,locked:!hasLifei},
    {id:'space',name:'航天器',img:IMG2,locked:!hasSpace}
  ];""")

# 8. Fix character card image rendering
old8 = """    }else{
      if(IMG.complete&&IMG.naturalWidth){const ih=48,iw=ih*(IMG.naturalWidth/IMG.naturalHeight);cc.drawImage(IMG,(55-iw)/2,60-ih,iw,ih);}
      else{cc.fillStyle='#666';cc.font='10px sans-serif';cc.textAlign='center';cc.fillText('加载中',27,35);}
    }"""
text = text.replace(old8, """    }else{
      var cimg=ch.img||IMG;
      if(cimg.complete&&cimg.naturalWidth){const ih=48,iw=ih*(cimg.naturalWidth/cimg.naturalHeight);cc.drawImage(cimg,(55-iw)/2,60-ih,iw,ih);}
      else{cc.fillStyle='#666';cc.font='10px sans-serif';cc.textAlign='center';cc.fillText('加载中',27,35);}
    }""")

# 9. drpl - add space
old9 = """  if(chSel==='lifei'){drLifei();}else{drChess();}"""
text = text.replace(old9, """  if(chSel==='space'){drSpace();}else if(chSel==='lifei'){drLifei();}else{drChess();}""")

# 10. Add drSpace function
old10 = """  cx.drawImage(IMG,-cw/2,-ch,cw,ch);
}

// ── 适配形状的影子 ──"""
text = text.replace(old10, """  cx.drawImage(IMG,-cw/2,-ch,cw,ch);
}

function drSpace(){
  if(!IMG2.complete||!IMG2.naturalWidth)return;
  const s=ZM,ch=58*s,cw=ch*(IMG2.naturalWidth/IMG2.naturalHeight);
  cx.drawImage(IMG2,-cw/2,-ch,cw,ch);
}

// ── 适配形状的影子 ──""")

# 11. Shadow for space character
old11 = """  if(chSel==='lifei'){"""
text = text.replace(old11, """  if(chSel==='space'||chSel==='lifei'){""")

old11b = """    const ch2=58*s*pT,cw2=ch2*(IMG.naturalWidth/IMG.naturalHeight);"""
text = text.replace(old11b, """    var simg=chSel==='space'?IMG2:IMG;const ch2=58*s*pT,cw2=ch2*(simg.naturalWidth/simg.naturalHeight);""")

# 12. Collection includes both pools
old12 = """  PRIZES.forEach(p=>{"""
text = text.replace(old12, """  PRIZES.concat(PRIZES2).forEach(p=>{""")

old12b = """  document.getElementById('colProgress').textContent=`已收集 ${unlocked}/${PRIZES.length}`;"""
text = text.replace(old12b, """  document.getElementById('colProgress').textContent=`已收集 ${unlocked}/${PRIZES.length+PRIZES2.length}`;""")

# 13. showPullSummary - space unlock
old13 = """    if(results.some(function(r){return r.id==='p20';})){chSel='lifei';buildCharSelect();}"""
text = text.replace(old13, """    if(results.some(function(r){return r.id==='p20';})){chSel='lifei';buildCharSelect();}
    if(results.some(function(r){return r.id==='q20';})){chSel='space';buildCharSelect();}""")

open('D:/games/jump-jump/index.html','w',encoding='utf-8').write(text)
print('All changes applied')
