public class LogLine {

    private LogLevel logLevel;
    private String logLine;

    public LogLine(String logLine) {
    this.logLevel = switch (extractCode(logLine)) {
        case "TRC" -> LogLevel.TRACE;
        case "DBG" -> LogLevel.DEBUG;
        case "INF" -> LogLevel.INFO;
        case "WRN" -> LogLevel.WARNING;
        case "ERR" -> LogLevel.ERROR;
        case "FTL" -> LogLevel.FATAL;
        default -> LogLevel.UNKNOWN;
        };
    this.logLine = this.extractMessage( logLine).trim();
    }

    public LogLevel getLogLevel() {
        return this.logLevel;
    }

    public String getOutputForShortLog() {
        return(this.setCode() + ":" + this.logLine );
    }

    private String extractCode(String logLine) {
    return logLine.substring(logLine.indexOf("[") + 1, logLine.indexOf("]"));
    }

    private String extractMessage(String logLine) {
        return logLine.substring(logLine.indexOf(":") + 1);
    }

    private int setCode() {
        return switch(this.logLevel) {
            case LogLevel.UNKNOWN -> 0;
            case LogLevel.TRACE -> 1;
            case LogLevel.DEBUG -> 2;
            case LogLevel.INFO -> 4;
            case LogLevel.WARNING -> 5;
            case LogLevel.ERROR -> 6;
            default -> 42;
        };
    }
}
