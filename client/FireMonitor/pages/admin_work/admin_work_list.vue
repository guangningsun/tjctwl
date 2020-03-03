<template>
	<view>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
				<view class="action" @tap="BackPage">
					<text class="cuIcon-back text-white"></text>
				</view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
					施工安装
				</view>
				<view class="action">
					<text class="cuIcon-add lg margin-right-sm" @tap="gotoInstall"></text>
					<text class="cuIcon-filter lg" @tap="showModal" data-target="FilterModal"></text>
				</view>
			</view>
		</view>

		<view class="cu-card card-margin" style="margin-bottom: -30upx;" v-for="(item,index) in install_device_list" :key="index">
			<view class="cu-item">
				<view class="flex justify-between">
					<!-- <view class="cu-tag radius bg-olive">已完成</view> -->
					<view class="flex align-center text-left margin-top-sm margin-left-xl text-gray" style="width: 100%;">{{item.construction_createtime}}</view>
					<view class="cu-tag radius bg-green">{{item.deviceStatus}}</view>
				</view>
				<view class="flex">
					<image class="margin" :src="item.construction_image" style="width: 100upx; height: 100upx;"></image>
					<view class="margin-top-sm">
						<view>设备编码: {{item.device_sn}}</view>
						<view>设 备 名: {{item.device_name}}</view>
						<view>施工人员: {{item.construction_worker}}</view>
					</view>
				</view>
				<view class="flex justify-end">
					<button class="cu-btn line-blue margin-right-xs margin-bottom-sm" @tap="onInstallDetail(item)">详情</button>
					<button class="cu-btn line-orange margin-bottom-sm margin-right-xs" @tap="onReinstall(item)">重装</button>
				</view>
			</view>
		</view>
		
		<view class=" flex justify-center margin-top-sm text-gray margin-bottom-sm" v-if="showLoadMore">{{loadMoreText}}</view>	
		<!-- 过滤 modal -->
		<view class="cu-modal" :class="modalName=='FilterModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">条件筛选</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
		
				<form>
					<view class="cu-form-group">
						<view class="title">设备编码</view>
						<input class="text-left" placeholder="输入设备编码" name="input" v-model="search_device_sn"></input>
					</view>
				</form>
		
				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmSearch">查询</button>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				StatusBar: this.StatusBar,
				CustomBar: this.CustomBar,
				modalName: null,
				
				loadMoreText: "加载中...",
				showLoadMore: true,
				
				search_device_sn:'',
				
				request_num: 20,
				start_index: 0,
				
				install_device_list:[],
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
		onPullDownRefresh() {
			console.log('onPullDownRefresh!!!!');
			this.initData();
		},
		onReachBottom() {
			console.log("onReachBottom");
			this.showLoadMore = true;
		
			let params = {
				start_index: this.install_device_list.length - 1,
				num: this.request_num,
			};
		
			this.requestWithMethod(
				getApp().globalData.api_install_device + this.getParamsUrl(params),
				"GET",
				'',
				this.successCb,
				this.failCb,
				this.completeCb);
		},
		onLoad() {
			this.initData();
		},
		onUnload() {
			this.install_device_list = [],
				this.loadMoreText = "加载更多",
				this.showLoadMore = false;
		},
		methods: {
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			BackPage() {
				uni.navigateBack({
					delta: 1
				});
			},
			initData() {
				uni.stopPullDownRefresh();
				
				this.install_device_list = [],
				this.loadMoreText = "加载更多",
				this.showLoadMore = false;
				
				var params = {
					start_index: 0,
					num: this.request_num,
				};
				this.requestWithMethod(
					getApp().globalData.api_install_device + this.getParamsUrl(params),
					"GET",
					'',
					this.successCb,
					this.failCb,
					this.completeCb);
			},
			successCb(rsp) {
				console.log('success cb')
				if (rsp.data.error === 0) {
					// this.install_device_list = rsp.data.msg.install_device_list;
					let rspList = rsp.data.msg.install_device_list;
					this.install_device_list = this.install_device_list.concat(rspList);
					if (rspList.length < this.request_num) {
						this.showLoadMore = true;
						this.loadMoreText = "没有更多";
					} else {
						this.loadMoreText = "加载中...";
					}
				}
			},
			failCb(err) {
				console.log('api_get_danger_list failed', err);
			},
			completeCb(rsp) {},
			
			successSearchDeviceCb(rsp) {
				if (rsp.data.error === 0) {
					let installDeviceInfo = rsp.data.msg.install_device_list;
					this.install_device_list = installDeviceInfo;
					this.showLoadMore = false;
				}
			},
			failSearcheCb(err) {
				console.log('api_device search failed', err);
			},
			completeSearchCb(rsp) {},
			
			onConfirmSearch(){
				this.hideModal();
				this.requestWithMethod(
					getApp().globalData.api_install_device + this.search_device_sn,
					"GET",
					'',
					this.successSearchDeviceCb,
					this.failSearcheCb,
					this.completeSearchCb);
			},
			gotoInstall(){
				uni.navigateTo({
					url:'admin_install'
				})
			},
			onInstallDetail(item){
				uni.navigateTo({
					url: 'admin_install_detail?installDeviceInfo=' + encodeURIComponent(JSON.stringify(item))
				})
			},
			onReinstall(item){
				uni.navigateTo({
					url: 'admin_reinstall?installDeviceInfo=' + encodeURIComponent(JSON.stringify(item))
				})
			}
		}
	}
</script>

<style>

</style>
