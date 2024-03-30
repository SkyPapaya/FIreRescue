package com.skypapaya.firerescuemanagesystem.controller;

import com.skypapaya.firerescuemanagesystem.DAO.EnvironmentDAO;
import com.skypapaya.firerescuemanagesystem.DO.EnvironmentDO;
import com.skypapaya.firerescuemanagesystem.model.Result;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class EnvironmentController {

    @Autowired
    EnvironmentDAO environmentDAO;

    //返回所有环境信息
    @GetMapping("/environments")
    public Result findAll() {
        List<EnvironmentDO> environments = environmentDAO.findAll();
        return Result.success(environments);
    }

    //环境分页查询
    @GetMapping("/environmentPage")
    public Result page(@RequestParam("pageNum") int pageNum, @RequestParam("size") int size) {
        pageNum = (pageNum - 1) * size;
        Map<String, Object> res = new HashMap<>();
        res.put("total", environmentDAO.count());
        res.put("data", environmentDAO.page(pageNum, size));
        return Result.success(res);
    }

    @GetMapping("/environmentCount")
    public int count() {
        return environmentDAO.count();
    }

    @PostMapping("/insertEnvironment")
    @ResponseBody
    public int insertEnvironment(@RequestBody EnvironmentDO environment) {
        return environmentDAO.insertEnvironment(environment);
    }


}
