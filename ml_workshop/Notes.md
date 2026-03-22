### 2

Spam is a classic example. 
Feels like there are specific rules.
Maybe I could code it up… lots of problems.
Fundamental problem is there are soooo many different cases – how am I going to capture them all? How do I look through them all? How do I not just play whack a mole. 

https://blog.usecure.io/the-most-common-examples-of-a-phishing-email


### 4

So what does ML cover? A lot of examples!
What are we going to be dealing with today? 

Recap:
Where did we start? Explicit rules to do tasks.
Then we started collecting lots of data.
So could you let a computer learn how to do a task given all of this data?
That is machine learning. 

https://www.flickr.com/photos/drbeachvacation/35477618781
https://www.quantamagazine.org/playing-hide-and-seek-machines-invent-new-tools-20191118/

### 5

One last thing… 

Any questions so far? 

https://medium.com/@kamalmeet/building-blocks-for-ai-part-2-clustering-and-classification-ce537056b7f9
https://en.wikipedia.org/wiki/Principal_component_analysis
https://www.stratascratch.com/blog/a-comprehensive-overview-of-3-popular-machine-learning-models/

### 6 

There are a lot of different models, and one big take away is that ML is full of loads of algorithms
However this is, I think, a useful abstraction. 
All Models make predictions
Use the analogy of taking an exam/class 
What I want to be really clear on are the orange boxes – this is what you need to understand about a model to use it well 
Go through each of the the three in a class analogy (update is all about study methods, loss function is about what your prof cares about, model is you, the learner)

### 9 

Recap what we’ve learned so far:
What is ML
Paying attention to the big three
Worrying about overfitting

What is regression? Phrase as a task. 
Dependent vs independent variables 

So what does goodness mean? 
MSE is about the mean and is the most often used 
Note things like quantile 

Talk about how nice it is to report R2

Any Questions?

### 10

https://www.aces.edu/blog/topics/forestry/how-tree-growth-affects-tree-failure/

### 11

What on earth is a decision tree? 
It’s like playing 20 questions. 

### 12

Okay how does the update work. 
Work through the example and move things around. 
Note this is sum of squared errors

### 15

How do you deal with multiple features?
Note this is really laborious but computers are good at that!
Note the predictions are kind of jumpy. 

Any questions?

Will you see decision trees get used on their own? 

### 16

Ensembling is one of the coolest things in ML in my opinion. 
So obviously things have to be different otherwise I’d get a bunch of clones. 
It’s all about creating different datasets
Explain bootstrapping

Any questions?

Summarize the big three and move to the lab 

Length, weight, scars, scale size, etc. 

https://vitalflux.com/random-forest-classifier-python-code-example/


### 19

Recap:
What is ML
The architectures and comparing and contrasting them
Overfitting as the biggest enemy

What is classification and how is it different than regression 
Talk about probabilities and thresholds

This is where the loss functions get cool and “functional” 
Introduce class imbalance
Precision is about being confident in the answer when the answer is a positive 
Catching the disease or issue or whatever 

CCE solves a lot of this. 
Walk through the predict only one thing example. 
A, P, R are good for reporting, CCE is good for optimizing . 

### 21

Let me motivate this. These are the workhorses. 
Stuff over tabular data – random forests are by and large going to do the trick. 
Where Neural nets shine is non-tabular data. 

Three layers. 
Go through indices
Note that this looks really scary but it’s going to get all hidden away nicely for us. 
Go through the math step by step. 
Talk about “activation” 

So what are we going to tune? 
Distinguish the hyperparameters based off of this. 

### 22 

Explain the principle behind gradient descent.
What is this picture
Where would I want to go?
How do I compute that

Talk about learning rates, stochastic gradient descent, etc.

Note I’m brushing over a lot. 

### 23

So far we’ve left the’s g’s alone. So what might they be? 

This just becomes logistic regression! 

You can actually use these libraries to fit all kinds of models if you like. 


### 24

Walk through this architecture. 
What is a softmax? 

Review hyperparameters. 

### 25

Who that was a lot
Thankfully, there are frameworks
Big takeaways:
We follow gradients (different ways to do that) [and it’s really important to know that]
We are tuning loads of coefficients 
We can change our layers
We can change our activation functions 
You can kind of do whatever you like with these [all of these parameters mean Neural Networks are an artform] [note we’ll make some comments later on using prior art]
The frameworks handle the math

### 27 

Recap:
What is machine learning
The big three (compare and contrast)
Overfitting is your worst nightmare (use this to get into the data problem) 

70,000 images over 10 things… what would we need for watching a reef with loads and loads of fish!
Briefly mention augmentation 

So these needed a lot of data – what if I don’t have that data? 

### 28



https://www.ibm.com/think/topics/data-augmentation


### 29

So folks have done a lot of work to create really good models. 
Note the amount of data to train this is crazy. Also the amount of compute. 
Someone has really used their artistry here. 
Walk through the layers and what they may be doing. 

### 32

Use Ml to explore – basically allows you to run experiments. 

Overfitting first and then pick it off the shelf
