# exercise-1-modularity-WayGang
exercise-1-modularity-WayGang created by GitHub Classroom



The architecture of this system:

![image](https://github.com/ec500-software-engineering/exercise-1-modularity-WayGang/blob/master/WechatIMG2.png)
"multimain.py" is the main class.
Run this, the result is:
![image](https://github.com/ec500-software-engineering/exercise-1-modularity-WayGang/blob/master/modularity.png)

As you can see from this result, all the modules will start together, and processing respectively.
Assuming that:

the AI model will produce the result slower than other modules;
the Alert system should check every data and it could take a while;
the storage sysyem seems the fastest one.

The result shows the importance of multi-threading in this program.


If we run the singlethread.py, which means the system is no more multi-threaded:
this is the result:
![image](https://github.com/ec500-software-engineering/exercise-1-modularity-WayGang/blob/master/singlethread.png)
as we can see in this picture:

Every module of this system starts processing in an order, which is not what we want;

Every module of this system has to processing in one run, for example, sometimes we don't need to alert or AI prediction, but it is all in one run, which is not what we want.
