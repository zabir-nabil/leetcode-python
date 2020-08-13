// https://leetcode.com/problems/reverse-string/
// easy, but used c++

using namespace std;
class Solution {
public:
    
    void reverseString(vector<char>& s) {
        
        for(int i=0;i<s.size();i++)
        {
            char c = s[i];
            int j = s.size() - 1 - i;
            s[i] = s[j];
            s[j] = c;
            if ((j-i) <=1)
            {
                break;
            }
            //std::cout<<c<<endl;
            
        }
        
    }
};