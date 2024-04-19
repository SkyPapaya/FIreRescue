package com.skypapaya.firerescuemanagesystem.DO;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.Data;

import java.time.LocalDateTime;

import static java.time.LocalDateTime.now;

@Data
public class VitalSignsDO {
    long id;
    float breathRate;
    Integer heartRate;
    float signalStrength;
    Integer active;
    Integer distance;
    Integer exist;
    Integer life;
    Integer people;
    @JsonIgnore
    VitalSignsDO vitalSignsDO;
    LocalDateTime createTime;
    LocalDateTime modifyTime;

    public VitalSignsDO getVitalSignsDO() {
        return vitalSignsDO;
    }

    public void setVitalSignsDO(VitalSignsDO vitalSignsDO) {
        this.vitalSignsDO = vitalSignsDO;
    }

    public LocalDateTime getCreateTime() {
        return createTime;
    }

    public void setCreateTime(LocalDateTime createTime) {
        this.createTime = createTime;
    }

    public LocalDateTime getModifyTime() {
        return modifyTime;
    }

    public void setModifyTime(LocalDateTime modifyTime) {
        this.modifyTime = modifyTime;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public float getBreathRate() {
        return breathRate;
    }

    public void setBreathRate(float breathRate) {
        this.breathRate = breathRate;
    }

    public Integer getHeartRate() {
        return heartRate;
    }

    public void setHeartRate(Integer heartRate) {
        this.heartRate = heartRate;
    }

    public float getSignalStrength() {
        return signalStrength;
    }

    public void setSignalStrength(float signalStrength) {
        this.signalStrength = signalStrength;
    }

    public Integer getActive() {
        return active;
    }

    public void setActive(Integer active) {
        this.active = active;
    }

    public Integer getDistance() {
        return distance;
    }

    public void setDistance(Integer distance) {
        this.distance = distance;
    }

    public Integer getExist() {
        return exist;
    }

    public void setExist(Integer exist) {
        this.exist = exist;
    }

    public Integer getLife() {
        return life;
    }

    public void setLife(Integer life) {
        this.life = life;
    }

    public Integer getPeople() {
        return people;
    }

    public void setPeople(Integer people) {
        this.people = people;
    }


    public VitalSignsDO(float breathRate, Integer heatRate, float signalStrength, Integer active, Integer distance, Integer exist, Integer life, Integer people) {
        this.breathRate = breathRate;
        this.heartRate = heatRate;
        this.signalStrength = signalStrength;
        this.active = active;
        this.distance = distance;
        this.exist = exist;
        this.life = life;
        this.people = people;
        this.createTime = now();
        this.modifyTime = now();
    }

    public VitalSignsDO() {
    }


}
