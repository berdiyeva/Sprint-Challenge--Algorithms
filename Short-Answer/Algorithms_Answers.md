#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) It has one loop which takes in n so it has a linear run complexity.


b) It has a nested loop which makes my insticts say O(n^2) but because the inner loop is multiplying j and is not executing every time it is a O(log(n) therefore I believe the answer should be O(n log(n))


c) O(n) it has just one loop. so it has a linear run complexity.

## Exercise II


So I have multistored building and a bunch of eggs, the aim is to find the f floor with the minimun waste of eggs. 

    The best solution will be I think if I start from the middle of the multistored building and throw an egg, if it breaks I can eliminate the higher half of building and focus on the lower ones, and vice versa. 
    I can use binary search algorith to find the desired f floor. 
    The runtime complexity of a binary search is O(log n) since I cut my search space in half each pass.



I could start from the first floor and throw an egg, but this way I have to perform multiple steps and waste more eggs to reach the f floor. 

Better solution is to skip some floors and throw less eggs. 

