## Execution instructions

### Conda
**Step 1:** Start the Docker server.

**Step 2:** Run Grobid on **localhost:8070**:

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

You can check if Grobid is running properly by openning a web browser and visit the following URL: [http://localhost:8070](http://localhost:8070).

**Step 3:** Open a new command line and create a blank virtual environment with [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) with a name in python 3.10

```
conda create -n text_analysis python=3.10
```

**Step 4:** Activate the environment.

```
conda activate text_analysis
```

**Step 5:** Install the dependencies from `requirements.txt` file:

```
pip install -r requirements.txt
```

**Step 6:** Before running the main program, it is recommended to run the `testing.py` file found in the "**tests**" folder. For this purpose, stay in the main directory ("Text-Analysis") and execute

```
python tests/testing.py
```
    
**Step 7:** After passing the tests, stay in the main directory and execute the **main** program

```
python main.py
```

Once executed, the program will save the results in the "**results**" folder:
- A figure of wordcloud saved as "wordcloud.png".
- A histogram saved as "figures.png".
- URLs of each paper saved as "links.txt".

**Step 8:** Once the results have been obtained, stop the container where it is running Grobid.

To find out the CONTAINER_ID, execute:

```
docker container ps
```

Then, stop the container

```
docker container stop CONTAINER_ID
```


### Docker compose
**Step 1:** Start the Docker server.

**Step 2:** Stay in the main directory ("Text-Analysis") and execute (*Note: make sure there are no programs using port 8070 because that's where Grobid will run*):  

```
docker-compose up --build
```

In this case, docker-compose will run the tests ("tests/testing.py") before running the main program ("main.py").

If all tests are passed, then the main program will be executed, otherwise it stops.
    
Once executed, the program will save the results in the "**results**" folder:
- A figure of wordcloud saved as "wordcloud.png".
- A histogram saved as "figures.png".
- URLs of each paper saved as "links.txt".

**Step 4:** Once the results have been obtained, execute

```
docker-compose down
```
