(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-login-login"],{"1c69":function(e,t,a){"use strict";a.r(t);var i=a("562d"),n=a.n(i);for(var s in i)"default"!==s&&function(e){a.d(t,e,function(){return i[e]})}(s);t["default"]=n.a},"54e7":function(e,t,a){"use strict";var i,n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-uni-view",{staticClass:"content"},[a("v-uni-view",{staticClass:"mak-box"},[a("v-uni-image",{staticClass:"mak-logo",attrs:{src:"../../static/login.png",mode:"aspectFit"}}),a("v-uni-view",{staticClass:"mak-title"},[e._v("天津城投物联")]),a("v-uni-view",{staticClass:"flex padding align-center radius"},[a("v-uni-form",[a("v-uni-view",{staticClass:"cu-form-group"},[a("v-uni-view",{staticClass:"title"},[e._v("用户名")]),a("v-uni-input",{attrs:{placeholder:"请输入用户名",name:"input"},model:{value:e.user_name,callback:function(t){e.user_name=t},expression:"user_name"}})],1),a("v-uni-view",{staticClass:"cu-form-group"},[a("v-uni-view",{staticClass:"title"},[e._v("密   码")]),a("v-uni-input",{attrs:{password:!0,placeholder:"请输入密码",name:"input","data-val":"password"},model:{value:e.user_pwd,callback:function(t){e.user_pwd=t},expression:"user_pwd"}})],1)],1)],1)],1),a("v-uni-view",{staticClass:"justify-between bottom-box"},[a("v-uni-view",{staticClass:"flex text-df padding justify-center"},[a("v-uni-view",{staticClass:"text-grey",on:{click:function(t){arguments[0]=t=e.$handleEvent(t),e.showForgetToast.apply(void 0,arguments)}}},[e._v("忘记密码？")])],1),a("v-uni-view",{staticClass:"padding flex flex-direction"},[a("v-uni-button",{staticClass:"cu-btn bg-dark-purple lg",on:{click:function(t){arguments[0]=t=e.$handleEvent(t),e.onLogin.apply(void 0,arguments)}}},[e._v("登录")])],1)],1)],1)},s=[];a.d(t,"b",function(){return n}),a.d(t,"c",function(){return s}),a.d(t,"a",function(){return i})},"562d":function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0;var i={data:function(){return{user_type:0,user_name:"",user_pwd:""}},methods:{successCallback:function(e){if(uni.hideLoading(),0===e.data.error){var t=e.data.msg,a=t.user_permission;this.saveUserData(t),"0"===a?uni.navigateTo({url:"../admin_home/admin_home"}):"1"===a&&uni.navigateTo({url:"../user_home/user_home"})}},failCallback:function(e){uni.hideLoading(),this.showToast("登录失败!"),console.log("登录失败："+e.errMsg)},completeCallback:function(e){void 0!=e.data&&1===e.data.error&&(console.log("login not match"),-1!=e.data.msg.indexOf("doesn`t match")&&getApp().showToast("用户名或密码不正确，\n 请核实后输入"))},onLogin:function(){uni.showLoading({title:"正在登录"});var e={username:this.user_name,password:this.user_pwd};this.request(getApp().globalData.api_login,e,this.successCallback,this.failCallback,this.completeCallback)},showForgetToast:function(){this.showToast("请联系管理员更改密码")},saveUserData:function(e){getApp().globalData.user_id=e.id,uni.setStorage({key:"key_user_id",data:e.id}),uni.setStorage({key:"key_login_name",data:e.login_name}),uni.setStorage({key:"key_password",data:e.password}),uni.setStorage({key:"key_user_name",data:e.username}),uni.setStorage({key:"key_user_type",data:e.user_permission}),uni.setStorage({key:"key_phone_number",data:e.phone_number}),uni.setStorage({key:"key_user_sex",data:e.user_sex}),uni.setStorage({key:"key_user_age",data:e.user_age})}}};t.default=i},"7c79":function(e,t,a){var i=a("ab08");"string"===typeof i&&(i=[[e.i,i,""]]),i.locals&&(e.exports=i.locals);var n=a("4f06").default;n("e66d9a86",i,!0,{sourceMap:!1,shadowMode:!1})},aa89:function(e,t,a){"use strict";var i=a("7c79"),n=a.n(i);n.a},ab08:function(e,t,a){t=e.exports=a("2350")(!1),t.push([e.i,".mak-box[data-v-027fe238]{padding:%?100?% %?100?%;position:relative;background-color:#fff}.content[data-v-027fe238]{background-color:#fff;min-height:100vh}.bottom-box[data-v-027fe238]{padding:%?20?% %?20?%;position:relative;background-color:#fff}.mak-logo[data-v-027fe238]{width:100%;width:100%;height:%?310?%}.mak-title[data-v-027fe238]{position:absolute;top:0;line-height:%?500?%;font-size:%?56?%;color:#fff;text-align:center;width:100%;margin-left:%?-100?%}",""])},c333:function(e,t,a){"use strict";a.r(t);var i=a("54e7"),n=a("1c69");for(var s in n)"default"!==s&&function(e){a.d(t,e,function(){return n[e]})}(s);a("aa89");var o,u=a("f0c5"),r=Object(u["a"])(n["default"],i["b"],i["c"],!1,null,"027fe238",null,!1,i["a"],o);t["default"]=r.exports}}]);