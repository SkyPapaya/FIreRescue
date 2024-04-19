package com.skypapaya.firerescuemanagesystem.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.skypapaya.firerescuemanagesystem.DAO.EnvironmentDAO;
import com.skypapaya.firerescuemanagesystem.DAO.VitalSignsDAO;
import com.skypapaya.firerescuemanagesystem.DO.EnvironmentDO;
import com.skypapaya.firerescuemanagesystem.DO.VitalSignsDO;
import com.skypapaya.firerescuemanagesystem.model.MqttSign;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

import java.io.InputStream;

public class MqttPostPropertyMessageListener implements IMqttMessageListener {
    private  VitalSignsDAO vitalSignsDAO;
    private  EnvironmentDAO environmentDAO;

    public MqttPostPropertyMessageListener(VitalSignsDAO vitalSignsDAO, EnvironmentDAO environmentDAO) {
        this.vitalSignsDAO = vitalSignsDAO;
        this.environmentDAO = environmentDAO;
    }

    @Override
    public void messageArrived(String var1, MqttMessage var2) throws Exception {
        try {
            JSONObject jsonObject = JSON.parseObject(var2.toString());

            float breathingRate = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("BreathingRate").getString("value"));
            Integer heartRate = Integer.parseInt(jsonObject.getJSONObject("checkFailedData").getJSONObject("HeartRate").getString("value"));
            float signalStrength = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("SignalStrength").getString("value"));
            Integer active = Integer.parseInt(jsonObject.getJSONObject("checkFailedData").getJSONObject("active").getString("value"));
            Integer distance = Integer.parseInt(jsonObject.getJSONObject("checkFailedData").getJSONObject("distance").getString("value"));
            Integer exist = Integer.parseInt(jsonObject.getJSONObject("checkFailedData").getJSONObject("exist").getString("value"));
            Integer life = Integer.parseInt(jsonObject.getJSONObject("checkFailedData").getJSONObject("life").getString("value"));
            Integer people = Integer.parseInt(jsonObject.getJSONObject("checkFailedData").getJSONObject("people").getString("value"));

            VitalSignsDO vitalSignsDO = new VitalSignsDO(breathingRate, heartRate, signalStrength, active, distance, exist, life, people);
            vitalSignsDAO.insertVitalSignsDO(vitalSignsDO);

            float co = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("CO").getString("value"));
            float fire = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("FIRE").getString("value"));
            float humidity = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("Humidity").getString("value"));
            float risk = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("Risk").getString("value"));
            float smoke = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("smoke").getString("value"));
            float temperature = Float.parseFloat(jsonObject.getJSONObject("checkFailedData").getJSONObject("temperature").getString("value"));

            EnvironmentDO environmentDO = new EnvironmentDO(co, fire, humidity, risk, smoke, temperature);
            environmentDAO.insertEnvironmentDO(environmentDO);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void getMessage() {
        String productKey = "k0yvucnhaHD";
        String deviceName = "java_server_01";
        String deviceSecret = "63f97e57a1ac4590d048c461c9e0de22";

        MqttSign sign = new MqttSign();
        sign.calculate(productKey, deviceName, deviceSecret);

        String port = "443";
        String broker = "ssl://" + productKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com" + ":" + port;
        MemoryPersistence persistence = new MemoryPersistence();

        try {
            MqttClient sampleClient = new MqttClient(broker, sign.getClientid(), persistence);
            MqttConnectOptions connOpts = new MqttConnectOptions();
            connOpts.setCleanSession(true);
            connOpts.setKeepAliveInterval(180);
            connOpts.setUserName(sign.getUsername());
            connOpts.setPassword(sign.getPassword().toCharArray());
            sampleClient.connect(connOpts);

            String topicReply = "/sys/" + productKey + "/" + deviceName + "/thing/event/property/post_reply";
            sampleClient.subscribe(topicReply, this);

        } catch (MqttException e) {
            e.printStackTrace();
        }
    }
}
