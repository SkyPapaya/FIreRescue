package com.skypapaya.firerescuemanagesystem.DAO;

import com.skypapaya.firerescuemanagesystem.DO.VitalSignsDO;
import com.skypapaya.firerescuemanagesystem.model.Result;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import java.rmi.server.RemoteRef;
import java.util.List;

@Mapper
@Repository
public interface VitalSignsDAO {
    public int insertVitalSignsDO(VitalSignsDO vitalSignsDO);

    public VitalSignsDO getTheLastedVitalSigns();
}
