package com.skypapaya.firerescuemanagesystem.DAO;

import com.skypapaya.firerescuemanagesystem.DO.EnvironmentDO;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.web.bind.annotation.RequestParam;

import java.time.LocalDateTime;
import java.util.List;


@Mapper
public interface EnvironmentDAO {

    // 1.查询所有环境数据
    public List<EnvironmentDO> findAll();

    // 2.插入环境数据
    int insertEnvironment(EnvironmentDO environment);

    // 3.删除环境数据
    int delete(@Param("id") Long id);

    // 4.分页查询的实现
    List<EnvironmentDO> page(int pageNum, int size);

    // 5.返回数据库的总条数
    int count();

    // 6.根据id查询环境数据
    EnvironmentDO findById(@Param("id") Long id);

    // 7.更新环境数据
    int update(EnvironmentDO environment);

    // 9.根据温度查询环境数据
    List<EnvironmentDO> findByTemperature(@Param("min") int min, @Param("max") int max);

    // 10.根据co查询环境数据
    List<EnvironmentDO> findByCo(@Param("min") int min, @Param("max") int max);


    // 12.根据probability查询环境数据
    List<EnvironmentDO> findByProbability(@Param("min") int min, @Param("max") int max);

}
