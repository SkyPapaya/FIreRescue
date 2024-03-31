package com.skypapaya.firerescuemanagesystem.DAO;

import com.skypapaya.firerescuemanagesystem.DO.AnalyzeDataDO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface AnalyzeDataDAO {

    //返回指定年份的数据（直接）
    public AnalyzeDataDO findByYearDe(@Param("year") int year);

    //返回指定年份的数据（间接）
    public AnalyzeDataDO findByYearIn(@Param("year") int year);


}
