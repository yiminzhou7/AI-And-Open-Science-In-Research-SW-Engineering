## Execution instructions
Run the Docker server. Then, run Grobid on **localhost:8070**:

```
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

You can check if Grobid is running properly by openning a web browser and visit the following URL: [http://localhost:8070](http://localhost:8070).

Now, create a virtual environment with **conda**. Create a blanck virtual environment with a name (in my case *text_analysis*) in python 3.10 with this command:

```
conda create -n text_analysis python=3.10
```

Activate the environment.

```
conda activate text_analysis
```

Then, install the dependencies from "requirements.txt" file with the command:

```
pip install -r requirements.txt
```

    
Before running the main program, it is recommended to run the "testing.py" file found in the "**tests**" folder. 
For this purpose, go to the main directory ("Text-Analysis") and execute

```
python tests.testing.py
```
    
After passing the tests, stay in the main directory and execute the **main** program:

```
python main.py
```

Once executed, the program will show on screen all the links it has found from the different papers. Additionally, it will create a wordcloud based on the abstracts and a histogram of number of figures per paper and save them in the "**results**" folder.
