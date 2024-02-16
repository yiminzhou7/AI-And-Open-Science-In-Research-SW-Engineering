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
3. Create a virtual environment with **conda**: 

    Create a blanck virtual environment with a name in python 3.10
    ```
    docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
    ```
    Install the dependencies from `requirements.txt` file:
    ```
    pip -r install requirements.txt
    ```
4. Before running the main program, it is recommended to run the `testing.py` file found in the "**tests**" folder. For this purpose, go to the main directory ("Text-Analysis") and execute
    ```
    python -m unittest tests.testing
    ```
5. After passing the tests, stay in the main directory and execute the **main** program
    ```
    python main.py
    ```
    Once executed, the program will show on screen all the links it has found from the different papers. Additionally, it will create a wordcloud based on the abstracts and a histogram of number of figures per paper and save them in the "**results**" folder.
    
   
