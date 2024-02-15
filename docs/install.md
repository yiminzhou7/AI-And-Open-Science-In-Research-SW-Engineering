## Installation instructions
1. Clone the repository from GitHub to your local machine:
    ```
    git clone https://github.com/yiminzhou7/AI-And-Open-Science-In-Research-SW-Engineering.git
    ```
2. Start the docker server
3. Install Grobid
    ```
    docker pull lfoppiano/grobid:0.7.2
    ```


## Execution instructions
1. Run the Docker server.
2. Run Grobid on **localhost:8070**:
    ```
    docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
    ```
    You can check if Grobid is running properly by openning a web browser and visit the following URL: [http://localhost:8070](http://localhost:8070).
3. Create a blank virtual environment with conda in python 3.10:
