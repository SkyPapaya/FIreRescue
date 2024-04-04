package com.skypapaya.firerescuemanagesystem.controller;
import com.skypapaya.firerescuemanagesystem.DAO.EnvironmentDAO;
import com.skypapaya.firerescuemanagesystem.DO.EnvironmentDO;
import com.skypapaya.firerescuemanagesystem.model.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
@RestController
public class EnvironmentController {
    @Autowired
    EnvironmentDAO environmentDAO;
    //查询最新的一条数据
    @GetMapping("environment/getTheLatest")
    public Result getTheLasted() {
        Result result = new Result();
        EnvironmentDO environment = environmentDAO.getTheLatest();
        if (environment == null) {
            result.setCode("404");
            result.setMessage("没有数据");
            return result;
        }
        result.setData(environment);
        return Result.success(environment);
    }
    //插入数据
    @ResponseBody
    @PostMapping("environment/insertEnvironment")
    public Result insertEnvironmentDO(@RequestBody EnvironmentDO environment) {
        EnvironmentDO environmentDO = new EnvironmentDO();
        int res = environmentDAO.insertEnvironmentDO(environmentDO);
        if (res == 1) {
            return Result.success("插入成功");
        } else {
            return Result.error("插入失败");
        }
    }
}
