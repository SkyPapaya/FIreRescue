package com.skypapaya.firerescuemanagesystem;

import com.skypapaya.firerescuemanagesystem.DAO.EnvironmentDAO;
import com.skypapaya.firerescuemanagesystem.DAO.UserDAO;

import com.skypapaya.firerescuemanagesystem.DAO.VitalSignsDAO;
import com.skypapaya.firerescuemanagesystem.service.MqttPostPropertyMessageListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication

public class FireRescueManageSystemApplication implements ApplicationRunner {

    @Autowired
    UserDAO userDAO;
    @Autowired
    EnvironmentDAO environmentDAO;
    @Autowired
    VitalSignsDAO vitalSignsDAO;


    public static void main(String[] args) {
        SpringApplication.run(FireRescueManageSystemApplication.class, args);
    }

    @Override
    public void run(ApplicationArguments args) throws Exception {
        MqttPostPropertyMessageListener mqttPostPropertyMessageListener = new MqttPostPropertyMessageListener(vitalSignsDAO,environmentDAO);

        mqttPostPropertyMessageListener.getMessage();


    }
}
