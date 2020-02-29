<template>
	<view>
		<view class="cu-custom" :style="[{height:CustomBar + 'px'}]">
			<view class="cu-bar bg-gradual-dark-purple fixed" :style="style" :class="[bgImage!=''?'none-bg text-white bg-img':'',bgColor]">
				<!-- <view class="cu-bar bg-gradual-dark-purple" style="z-index: 9999;"> -->
				<view class="action" @tap="BackPage">
					<text class="cuIcon-back text-white"></text>
				</view>
				<view class="content" :style="[{top:StatusBar + 'px'}]">
					隐患整改
				</view>
				<view class="action">
					<text class="cuIcon-roundadd" @tap="goToAddDanger"></text>
				</view>
			</view>
		</view>

		<view class="cu-card"  v-for="(item,index) in danger_list" :key="index">
			<view class="cu-item">
				<view class="flex cu-form-group">
					<view class="title">隐患等级</view>
					<view>{{dangerLevel[item.danger_level]}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">隐患类别</view>
					<view>{{dangerType[item.danger_type]}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">隐患楼层</view>
					<view>{{item.danger_floor_level}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">地址</view>
					<view>{{item.danger_address_detail}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">上报人</view>
					<view>{{item.danger_create_user}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">上报时间</view>
					<view>{{item.danger_create_time}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">任务状态</view>
					<view>{{dangerStatus[item.danger_status]}}</view>
				</view>
				<view class="flex cu-form-group">
					<view class="title">隐患照片</view>
					<image :src="host + item.danger_image" style="width: 200upx; height: 200upx;" mode="aspectFill"></image>
				</view>
				<view class="flex cu-form-group">
					<view class="title">隐患描述</view>
					<view>{{item.danger_desc}}</view>
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
				
				host:getApp().globalData.domain_port2,

				danger_list: [],

				// danger_list: [{
				// 	danger_create_user:'sdfd',
				// 	danger_floor_level:'2',
				// 	danger_address_detail:'sddddddd',
				// 	danger_desc:'fdsfsf',
				// 	danger_image:'urlurl',
				// 	danger_create_time:'2020-02-24',
				// 	danger_status:'0',
				// 	danger_type:'0',
				// 	danger_level:'0'
				// },{
				// 	danger_create_user:'rrrrr',
				// 	danger_floor_level:'3',
				// 	danger_address_detail:'ytytyty',
				// 	danger_desc:'ssssfffff',
				// 	danger_image:'urlurl',
				// 	danger_create_time:'2020-02-24',
				// 	danger_status:'1',
				// 	danger_type:'1',
				// 	danger_level:'1'
				// }],

				dangerLevel: {
					'0': "一般隐患",
					'1': "较大隐患",
					'2': "重大隐患",
					'3': "特别重大隐患"
				},

				dangerType: {
					'0': "消防管理",
					'1': "消防组织",
					'2': "人员设备",
					'3': "特别重大隐患"
				},

				dangerStatus: {
					'0': "待整改",
					'1': "整改中",
					'2': "整改完毕",
					'3': "驳回"
				},

				default_img: 'this.src="' + require('../../static/default_device_img.png') + '"',
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
		onLoad: function(option) {
			
			let user_id = getApp().globalData.user_id;
			if (this.isEmpty(user_id)) {
				user_id = uni.getStorageSync('key_user_id');
			}
			let params = {
				danger_create_user: user_id,
			};
			
			this.requestWithMethod(
				getApp().globalData.api_danger,
				"GET",
				params,
				this.successCb,
				this.failCb,
				this.completeCb);
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
			goToAddDanger() {
				uni.navigateTo({
					url: '../user_home/user_add_danger',
				})
			},
			
			successCb(rsp) {
				console.log('success cb')
				if (rsp.data.error === 0) {
					this.danger_list = rsp.data.msg.danger_info;
				}
			},
			failCb(err) {
				console.log('api_get_danger_list failed', err);
			},
			completeCb(rsp) {},
			
		}
	}
</script>

<style>

</style>
