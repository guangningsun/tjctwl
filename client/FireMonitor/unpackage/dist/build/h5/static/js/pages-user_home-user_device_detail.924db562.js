(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-user_home-user_device_detail"],{"25cc1":function(t,i,e){"use strict";e.r(i);var a=e("b24a"),s=e("d823");for(var n in s)"default"!==n&&function(t){e.d(i,t,function(){return s[t]})}(n);var c,l=e("f0c5"),o=Object(l["a"])(s["default"],a["b"],a["c"],!1,null,"73636c1f",null,!1,a["a"],c);i["default"]=o.exports},b24a:function(t,i,e){"use strict";var a,s=function(){var t=this,i=t.$createElement,e=t._self._c||i;return e("v-uni-view",[e("v-uni-view",{staticClass:"cu-custom",style:[{height:t.CustomBar+"px"}]},[e("v-uni-view",{staticClass:"cu-bar bg-gradual-dark-purple fixed",class:[""!=t.bgImage?"none-bg text-white bg-img":"",t.bgColor],style:t.style},[e("v-uni-view",{staticClass:"action",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.BackPage.apply(void 0,arguments)}}},[e("v-uni-text",{staticClass:"cuIcon-back text-white"})],1),e("v-uni-view",{staticClass:"content",style:[{top:t.StatusBar+"px"}]},[t._v("设备详情")]),e("v-uni-view",{staticClass:"action"},[e("v-uni-text",{staticClass:"cuIcon-more",attrs:{"data-target":"DrawerModalR"},on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.showModal.apply(void 0,arguments)}}})],1)],1)],1),e("v-uni-view",{staticClass:"cu-card"},[e("v-uni-view",{staticClass:"cu-item"},[e("v-uni-view",{staticClass:"bg-white"},[e("v-uni-view",{staticClass:"padding-sm cf"},[e("v-uni-view",{staticClass:"fl flex align-center"},[e("v-uni-image",{staticStyle:{width:"35upx",height:"35upx","margin-right":"15upx"},attrs:{src:"/static/home/signal.png"}}),e("v-uni-view",{staticClass:"cu-tag radius bg-gradual-green text-sm",staticStyle:{"margin-right":"10upx",padding:"8upx"}},[t._v(t._s(t.signal))])],1),e("v-uni-view",{staticClass:"flex fr align-center"},[e("v-uni-image",{staticStyle:{width:"55upx",height:"55upx","margin-right":"15upx"},attrs:{src:"/static/home/battery.png"}}),e("v-uni-view",{staticClass:"cu-tag radius line-black text-xs",staticStyle:{"margin-right":"10upx",padding:"8upx"}},[t._v(t._s(t.battery))])],1)],1),e("v-uni-view",{staticClass:"flex justify-center margin-top margin-bottom"},[e("img",{staticStyle:{width:"150upx",height:"150upx"},attrs:{src:t.image,onerror:t.default_img}})])],1),e("v-uni-view",{staticClass:"flex cu-form-group"},[e("v-uni-view",{staticClass:"title"},[t._v("设备编码")]),e("v-uni-view",[t._v(t._s(t.code))])],1),e("v-uni-view",{staticClass:"flex cu-form-group"},[e("v-uni-view",{staticClass:"title"},[t._v("设备名称")]),e("v-uni-view",[t._v(t._s(t.name))])],1),e("v-uni-view",{staticClass:"flex cu-form-group"},[e("v-uni-view",{staticClass:"title"},[t._v("设备类型")]),e("v-uni-view",[t._v(t._s(t.model))])],1),e("v-uni-view",{staticClass:"flex cu-form-group"},[e("v-uni-view",{staticClass:"title"},[t._v("地址")]),e("v-uni-view",[t._v(t._s(t.address))])],1),e("v-uni-view",{staticClass:"flex cu-form-group"},[e("v-uni-view",{staticClass:"title"},[t._v("安装位置")]),e("v-uni-view",[t._v(t._s(t.location))])],1)],1)],1),e("v-uni-view",{staticClass:"justify-between bottom-box"},[e("v-uni-view",{staticClass:"padding flex flex-direction"},[e("v-uni-button",{staticClass:"cu-btn bg-dark-purple lg",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.onModifyDevice.apply(void 0,arguments)}}},[t._v("修改信息")])],1)],1),e("v-uni-view",{staticClass:"cu-modal drawer-modal justify-end",class:"DrawerModalR"==t.modalName?"show":"",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.hideModal.apply(void 0,arguments)}}},[e("v-uni-view",{staticClass:"cu-dialog basis-lg",style:[{top:t.CustomBar+"px",height:"calc(100vh - "+t.CustomBar+"px)"}],on:{click:function(i){i.stopPropagation(),arguments[0]=i=t.$handleEvent(i)}}},[e("v-uni-view",{staticClass:"cu-list menu"},[e("v-uni-view",{staticClass:"cu-item"},[e("v-uni-button",{staticClass:"cu-btn content",attrs:{"data-target":"DeleteModal"},on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.showModal.apply(void 0,arguments)}}},[e("v-uni-text",{staticClass:"cuIcon-deletefill text-red"}),e("v-uni-text",{staticClass:"text-black"},[t._v("删除设备")])],1)],1),e("v-uni-view",{staticClass:"cu-item",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.onDownloadQrCode.apply(void 0,arguments)}}},[e("v-uni-button",{staticClass:"cu-btn content"},[e("v-uni-text",{staticClass:"cuIcon-down text-olive"}),e("v-uni-text",{staticClass:"text-black"},[t._v("下载二维码")])],1)],1),e("v-uni-view",{staticClass:"cu-item"},[e("v-uni-button",{staticClass:"cu-btn content"},[e("v-uni-text",{staticClass:"cuIcon-share text-light-orange"}),e("v-uni-text",{staticClass:"text-black"},[t._v("分享")])],1)],1)],1)],1)],1),e("v-uni-view",{staticClass:"cu-modal",class:"DeleteModal"==t.modalName?"show":""},[e("v-uni-view",{staticClass:"cu-dialog"},[e("v-uni-view",{staticClass:"cu-bar bg-white justify-end"},[e("v-uni-view",{staticClass:"content"},[t._v("删除设备")]),e("v-uni-view",{staticClass:"action",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.hideModal.apply(void 0,arguments)}}},[e("v-uni-text",{staticClass:"cuIcon-close text-light-purple"})],1)],1),e("v-uni-view",{staticClass:"padding-xl"},[t._v("是否删除当前设备？")]),e("v-uni-view",{staticClass:"cu-bar bg-white justify-end"},[e("v-uni-view",{staticClass:"action"},[e("v-uni-button",{staticClass:"cu-btn line-green text-purple",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.hideModal.apply(void 0,arguments)}}},[t._v("取消")]),e("v-uni-button",{staticClass:"cu-btn bg-gradual-dark-purple margin-left",on:{click:function(i){arguments[0]=i=t.$handleEvent(i),t.onConfirmDelete.apply(void 0,arguments)}}},[t._v("确定")])],1)],1)],1)],1)],1)},n=[];e.d(i,"b",function(){return s}),e.d(i,"c",function(){return n}),e.d(i,"a",function(){return a})},d823:function(t,i,e){"use strict";e.r(i);var a=e("ff19"),s=e.n(a);for(var n in a)"default"!==n&&function(t){e.d(i,t,function(){return a[t]})}(n);i["default"]=s.a},ff19:function(t,i,e){"use strict";Object.defineProperty(i,"__esModule",{value:!0}),i.default=void 0;var a={data:function(){return{StatusBar:this.StatusBar,CustomBar:this.CustomBar,modalName:null,code:"",name:"",model:"",address:"",location:"",signal:"",battery:"",image:"",default_img:'this.src="'+e("9c4c")+'"'}},computed:{style:function(){var t=this.StatusBar,i=this.CustomBar,e=this.bgImage,a="height:".concat(i,"px;padding-top:").concat(t,"px;");return this.bgImage&&(a="".concat(a,"background-image:url(").concat(e,");")),a}},onLoad:function(t){var i=JSON.parse(t.deviceInfo);this.code=i.code,this.name=i.name,this.model=i.model,this.address=i.address,this.location=i.location,this.signal=i.signal,this.battery=i.battery,this.image=i.image},props:{bgColor:{type:String,default:""},isBack:{type:[Boolean,String],default:!1},bgImage:{type:String,default:""}},methods:{showModal:function(t){this.modalName=t.currentTarget.dataset.target},hideModal:function(t){this.modalName=null},onModifyDevice:function(t){},BackPage:function(){uni.navigateBack({delta:1})},successDeleteCb:function(t){console.log("success delete cb"),0===t.data.error&&(uni.hideLoading(),this.showToast("成功删除设备"),setTimeout(function(){uni.navigateBack({delta:1})},1500))},failDeleteCb:function(t){console.log("api_bound_device failed",t)},completeDeleteCb:function(t){},onConfirmDelete:function(t){this.hideModal(),uni.showLoading({title:"正在删除设备..."});var i=getApp().globalData.user_id;this.isEmpty(i)&&(i=uni.getStorageSync("key_user_id"));var e={device_sn:this.code};this.requestWithMethod(getApp().globalData.api_device_opt+i+"/","DELETE",e,this.successDeleteCb,this.failDeleteCb,this.completeDeleteCb)},onDownloadQrCode:function(t){this.hideModal(t),plus.gallery.save("../../static/logo.png",function(){uni.showToast({title:"保存成功",icon:"none"})},function(){uni.showToast({title:"保存失败，请重试！",icon:"none"})})}}};i.default=a}}]);