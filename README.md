## Benchmark Experiment

<br>

* _**Formulate a hypothesis/problem statement about behavior of response times of these three web servers.**_

  The delay upon sending a request from point a to point b is proportional to the length between the same points.
</br>

* _**Plan an experiment, which measures response times of these three web servers.**_

  To test the hypothesis I will setup an experiment. I will write a script that sends 10.000 requests to 3 different servers     located in different countries around the world. I will then measure the average response time. I will then measure the         distance between my exact location and the 3 server locations. 

  If the hypothesis is correct I would expect that a request to a server with the distance X would take the time T to return     the response. I would also expect that another request with twice the distance (X * 2) would take exactly double the time of   the first request, T * 2. 
</br>

* _**Execute the experiment, which measures response times of these three webservers.**_

  | Server | Location | Iterations | Total time (sec) | Average time (ms) |
  | --- | --- | --- | --- | ---|
  | http://139.59.132.185:8080 | Frankfurt | 100 | 4.3 | 43.0 |
  | http://192.81.216.124:8080 | US (New York) | 100 | 19.3 | 193.0 |
  | http://128.199.180.131:8080 | Singapore | 100 | 34.6 | 346.0 |
</br>

* _**Evaluate your experiment and interpret the measurements and results.**_

  | From | To | Distance (km) |
  | --- | --- | --- |
  | Copenhagen | Frankfurt | 671 |
  | Copenhagen | US (New York) | 6.188 |
  | Copenhagen | Singapore | 9973 |
</br>

* _**Discuss what you are measuring, how you are measuring, and what could influence your results., see Peter Sestoft “Microbenchmarks in Java and C#” https://www.itu.dk/people/sestoft/papers/benchmarking.pdf for inspiration.**_
