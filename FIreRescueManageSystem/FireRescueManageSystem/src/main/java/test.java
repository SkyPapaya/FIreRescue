
import com.alibaba.fastjson.JSONObject;

public class test {
    public static void main(String[] args) {
        String jsonString = "{\"checkFailedData\":{\"Risk\":{\"code\":5092,\"message\":\"property not found\",\"time\":1712066459367,\"value\":0.4694334},\"red\":{\"code\":6310,\"message\":\"tsl parse: data type is not string -> red\",\"time\":1712066459367,\"value\":0}},\"deviceName\":\"863569067667709\",\"deviceType\":\"CustomCategory\",\"gmtCreate\":1712066459378,\"iotId\":\"FXNobzrdSgeUMC6VnZ33k0yvu0\",\"items\":{\"BreathingRate\":{\"time\":1712066459367,\"value\":20},\"CO\":{\"time\":1712066459367,\"value\":7.33},\"FIRE\":{\"time\":1712066459367,\"value\":0},\"HeartRate\":{\"time\":1712066459367,\"value\":55},\"Humidity\":{\"time\":1712066459367,\"value\":79.8},\"active\":{\"time\":1712066459367,\"value\":3},\"exist\":{\"time\":1712066459367,\"value\":0},\"people\":{\"time\":1712066459367,\"value\":0},\"smoke\":{\"time\":1712066459367,\"value\":4.52},\"temperature\":{\"time\":1712066459367,\"value\":22.47},\"timestamp\":{\"time\":1712066459367,\"value\":\"2024-03-25 16:36:42\"}},\"productKey\":\"k0yvucnhaHD\",\"requestId\":\"null\"}";
        JSONObject jsonObject = JSONObject.parseObject(jsonString);

        // 获取特定值的示例
        String deviceName = jsonObject.getString("deviceName");
        double humidityValue = jsonObject.getJSONObject("items").getJSONObject("Humidity").getDouble("value");

        // 打印获取的值
        System.out.println("Humidity Value: " + humidityValue);

    }
}
