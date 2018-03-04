#include <iostream>
#include <vector>

//#include "TeemoAttaking.cpp"
//#include "average-of-levels-in-binary-tree.cpp"
//#include "minimum-height-trees.cpp"
//#include "add-strings.cpp"
//#include "longest-palindromic-substring.cpp"
//#include "longest-palindromic-subsequence.cpp"
//#include "license-key-formatting.cpp"
//#include "unique-paths.cpp"
//#include "unique-paths-ii.cpp"
//#include "best-time-to-buy-and-sell-stock.cpp"
//#include "best-time-to-buy-and-sell-stock-ii.cpp"
//#include "best-time-to-buy-and-sell-stock-iii.cpp"
#include "implement-trie-prefix-tree.cpp"

int main() {
//    Solution s = Solution();
//    TeemoAttaking ta = TeemoAttaking();
//    std::vector<int> ts = {1,4};
//    std::cout << ta.findPoisonedDuration(ts, 2) << std::endl;
//    ts = {1};
//    std::cout << ta.findPoisonedDuration(ts, 2) << std::endl;

//    TreeNode *n3 = new TreeNode(3);
//    TreeNode *n9 = new TreeNode(9);
//    TreeNode *n20 = new TreeNode(20);
//    TreeNode *n15 = new TreeNode(15);
//    TreeNode *n7 = new TreeNode(7);
//    n3->left = n9;
//    n3->right = n20;
//    n20->left = n15;
//    n20->right = n7;
//
//    vector<double> res = s.averageOfLevels(n3) ;
//    for (vector<double>::const_iterator iter=res.cbegin(); iter!=res.cend(); iter++) {
//        std::cout << (*iter) << std::endl;
//    }

//    vector<pair<int, int>> edges = {{0, 3},
//                                    {1, 3},
//                                    {2, 3},
//                                    {4, 3},
//                                    {5, 4}};
//    for (auto root:s.findMinHeightTrees(6, edges)) {
//        std::cout << root << std::endl;
//    }
//
//    edges = {};
//    for (auto root:s.findMinHeightTrees(1, edges)) {
//        std::cout << root << std::endl;
//    }

//    std::cout << s.addStrings("1234", "987") << std::endl;
//    std::cout << s.longestPalindromeSubseq_BottomUp("babbabcbbab") << std::endl;
//    std::cout << s.longestPalindromeSubseq_TopDownWithMemo("babbabcbbab") << std::endl;

//    vector<vector<int>> grid = {{1,0,0},{0,1,1},{0,0,0}};
//    std::cout << s.uniquePathsWithObstacles(grid) << std::endl;

//    vector<int> prices = {7, 1, 5, 3, 6, 4};
//    std::cout << s.maxProfit(prices) << std::endl;
//
//    prices = {7, 6, 5, 5, 4, 4};
//    std::cout << s.maxProfit(prices) << std::endl;

//    vector<int> prices = {7, 1, 5, 3, 6, 4};
//    std::cout << s.maxProfit(prices) << std::endl;
//
//    prices = {7, 6, 5, 5, 4, 4};
//    std::cout << s.maxProfit(prices) << std::endl;
//
//    prices = {7, 1, 5, 3, 6, 3, 4, 2};
//    std::cout << s.maxProfit(prices) << std::endl;

    Trie* tree = new Trie();
    tree->insert("hello");
    tree->insert("world");
    std::cout << tree->search("hello") << std::endl;
    std::cout << tree->search("hi") << std::endl;
    std::cout << tree->startsWith("wor") << std::endl;
    std::cout << tree->startsWith("word") << std::endl;

    return 0;
}