#include <iostream>
#include <set>
#include <string>
using namespace std;

const int N_CHARACTERS = 14;

int main() {
  freopen("day6.input.txt", "r", stdin);

  string s;
  getline(cin, s);

  set<char> chars(s.begin(), s.begin() + (N_CHARACTERS - 1));

  for (int i = (N_CHARACTERS - 1); i < s.size(); i++) {
    auto ss = s.substr(i - (N_CHARACTERS - 1), N_CHARACTERS);
    if (ss.find(s[i - N_CHARACTERS]) == ss.npos)
      chars.erase(s[i - N_CHARACTERS]);
    chars.insert(s[i]);
    if (chars.size() == N_CHARACTERS) {
      cout << i + 1 << endl;
      break;
    }
  }
}
