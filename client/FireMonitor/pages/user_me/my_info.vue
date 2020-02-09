<template>
	<view>
		<cu-custom bgColor="bg-gradual-dark-purple" :isBack="true">
			<block slot="content">帐户管理</block>
		</cu-custom>

		<view class="cu-item">
			<view class="cu-form-group margin-top">
				<view class="flex align-center">
					<text class="text-lg">头像</text>
				</view>
				<view class="margin cu-avatar lg round" style="background-image:url(../../static/me/head3.png);"></view>
			</view>
		</view>

		<view class="cu-list menu margin-top">
			<view class="cu-item" :class="menuArrow?'arrow':''" @tap="showModal" data-target="ModifyNicknameModal">
				<view class="content">
					<text class="text-lg">昵称</text>
				</view>
				<view class="action">
					<text class="text-grey text-lg margin-right-sm">昵称XX</text>
					<text class="cuIcon-right text-gray"></text>
				</view>
			</view>
			<view class="cu-item" :class="menuArrow?'arrow':''" @tap="showModal" data-target="ModifyTelModal">
				<view class="content">
					<text class="text-lg">手机</text>
				</view>
				<view class="action">
					<text class="text-grey text-lg margin-right-sm">17499939339</text>
					<text class="cuIcon-right text-gray"></text>
				</view>
			</view>
			<view class="cu-item" :class="menuArrow?'arrow':''" @tap="gotoModifyPass">
				<view class="content">
					<text class="text-lg">密码</text>
				</view>
				<view class="action">
					<text class="cuIcon-right text-gray"></text>
				</view>
			</view>
		</view>

		<!-- 修改telmodal -->
		<view class="cu-modal" :class="modalName=='ModifyTelModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">修改电话</view>
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
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmModify">修改</button>
					</view>
				</view>
			</view>
		</view>
		
		<!-- 修改昵称modal -->
		<view class="cu-modal" :class="modalName=='ModifyNicknameModal'?'show':''">
			<view class="cu-dialog">
				<view class="cu-bar bg-white justify-end">
					<view class="content">修改昵称</view>
					<view class="action" @tap="hideModal">
						<text class="cuIcon-close text-light-purple"></text>
					</view>
				</view>
		
				<form>
					<view class="cu-form-group">
						<view class="title">昵称</view>
						<input class="text-left" placeholder="输入新昵称" name="input"></input>
					</view>
				</form>
		
				<view class="cu-bar bg-white justify-end">
					<view class="action">
						<button class="cu-btn line-green text-purple" @tap="hideModal">取消</button>
						<button class="cu-btn bg-gradual-dark-purple margin-left" @tap="onConfirmModify">修改</button>
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
				modalName: null,
			}
		},
		methods: {
			showModal(e) {
				this.modalName = e.currentTarget.dataset.target
			},
			hideModal(e) {
				this.modalName = null
			},
			gotoModifyPass(){
				uni.navigateTo({
					url:'./modify_pass'
				})
			}
		}
	}
</script>

<style>

</style>
