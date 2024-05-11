package com.skypapaya.firerescuemanagesystem.DO;

import lombok.Data;

import java.time.LocalDateTime;

@Data
public class AnalyzeDataDO {

    int year;
    //直接损失
//    double deJan;
//    double deFeb;
//    double deMar;
//    double deApr;
//    double deMay;
//    double deJun;
//    double deJul;
//    double deAug;
//    double deSep;
//    double deOct;
//    double deNov;
//    double deDec;
    //间接损失
    double inJan;
    double inFeb;
    double inMar;
    double inApr;
    double inMay;
    double inJun;
    double inJul;
    double inAug;
    double inSep;
    double inOct;
    double inNov;
    double inDec;
    LocalDateTime gmtCreated;
    LocalDateTime gmtModified;


}
