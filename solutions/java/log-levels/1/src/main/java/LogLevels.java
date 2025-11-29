public class LogLevels {
    
    public static String message(String logLine) {
        String[] splitStr = logLine.split(" ", 2);
        return splitStr[1].trim();
    }

    public static String logLevel(String logLine) {
        if (logLine.contains("ERROR")){
            return "error";
        }
        if (logLine.contains("WARNING")){
            return "warning";
        }
        return "info";
    }

    public static String reformat(String logLine) {
        return String.format("%s (%s)", message(logLine), logLevel(logLine));
    }
}
