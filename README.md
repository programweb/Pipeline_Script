# SciPy Pipeline
## Python executed in terminal 

I wrote this for a set of Python files that you want to execute in a certain order.
It is simple.  For example, input from one file does not flow to the other.
That wouldn't be too hard to add.  This could also be done as a BASH or Shell
script.  But generally, if you want a more robust pipeline solution written in
Python, you might want to try a program like Snakemake or Nextflow.  Galaxy is
another possibility and more accessible to non-programmers.
&nbsp;

In bioinformatics and data science, pipelines of sometimes thousands of files or
processes are required.

1. Make a master file (.txt file is fine) with the paths to all the scripts you want to execute on a separate line
1. Execute the pipeline.py file in the terminal.
   ```python
   $ ./pipeline.py
   ```
1. pipeline.py asks for the path to the master file & checks to see if the path exists
1. pipeline.py checks that all the Python files listed in the master file exist
1. pipeline.py confirms with the user that the file paths in the master are correct (displaying the paths in order to the user)
1. pipeline.py runs all the Python files in order
1. pipeline.py confirms completion or reports any errors to the user in the terminal
&nbsp;

For a quick demo I have added a master file (master.txt) with 5 files to execute.
Of course, files in an actual bioinformatic pipeline would be used instead; but,
it is often better to start with a simple example.
&nbsp;

Flexibility:
* it is easily configured by changing the paths in the master text file
* the files could be on different directories
* although there are only 5 files in the demonstration, several thousand filepaths could, in fact, be added.
&nbsp;

```python
$ ./pipeline.py
BIOINFORMATICS PIPELINE
Enter the path to the master file (which contains the file paths in the order you want to execute them on separate lines): biopipeline_227/master.txt
Filepaths: ['biopipeline_227/001.py', 'biopipeline_227/002.py', 'biopipeline_227/003.py', 'biopipeline_227/004.py', 'biopipeline_227/005.py']
Are these file paths correct? [Y/N] y

biopipeline_227/001.py
2023-11-26 15:46:56.080038
biopipeline_227/002.py
2023-11-26 15:46:56.121211
biopipeline_227/003.py
2023-11-26 15:46:56.162477
biopipeline_227/004.py
2023-11-26 15:46:56.204594
biopipeline_227/005.py
2023-11-26 15:46:56.246912

Bioinformatics pipeline completed successfully.
```
