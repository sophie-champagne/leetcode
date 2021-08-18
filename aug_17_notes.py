https://leetcode.com/problems/valid-anagram/
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode.com/problems/permutations/

backtracking:
inefficient in time and space
it does cover every possibility (only once)

123456

213546
  
result = [213456, 213465, 213546]

8 ary
   1
 1 2 3 4 5 6 7 8  
1234567
      1
   2     3
  2 2   4 5
1. Sorting 
	most likely heap based problem
    learn the most common sorting algos, runtime, space and general idea of how they are implemented
    insertion sort O(N^2)
    bubble sort
    selection sort
    
    quicksort O(N^2)
    mergesort O(NlogN)
    
    bogosort O(infinity) https://en.wikipedia.org/wiki/Bogosort
      randomize the array
      check if it is sorted, if not, start over
    
2. Dynamic Programming 
	usually asked by companies that think they are too good
    waste of time
    usually you need to know the "trick" to the problem
    - fibonacci problems
    - main concept: memoization
    - if you like it, feel free to learn more, if not, just do the easy problems and move on
3. LRU cache 
	specific LC problem
    OOD skills
    microsoft loves asking this question
4. backtracking 
   8 queens problem
   interesting to learn, boring once you've done a few
   permutations, combinations, etc
5. bitwise: brain teaser 
   not common at all
   "fun"
   detect the non duplicated number
   [1,2,3,4,3,2,1]
6. String operation 
	very important
    learning standard string function substring, trim, join, split, regex, etc

1. space
  2 scans 
  	1. for variables that grow
    2. how will those variables grow
2. ascii stuff

ints are 4 bytes
int x = 0;
0000
x = x + 1
RAM: 0001
  
  
cpu register
eax: 0001
ebx:
ecx: 
...  

char: 'a'
  https://www.asciitable.com/
  https://home.unicode.org/
encodings
'a' = 97
'A' = 65
  
string s = "Abc"
  [0000000....100101, 98, 99]
  s += "a"
  [65, 98, 99, 97]
hashmap/sets/dicts
000000000000 x26


            alpha[s.charAt(i) - 'a'] ++;
x = s.charAt(i) => char fixed sized
y = 'a'
z = x - y
alpha[z] ++

4 * 26 bytes (alpha)
+ 4 bytes (int i)
= 108 bytes thru whole execution
O(108) => O(1) space

int[] alpha = new int[26]; // variable, never grows [26]
alpha = dictionary
alpha['A']
alpha[65]

we don't want  
A = 65
B = 66
  ...

we want:
'A' = 0
'B' = 1 

alpha[0] = number of times A has appeared in s - t

alpha['A' - 'A']
alpha[65 - 65] => alpha[0]

alpha['B' - 'A']
alpha[66 - 65] => alpha[1]
....
s = "AAAaaa"
t = "aaaaaa"  
alpha[var] = the number of times letter "var" has appeared in s - times appeared in t
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length())
            return false;
        int[] alpha = new int[26]; // variable, never grows [26]
        for(int i = 0; i< s.length(); i++) { // variable, never grows
            alpha[getLetterOffset(s.charAt(i))] ++;
            alpha[t.charAt(i) - 'a'] --;
        }
        for(int i=0;i<26;i++) // variable never grow
            if(alpha[i] != 0)
                return false;
        return true;
    }
}


  
