(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-user_home-user_add_danger"],{"11bc":function(i,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var n={data:function(){return{class_picker_index:-1,class_picker:["11","22","33"],type_picker_index:-1,type_picker:["tt","tt2","tt3"],floor_picker_index:-1,floor_picker:["ff","ff2","ff3"],textareaDangerDescValue:"",imgList:[]}},methods:{classPickerChange:function(i){-1===this.class_picker_index?this.class_picker_index=0:this.class_picker_index=i.detail.value,this.checkBtnEnable()},typePickerChange:function(i){-1===this.type_picker_index?this.type_picker_index=0:this.type_picker_index=i.detail.value,this.checkBtnEnable()},textareaDangerDescInput:function(i){this.textareaDangerDescValue=i.detail.value},floorPickerChange:function(i){-1===this.floor_picker_index?this.floor_picker_index=0:this.floor_picker_index=i.detail.value,this.checkBtnEnable()},checkBtnEnable:function(){""==this.date||""==this.class_picker[this.class_picker_index]||void 0==this.class_picker[this.class_picker_index]||""==this.type_picker[this.type_picker_index]||void 0==this.type_picker[this.type_picker_index]||""==this.floor_picker[this.floor_picker_index]||void 0==this.floor_picker[this.floor_picker_index]?this.btn_disabled=!0:this.btn_disabled=!1},DelImg:function(i){var e=this;uni.showModal({title:"删除照片",content:"确定要删除这张照片吗？",cancelText:"否",confirmText:"是",success:function(t){t.confirm&&e.imgList.splice(i.currentTarget.dataset.index,1)}})},ChooseImage:function(){var i=this;uni.chooseImage({count:4,sizeType:["original","compressed"],sourceType:["album","camera"],success:function(e){0!=i.imgList.length?i.imgList=i.imgList.concat(e.tempFilePaths):i.imgList=e.tempFilePaths}})},onAddDanger:function(){}}};e.default=n},ab51:function(i,e,t){"use strict";t.r(e);var n=t("11bc"),s=t.n(n);for(var a in n)"default"!==a&&function(i){t.d(e,i,function(){return n[i]})}(a);e["default"]=s.a},cdcb:function(i,e,t){"use strict";t.r(e);var n=t("e4bc"),s=t("ab51");for(var a in s)"default"!==a&&function(i){t.d(e,i,function(){return s[i]})}(a);var c,r=t("f0c5"),l=Object(r["a"])(s["default"],n["b"],n["c"],!1,null,"11d236cc",null,!1,n["a"],c);e["default"]=l.exports},e4bc:function(i,e,t){"use strict";var n,s=function(){var i=this,e=i.$createElement,t=i._self._c||e;return t("v-uni-view",[t("cu-custom",{attrs:{bgColor:"bg-gradual-dark-purple",isBack:!0}},[t("template",{attrs:{slot:"content"},slot:"content"},[i._v("隐患上报")])],2),t("v-uni-view",{staticClass:"cu-card"},[t("v-uni-view",{staticClass:"cu-item"},[t("v-uni-view",{staticClass:"flex cu-form-group"},[t("v-uni-view",{staticClass:"title"},[i._v("上报人")]),t("v-uni-view",[i._v("0")])],1),t("v-uni-view",{staticClass:"cu-form-group"},[t("v-uni-view",{staticClass:"title"},[i._v("隐患等级")]),t("v-uni-picker",{attrs:{value:i.class_picker_index,range:i.class_picker},on:{change:function(e){arguments[0]=e=i.$handleEvent(e),i.classPickerChange.apply(void 0,arguments)}}},[t("v-uni-view",{staticClass:"picker text-gray"},[i._v(i._s(i.class_picker_index>-1?i.class_picker[i.class_picker_index]:"选择隐患等级"))])],1)],1),t("v-uni-view",{staticClass:"cu-form-group"},[t("v-uni-view",{staticClass:"title"},[i._v("隐患类型")]),t("v-uni-picker",{attrs:{value:i.type_picker_index,range:i.type_picker},on:{change:function(e){arguments[0]=e=i.$handleEvent(e),i.typePickerChange.apply(void 0,arguments)}}},[t("v-uni-view",{staticClass:"picker text-gray"},[i._v(i._s(i.type_picker_index>-1?i.type_picker[i.type_picker_index]:"选择隐患类型"))])],1)],1),t("v-uni-view",{staticClass:"cu-form-group"},[t("v-uni-view",{staticClass:"title"},[i._v("隐患楼层")]),t("v-uni-picker",{attrs:{value:i.floor_picker_index,range:i.floor_picker},on:{change:function(e){arguments[0]=e=i.$handleEvent(e),i.floorPickerChange.apply(void 0,arguments)}}},[t("v-uni-view",{staticClass:"picker text-gray"},[i._v(i._s(i.floor_picker_index>-1?i.floor_picker[i.floor_picker_index]:"选择隐患楼层"))])],1)],1),t("v-uni-view",{staticClass:"cu-form-group"},[t("v-uni-view",{staticClass:"title"},[i._v("具体位置")]),t("v-uni-input",{attrs:{placeholder:"请输入具体位置",name:"input"}})],1),t("v-uni-view",{staticClass:"cu-form-group align-start"},[t("v-uni-view",{staticClass:"title"},[i._v("隐患描述")]),t("v-uni-textarea",{attrs:{maxlength:"-1",disabled:null!=i.modalName,placeholder:"请输入隐患描述"},on:{input:function(e){arguments[0]=e=i.$handleEvent(e),i.textareaDangerDescInput.apply(void 0,arguments)}}})],1),t("v-uni-view",{staticClass:"cu-bar bg-white margin-top solid-top"},[t("v-uni-view",{staticClass:"action"},[i._v("图片上传")]),t("v-uni-view",{staticClass:"action"},[i._v(i._s(i.imgList.length)+"/4")])],1),t("v-uni-view",{staticClass:"cu-form-group margin-bottom-sm"},[t("v-uni-view",{staticClass:"grid col-4 grid-square flex-sub"},[i._l(i.imgList,function(e,n){return t("v-uni-view",{key:n,staticClass:"bg-img",attrs:{"data-url":i.imgList[n]},on:{click:function(e){arguments[0]=e=i.$handleEvent(e),i.ViewImage.apply(void 0,arguments)}}},[t("v-uni-image",{attrs:{src:i.imgList[n],mode:"aspectFill"}}),t("v-uni-view",{staticClass:"cu-tag bg-red",attrs:{"data-index":n},on:{click:function(e){e.stopPropagation(),arguments[0]=e=i.$handleEvent(e),i.DelImg.apply(void 0,arguments)}}},[t("v-uni-text",{staticClass:"cuIcon-close"})],1)],1)}),i.imgList.length<4?t("v-uni-view",{staticClass:"solids",on:{click:function(e){arguments[0]=e=i.$handleEvent(e),i.ChooseImage.apply(void 0,arguments)}}},[t("v-uni-text",{staticClass:"cuIcon-cameraadd"})],1):i._e()],2)],1)],1),t("v-uni-view",{staticClass:"justify-between bottom-box"},[t("v-uni-view",{staticClass:"padding flex flex-direction"},[t("v-uni-button",{staticClass:"cu-btn bg-dark-purple lg",on:{click:function(e){arguments[0]=e=i.$handleEvent(e),i.onAddDanger.apply(void 0,arguments)}}},[i._v("提交")])],1)],1)],1)],1)},a=[];t.d(e,"b",function(){return s}),t.d(e,"c",function(){return a}),t.d(e,"a",function(){return n})}}]);