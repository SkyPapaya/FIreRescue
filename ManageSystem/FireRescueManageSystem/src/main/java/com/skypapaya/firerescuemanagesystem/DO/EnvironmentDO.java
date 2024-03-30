package com.skypapaya.firerescuemanagesystem.DO;

import lombok.Data;

import java.time.LocalDateTime;

@Data
public class EnvironmentDO {

    Long id;
    String thermalImage;
    String humidity;
    int temperature;
    String people;
    int fireExist;
    int smoke;
    int co;
    int risk;
    String address;
    LocalDateTime createTime;
    LocalDateTime modifyTime;
}
