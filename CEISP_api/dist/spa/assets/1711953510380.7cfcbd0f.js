import{i as he,j,k as T,f as v,m as ee,t as Ae,u as be,v as Me,R as Fe,h as g,x as fe,y as Ve,z as De,A as G,B as ge,q as te,C as Qe,e as ae,D as ze,E as Ee,l as L,F as He,G as We,H as je,g as Ke,I as Oe,p as Ne}from"./index.72b74f6b.js";import{u as Ue}from"./uid.42677368.js";import{b as me}from"./QLayout.01a6ef7f.js";import{u as p,r as Ge}from"./rtl.49e07ec0.js";import{u as de}from"./use-timeout.c4e98ea7.js";let Xe=0;const Je=["click","keydown"],Ye={icon:String,label:[Number,String],alert:[Boolean,String],alertIcon:String,name:{type:[Number,String],default:()=>`t_${Xe++}`},noCaps:Boolean,tabindex:[String,Number],disable:Boolean,contentClass:String,ripple:{type:[Boolean,Object],default:!0}};function Ze(e,P,w,c){const a=he(be,j);if(a===j)return console.error("QTab/QRouteTab component needs to be child of QTabs"),j;const{proxy:R}=te(),C=T(null),D=T(null),x=T(null),Q=v(()=>e.disable===!0||e.ripple===!1?!1:Object.assign({keyCodes:[13,32],early:!0},e.ripple===!0?{}:e.ripple)),I=v(()=>a.currentModel.value===e.name),z=v(()=>"q-tab relative-position self-stretch flex flex-center text-center"+(I.value===!0?" q-tab--active"+(a.tabProps.value.activeClass?" "+a.tabProps.value.activeClass:"")+(a.tabProps.value.activeColor?` text-${a.tabProps.value.activeColor}`:"")+(a.tabProps.value.activeBgColor?` bg-${a.tabProps.value.activeBgColor}`:""):" q-tab--inactive")+(e.icon&&e.label&&a.tabProps.value.inlineLabel===!1?" q-tab--full":"")+(e.noCaps===!0||a.tabProps.value.noCaps===!0?" q-tab--no-caps":"")+(e.disable===!0?" disabled":" q-focusable q-hoverable cursor-pointer")+(c!==void 0?c.linkClass.value:"")),$=v(()=>"q-tab__content self-stretch flex-center relative-position q-anchor--skip non-selectable "+(a.tabProps.value.inlineLabel===!0?"row no-wrap q-tab__content--inline":"column")+(e.contentClass!==void 0?` ${e.contentClass}`:"")),y=v(()=>e.disable===!0||a.hasFocus.value===!0||I.value===!1&&a.hasActiveTab.value===!0?-1:e.tabindex||0);function _(r,b){if(b!==!0&&C.value!==null&&C.value.focus(),e.disable===!0){c!==void 0&&c.hasRouterLink.value===!0&&fe(r);return}if(c===void 0){a.updateModel({name:e.name}),w("click",r);return}if(c.hasRouterLink.value===!0){const l=(u={})=>{let q;const S=u.to===void 0||Qe(u.to,e.to)===!0?a.avoidRouteWatcher=Ue():null;return c.navigateToRouterLink(r,{...u,returnRouterError:!0}).catch(M=>{q=M}).then(M=>{if(S===a.avoidRouteWatcher&&(a.avoidRouteWatcher=!1,q===void 0&&(M===void 0||M.message!==void 0&&M.message.startsWith("Avoided redundant navigation")===!0)&&a.updateModel({name:e.name})),u.returnRouterError===!0)return q!==void 0?Promise.reject(q):M})};w("click",r,l),r.defaultPrevented!==!0&&l();return}w("click",r)}function h(r){Ve(r,[13,32])?_(r,!0):De(r)!==!0&&r.keyCode>=35&&r.keyCode<=40&&r.altKey!==!0&&r.metaKey!==!0&&a.onKbdNavigate(r.keyCode,R.$el)===!0&&fe(r),w("keydown",r)}function k(){const r=a.tabProps.value.narrowIndicator,b=[],l=g("div",{ref:x,class:["q-tab__indicator",a.tabProps.value.indicatorClass]});e.icon!==void 0&&b.push(g(G,{class:"q-tab__icon",name:e.icon})),e.label!==void 0&&b.push(g("div",{class:"q-tab__label"},e.label)),e.alert!==!1&&b.push(e.alertIcon!==void 0?g(G,{class:"q-tab__alert-icon",color:e.alert!==!0?e.alert:void 0,name:e.alertIcon}):g("div",{class:"q-tab__alert"+(e.alert!==!0?` text-${e.alert}`:"")})),r===!0&&b.push(l);const u=[g("div",{class:"q-focus-helper",tabindex:-1,ref:C}),g("div",{class:$.value},ge(P.default,b))];return r===!1&&u.push(l),u}const A={name:v(()=>e.name),rootRef:D,tabIndicatorRef:x,routeData:c};ee(()=>{a.unregisterTab(A)}),Ae(()=>{a.registerTab(A)});function E(r,b){const l={ref:D,class:z.value,tabindex:y.value,role:"tab","aria-selected":I.value===!0?"true":"false","aria-disabled":e.disable===!0?"true":void 0,onClick:_,onKeydown:h,...b};return Me(g(r,l,k()),[[Fe,Q.value]])}return{renderTab:E,$tabs:a}}var rt=ae({name:"QRouteTab",props:{...ze,...Ye},emits:Je,setup(e,{slots:P,emit:w}){const c=Ee({useDisableForRouterLinkProps:!1}),{renderTab:a,$tabs:R}=Ze(e,P,w,{exact:v(()=>e.exact),...c});return L(()=>`${e.name} | ${e.exact} | ${(c.resolvedLink.value||{}).href}`,()=>{R.verifyRouteModel()}),()=>a(c.linkTag.value,c.linkAttrs.value)}});function pe(e,P,w){const c=w===!0?["left","right"]:["top","bottom"];return`absolute-${P===!0?c[0]:c[1]}${e?` text-${e}`:""}`}const et=["left","center","right","justify"];var it=ae({name:"QTabs",props:{modelValue:[Number,String],align:{type:String,default:"center",validator:e=>et.includes(e)},breakpoint:{type:[String,Number],default:600},vertical:Boolean,shrink:Boolean,stretch:Boolean,activeClass:String,activeColor:String,activeBgColor:String,indicatorColor:String,leftIcon:String,rightIcon:String,outsideArrows:Boolean,mobileArrows:Boolean,switchIndicator:Boolean,narrowIndicator:Boolean,inlineLabel:Boolean,noCaps:Boolean,dense:Boolean,contentClass:String,"onUpdate:modelValue":[Function,Array]},setup(e,{slots:P,emit:w}){const{proxy:c}=te(),{$q:a}=c,{registerTick:R}=p(),{registerTick:C}=p(),{registerTick:D}=p(),{registerTimeout:x,removeTimeout:Q}=de(),{registerTimeout:I,removeTimeout:z}=de(),$=T(null),y=T(null),_=T(e.modelValue),h=T(!1),k=T(!0),A=T(!1),E=T(!1),r=[],b=T(0),l=T(!1);let u=null,q=null,S;const M=v(()=>({activeClass:e.activeClass,activeColor:e.activeColor,activeBgColor:e.activeBgColor,indicatorClass:pe(e.indicatorColor,e.switchIndicator,e.vertical),narrowIndicator:e.narrowIndicator,inlineLabel:e.inlineLabel,noCaps:e.noCaps})),Te=v(()=>{const t=b.value,n=_.value;for(let o=0;o<t;o++)if(r[o].name.value===n)return!0;return!1}),ye=v(()=>`q-tabs__content--align-${h.value===!0?"left":E.value===!0?"justify":e.align}`),we=v(()=>`q-tabs row no-wrap items-center q-tabs--${h.value===!0?"":"not-"}scrollable q-tabs--${e.vertical===!0?"vertical":"horizontal"} q-tabs__arrows--${e.outsideArrows===!0?"outside":"inside"} q-tabs--mobile-with${e.mobileArrows===!0?"":"out"}-arrows`+(e.dense===!0?" q-tabs--dense":"")+(e.shrink===!0?" col-shrink":"")+(e.stretch===!0?" self-stretch":"")),Ce=v(()=>"q-tabs__content scroll--mobile row no-wrap items-center self-stretch hide-scrollbar relative-position "+ye.value+(e.contentClass!==void 0?` ${e.contentClass}`:"")),K=v(()=>e.vertical===!0?{container:"height",content:"offsetHeight",scroll:"scrollHeight"}:{container:"width",content:"offsetWidth",scroll:"scrollWidth"}),O=v(()=>e.vertical!==!0&&a.lang.rtl===!0),X=v(()=>Ge===!1&&O.value===!0);L(O,W),L(()=>e.modelValue,t=>{J({name:t,setCurrent:!0,skipEmit:!0})}),L(()=>e.outsideArrows,N);function J({name:t,setCurrent:n,skipEmit:o}){_.value!==t&&(o!==!0&&e["onUpdate:modelValue"]!==void 0&&w("update:modelValue",t),(n===!0||e["onUpdate:modelValue"]===void 0)&&(qe(_.value,t),_.value=t))}function N(){R(()=>{ne({width:$.value.offsetWidth,height:$.value.offsetHeight})})}function ne(t){if(K.value===void 0||y.value===null)return;const n=t[K.value.container],o=Math.min(y.value[K.value.scroll],Array.prototype.reduce.call(y.value.children,(d,s)=>d+(s[K.value.content]||0),0)),f=n>0&&o>n;h.value=f,f===!0&&C(W),E.value=n<parseInt(e.breakpoint,10)}function qe(t,n){const o=t!=null&&t!==""?r.find(d=>d.name.value===t):null,f=n!=null&&n!==""?r.find(d=>d.name.value===n):null;if(o&&f){const d=o.tabIndicatorRef.value,s=f.tabIndicatorRef.value;u!==null&&(clearTimeout(u),u=null),d.style.transition="none",d.style.transform="none",s.style.transition="none",s.style.transform="none";const i=d.getBoundingClientRect(),m=s.getBoundingClientRect();s.style.transform=e.vertical===!0?`translate3d(0,${i.top-m.top}px,0) scale3d(1,${m.height?i.height/m.height:1},1)`:`translate3d(${i.left-m.left}px,0,0) scale3d(${m.width?i.width/m.width:1},1,1)`,D(()=>{u=setTimeout(()=>{u=null,s.style.transition="transform .25s cubic-bezier(.4, 0, .2, 1)",s.style.transform="none"},70)})}f&&h.value===!0&&H(f.rootRef.value)}function H(t){const{left:n,width:o,top:f,height:d}=y.value.getBoundingClientRect(),s=t.getBoundingClientRect();let i=e.vertical===!0?s.top-f:s.left-n;if(i<0){y.value[e.vertical===!0?"scrollTop":"scrollLeft"]+=Math.floor(i),W();return}i+=e.vertical===!0?s.height-d:s.width-o,i>0&&(y.value[e.vertical===!0?"scrollTop":"scrollLeft"]+=Math.ceil(i),W())}function W(){const t=y.value;if(t===null)return;const n=t.getBoundingClientRect(),o=e.vertical===!0?t.scrollTop:Math.abs(t.scrollLeft);O.value===!0?(k.value=Math.ceil(o+n.width)<t.scrollWidth-1,A.value=o>0):(k.value=o>0,A.value=e.vertical===!0?Math.ceil(o+n.height)<t.scrollHeight:Math.ceil(o+n.width)<t.scrollWidth)}function le(t){q!==null&&clearInterval(q),q=setInterval(()=>{ke(t)===!0&&F()},5)}function oe(){le(X.value===!0?Number.MAX_SAFE_INTEGER:0)}function re(){le(X.value===!0?0:Number.MAX_SAFE_INTEGER)}function F(){q!==null&&(clearInterval(q),q=null)}function Re(t,n){const o=Array.prototype.filter.call(y.value.children,m=>m===n||m.matches&&m.matches(".q-tab.q-focusable")===!0),f=o.length;if(f===0)return;if(t===36)return H(o[0]),o[0].focus(),!0;if(t===35)return H(o[f-1]),o[f-1].focus(),!0;const d=t===(e.vertical===!0?38:37),s=t===(e.vertical===!0?40:39),i=d===!0?-1:s===!0?1:void 0;if(i!==void 0){const m=O.value===!0?-1:1,B=o.indexOf(n)+i*m;return B>=0&&B<f&&(H(o[B]),o[B].focus({preventScroll:!0})),!0}}const _e=v(()=>X.value===!0?{get:t=>Math.abs(t.scrollLeft),set:(t,n)=>{t.scrollLeft=-n}}:e.vertical===!0?{get:t=>t.scrollTop,set:(t,n)=>{t.scrollTop=n}}:{get:t=>t.scrollLeft,set:(t,n)=>{t.scrollLeft=n}});function ke(t){const n=y.value,{get:o,set:f}=_e.value;let d=!1,s=o(n);const i=t<s?-1:1;return s+=i*5,s<0?(d=!0,s=0):(i===-1&&s<=t||i===1&&s>=t)&&(d=!0,s=t),f(n,s),W(),d}function ie(t,n){for(const o in t)if(t[o]!==n[o])return!1;return!0}function Le(){let t=null,n={matchedLen:0,queryDiff:9999,hrefLen:0};const o=r.filter(i=>i.routeData!==void 0&&i.routeData.hasRouterLink.value===!0),{hash:f,query:d}=c.$route,s=Object.keys(d).length;for(const i of o){const m=i.routeData.exact.value===!0;if(i.routeData[m===!0?"linkIsExactActive":"linkIsActive"].value!==!0)continue;const{hash:B,query:Y,matched:$e,href:Be}=i.routeData.resolvedLink.value,Z=Object.keys(Y).length;if(m===!0){if(B!==f||Z!==s||ie(d,Y)===!1)continue;t=i.name.value;break}if(B!==""&&B!==f||Z!==0&&ie(Y,d)===!1)continue;const V={matchedLen:$e.length,queryDiff:s-Z,hrefLen:Be.length-B.length};if(V.matchedLen>n.matchedLen){t=i.name.value,n=V;continue}else if(V.matchedLen!==n.matchedLen)continue;if(V.queryDiff<n.queryDiff)t=i.name.value,n=V;else if(V.queryDiff!==n.queryDiff)continue;V.hrefLen>n.hrefLen&&(t=i.name.value,n=V)}t===null&&r.some(i=>i.routeData===void 0&&i.name.value===_.value)===!0||J({name:t,setCurrent:!0})}function Se(t){if(Q(),l.value!==!0&&$.value!==null&&t.target&&typeof t.target.closest=="function"){const n=t.target.closest(".q-tab");n&&$.value.contains(n)===!0&&(l.value=!0,h.value===!0&&H(n))}}function Pe(){x(()=>{l.value=!1},30)}function U(){se.avoidRouteWatcher===!1?I(Le):z()}function ue(){if(S===void 0){const t=L(()=>c.$route.fullPath,U);S=()=>{t(),S=void 0}}}function xe(t){r.push(t),b.value++,N(),t.routeData===void 0||c.$route===void 0?I(()=>{if(h.value===!0){const n=_.value,o=n!=null&&n!==""?r.find(f=>f.name.value===n):null;o&&H(o.rootRef.value)}}):(ue(),t.routeData.hasRouterLink.value===!0&&U())}function Ie(t){r.splice(r.indexOf(t),1),b.value--,N(),S!==void 0&&t.routeData!==void 0&&(r.every(n=>n.routeData===void 0)===!0&&S(),U())}const se={currentModel:_,tabProps:M,hasFocus:l,hasActiveTab:Te,registerTab:xe,unregisterTab:Ie,verifyRouteModel:U,updateModel:J,onKbdNavigate:Re,avoidRouteWatcher:!1};He(be,se);function ce(){u!==null&&clearTimeout(u),F(),S!==void 0&&S()}let ve;return ee(ce),We(()=>{ve=S!==void 0,ce()}),je(()=>{ve===!0&&ue(),N()}),()=>g("div",{ref:$,class:we.value,role:"tablist",onFocusin:Se,onFocusout:Pe},[g(me,{onResize:ne}),g("div",{ref:y,class:Ce.value,onScroll:W},Ke(P.default)),g(G,{class:"q-tabs__arrow q-tabs__arrow--left absolute q-tab__icon"+(k.value===!0?"":" q-tabs__arrow--faded"),name:e.leftIcon||a.iconSet.tabs[e.vertical===!0?"up":"left"],onMousedownPassive:oe,onTouchstartPassive:oe,onMouseupPassive:F,onMouseleavePassive:F,onTouchendPassive:F}),g(G,{class:"q-tabs__arrow q-tabs__arrow--right absolute q-tab__icon"+(A.value===!0?"":" q-tabs__arrow--faded"),name:e.rightIcon||a.iconSet.tabs[e.vertical===!0?"down":"right"],onMousedownPassive:re,onTouchstartPassive:re,onMouseupPassive:F,onMouseleavePassive:F,onTouchendPassive:F})])}}),ut=ae({name:"QFooter",props:{modelValue:{type:Boolean,default:!0},reveal:Boolean,bordered:Boolean,elevated:Boolean,heightHint:{type:[String,Number],default:50}},emits:["reveal","focusin"],setup(e,{slots:P,emit:w}){const{proxy:{$q:c}}=te(),a=he(Ne,j);if(a===j)return console.error("QFooter needs to be child of QLayout"),j;const R=T(parseInt(e.heightHint,10)),C=T(!0),D=T(Oe.value===!0||a.isContainer.value===!0?0:window.innerHeight),x=v(()=>e.reveal===!0||a.view.value.indexOf("F")!==-1||c.platform.is.ios&&a.isContainer.value===!0),Q=v(()=>a.isContainer.value===!0?a.containerHeight.value:D.value),I=v(()=>{if(e.modelValue!==!0)return 0;if(x.value===!0)return C.value===!0?R.value:0;const l=a.scroll.value.position+Q.value+R.value-a.height.value;return l>0?l:0}),z=v(()=>e.modelValue!==!0||x.value===!0&&C.value!==!0),$=v(()=>e.modelValue===!0&&z.value===!0&&e.reveal===!0),y=v(()=>"q-footer q-layout__section--marginal "+(x.value===!0?"fixed":"absolute")+"-bottom"+(e.bordered===!0?" q-footer--bordered":"")+(z.value===!0?" q-footer--hidden":"")+(e.modelValue!==!0?" q-layout--prevent-focus"+(x.value!==!0?" hidden":""):"")),_=v(()=>{const l=a.rows.value.bottom,u={};return l[0]==="l"&&a.left.space===!0&&(u[c.lang.rtl===!0?"right":"left"]=`${a.left.size}px`),l[2]==="r"&&a.right.space===!0&&(u[c.lang.rtl===!0?"left":"right"]=`${a.right.size}px`),u});function h(l,u){a.update("footer",l,u)}function k(l,u){l.value!==u&&(l.value=u)}function A({height:l}){k(R,l),h("size",l)}function E(){if(e.reveal!==!0)return;const{direction:l,position:u,inflectionPoint:q}=a.scroll.value;k(C,l==="up"||u-q<100||a.height.value-Q.value-u-R.value<300)}function r(l){$.value===!0&&k(C,!0),w("focusin",l)}L(()=>e.modelValue,l=>{h("space",l),k(C,!0),a.animate()}),L(I,l=>{h("offset",l)}),L(()=>e.reveal,l=>{l===!1&&k(C,e.modelValue)}),L(C,l=>{a.animate(),w("reveal",l)}),L([R,a.scroll,a.height],E),L(()=>c.screen.height,l=>{a.isContainer.value!==!0&&k(D,l)});const b={};return a.instances.footer=b,e.modelValue===!0&&h("size",R.value),h("space",e.modelValue),h("offset",I.value),ee(()=>{a.instances.footer===b&&(a.instances.footer=void 0,h("size",0),h("offset",0),h("space",!1))}),()=>{const l=ge(P.default,[g(me,{debounce:0,onResize:A})]);return e.elevated===!0&&l.push(g("div",{class:"q-layout__shadow absolute-full overflow-hidden no-pointer-events"})),g("footer",{class:y.value,style:_.value,onFocusin:r},l)}}}),st="/assets/1711953510380.465f110e.png";export{it as Q,st as _,rt as a,ut as b};