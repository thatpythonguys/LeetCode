#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
  string s;
  int num = 0;
  cout << "Enter Numeral:";
  cin >> s;
  cout << s;
  unordered_map<char, int> RomanToArabic;
  RomanToArabic = { 
    {'I', 1}, 
    {'V', 5}, 
    {'X', 10}, 
    {'L', 50}, 
    {'C', 100}, 
    {'D', 500},
    {'M', 1000} };
  for (int i = 0; i != s.size(); i++) {
    cout << i << "\n" << s[i];
    if (i == s.size() - 1) {
      num = num + RomanToArabic[s[i]];
    }
    else if (RomanToArabic[s[i]] < RomanToArabic[s[i + 1]]) {
      num = num - RomanToArabic[s[i]];
    }
    else if (RomanToArabic[s[i]] >= RomanToArabic[s[i + 1]]) {
      num = num + RomanToArabic[s[i]];
    }
  }
  cout << "\n" << num;
  /*int romanToInt(string s){
    for (int i = 0, i < s.length(), s++)
    if
  } */
return 0;
}
