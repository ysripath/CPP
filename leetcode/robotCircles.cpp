class Solution {
public:
    bool judgeCircle(string moves) {
        int countU = std::count(moves.begin(), moves.end(), 'U');
        int countD = std::count(moves.begin(), moves.end(), 'D');
        if (countU != countD)
            return false;
        int countL = std::count(moves.begin(), moves.end(), 'L');
        int countR = std::count(moves.begin(), moves.end(), 'R');
        if (countL != countR)
            return false;
        return true;
    }
};
