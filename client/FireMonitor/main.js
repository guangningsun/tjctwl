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
	uni.request({
		url: getApp().globalData.domain_port + api,
		method: "POST",
		dataType: 'json',
		header: {
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		data: params,
		success: res => {
			console.log('api:' + api + ' request success.');
			//确保successCallback是一个函数   
			if (typeof successCallback === "function") {
				//调用它，既然我们已经确定了它是可调用的
				successCallback(res);
			}
		},
		fail: (err) => {
			console.log('api:' + api + ' request failed:', err);
			if (typeof failedCallback === "function") {
				failedCallback(err);
			}
		},
		complete: (rsp) => {
			console.log('api:' + api + ' request complete.');
			if (typeof completeCallback === "function") {
				completeCallback(rsp);
			}
		}
	});
}

Vue.prototype.requestWithMethod = function(api, method, params, successCallback, failedCallback, completeCallback) {
	uni.request({
		url: getApp().globalData.domain_port + api,
		method: method,
		dataType: 'json',
		header: {
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		data: params,
		success: res => {
			console.log('api:' + api + ' request success.');
			//确保successCallback是一个函数
			if (typeof successCallback === "function") {
				//调用它，既然我们已经确定了它是可调用的
				successCallback(res);
			}
		},
		fail: (err) => {
			console.log('api:' + api + ' request failed:', err);
			if (typeof failedCallback === "function") {
				failedCallback(err);
			}
		},
		complete: (rsp) => {
			console.log('api:' + api + ' request complete.');
			if (typeof completeCallback === "function") {
				completeCallback(rsp);
			}
		}
	});
}

Vue.prototype.containsStr = function(rawStr, containStr) {
	if (rawStr != undefined && containStr != undefined) {
		return rawStr.indexOf(containStr) != -1
	}
}

// Vue.prototype.getParamsUrl = function(params){
// 	var paramsUrl = params.start_index + '/' +
// 		params.num + '/' +
// 		params.start_time + '/' +
// 		params.end_time;

// 	return paramsUrl;
// }

Vue.prototype.getParamsUrl = function(params) {
	var paramsUrl = params.start_index + '/' + params.num;
	if (params.start_time !== undefined) {
		paramsUrl += '/' + params.start_time;
	}
	if (params.end_time !== undefined) {
		paramsUrl +=  '/' + params.end_time;
	}
	return paramsUrl;
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
