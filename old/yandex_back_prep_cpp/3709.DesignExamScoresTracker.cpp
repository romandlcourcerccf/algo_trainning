#include <vector>

class ExamTracker
{
public:
    ExamTracker()
    {
    }

    void record(int time, int score)
    {
        this->times.push_back(time);
        this->scores.push_back(score);

        this->calc_prefix(time, score);
    }

    long long totalScore(int startTime, int endTime)
    {
        
    }

private:
    std::vector<int> times;
    std::vector<int> scores;

    void calc_prefix(int time, int score)
    {
    }
};

/**
 * Your ExamTracker object will be instantiated and called as such:
 * ExamTracker* obj = new ExamTracker();
 * obj->record(time,score);
 * long long param_2 = obj->totalScore(startTime,endTime);
 */