package com.skypapaya.firerescuemanagesystem.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.skypapaya.firerescuemanagesystem.model.MqttSign;
import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.*;

class MqttPostPropertyMessageListener implements IMqttMessageListener {

    private static void extractValues(JSONObject jsonObject) {
        for (String key : jsonObject.keySet()) {
            Object value = jsonObject.get(key);
            if (value instanceof JSONObject) {
                // 如果值是 JSONObject，则递归调用此函数
                extractValues((JSONObject) value);
            } else if (value instanceof JSONArray) {
                // 如果值是 JSONArray，则遍历数组递归调用此函数
                JSONArray jsonArray = (JSONArray) value;
                for (int i = 0; i < jsonArray.size(); i++) {
                    extractValues(jsonArray.getJSONObject(i));
                }
            } else {
                // 如果值是具体的值，且键是"value"，则打印该值
                if ("value".equals(key)) {
                    System.out.println(value);
                }
            }
        }
    }

    @Override
    public void messageArrived(String var1, MqttMessage var2) throws Exception {
        System.out.println("reply topic  : " + var1);
        System.out.println("reply payload: " + var2.toString());
        //循环处理在这个触发
        //解析json信息并存入数据库
        JSONObject jsonObject = JSON.parseObject(var2.toString());

        //double coValue = jsonObject.getJSONObject("items").getJSONObject("CO").getDouble("value");
        JSONObject co = jsonObject.getJSONObject("items");

        System.out.println("CO value: " + jsonObject);
    }
}

public class MqttMessageService {
    public static void main(String[] args) {
        String productKey = "k0yvucnhaHD";
        String deviceName = "java_server_01";
        String deviceSecret = "63f97e57a1ac4590d048c461c9e0de22";

        //计算Mqtt建联参数
        MqttSign sign = new MqttSign();
        sign.calculate(productKey, deviceName, deviceSecret);

//        System.out.println("username: " + sign.getUsername());
//        System.out.println("password: " + sign.getPassword());
//        System.out.println("clientid: " + sign.getClientid());

        //使用Paho连接阿里云物联网平台
        String port = "443";
        String broker = "ssl://" + productKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com" + ":" + port;
        MemoryPersistence persistence = new MemoryPersistence();
        try {
            //Paho Mqtt 客户端
            MqttClient sampleClient = new MqttClient(broker, sign.getClientid(), persistence);

            //Paho Mqtt 连接参数
            MqttConnectOptions connOpts = new MqttConnectOptions();
            connOpts.setCleanSession(true);
            connOpts.setKeepAliveInterval(180);
            connOpts.setUserName(sign.getUsername());
            connOpts.setPassword(sign.getPassword().toCharArray());
            sampleClient.connect(connOpts);
            //System.out.println("broker: " + broker + " Connected");

            //Paho Mqtt 消息订阅
            String topicReply = "/sys/" + productKey + "/" + deviceName + "/thing/event/property/post_reply";
            sampleClient.subscribe(topicReply, new MqttPostPropertyMessageListener());

            //Paho Mqtt 消息发布
            String topic = "/sys/" + productKey + "/" + deviceName + "/thing/event/property/post";
            String content = "{\"id\":\"1\",\"version\":\"1.0\",\"params\":{\"LightSwitch\":1}}";
            MqttMessage message = new MqttMessage(content.getBytes());
            message.setQos(0);
            sampleClient.publish(topic, message);
            // Thread.sleep(20000);

            //Paho Mqtt 断开连接
            //sampleClient.disconnect();
            //System.out.println("Disconnected");
            //System.exit(0);
        } catch (MqttException e) {
            System.out.println("reason " + e.getReasonCode());
            System.out.println("msg " + e.getMessage());
            System.out.println("loc " + e.getLocalizedMessage());
            System.out.println("cause " + e.getCause());
            System.out.println("excep " + e);
            e.printStackTrace();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
        }
    }
}