<template>
	<view>
		<mask v-if="showMask"></mask>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
				<view class="action"></view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
					事件
				</view>
				<view class="action" @tap="onSetAllRead">
					<!-- <text class="cuIcon-roundcheck" :class="[enableClearAll ? 'text-white' : 'text-gray']"></text> -->
					<text class="cuIcon-roundcheck text-white"></text>
				</view>
			</view>
		</view>

		<view class="box">
			<view class="cu-bar bg-gradual-dark-purple search">
				<view class="search-form radius">
					<text class="cuIcon-search"></text>
					<input @focus="InputFocus" @blur="InputBlur" :adjust-position="false" type="text" placeholder="搜索事件" confirm-type="search"></input>
				</view>
				<view class="action" @tap="showModal" data-target="DrawerModalR">
					<text class="cuIcon-calendar"></text>
				</view>
			</view>
		</view>

		<view style="padding-bottom: 100upx;">
			<view class="cu-list margin-top bg-white">
				<view class="cu-item flex solid-bottom" v-for="(item,index) in event_list" :key="index" @tap="onClickEvent(item)">
					<view class="flex align-center margin">
						<image :src="containStr(item.event_msg,'心跳') ? '../../static/event/heartbeat.png' : '../../static/event/upload.png'"
						 style="width: 80upx; height: 80upx;"></image>
					</view>
					<view class="flex align-center justify-between" style="width: 100%;">
						<view class="margin-top-sm margin-bottom-sm">
							<view class="title">
								{{item.event_msg}}
							</view>
							<view class="text-gray text-df">
								安装位置：{{item.event_device_location}}
							</view>
						</view>
						<view class="margin-sm">
							<view class="text-grey text-sm text-right">{{item.event_create_time}}</view>
							<view class="flex justify-end">
								<view class="cu-tag round sm margin-sm" :class="!item.if_read ? 'bg-red': 'bg-gray'"></view>
							</view>
						</view>
					</view>
				</view>
			</view>
			<view class=" flex justify-center margin-top-sm text-gray margin-bottom-sm" v-if="showLoadMore">{{loadMoreText}}</view>
		</view>

		<view class="box">
			<view class="cu-bar mytabbar foot tabbar bg-white">
				<navigator hover-class="none" :url="'../user_home/user_home'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/device_normal.png"></image>
					</view>
					<view class="text-black">设备</view>
				</navigator>
				<navigator hover-class="none" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/event_activate.png"></image>
					</view>
					<view class="text-light-purple">事件</view>
				</navigator>
				<navigator hover-class="none" :url="'../user_me/user_me'" class="action">
					<view class="cuIcon-cu-image">
						<image src="/static/tabbar/me-normal.png"></image>
					</view>
					<view class="text-black">我的</view>
				</navigator>
			</view>
		</view>

		<!-- 右侧model -->
		<view class="cu-modal drawer-modal justify-end" :class="modalName=='DrawerModalR'?'show':''" @tap="hideModal">
			<view class="cu-dialog basis-lg" @tap.stop="" :style="[{top:CustomBar+'px',height:'calc(100vh - ' + CustomBar + 'px)'}]">
				<view class="cu-list menu">
					<view class="cu-item">
						<button class="cu-btn content" @tap="onStartDate" disabled="disable">
							<text class="cuIcon-btn text-olive"></text>
							<text class="text-black">起始日期</text>
						</button>
						<picker mode="date" :value="startDate" start="2015-09-01" end="2020-09-01" @change="startDateChange" @tap="hideModal">
							<view class="flex align-center justify-end">
								<view class="picker">
									{{startDate}}
								</view>
								<text class="cuIcon-right text-gray"></text>
							</view>
						</picker>

					</view>
					<view class="cu-item">
						<button class="cu-btn content" @tap="onEndDate" disabled="disable">
							<text class="cuIcon-btn text-light-orange"></text>
							<text class="text-black">结束日期</text>
						</button>
						<picker mode="date" :value="endDate" start="2015-09-01" end="2020-09-01" @change="endDateChange" @tap="hideModal">
							<view class="flex align-center justify-end">
								<view class="picker">
									{{endDate}}
								</view>
								<text class="cuIcon-right text-gray"></text>
							</view>
						</picker>
					</view>
				</view>

				<view class="padding flex flex-direction">
					<button class="cu-btn bg-dark-purple lg" @click="onDateSearch">查询</button>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import mask from '../../components/mask.vue';
	export default {
		data() {
			return {
				showMask: false,
				
				StatusBar: this.StatusBar,
				CustomBar: this.CustomBar,
				modalName: null,
				startDate: '请选择',
				endDate: '请选择',
				enableClearAll: false,

				loadMoreText: "加载中...",
				showLoadMore: true,

				clickItem: null,

				event_request_num: 20,
				event_start_index: 0,

				paramUrl: '',

				event_list: [],
				// event_list: [{
				// 	if_read: true,
				// 	event_create_time: '2020-02-01 10:00',
				// 	event_device_location: 'jjjjj',
				// 	event_msg: '心跳',
				// }, {
				// 	if_read: false,
				// 	event_create_time: '2020-02-01 10:00',
				// 	event_device_location: 'jjjjj',
				// 	event_msg: '电压',
				// }, {
				// 	if_read: false,
				// 	event_create_time: '2020-02-01 10:00',
				// 	event_device_location: 'jjjjj',
				// 	event_msg: 'msgmsg',
				// }],
			}
		},
		components: {
			mask
		},
		onBackPress() {
			if (this.showMask) {
				this.showMask = false;
				return true;
			} else {
				this.showQuitDialog();
				return true;
			}
		},
		computed: {
			style() {
				var StatusBar = this.StatusBar;
				var CustomBar = this.CustomBar;
				var bgImage = this.bgImage;
				var style = `height:${CustomBar}px;padding-top:${StatusBar}px;`;
				if (this.bgImage) {
					style = `${style}background-image:url(${bgImage});`;
				}
				return style
			}
		},
		onLoad() {
			this.initData();

		},
		onUnload() {
			this.event_list = [],
				this.loadMoreText = "加载更多",
				this.showLoadMore = false;
		},
		onReachBottom() {
			console.log("onReachBottom");
			this.showLoadMore = true;

			let user_id = getApp().globalData.user_id;
			if (this.isEmpty(user_id)) {
				user_id = uni.getStorageSync('key_user_id');
			}
			
			let startIndex = this.event_list.length - 1;
			if(this.event_list.length === 1){
				startIndex = 1;
			}
			
			let params = {
				start_index: startIndex,
				num: this.event_request_num,
				start_time: this.startDate === '请选择' ? 0 : this.startDate + ' 00:00:00',
				end_time: this.endDate === '请选择' ? 0 : this.endDate + ' 23:59:59',
			};

			this.requestWithMethod(
				getApp().globalData.api_event + user_id + '/' + this.getParamsUrl(params),
				"GET",
				'',
				this.successCb,
				this.failCb,
				this.completeCb);
		},
		onPullDownRefresh() {
			console.log('onPullDownRefresh!!!!');
			this.startDate = '请选择';
			this.endDate = '请选择';
			this.initData();
		},
		props: {
			bgColor: {
				type: String,
				default: ''
			},
			isBack: {
				type: [Boolean, String],
				default: false
			},
			bgImage: {
				type: String,
				default: ''
			},
		},
		methods: {
			// getEventParamsUrl(params) {
			// 	var paramsUrl = params.start_index + '/' +
			// 		params.num + '/' +
			// 		params.start_time + '/' +
			// 		params.end_time;

			// 	return paramsUrl;
			// },
			containStr(str1, str2) {
				return this.containsStr(str1, str2);
			},
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			startDateChange(e) {
				this.startDate = e.detail.value;
				e.currentTarget.dataset.target = 'DrawerModalR';
				this.showModal(e);
			},
			endDateChange(e) {
				this.endDate = e.detail.value;
				e.currentTarget.dataset.target = 'DrawerModalR';
				this.showModal(e);
			},
			initData() {
				uni.stopPullDownRefresh();
				
				this.event_list = [],
				this.loadMoreText = "加载更多",
				this.showLoadMore = false;
				
				var user_id = getApp().globalData.user_id;
				if (this.isEmpty(user_id)) {
					user_id = uni.getStorageSync('key_user_id');
				}
				var params = {
					start_index: 0,
					num: this.event_request_num,
					start_time: this.startDate === '请选择' ? 0 : this.startDate + '00:00:00',
					end_time: this.endDate === '请选择' ? 0 : this.endDate + ' 23:59:59',
				};
				this.requestWithMethod(
					getApp().globalData.api_event + user_id + '/' + this.getParamsUrl(params),
					"GET",
					'',
					this.successCb,
					this.failCb,
					this.completeCb);
			},
			successCb(rsp) {
				console.log('success event cb')
				if (rsp.data.error === 0) {
					let rspEventList = rsp.data.msg.event_info;
					this.event_list = this.event_list.concat(rspEventList);
					if (rspEventList.length < this.event_request_num) {
						this.loadMoreText = "没有更多事件";
					} else {
						this.loadMoreText = "加载中...";
					}
				}
			},
			failCb(err) {
				console.log('api_event_list failed', err);
			},
			completeCb(rsp) {},
			////////////////////////////////////////
			successReadCb(rsp) {
				console.log(rsp);
				console.log('success event set read cb');
				if (rsp.data.error === 0) {
					console.log('event set read success!')
					if (this.containsStr(rsp.data.msg, '已读')) {
						this.clickItem.if_read = true;
					}
				}
			},
			failReadCb(err) {
				console.log('api_event set read failed', err);
			},
			completeReadCb(rsp) {},

			onClickEvent(item) {
				this.clickItem = item;
				if (item.if_read === false) {
					let params = {
						event_id: item.id
					};
					this.request(
						getApp().globalData.api_update_event_read_state,
						params,
						this.successReadCb,
						this.failReadCb,
						this.completeReadCb);
				}
			},

			///////////////////////////////

			successAllReadCb(rsp) {
				console.log(rsp);
				console.log('success event set read cb');
				if (rsp.data.error === 0) {
					uni.showToast({
						title:'全部消息已读',
					})
					this.event_list.forEach(function(value) {
						value.if_read = true;
					})
				}
			},
			failAllReadCb(err) {
				console.log('api_event set read failed', err);
			},
			completeAllReadCb(rsp) {},

			onSetAllRead() {
				let user_id = getApp().globalData.user_id;
				if (this.isEmpty(user_id)) {
					user_id = uni.getStorageSync('key_user_id');
				}
				let params = {
					user_id: user_id
				};
				this.requestWithMethod(
					getApp().globalData.api_update_event_read_state_all,
					"POST",
					params,
					this.successAllReadCb,
					this.failAllReadCb,
					this.completeAllReadCb);
			},

			///////////////////////
			successDateSearchCb(rsp) {
				console.log('success event date search cb')
				uni.hideLoading();
				this.event_list = [];
				if (rsp.data.error === 0) {
					let rspEventList = rsp.data.msg.event_info;
					this.event_list = this.event_list.concat(rspEventList);
					if (rspEventList.length < this.event_request_num) {
						this.loadMoreText = "没有更多事件";
					} else {
						this.loadMoreText = "加载中...";
					}
				}
			},
			failDateSearchCb(err) {
				console.log('api_event_list date search failed', err);
			},
			completeDateSearchCb(rsp) {},
			onDateSearch() {
				if (this.startDate !== '请选择' && this.endDate !== '请选择') {
					var startTimeStamp = Date.parse(new Date(this.startDate));
					var endTimeStamp = Date.parse(new Date(this.endDate));
					if (startTimeStamp <= endTimeStamp) {
						this.hideModal();
						let startTimeParam = this.startDate + ' 00:00:00';
						let endTimeParam = this.endDate + ' 23:59:59';

						var user_id = getApp().globalData.user_id;
						if (this.isEmpty(user_id)) {
							user_id = uni.getStorageSync('key_user_id');
						}
						var params = {
							start_index: 0,
							num: this.event_request_num,
							start_time: startTimeParam,
							end_time: endTimeParam,
						};
						uni.showLoading({
							title: "正在查询...",
						})
						this.requestWithMethod(
							getApp().globalData.api_event + user_id + '/' + this.getParamsUrl(params),
							"GET",
							params,
							this.successDateSearchCb,
							this.failDateSearchCb,
							this.completeDateSearchCb);
					}
				}
			},
		}
	}
</script>

<style>
	.mytabbar {
		z-index: 9999;
	}
</style>
