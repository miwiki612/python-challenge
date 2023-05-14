### Description
- Folder <PyBank> and <PyPoll> contains main.py which read data in Folder <PyBank/Resources> and <PyPoll/Resources>, then print result in terminal and write result as “analysis.csv” in <PyBank/analysis> and <PyPoll/analysis>.
- General logic in main.py. Both code read and convert data as dictionary then use dictionary to finish the task
- Analysis results use .append to add answers for questions. Format is adjusted during .append via f’ string.

### Concerns
- In instructor’s .py the os.path.join works with “..”, but I got errors and used “.”
- I got some issue with git push, please use branch “master”, ignore “main”

