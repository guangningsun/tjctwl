(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-user_home-user_add_device"],{1664:function(t,e,i){"use strict";i.r(e);var n=i("d338"),a=i.n(n);for(var s in n)"default"!==s&&function(t){i.d(e,t,function(){return n[t]})}(s);e["default"]=a.a},"16c2":function(t,e,i){"use strict";var n,a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-uni-view",[i("cu-custom",{attrs:{bgColor:"bg-gradual-dark-purple",isBack:!0}},[i("template",{attrs:{slot:"content"},slot:"content"},[t._v("添加设备")])],2),i("v-uni-view",{staticClass:"cu-card"},[i("v-uni-view",{staticClass:"cu-item"},[i("v-uni-view",{staticClass:"flex justify-center margin-top margin-bottom-xs",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.openScan.apply(void 0,arguments)}}},[i("v-uni-image",{staticClass:"flex justify-center margin-top margin-bottom-sm",staticStyle:{width:"200upx",height:"200upx"},attrs:{src:"../../static/home/qrcodescan.png"}})],1),i("v-uni-view",{staticClass:"flex justify-center text-gray"},[t._v("扫一扫获取设备基本信息")]),i("v-uni-form",[i("v-uni-view",{staticClass:"cu-form-group margin-top"},[i("v-uni-view",{staticClass:"title"},[t._v("设备编码")]),i("v-uni-input",{attrs:{placeholder:"设备的编码",name:"input"},model:{value:t.device_sn,callback:function(e){t.device_sn=e},expression:"device_sn"}})],1),i("v-uni-view",{staticClass:"cu-form-group"},[i("v-uni-view",{staticClass:"title"},[t._v("设备名称")]),i("v-uni-input",{attrs:{placeholder:"设备的名称",name:"input"},model:{value:t.name,callback:function(e){t.name=e},expression:"name"}})],1),i("v-uni-view",{staticClass:"cu-form-group"},[i("v-uni-view",{staticClass:"title"},[t._v("地址")]),i("v-uni-input",{attrs:{placeholder:"设备所在的地址",name:"input"},model:{value:t.address,callback:function(e){t.address=e},expression:"address"}})],1),i("v-uni-view",{staticClass:"cu-form-group"},[i("v-uni-view",{staticClass:"title"},[t._v("安装位置")]),i("v-uni-input",{attrs:{placeholder:"设备的安装位置",name:"input"},model:{value:t.location,callback:function(e){t.location=e},expression:"location"}})],1)],1)],1),i("v-uni-view",{staticClass:"justify-between bottom-box"},[i("v-uni-view",{staticClass:"padding flex flex-direction"},[i("v-uni-button",{staticClass:"cu-btn bg-dark-purple lg",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.onAddDevice.apply(void 0,arguments)}}},[t._v("添加")])],1)],1)],1)],1)},s=[];i.d(e,"b",function(){return a}),i.d(e,"c",function(){return s}),i.d(e,"a",function(){return n})},d338:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var n={data:function(){return{tel_notic:!1,sms_notic:!1,device_sn:"",name:"",address:"",location:"",shouldRequestModify:!1}},onLoad:function(){var t=this;uni.$on("scanResult",function(e){t.device_sn=e.result})},onUnload:function(){uni.$off("scanResult")},methods:{successUpdateDeviceCb:function(t){uni.hideLoading(),0===t.data.error&&(console.log("successUpdateDeviceCb"),uni.showToast({title:"成功添加设备"})),setTimeout(function(){uni.navigateBack({delta:1})},1500)},failUpdateDeviceCb:function(t){uni.hideLoading(),console.log("api_update_device failed: 设备成功添加，但是修改设备修复失败"+t),this.showToast("设备成功添加，但是修改设备修复失败"),setTimeout(function(){uni.navigateBack({delta:1})},1500)},completeUpdateDeviceCb:function(t){},successCallback:function(t){if(0===t.data.error)if(this.shouldRequestModify){var e=getApp().globalData.user_id;this.isEmpty(e)&&(e=uni.getStorageSync("key_user_id"));var i={user_id:e,device_name:this.name,device_address:this.address,install_location:this.location};this.requestWithMethod(getApp().globalData.api_update_device+this.device_sn+"/","PUT",i,this.successUpdateDeviceCb,this.failUpdateDeviceCb,this.completeUpdateDeviceCb)}else uni.hideLoading(),setTimeout(function(){uni.navigateBack({delta:1})},1500)},failCallback:function(t){uni.hideLoading(),console.log("api_device_opt failed",t)},completeCallback:function(t){},onAddDevice:function(){this.isEmpty(this.name)&&this.isEmpty(this.address)&&this.isEmpty(this.location)||(this.shouldRequestModify=!0),uni.showLoading({title:"正在添加设备"});var t=getApp().globalData.user_id;this.isEmpty(t)&&(t=uni.getStorageSync("key_user_id"));var e={device_sn:this.device_sn};this.isEmpty(this.device_sn)?this.showToast("请至少输入设备编码!"):this.requestWithMethod(getApp().globalData.api_device_opt+t+"/","PUT",e,this.successCallback,this.failCallback,this.completeCallback)},switchEnableTel:function(t){this.switch_enable_tel=t.detail.value},switchEnableSms:function(t){this.switch_enable_sms=t.detail.value},openScan:function(){uni.navigateTo({url:"../scan/scan"})}}};e.default=n},d781:function(t,e,i){"use strict";i.r(e);var n=i("16c2"),a=i("1664");for(var s in a)"default"!==s&&function(t){i.d(e,t,function(){return a[t]})}(s);var c,o=i("f0c5"),u=Object(o["a"])(a["default"],n["b"],n["c"],!1,null,"268571e6",null,!1,n["a"],c);e["default"]=u.exports}}]);