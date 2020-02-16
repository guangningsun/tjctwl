import Vue from 'vue'
import App from './App'

import cuCustom from './colorui/components/cu-custom.vue'
Vue.component('cu-custom', cuCustom)

Vue.config.productionTip = false

Vue.prototype.showToast = function(msg) {
	uni.showToast({
		title: msg,
		icon: 'none'
	})
}

Vue.prototype.request = function(api, params, successCallback, failedCallback, completeCallback) {
	console.log('main request');
	uni.request({
		url: getApp().globalData.domain_port + api,
		method: "POST",
		dataType: 'json',
		header: {
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		data: params,
		success: res => {
			console.log(api + ' request success.');
			//确保successCallback是一个函数   
			if (typeof successCallback === "function") {
				//调用它，既然我们已经确定了它是可调用的
				successCallback(res);
			}
		},
		fail: (err) => {
			console.log(api + ' request failed:', err);
			if (typeof failedCallback === "function") {
				failedCallback(err);
			}
		},
		complete: (rsp) => {
			console.log(api + ' request complete.');
			if (typeof completeCallback === "function") {
				completeCallback(rsp);
			}
		}
	});
}

//判断字符是否为空的方法
Vue.prototype.isEmpty = function(obj) {
	if (typeof obj == "undefined" || obj == null || obj == "") {
		return true;
	} else {
		return false;
	}
}

App.mpType = 'app'

const app = new Vue({
	...App
})
app.$mount()
