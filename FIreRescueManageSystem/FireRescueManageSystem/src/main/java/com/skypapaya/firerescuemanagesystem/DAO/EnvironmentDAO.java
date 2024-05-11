package com.skypapaya.firerescuemanagesystem.DAO;

import com.skypapaya.firerescuemanagesystem.DO.EnvironmentDO;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;


@Mapper
@Repository
public interface EnvironmentDAO {

    public int insertEnvironmentDO(EnvironmentDO environmentDO);
    public List<EnvironmentDO> getTheLatest();




}
