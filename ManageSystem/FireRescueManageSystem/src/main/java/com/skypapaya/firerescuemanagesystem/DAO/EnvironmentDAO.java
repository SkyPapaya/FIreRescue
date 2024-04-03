package com.skypapaya.firerescuemanagesystem.DAO;

import com.skypapaya.firerescuemanagesystem.DO.EnvironmentDO;
import com.skypapaya.firerescuemanagesystem.model.Result;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDateTime;
import java.util.List;


@Mapper
@Repository
public interface EnvironmentDAO {

    public int insertEnvironmentDO(EnvironmentDO environmentDO);
    public EnvironmentDO getTheLasted();




}
