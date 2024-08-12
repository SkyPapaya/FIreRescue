import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import VueSetupExtend from 'vite-plugin-vue-setup-extend';
import AutoImport from 'unplugin-auto-import/vite';
import Components from 'unplugin-vue-components/vite';
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers';



export default defineConfig({
	build: {
		chunkSizeWarningLimit: 16000
	},

	base: './',
	plugins: [
		vue(),
		VueSetupExtend(),
		AutoImport({
			resolvers: [ElementPlusResolver()]
		}),
		Components({
			resolvers: [ElementPlusResolver()]
		})
	],
	optimizeDeps: {
		include: ['schart.js']
	},
	//跨域代理
	server:{
		//端口号
		port: 5173,
		proxy: {
			// 代理所有以 /api 开头的请求
			'/api': {
				target: 'http://localhost:8080', // 你的后端 API 地址
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/api/, ''), // 可选：移除 /api 前缀
			},
		},
	},


});
