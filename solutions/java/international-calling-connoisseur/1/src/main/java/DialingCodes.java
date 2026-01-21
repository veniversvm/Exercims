import java.util.Map;
import java.util.HashMap;

public class DialingCodes {

    private Map<Integer, String> map =new HashMap<>();

    public Map<Integer, String> getCodes() {
        return map;
    }

    public void setDialingCode(Integer code, String country) {
        this.map.put(code, country);
    }

    public String getCountry(Integer code) {
        return map.containsKey(code) ? map.get(code) : "";
    }

    public void addNewDialingCode(Integer code, String country) {
        if (map.containsKey(code) || map.containsValue(country)) 
            return;
        
        setDialingCode(code, country);
    }

    public Integer findDialingCode(String country) {
         for (Map.Entry<Integer, String> e : map.entrySet()) {
                 if (country == e.getValue())
                     return e.getKey();
             }
        return null;
    }

    public void updateCountryDialingCode(Integer code, String country) {
        if (!map.containsValue(country)) 
            return;
        // The country is elminated
        map.remove(findDialingCode(country));
        // Create a new entry
        addNewDialingCode(code,country);
        
    }
}
