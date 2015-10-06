#Question 1
Suppose we perform the PCY algorithm to find frequent pairs, with market-basket data meeting the following specifications:  
* s, the support threshold, is 10,000.
* There are one million items, which are represented by the integers 0,1,...,999999.
* There are 250,000 frequent items, that is, items that occur 10,000 times or more.
* There are one million pairs that occur 10,000 times or more.
* There are P pairs that occur exactly once and consist of 2 frequent items.
* No other pairs occur at all.
* Integers are always represented by 4 bytes.  
* When we hash pairs, they distribute among buckets randomly, but as evenly as possible; i.e., you may assume that each bucket gets exactly its fair share of the P pairs that occur once.  

Suppose there are S bytes of main memory. In order to run the PCY algorithm successfully, the number of buckets must be sufficiently large that most buckets are not large. In addition, on the second pass, there must be enough room to count all the candidate pairs. As a function of S, what is the largest value of P for which we can successfully run the PCY algorithm on this data? Demonstrate that you have the correct formula by indicating which of the following is a value for S and a value for P that is approximately (i.e., to within 10%) the largest possible value of P for that S.

A) S = 300,000,000; P = 3,500,000,000			
B) S = 500,000,000; P = 5,000,000,000	
C) S = 100,000,000; P = 120,000,000			
D) S = 100,000,000; P = 540,000,000

key: B  
reference: http://www.cnblogs.com/Answer1215/p/4027903.html  
Expected memory required for pass 2:  

Expected number of frequent buckets: 1,000,000.  
Each frequent bucket hashes (1 + P/#buckets) pairs, which we'll simplify to P/#buckets pairs.  
Probability of a bucket to be frequent: 1,000,000 / #buckets  
Number of pairs that are both frequent, and map to a frequent bucket:   
P * (1,000,000 / #buckets)  
Total expected memory consumption for pass 2 (12 bytes per pair):  
P * 12,000,000 / #buckets  

In pass 1, we need some space to count items (~4MB), and we can use the remainder of S as a hash table to help eliminate non-frequent pairs later on. This hash table is one integer (4 bytes) per bucket, so we can have at most (S - 4MB) / 4 ~= S/4 buckets in this hash table.   

Before we do pass 2, we will compress this table to a bitmap, but the number of buckets is still S/4. The buckets will just take less space in pass 2.  

That's true, S/4 is an upper bound for #buckets (::facepalm:: how did I miss this simple bound?)  
If we'll use S/4 buckets, and compress it to S/32 bytes using bitmapping, we're left with S*31/32 bytes for counting pairs.  

According to my analysis, on the 2nd pass we'll need  (P * 12,000,000 / #buckets) bytes for counting.  
So if #buckets = S/4,  
We'll need P * 12,000,000 / (S/4) = 48,000,000*P/S   byes for counting.  

since we have S*31/32 bytes free:  
S*31/32 =  48,000,000*P/S  
so
S^2 = 49,548,387 * P  

and our bound:  
P < S^2 / 49,548,387  
***
#Question 2
During a run of Toivonen's Algorithm with set of items {A,B,C,D,E,F,G,H} a sample is found to have the following maximal frequent itemsets: {A,B}, {A,C}, {A,D}, {B,C}, {E}, {F}. Compute the negative border. Then, identify in the list below the set that is NOT in the negative border.

A) {F,G}		
B) {B,F}			
C) {D,F}			
D) {A,E}

key: A  
This set is not in the negative border because immediate proper subset {G} is not frequent.  
