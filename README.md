## Benchmark Experiment

<br>

* _**Formulate a hypothesis/problem statement about behavior of response times of these three web servers.**_

  The response time for a single request sent from point A to point B is proportional to the distance between the same points A and B. In other words you can calculate the response time for any request given the distance between you and the receiver.
</br>

* _**Plan an experiment, which measures response times of these three web servers.**_

  Testing this hypothesis requires a script that measures the reponse time for a number of requests sent to 3 different servers around the orld. Furthermore, to test and validate the hypothesis a distance between me and the 3 server locations must be calculated from a birdview perspective.
</br>

* _**Execute the experiment, which measures response times of these three webservers.**_

  | Server | Location | Iterations | Total time (sec) | Average time (ms) |
  | --- | --- | --- | --- | ---|
  | http://139.59.132.185:8080 | Frankfurt | 100 | 4.3 | 43.0 |
  | http://192.81.216.124:8080 | US (New York) | 100 | 19.3 | 193.0 |
  | http://128.199.180.131:8080 | Singapore | 100 | 34.6 | 346.0 |
</br>

* _**Execute the experiment, which calculates the distance for the three webservers.**_

  | From | To | Distance (km) |
  | --- | --- | --- |
  | Copenhagen | Frankfurt | 671 |
  | Copenhagen | US (New York) | 6188 |
  | Copenhagen | Singapore | 9973 |
</br>

* _**Evaluate your experiment and interpret the measurements and results.**_

  From the distances we would expect the following:
  
  1. The response time from CPH to Frankfurt is (6188 / 671) = 9.2 times faster than from CPH tp New York
  
  This
  
  2. The response time from CPH to Frankfurt is (9973 / 671) = 14.9 times faster than from CPH tp Singapore
  
  
  
  
  
</br>

* _**Discuss what you are measuring, how you are measuring, and what could influence your results., see Peter Sestoft “Microbenchmarks in Java and C#” https://www.itu.dk/people/sestoft/papers/benchmarking.pdf for inspiration.**_
