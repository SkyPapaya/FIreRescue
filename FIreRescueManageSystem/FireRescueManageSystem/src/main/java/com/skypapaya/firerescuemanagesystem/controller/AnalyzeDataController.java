package com.skypapaya.firerescuemanagesystem.controller;

import com.skypapaya.firerescuemanagesystem.DAO.AnalyzeDataDAO;
import com.skypapaya.firerescuemanagesystem.DO.AnalyzeDataDO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AnalyzeDataController {

    @Autowired
    AnalyzeDataDAO analyzeDataDAO;

    //返回指定年份的数据（直接）
//    @GetMapping("/findByYearDe")
//    public AnalyzeDataDO findByYearDe(@RequestParam("year") int year) {
//        return analyzeDataDAO.findByYearDe(year);
//    }

    //返回指定年份的数据（间接）
    @GetMapping("/findByYearIn")
    public AnalyzeDataDO findByYearIn(@RequestParam("year") int year) {
        return analyzeDataDAO.findByYearIn(year);
    }
}
