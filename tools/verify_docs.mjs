// Offline source/render-unit checks only; no browser, HTTP or SQL access.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const out=path.join(root,'docs');
const html=fs.readFileSync(path.join(out,'index.html'),'utf8');
const embedded=html.match(/<script type="application\/json" id="catalog">([\s\S]*?)<\/script>/)[1];
const script=html.match(/<script>\s*([\s\S]*?)<\/script>/)[1];
const data=JSON.parse(embedded);
assert.equal(data.models.length,238);
const elements=new Map();
const el=id=>{if(!elements.has(id))elements.set(id,{innerHTML:'',textContent:'',value:'',hidden:true,addEventListener(){},scrollIntoView(){}});return elements.get(id)};
el('catalog').textContent=embedded;
const context=vm.createContext({document:{getElementById:el,addEventListener(){}},location:{hash:''},history:{replaceState(){}},window:{scrollTo(){}},navigator:{}});
new vm.Script(script,{filename:'api-reference-inline.js'}).runInContext(context);
let rendered=0;
for(const m of data.models){
  for(const tab of ['guide','read','fields','errors']){
    vm.runInContext(`selected=${m.code};tab=${JSON.stringify(tab)};render();`,context);
    assert.ok(el('content').innerHTML.includes(`Model ${m.code} /`));
    assert.ok(!el('content').innerHTML.includes('[object Object]'));
    assert.ok(!el('content').innerHTML.includes('\ufffd'));
    rendered++;
  }
}
for(const query of ['BankingOperations','Perakende müşteri','238','FirstName']){
  el('search').value=query;
  vm.runInContext('renderNav()',context);
  assert.ok(el('nav').innerHTML.includes('data-model='),query);
}
el('search').value='MODEL_BULUNMAMALI_ZZZ_9876';vm.runInContext('renderNav()',context);
assert.ok(el('nav').innerHTML.includes('Eşleşen model bulunamadı'));
for(const name of Object.keys(data.types)){
  const result=vm.runInContext(`fields(${JSON.stringify(name)})`,context);
  assert.equal(typeof result,'string');
  assert.ok(!result.includes('[object Object]'));
}
const collection=JSON.parse(fs.readFileSync(path.join(out,'Nebim-V3-238-model.postman_collection.json'),'utf8'));
let requests=0;
for(const [index,folder] of collection.item.entries()){
  assert.ok(folder.name.startsWith(String(index+1).padStart(3,'0')));
  for(const item of folder.item){
    assert.ok(['GET','POST'].includes(item.request.method));
    assert.ok(item.request.url.startsWith('{{baseUrl}}/'));
    if(item.request.body)JSON.parse(item.request.body.raw);
    for(const response of item.response||[])JSON.parse(response.body);
    requests++;
  }
}
const validation=JSON.parse(fs.readFileSync(path.join(out,'validation.json'),'utf8'));
validation.renderUnitChecks={passed:true,modelTabRenders:rendered,typeRenders:Object.keys(data.types).length,searchChecks:5,postmanRequests:requests,
  scope:'Node VM with synthetic DOM: script syntax/render functions/search and JSON examples; not a browser visual/clipboard/download/Postman import test',
  browserVisualTestExecuted:false};
fs.writeFileSync(path.join(out,'validation.json'),JSON.stringify(validation,null,2)+'\n');
console.log(JSON.stringify(validation.renderUnitChecks));
