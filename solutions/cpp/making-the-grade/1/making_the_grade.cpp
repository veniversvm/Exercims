#include <array>
#include <string>
#include <vector>
// I include theses libraries to the problem
#include <cmath>

// Round down all provided student scores.
std::vector<int> round_down_scores(std::vector<double> student_scores) {
    std::vector<int> round_scores {};
    for (int i = 0; i < student_scores.size(); i++)
        {
            round_scores.push_back(floor(student_scores.at(i)));
        }
    return round_scores;
}

// Count the number of failing students out of the group provided.
int count_failed_students(std::vector<int> student_scores) {
    int count {0};
    for (int i = 0; i < student_scores.size(); i++)
        {
            if (student_scores.at(i) <= 40)
                count++;
        }
    return count;
}

// Create a list of grade thresholds based on the provided highest grade.
std::array<int, 4> letter_grades(int highest_score) {
    std::array<int, 4> grades {};
    int step = (highest_score - 40 ) / 4;
    int i = 0; 
    int grade = 41; 
    
    while(i < highest_score && i < 4)
    {
        grades.at(i) = grade;
        grade += step;
        i++;
    }
    
    return grades;
}
// Organize the student's rank, name, and grade information in ascending order.
std::vector<std::string> student_ranking(
    std::vector<int> student_scores, std::vector<std::string> student_names) {
    
    std::vector<std::string> student_ranking_vec {};
    if (student_scores.size() != student_names.size())
        return student_ranking_vec;

    student_ranking_vec.resize(student_scores.size());
    
    for (int i = 0; i < student_scores.size(); i++ )
        {
            student_ranking_vec.at(i) = std::to_string(i + 1) + ". " + student_names.at(i) + ": " + std::to_string(student_scores.at(i));
        }
    
    return student_ranking_vec;
}

// Create a string that contains the name of the first student to make a perfect
// score on the exam.
std::string perfect_score(std::vector<int> student_scores,
                          std::vector<std::string> student_names) {
    if (student_scores.size() != student_names.size())
        return "";

    for (int i = 0; i < student_scores.size(); i++)
        {
            if (student_scores.at(i) == 100)
                return student_names.at(i);
        }
    return "";
}
