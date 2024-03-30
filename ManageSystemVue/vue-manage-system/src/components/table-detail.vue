<template>
	<el-descriptions title="" :column="2" border>
		<el-descriptions-item>
			<template #label> 用户ID </template>
			{{ data.id }}
		</el-descriptions-item>
		<el-descriptions-item>
			<template #label> 用户名 </template>
			{{ data.name }}
		</el-descriptions-item>
		<el-descriptions-item>
			<template #label> 邮箱 </template>
			{{ data.e_mail }}
		</el-descriptions-item>
		<el-descriptions-item>
			<template #label> 电话号码 </template>
			{{ data.phone  }}
		</el-descriptions-item>
		<el-descriptions-item :span="2">
			<template #label> 权限 </template>
			{{ data.authority }}
		</el-descriptions-item>
		<el-descriptions-item>
			<template #label> 地址 </template>
			{{ data.address }}
		</el-descriptions-item>
		<el-descriptions-item>
			<template #label> 注册时间 </template>
			<img :src="data.createdTime" style="width: 120px" alt="" />
		</el-descriptions-item>
	</el-descriptions>
</template>

<script lang="ts" setup>
const props = defineProps({
	data: {
		type: Object,
		required: true
	}
});
</script>
