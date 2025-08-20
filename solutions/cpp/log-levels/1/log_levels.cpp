#include <string>

namespace log_line {
    std::string message(std::string line) {
        // return the message
        //int find = line.find(":");
        return line.substr(line.find(":")+2);
    }
    
    std::string log_level(std::string line) {
        // return the log level
        return line.substr(line.find("[")+1, line.find("]")-1);
    }
    
    std::string reformat(std::string line) {
        // return the reformatted message
        return message(line) + " (" + log_level(line) + ")";
    }
}  // namespace log_line
