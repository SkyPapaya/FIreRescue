package com.skypapaya.firerescuemanagesystem.model;

public class Result {
    //状态码
    String code;
    //发送的信息
    String message;
    //返回的数据
    Object data;

    public Result(String code, String message, Object data) {
        this.code = code;
        this.message = message;
        this.data = data;
    }

    public Result(String code, String message) {
        this.code = code;
        this.message = message;
    }

    public Result() {
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public Object getData() {
        return data;
    }

    public void setData(Object data) {
        this.data = data;
    }

    //传输成功
    public static Result success() {
        return new Result("200", "success");
    }

    public static Result success(Object data) {
        return new Result("200", "success", data);
    }

    public static Result error(String message) {
        return new Result("500", message);
    }

    public static Result error(String code, String message) {
        return new Result(code, message);
    }

    //传输失败
    public static Result fail() {
        return new Result("500", "fail");
    }
}
