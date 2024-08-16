package com.skypapaya.firerescuemanagesystem.service;

import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import java.io.BufferedReader;
import java.io.InputStreamReader;

@Component
public class PythonScriptRunner {

    @PostConstruct
    public void runPythonScript() {
        try {
            // 替换为你的Python脚本路径
            String pythonScriptPath1 = "D:\\Code\\FireRescue\\FireRescue\\RadarThermogram\\EscapeRout.py";
            String pythonScriptPath2 = "D:\\Code\\FireRescue\\FireRescue\\RadarThermogram\\mqtt.py";


            ProcessBuilder processBuilder1= new ProcessBuilder("python3", pythonScriptPath1);
            ProcessBuilder processBuilder2 = new ProcessBuilder("python3", pythonScriptPath2);

            processBuilder1.redirectErrorStream(true);
            Process process1 = processBuilder1.start();

            processBuilder2.redirectErrorStream(true);
            Process process2 = processBuilder2.start();

            BufferedReader reader1 = new BufferedReader(new InputStreamReader(process1.getInputStream()));
            BufferedReader reader2 = new BufferedReader(new InputStreamReader(process2.getInputStream()));
            String line;
            while ((line = reader1.readLine()) != null) {
                System.out.println(line);
            }

            while ((line = reader2.readLine()) != null) {
                System.out.println(line);
            }

            int exitCode1 = process1.waitFor();
            System.out.println("Python script exited with code: " + exitCode1);

            int exitCode2 = process2.waitFor();
            System.out.println("Python script exited with code: " + exitCode2);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
