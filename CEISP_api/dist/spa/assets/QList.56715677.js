import{e as o,f as n,h as d,g as l,q as i}from"./index.72b74f6b.js";import{u,a as c}from"./use-dark.d9f79254.js";var q=o({name:"QList",props:{...u,bordered:Boolean,dense:Boolean,separator:Boolean,padding:Boolean,tag:{type:String,default:"div"}},setup(e,{slots:a}){const t=i(),r=c(e,t.proxy.$q),s=n(()=>"q-list"+(e.bordered===!0?" q-list--bordered":"")+(e.dense===!0?" q-list--dense":"")+(e.separator===!0?" q-list--separator":"")+(r.value===!0?" q-list--dark":"")+(e.padding===!0?" q-list--padding":""));return()=>d(e.tag,{class:s.value},l(a.default))}});export{q as Q};