public class LogLevels {

    public static String message(String logLine) {
        return logLine.replaceAll(
                "\\[(ERROR|WARNING|INFO)\\]:\\s*(.*)",
                "$2"
        ).trim();
    }

    public static String logLevel(String logLine) {
        String logLevel = logLine.replaceAll(
                "\\[(ERROR|WARNING|INFO)\\]:\\s*(.*)",
                "$1"
        );
        return logLevel.toLowerCase();
    }

    public static String reformat(String logLine) {
        String removedWhiteSpace = logLine.replaceAll("\\t\\s", "");
        String logLineFormated = removedWhiteSpace.replaceAll(
                "\\[(ERROR|WARNING|INFO)\\]:\\s*(.*)",
                "$2 "+"("+LogLevels.logLevel(logLine)+")"
        );
        return logLineFormated.replaceAll("\\r\\n","");
    }
}
