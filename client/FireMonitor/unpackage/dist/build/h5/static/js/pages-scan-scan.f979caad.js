(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-scan-scan"],{"400b":function(t,e,n){"use strict";n.r(e);var i=n("479f"),a=n("e156");for(var o in a)"default"!==o&&function(t){n.d(e,t,function(){return a[t]})}(o);var s,c=n("f0c5"),f=Object(c["a"])(a["default"],i["b"],i["c"],!1,null,"76bf80c2",null,!1,i["a"],s);e["default"]=f.exports},"479f":function(t,e,n){"use strict";var i,a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-uni-view")},o=[];n.d(e,"b",function(){return a}),n.d(e,"c",function(){return o}),n.d(e,"a",function(){return i})},c768:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var i=null,a={data:function(){return{flash:!1,title:"扫描设备信息",tips:"请将二维码置于扫码框内",light:"轻触照亮",album:"相册",cancel:"用戶取消选择",error:"无法识别"}},onLoad:function(t){var e=getCurrentPages();e[e.length-1]},methods:{galleryImg:function(){var t=this;plus.gallery.pick(function(e){t.scanImg(e)},function(e){t.tip(t.$t("scan.cancel")),i.start()},{filter:"image"})},scanImg:function(t){var e=this;plus.barcode.scan(t,function(t,n){e.onmarked(t,n)},function(t){e.tip(e.$t("scan.error")),i.start()})},onmarked:function(t,e){switch(t){case plus.barcode.QR:"QR: ";break;case plus.barcode.EAN13:"EAN13: ";break;case plus.barcode.EAN8:"EAN8: ";break}plus.navigator.setFullscreen(!1),uni.navigateBack({delta:1}),uni.$emit("scanResult",{result:e}),i.close()},createBarcode:function(t){i=plus.barcode.create("barcode",[plus.barcode.QR],{top:"0",left:"0",width:"100%",height:"100%",scanbarColor:"#1DA7FF",position:"static",frameColor:"#1DA7FF"}),i.onmarked=this.onmarked,i.setFlash(this.flash),t.append(i),i.start()},createView:function(t){var e=this,n=new plus.nativeObj.View("backView",{top:"0px",left:"0px",height:"40px",width:"40px"},[{tag:"img",id:"backBar",src:"static/backBar.png",position:{top:"10px",left:"5px",width:"35px",height:"35px"}}]),a=new plus.nativeObj.View("albumView",{top:"0px",left:"78%",height:"40px",width:"70px"},[{tag:"font",id:"openAlbum",text:e.album,textStyles:{size:"18px",color:"#ffffff"},position:{top:"10px",left:"10px",width:"70px",height:"40px"}}]),o=new plus.nativeObj.View("scanBarView",{top:"60%",left:"40%",height:"10%",width:"20%"},[{tag:"img",id:"scanBar",src:"static/scanBar.png",position:{width:"28%",left:"36%",height:"30%",top:"50px"}},{tag:"font",id:"font",text:e.light,textStyles:{size:"10px",color:"#ffffff"},position:{top:"55px",width:"80%",left:"10%"}}]),s=new plus.nativeObj.View("content",{top:"0px",left:"0px",height:"100%",width:"100%"},[{tag:"font",id:"scanTitle",text:e.title,textStyles:{size:"18px",color:"#ffffff"},position:{top:"20px",left:"0px",width:"100%",height:"40px"}},{tag:"font",id:"scanTips",text:e.tips,textStyles:{size:"14px",color:"#ffffff",whiteSpace:"normal"},position:{top:"90px",left:"10%",width:"80%",height:"wrap_content"}}]);n.interceptTouchEvent(!0),o.interceptTouchEvent(!0),t.append(s),t.append(o),t.append(n),t.append(a),n.addEventListener("click",function(t){uni.navigateBack({delta:1}),i.close(),plus.navigator.setFullscreen(!1)},!1),a.addEventListener("click",function(t){e.galleryImg()},!1),o.addEventListener("click",function(t){e.flash=!e.flash,e.flash?o.draw([{tag:"img",id:"scanBar",src:"static/yellow-scanBar.png",position:{width:"28%",left:"36%",height:"30%",top:"50px"}},{tag:"font",id:"font",text:e.light,textStyles:{size:"10px",color:"#ffffff"},position:{top:"55px",width:"80%",left:"10%"}}]):o.draw([{tag:"img",id:"scanBar",src:"static/scanBar.png",position:{width:"28%",left:"36%",height:"30%",top:"50px"}},{tag:"font",id:"font",text:e.light,textStyles:{size:"10px",color:"#ffffff"},position:{top:"55px",width:"80%",left:"10%"}}]),i&&i.setFlash(e.flash)},!1)}},onBackPress:function(){},onUnload:function(){plus.navigator.setFullscreen(!1)}};e.default=a},e156:function(t,e,n){"use strict";n.r(e);var i=n("c768"),a=n.n(i);for(var o in i)"default"!==o&&function(t){n.d(e,t,function(){return i[t]})}(o);e["default"]=a.a}}]);