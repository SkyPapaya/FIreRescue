package com.skypapaya.firerescuemanagesystem.config;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@MapperScan("com.skypapaya.firerescuemanagesystem.DAO")
public class MyBatisConfig {
}

