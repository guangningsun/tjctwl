<template>
	<view>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
				<view class="action" @tap="BackPage">
					<text class="cuIcon-back text-white"></text>
				</view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
					隐患整改
				</view>
				<view class="action">
					<text class="cuIcon-add lg" @tap="addDanger"></text>
				</view>
			</view>
		</view>

		<scroll-view scroll-x class="bg-white nav text-center">
			<view class="cu-item" :class="index==TabCur?'text-blue cur':''" v-for="(item,index) in tabNameList" :key="index"
			 @tap="tabSelect" :data-id="index">
				{{item}}
			</view>
		</scroll-view>

		<view v-show="danger_info_list.length > 0" class="flex align-center margin-sm" style="margin-bottom: 0upx;">
			<text class="text-blue margin-right-xs">{{tabNameList[TabCur]}}任务</text>
			<text class="text-light-red margin-right-xs">{{danger_info_list.length}}</text>
			<text class="text-blue margin-right-xs">个</text>
		</view>

		<view class="cu-card card-margin" style="margin-bottom: -30upx;" v-for="(item,index) in danger_info_list" :key="index">
			<view class="cu-item">

				<view class="cu-form-group ">
					<view class="title">隐患等级</view>
					<view>{{item.danger_level}}</view>
				</view>

				<view class="cu-form-group ">
					<view class="title">隐患类型</view>
					<view>{{item.danger_status}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">上报人</view>
					<view>{{item.danger_create_user}}</view>
				</view>

				<view class="cu-form-group">
					<view class="title">隐患楼层</view>
					<view>{{item.danger_floor_level}}</view>
				</view>

				<view class="cu-form-group">
					<view class="title">具体位置</view>
					<view>{{item.danger_address_detail}}</view>
				</view>

				<view class="cu-form-group ">
					<view class="title">隐患描述</view>
					<view class="text-content">{{item.danger_desc}}</view>
				</view>

				<view class="cu-form-group ">
					<view class="title">隐患时间</view>
					<view>{{item.danger_create_time}}</view>
				</view>
				<view class="cu-bar bg-white margin-top solid-top">
					<view class="action text-black">
						隐患照片
					</view>
				</view>
				<view class="cu-form-group margin-bottom-sm solid-bottom">
					<view class="grid col-4 grid-square flex-sub">
						<view class="bg-img" @tap="ViewImage">
							<image :src="item.danger_image" mode="aspectFill"></image>
						</view>
					</view>
				</view>

				<view v-show="item.danger_status === '1' || item.danger_status === '3'">
					<view class="cu-form-group align-start">
						<view class="title">隐患描述</view>
						<textarea class="text-right" maxlength="-1" :disabled="modalName!=null" @input="textareaDangerDescInput" v-model="desc"
						 placeholder="请输入隐患描述"></textarea>
					</view>

					<view class="cu-bar bg-white margin-top solid-top">
						<view class="action text-black">
							图片上传
						</view>
						<view class="action">
							{{imgList.length}}/1
						</view>
					</view>
					<view class="cu-form-group margin-bottom-sm">
						<view class="grid col-4 grid-square flex-sub">
							<view class="bg-img" v-for="(item,index) in imgList" :key="index" @tap="ViewImage" :data-url="imgList[index]">
								<image :src="imgList[index]" mode="aspectFill"></image>
								<view class="cu-tag bg-red" @tap.stop="DelImg" :data-index="index">
									<text class='cuIcon-close'></text>
								</view>
							</view>
							<view class="solids" @tap="ChooseImage" v-if="imgList.length<4">
								<text class='cuIcon-cameraadd'></text>
							</view>
						</view>
					</view>
				</view>

				<view class="flex justify-end">
					<button class="cu-btn line-blue margin-right-xs margin-bottom-sm" @tap="onBtnAction(item)">
						{{btnNameList[TabCur]}}
					</button>
					<button v-show="item.danger_status === '1' || item.danger_status === '3'" class="cu-btn line-blue margin-right-xs margin-bottom-sm"
					 @tap="onAddDesc(item)">
						确认修改
					</button>
				</view>
			</view>
		</view>
		
		<view v-show="danger_info_list.length > 0" class=" flex justify-center margin-top-sm text-gray margin-bottom-sm" v-if="showLoadMore">{{loadMoreText}}</view>
		
		<view v-show="danger_info_list.length === 0" style="height: 500upx;" class="flex align-center justify-center margin-top-xl">
			<view style="background-color: #00000000;">
				<image src="../../static/empty.png" mode="aspectFit" style="width: 200upx; height: 200upx;"></image>
				<view class="text-df text-gray text-center">
					{{tabNameList[TabCur]}}列表为空
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

				imgList: [],
				desc: '',

				tabNameList: ['待整改', '整改中', '已完成', '驳回'],
				btnNameList: ['领取任务', '整改完成', '驳回','整改完成'],
				TabCur: 0,

				request_num: 20,
				start_index: 0,

				danger_info_list: [],
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
			this.initData(this.TabCur);
		},
		onReachBottom() {
			console.log("onReachBottom");
			this.showLoadMore = true;

			let startIndex = this.danger_info_list.length - 1;
			if (this.danger_info_list.length === 1) {
				startIndex = 1;
			}

			let params = {
				start_index: startIndex,
				num: this.request_num,
			};
			this.reqData(params, this.TabCur);
		},
		onLoad() {
			this.initData(0);
		},
		onUnload() {
			this.danger_info_list = [],
			this.loadMoreText = "加载更多",
			this.showLoadMore = false;
		},
		methods: {
			textareaDangerDescInput(e) {
				this.desc = e.detail.value
			},
			tabSelect(e) {
				this.TabCur = e.currentTarget.dataset.id;
				this.initData(this.TabCur);
			},
			BackPage() {
				uni.navigateBack({
					delta: 1
				});
			},

			initData(tabIndex) {
				this.danger_info_list = [],
				this.loadMoreText = "加载更多",
				this.showLoadMore = false;

				let params = {
					start_index: 0,
					num: this.request_num,
				};
				this.reqData(params, tabIndex);
			},

			reqData(params, status) {
				uni.stopPullDownRefresh();
				this.requestWithMethod(
					getApp().globalData.api_admin_danger + this.getParamsUrl(params) + '/' + status,
					"GET",
					'',
					this.successCb,
					this.failCb,
					this.completeCb);
			},
			successCb(rsp) {
				console.log('success cb');
				if (rsp.data.error === 0) {
					// this.install_device_list = rsp.data.msg.install_device_list;
					let rspList = rsp.data.msg.danger_info;
					this.danger_info_list = this.danger_info_list.concat(rspList);
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

			addDanger() {
				uni.navigateTo({
					url: '../user_home/user_add_danger'
				})
			},

			//按钮操作
			onBtnAction(item) {
				switch (item.danger_status) {

					//待整改，只能领取任务
					case '0':
						this.onReceiveTask(item);
						break;

						//整改中，可以完成与添加
					case '1':
						this.onFinishTask(item);
						break;

						//整改完毕，可以驳回
					case '2':
						this.onReject(item);
						break;

						//驳回，与整改中一样
					case '3':
						this.onFinishTask(item);
						break;

					default:
						break;
				}
			},
			
			successUpdateStatus(rsp) {
				if (rsp.data.error === 0) {
					this.showToast('更新成功');
					this.initData(this.TabCur);
				}
			},
			
			failUpdateStatus(err) {
				this.showToast('更新失败 \n' + err);
			},
			
			completeUpdateStatus(rsp) {},
			
			updateDangerStatus(item, status){
				let params = {
					danger_id : item.id,
					danger_status : status,
				};
				
				this.request(
					getApp().globalData.api_update_danger_status,
					params,
					this.successUpdateStatus,
					this.failUpdateStatus,
					this.completeUpdateStatus);
			},

			//领取任务
			onReceiveTask(item) {
				this.updateDangerStatus(item,1);
			},

			//整改完毕
			onFinishTask(item) {
				this.updateDangerStatus(item,2)
			},

			//驳回
			onReject(item) {
				this.updateDangerStatus(item,3)
			},
			
			addDescAndImage(id, params){
				this.requestWithMethod(
					getApp().globalData.api_admin_danger + id,
					"PUT",
					params,
					this.successUpdateStatus,
					this.failUpdateStatus,
					this.completeUpdateStatus)
			},
			
			//添加描述与照片
			onAddDesc(item) {
				
				if(this.isEmpty(this.desc) && this.isEmpty(this.imgList[0])){
					this.showToast('请检查输入!')
					return;
				}
				let params = {};
				if(!this.isEmpty(this.desc)){
					params['danger_desc'] = this.desc;
				}
				if (!this.isEmpty(this.imgList[0])){
					params['danger_image'] = this.imgList[0];
				}
				//  params = {
				// 	danger_desc : this.desc,
				// 	danger_image : this.imgList[0],
				// };
				
				this.addDescAndImage(item.id, params);
			},
			
			DelImg(e) {
				uni.showModal({
					title: '删除照片',
					content: '确定要删除这张照片吗？',
					cancelText: '否',
					confirmText: '是',
					success: res => {
						if (res.confirm) {
							this.imgList.splice(e.currentTarget.dataset.index, 1)
						}
					}
				})
			},
			ChooseImage() {
				uni.chooseImage({
					count: 1, //默认9
					sizeType: ['original', 'compressed'], //可以指定是原图还是压缩图，默认二者都有
					sourceType: ['album', 'camera'],
					success: (res) => {
						if (this.imgList.length != 0) {
							this.imgList = this.imgList.concat(res.tempFilePaths)
						} else {
							this.imgList = res.tempFilePaths
						}
					}
				});
			},
		}
	}
</script>

<style>

</style>
