# 06/21 Hiring Hackathon

## Assignment: Develop "GitHub PR Query" tool

### GitHub PR Query tool

Design a command line utility to get list of all PRs in given time interval (last hour, day, 3 weeks, 6 months). 

The list should include:
  - all merged PRs in the specified interval
  - created PRs in the specified interval

Futhermore, the list should be annotated:
  - each PR info should contain creation date, merge date (if available) and time how long it took to merge PR
  - each PR should be marked by an offensive flag. The offensive PR is one which title does not contain jira issue key (e.g., `[SW-343]`)
  - each PR should contain summary of file statistics - list of (file extension, number of modified files with the extension)

Furthermore, the utility should print summary of authors:
  - summary of PR authors (opened/merged PRs) sorted by number of merged PRs

### Requirements
 - You can use any language, but Python is recommended
   - You can leverage any libraries: for example [PyGitHub](https://github.com/PyGithub/PyGithub) to communicate with GitHub API, or [dateparser](https://pypi.python.org/pypi/dateparser) to parse date
 - Create and submit code to your GitHub repository
 - Time limit is 2hours

## Submission of solution
Send a location of your solution GitHub repository to `venkatesh@h2o.ai`

## Evaluation
We will do evaluation of submitted solutions on Thursday and authors of successful solutions will be contacted.

### Hints
  - If you hit GitHub rate limit, you need to create an application id in GitHub settings under your account.
  
### Example

#### Example of input
Calling the following command line:

```bash
./ghq  --repo 'h2oai/h2o-3' --jira_key "PUBDEV" --since "3 days"
```

#### Example of outptu
The command returns list of all opened and merged PRs in project [h2oai/h2o-3](https://github.com/h2oai/h2o-3) in last 3 days:
```
*** GitHub repo h2oai/h2o-3 (from 2017-06-18 to 2017-06-21) ***
Title                                                                     State    Created at    Merged at    Time to merge     Offensive    File Stats
------------------------------------------------------------------------  -------  ------------  -----------  ----------------  -----------  ------------------------
Distributed XGBoost                                                       open     2017-06-21    ---          ---               !!!          'java': 11,'jar': 4
PUBDEV-4598 make class public for SharedTreeSubgraph for custom tree viz  open     2017-06-21    ---          ---                            'java': 3
[BUILD] Publication of SNAPSHOT artifacts into local Nexus repo           open     2017-06-20    ---          ---               !!!          'gradle': 1
[PUBDEV-4269] H2O should warn user about the minimal required Coloram…    open     2017-06-20    ---          ---                            'py': 2
PUBDEV-4578: Fixing h2o R package CRAN NOTE (#1287)                       open     2017-06-20    ---          ---                            'R': 1
[HOTFIX] Fix test runners to setup right number of nodes for clouding     open     2017-06-20    ---          ---               !!!          'sh': 3
PUBDEV-4445: prediction warning.  -Passed warning messages from model…    open     2017-06-19    ---          ---                            'java': 3,'py': 2,'R': 1
Add dart options to XGBoost (and quiet_mode)                              open     2017-06-18    ---          ---               !!!          'java': 1,'py': 1,'R': 1
Exposes bulk model bulding feature (can be used in 3rd party libraries)   closed   2017-06-19    2017-06-20   1 day, 0:04:01    !!!          'java': 2
Starting a new grid search is Grid endpoint                               closed   2017-06-20    2017-06-20   0:46:31           !!!          'md': 1
Publish 'tests' artifact                                                  closed   2017-06-16    2017-06-19   2 days, 22:42:59  !!!          'gradle': 1
PUBDEV-4416: Fixed streamParse in Orc Parser.                             closed   2017-06-17    2017-06-19   2 days, 14:39:28               'java': 1

*** Authors ***
Author          Merged PRs    All PRs
------------  ------------  ---------
michalkurka              2          2
miracode                 1          1
tomasnykodym             1          1
arnocandel               0          1
jakubhava                0          1
ledell                   0          1
mdymczyk                 0          1
mklechan                 0          1
mmalohlava               0          2
wendycwong               0          1
```
