#Question 1
The edit distance is the minimum number of character insertions and character deletions required to turn one string into another. Compute the edit distance between each pair of the strings he, she, his, and hers. Then, identify which of the following is a true statement about the number of pairs at a certain edit distance.

A) There are 2 pairs at distance 3.			
B) There are 4 pairs at distance 1.			
C) There are 3 pairs at distance 1.			
D) There is 1 pair at distance 2.	

key:D

|pairs|distance|
|:----:|:----:|
|(he,she)| 1 = 5 - 4|			
|(he,his)| 3 = 5 - 2|			
|(he,hers)| 2 = 6 - 4|			
|(she,his) | 4 = 6 - 2|			
|(she,hers) | 3 = 7 - 4|			
|(his,hers) | 3 = 7 - 4	|
***
#Question 2 
Consider the following matrix: 

|  |C1|      C2|      C3|      C4|    
|---|:---:|:---:|:---:|:---:|
|R1|	0|	1|	1|	0|    
|R2|	1|	0|	1|	1|    
|R3|	0|	1|	0|	1|   
|R4|	0|	0|	1|	0|    
|R5|	1|	0|	1|	0|   
|R6|	0|	1|	0|	0|    

Perform a minhashing of the data, with the order of rows: R4, R6, R1, R3, R5, R2. Which of the following is the correct minhash value of the stated column? Note: we give the minhash value in terms of the original name of the row, rather than the order of the row in the permutation. These two schemes are equivalent, since we only care whether hash values for two columns are equal, not what their actual values are.

A) The minhash value for C4 is R2			
B) The minhash value for C2 is R3			
C) The minhash value for C2 is R6		
D) The minhash value for C4 is R5		

key: C

|C1|      C2|      C3|      C4|    
|:---:|:---:|:---:|:---:|
|R5|R6|R4|R3|
***
#Question 3
Here is a matrix representing the signatures of seven columns, C1 through C7.

|C1|C2|C3|C4|C5|C6|C7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1|2|1|1|2|5|4|
|2|3|4|2|3|2|2|
|3|1|2|3|1|3|2|
|4|1|3|1|2|4|4|
|5|2|5|1|1|5|1|
|6|1|6|4|1|1|4|

Suppose we use locality-sensitive hashing with three bands of two rows each. Assume there are enough buckets available that the hash function for each band can be the identity function (i.e., columns hash to the same bucket if and only if they are identical in the band). Find all the candidate pairs, and then identify one of them in the list below.

A) C5 and C7			
B) C3 and C7			
C) C2 and C7			
D) C1 and C3

key: D

| |C1|C2|C3|C4|C5|C6|C7||
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|band1|1|2|1|1|2|5|4|(C1,C4) (C2,C5)|
||2|3|4|2|3|2|2||
|band2|3|1|2|3|1|3|2|(C1,C6) |
||4|1|3|1|2|4|4||
|band3|5|2|5|1|1|5|1|(C1,C3) (C4,C7)|
||6|1|6|4|1|1|4||
***
#Question 4
Find the set of 2-shingles for the "document":ABRACADABRA
and also for the "document":BRICABRAC

Answer the following questions:

How many 2-shingles does ABRACADABRA have?  
`key:{AB,BR,RA,AC,CA,AD,DA}`

How many 2-shingles does BRICABRAC have?  
`key:{BR,RI,IC,CA,AB,RA,AC}`

How many 2-shingles do they have in common?  
`key：5`

What is the Jaccard similarity between the two documents"?  
`key：5/9`

Then, find the true statement in the list below. 

A) The Jaccard similarity is 5/7.			
B) BRICABRAC has 7 2-shingles.	
C) The Jaccard similarity is 4/7.			
D) BRICABRAC has 8 2-shingles.

key: B
***
#Question 6
Suppose we want to assign points to whichever of the points (0,0) or (100,40) is nearer. Depending on whether we use the L1 or L2 norm, a point (x,y) could be clustered with a different one of these two points. For this problem, you should work out the conditions under which a point will be assigned to (0,0) when the L1 norm is used, but assigned to (100,40) when the L2 norm is used. Identify one of those points from the list below.

A) (61,8)		
B) (53,18)			
C) (53,10)			
D) (63,8)

key: A

python:import math  
L1 norm

||(0,0)|(100,40)||
|:---:|:---:|:---:|:---:|
|(61,8)|abs(61-0) + abs(8-0) = 69|abs(61-100)+abs(8-40) = 71|(0,0)|
|(53,18)|abs(53-0) + abs(18-0) = 71 | abs(53-100)+abs(18-40) = 69|(100,40)|
|(53,10)|abs(53-0) + abs(10-0) = 63 |abs(53-100)+abs(10-40) = 77|(0,0)|
|(63,8)|abs(63-0) + abs(8-0) = 71| abs(63-100)+abs(8-40) = 69|(100,40)|

L2 norm

||(0,0)|(100,40)||
|:---:|:---:|:---:|:---:|
|(61,8)|math.sqrt(math.pow(61-0,2) + math.pow(8-0,2)) = 61.5223536611|math.sqrt(math.pow(61-100,2) + math.pow(8-40,2)) = 50.4479930225|(100,40)|
|(53,18)|math.sqrt(math.pow(53-0,2) + math.pow(18-0,2)) = 55.9732078766|math.sqrt(math.pow(53-100,2) + math.pow(18-40,2)) = 51.8941229813|(100,40)|
|(53,10)|math.sqrt(math.pow(53-0,2) + math.pow(10-0,2)) = 53.9351462406|math.sqrt(math.pow(53-100,2) + math.pow(10-40,2)) = 55.7584074378813|(0,0)|
|(63,8)|math.sqrt(math.pow(63-0,2) + math.pow(8-0,2)) = 63.5059052372|math.sqrt(math.pow(63-100,2) + math.pow(8-40,2)) = 48.91829923455|(100,40)|

