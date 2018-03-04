cmake_minimum_required(VERSION 3.8)
project(leetcode_cpp)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp TeemoAttaking.cpp average-of-levels-in-binary-tree.cpp minimum-height-trees.cpp add-strings.cpp longest-palindromic-substring.cpp palindromic-substrings.cpp longest-palindromic-subsequence.cpp license-key-formatting.cpp unique-paths.cpp unique-paths-ii.cpp best-time-to-buy-and-sell-stock.cpp best-time-to-buy-and-sell-stock-ii.cpp factorial-trailing-zeroes.cpp best-time-to-buy-and-sell-stock-with-cooldown.cpp implement-trie-prefix-tree.cpp)
add_executable(leetcode_cpp ${SOURCE_FILES})