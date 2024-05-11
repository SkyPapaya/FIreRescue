package com.skypapaya.firerescuemanagesystem.controller;

import com.skypapaya.firerescuemanagesystem.DAO.VitalSignsDAO;
import com.skypapaya.firerescuemanagesystem.DO.VitalSignsDO;
import com.skypapaya.firerescuemanagesystem.model.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class VitalController {
    @Autowired
    VitalSignsDAO vitalSignsDAO;

    @GetMapping("vital/getTheLatest")
    public Result getTheLasted() {
        Result result = new Result();
        VitalSignsDO vitalSignsDO = vitalSignsDAO.getTheLastedVitalSigns();
        if (vitalSignsDO == null) {
            result.setCode("404");
            result.setMessage("没有数据");
            return result;
        }
        result.setData(vitalSignsDO);
        return Result.success(vitalSignsDO);
    }
}
