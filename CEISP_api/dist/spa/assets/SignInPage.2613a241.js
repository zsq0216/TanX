import{Q as t}from"./QInput.e2d496c4.js";import{X as b,N as V,k as d,o as v,c as P,w as a,a as s,A as p,d as x,$ as c,_ as u}from"./index.72b74f6b.js";import{Q}from"./prevent-scroll.e5f540d1.js";import{u as _,Q as C,b as N,a as h}from"./axios.1562a4a6.js";import{P as m}from"./Loading.f32cb570.js";import"./scroll.7d6d8e83.js";import"./use-dark.d9f79254.js";import"./uid.42677368.js";const $={__name:"SignInPage",setup(k){_();const f=b(),l=V({Tel:"",pwd:"",EnterpriseName:"",mail:"",confirmPassword:""}),g=/^[^\s@]+@[^\s@]+\.[^\s@]+$/,w=()=>{const i=new FormData;Object.keys(l).forEach(o=>{i.append(o,l[o])}),m.show(),console.log("im here"),h.post("http://47.122.24.142:7766/api/register",i,{headers:{"Content-Type":"multipart/form-data"}}).then(o=>{m.hide(),o.status===201?(console.log("success!"),u.create({color:"green-4",textColor:"white",icon:"cloud_done",message:"\u6CE8\u518C\u6210\u529F"}),f.push("/login")):o.status===202?(console.log("\u7528\u6237\u5DF2\u5B58\u5728"),u.create({color:"orange-5",textColor:"white",icon:"warning",message:"\u7528\u6237\u5DF2\u5B58\u5728"})):console.log("\u5176\u4ED6\u60C5\u51B5")}).catch(o=>{console.log(l),console.log("failed!"),m.hide(),console.error("Registration error:",o),u.create({color:"red-5",textColor:"white",icon:"error",message:"\u6CE8\u518C\u5931\u8D25"})})},r=d(!1),n=d(!1),y=()=>{Object.assign(l,{Tel:"",pwd:"",EnterpriseName:"",mail:"",confirmPassword:""})};return(i,o)=>(v(),P(C,{class:"row justify-center"},{default:a(()=>[s(N,{class:"col-5 row justify-center my-custom-margin"},{default:a(()=>[s(Q,{class:"q-gutter-md q-py-xl col-9",onSubmit:w,onReset:y},{default:a(()=>[s(t,{modelValue:l.Tel,"onUpdate:modelValue":o[0]||(o[0]=e=>l.Tel=e),label:"\u624B\u673A\u53F7",rules:[e=>e&&e.length>0||"\u8BF7\u8F93\u5165\u624B\u673A\u53F7"]},null,8,["modelValue","rules"]),s(t,{modelValue:l.EnterpriseName,"onUpdate:modelValue":o[1]||(o[1]=e=>l.EnterpriseName=e),label:"\u4F01\u4E1A\u540D\u79F0",rules:[e=>e&&e.length>0||"\u8BF7\u8F93\u5165\u4F01\u4E1A\u540D\u79F0"]},null,8,["modelValue","rules"]),s(t,{modelValue:l.mail,"onUpdate:modelValue":o[2]||(o[2]=e=>l.mail=e),label:"\u90AE\u7BB1",rules:[e=>e&&e.match(g)||"\u8BF7\u8F93\u5165\u6709\u6548\u7684\u90AE\u7BB1\u5730\u5740"]},null,8,["modelValue","rules"]),s(t,{modelValue:l.pwd,"onUpdate:modelValue":o[4]||(o[4]=e=>l.pwd=e),type:r.value?"text":"password",label:"\u5BC6\u7801",rules:[e=>e&&e.length>0||"\u8BF7\u8F93\u5165\u5BC6\u7801"]},{append:a(()=>[s(p,{name:r.value?"visibility_off":"visibility",class:"cursor-pointer",onClick:o[3]||(o[3]=e=>r.value=!r.value)},null,8,["name"])]),_:1},8,["modelValue","type","rules"]),s(t,{modelValue:l.confirmPassword,"onUpdate:modelValue":o[6]||(o[6]=e=>l.confirmPassword=e),label:"\u786E\u8BA4\u5BC6\u7801",type:n.value?"text":"password",rules:[e=>e&&e===l.pwd||"\u5BC6\u7801\u4E0D\u5339\u914D"]},{append:a(()=>[s(p,{name:n.value?"visibility_off":"visibility",class:"cursor-pointer",onClick:o[5]||(o[5]=e=>n.value=!n.value)},null,8,["name"])]),_:1},8,["modelValue","type","rules"]),x("div",null,[s(c,{label:"\u6CE8\u518C",type:"submit",color:"primary"}),s(c,{label:"\u91CD\u7F6E",type:"reset",color:"primary",flat:"",class:"q-ml-sm"})])]),_:1})]),_:1})]),_:1}))}};export{$ as default};
