import axios, { AxiosInstance, AxiosError, AxiosResponse, AxiosRequestConfig } from 'axios';
const service: AxiosInstance = axios.create({
    baseURL: 'http://localhost:8080', // 只需指定主机名和端口号
    timeout: 5000
});

// @ts-ignore
service.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        return config;
    },
    (error: AxiosError) => {
        console.error('Request Error:', error);
        return Promise.reject(error);
    }
);

service.interceptors.response.use(
    (response: AxiosResponse) => {
        if (response.status === 200) {
            let res = response.data;

            return res;
        } else {
            return Promise.reject('Response Error: Non-200 status code');
        }
    },
    (error: AxiosError) => {
        console.error('Response Error:', error);
        return Promise.reject(error);
    }
);

export default service;
