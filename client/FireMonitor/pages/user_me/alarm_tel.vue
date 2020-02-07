<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">火警电话通知</block>
		</cu-custom>

		<view class="cu-list">
			<view class="cu-item" :class="modalName=='move-box-0'?'move-cur':''" v-for="(item,index) in 1" :key="index"
			 @touchstart="ListTouchStart" @touchmove="ListTouchMove" @touchend="ListTouchEnd" :data-target="'move-box-0'">

				<view class="cu-form-group">
					<view class="flex align-center">
						<image class="margin-right-sm" src="../../static/me/tel_me.png" style="width: 47upx;height: 47upx;"></image>
						<text class="text-lg">手机号码</text>
					</view>
					<text class="text-gray">16872929338</text>

					<view class="move">
						<view class="bg-gradual-green" @tap="showModal" data-target="AddTelModal">添加</view>
						<view class="bg-gradual-light-purple" @tap="onModifyTel">修改</view>
						<view class="bg-gradual-red" @tap="onDeleteTel">删除</view>
					</view>
				</view>
			</view>
		</view>

		<view class="margin text-lg">
			可选择需要短信通知的设备
		</view>

		<view style="padding-bottom: 100upx;">
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
			
			<!-- ======================== -->
			
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
			<view class="cu-card card-margin">
				<view class="cu-item">
					<view class="flex padding-sm">
						<view class="flex-twice">
							<view class="flex text-df align-center">
								<view class="text-gray">设备ID:</view>
								<view class="margin-left-sm">123456</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">场 所:</view>
								<view class="margin-left-sm">办公室</view>
							</view>
							<view class="flex text-df align-center">
								<view class="text-gray">安装位置:</view>
								<view class="margin-left-sm">走廊</view>
							</view>
						</view>
						<view class="flex-sub">
							<checkbox-group @change="CheckboxChange">
								<view class="flex text-df justify-end text-right align-center">
									<view class="text-black margin-right-sm">电话通知</view>
									<checkbox class="light-purple" :class="checkbox[0].checked?'checked':''" :checked="checkbox[0].checked?true:false"
									 value="phone"></checkbox>
								</view>
								<view class="flex text-df justify-end text-right align-center margin-top-sm">
									<view class="text-black margin-right-sm">短信通知</view>
									<checkbox class="light-purple" :class="checkbox[1].checked?'checked':''" :checked="checkbox[1].checked?true:false"
									 value="sms"></checkbox>
								</view>
							</checkbox-group>
						</view>
					</view>
				</view>
			</view>
		</view>

		<view class="box">
			<view class="cu-bar mytabbar foot tabbar">
				<view class="bottom-box">
					<view class="padding">
						<button class="cu-btn bg-dark-purple lg " style="width: 690upx; margin-bottom: 20upx;" @click="onConfirmChangeTel">确定</button>
					</view>
				</view>
			</view>
		</view>

		<!-- 添加手机号modal -->
		<view class="cu-modal" :class="modalName=='AddTelModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">添加电话</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>

				<form>
					<view class="cu-form-group">
						<view class="title">手机号码</view>
						<input class="text-left" placeholder="输入新手机号" name="input"></input>
					</view>

					<view class="cu-form-group">
						<view class="title">验 证 码 </view>
						<input class="text-left" placeholder="请输入验证码" name="input"></input>
						<view class="cu-btn bg-purple light" @click="veryfiying" v-if="state===false">获取验证码</view>
						<view class="cu-btn bg-grey" v-if="state===true">倒计时{{ currentTime }}s</view>
					</view>
				</form>

				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmAdd">确定</button>
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
				state: false, //是否开启倒计时
				totalTime: 60, //总时间，单位秒
				recordingTime: 0, //记录时间变量
				currentTime: 0, //显示时间变量
				modalName: null,
				listTouchStart: 0,
				listTouchDirection: null,
				checkbox: [{
					value: 'phone',
					checked: false
				}, {
					value: 'sms',
					checked: false
				}],
			}
		},
		methods: {
			onModifyTel(e) {

			},
			onDeleteTel(e) {

			},
			onConfirmAdd(e) {

			},
			CheckboxChange(e) {
				var items = this.checkbox,
					values = e.detail.value;
				for (var i = 0, lenI = items.length; i < lenI; ++i) {
					items[i].checked = false;
					for (var j = 0, lenJ = values.length; j < lenJ; ++j) {
						if (items[i].value == values[j]) {
							items[i].checked = true;
							break
						}
					}
				}
			},
			veryfiying() {
				//把显示时间设为总时间
				this.currentTime = this.totalTime;
				//开始倒计时
				this.state = true;
				//执行倒计时
				this.veryfiyingTime();
			},
			veryfiyingTime() {
				let that = this;
				//判断是否开启
				if (this.state) {
					//判断显示时间是否已到0，判断记录时间是否已到总时间
					if (this.currentTime > 0 && this.recordingTime <= this.totalTime) {
						//记录时间增加 1
						this.recordingTime = this.recordingTime + 1;
						//显示时间，用总时间 - 记录时间
						this.currentTime = this.totalTime - this.recordingTime;
						//1秒钟后，再次执行本方法
						setTimeout(() => {
							//定时器内，this指向外部，找不到vue的方法，所以，需要用that变量。
							that.veryfiyingTime();
						}, 1000)
					} else {
						//时间已完成，还原相关变量
						this.state = false; //关闭倒计时
						this.recordingTime = 0; //记录时间为0
						this.currentTime = this.totalTime; //显示时间为总时间
					}
				} else {
					//倒计时未开启，初始化默认变量
					this.state = false;
					this.recordingTime = 0;
					this.currentTime = this.totalTime;
				}
			},

			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			// ListTouch触摸开始
			ListTouchStart(e) {
				this.listTouchStart = e.touches[0].pageX
			},
			// ListTouch计算方向
			ListTouchMove(e) {
				this.listTouchDirection = e.touches[0].pageX - this.listTouchStart > 0 ? 'right' : 'left'
			},

			// ListTouch计算滚动
			ListTouchEnd(e) {
				if (this.listTouchDirection == 'left') {
					this.modalName = e.currentTarget.dataset.target
				} else {
					this.modalName = null
				}
				this.listTouchDirection = null
			}
		}
	}
</script>

<style>
	.mytabbar {
		z-index: 9999;
	},
	.card-margin {
		margin-top: -30upx;
	}
</style>
