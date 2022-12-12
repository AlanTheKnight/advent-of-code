#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> heights;

pair<bool, int> solve(int r, int c, const int h, const int w) {
  if (r == 0 || c == 0 || r == h - 1 || c == w - 1) return make_pair(true, 0);

  int val = heights[r][c], vCount = 0, score = 1;
  int dx[] = {1, -1, 0, 0};
  int dy[] = {0, 0, 1, -1};

  for (int i = 0; i < 4; i++) {
    int score_cnt = 0;
    for (int row = r + dy[i], col = c + dx[i];
         row >= 0 && col >= 0 && row < h && col < w;
         row += dy[i], col += dx[i]) {
      score_cnt++;
      if (heights[row][col] >= val) {
        vCount++;
        break;
      }
    }
    score *= score_cnt;
  }

  return make_pair(vCount != 4, score);
}

int main(int argc, char* argv[]) {
  string line;
  fstream file("input/day8.input.txt");

  while (getline(file, line)) {
    heights.emplace_back();
    for (const char c : line) heights.back().emplace_back(c - '0');
  }

  const int h = heights.size(), w = heights[0].size();
  int part1_ans = 0, part2_ans = 0;

  vector<vector<bool>> visible(h, vector<bool>(w, false));

  for (int r = 0; r < h; r++) {
    for (int c = 0; c < w; c++) {
      auto x = solve(r, c, h, w);
      visible[r][c] = x.first;
      part2_ans = max(part2_ans, x.second);
    }
  }

  for (auto r : visible)
    for (auto c : r)
      if (c) part1_ans++;

  cout << part1_ans << " " << part2_ans << endl;
}
